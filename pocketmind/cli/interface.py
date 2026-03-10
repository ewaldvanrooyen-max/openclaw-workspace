"""
PocketMind CLI Interface

The main terminal interface for interacting with PocketMind.
Supports backup/sync commands for premium users.
"""

import sys
import os

# Try to import readchar for better input handling
try:
    import readchar
    HAS_READCHAR = True
except ImportError:
    HAS_READCHAR = False


class CLI:
    """
    Command-line interface for PocketMind.
    
    Handles user input and displays AI responses.
    Supports optional voice input (STT) and voice output (TTS).
    """
    
    def __init__(self, brain=None, voice_input=None, voice_output=None):
        """
        Initialize the CLI.
        
        Args:
            brain: Brain instance for generating responses
            voice_input: VoiceInput instance for speech-to-text
            voice_output: VoiceOutput instance for text-to-speech
        """
        self.brain = brain
        self.voice_input = voice_input
        self.voice_output = voice_output
        self.history = []
        self.running = False
        
        # Load user profile from storage
        self._load_profile()
        
        # Show welcome
        self._show_welcome()
    
    def _load_profile(self):
        """Load user profile from storage."""
        try:
            from storage.json_store import JSONStore
            store = JSONStore()
            profile = store.load("user_profile")
            self.profile = profile or {}
        except Exception:
            self.profile = {}
    
    def _show_welcome(self):
        """Show welcome message."""
        if self.profile and self.profile.get("name"):
            name = self.profile["name"]
            goal = self.profile.get("goal", "")
            
            print(f"👋 Welcome back, {name}!")
            if goal:
                print(f"   Goal: {goal}")
            print()
        else:
            print("👋 Welcome to PocketMind!")
            print("   Run with --onboard to set up your profile.\n")
    
    def run(self):
        """Main CLI loop."""
        self.running = True
        
        while self.running:
            try:
                # Get user input
                user_input = self._get_input()
                
                # Process commands
                if user_input:
                    self._process_input(user_input)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except EOFError:
                break
        
        self.running = False
    
    def _get_input(self) -> str:
        """Get user input with prompt."""
        try:
            name = self.profile.get("name", "User") if self.profile else "User"
            
            # Show voice indicator in prompt if voice is available
            voice_indicator = ""
            if self.voice_input:
                voice_indicator = " 🎤(speak)"
            elif self.voice_output:
                voice_indicator = " 🔊"
            
            prompt = f"\n[{name}]{voice_indicator}> "
            
            # Check for voice input first
            if self.voice_input:
                print(prompt, end="")
                sys.stdout.flush()
                
                # Check if user wants to type instead
                key = readchar.readkey()
                
                if key == '\n' or key == '\r':
                    # Enter pressed - use voice input
                    try:
                        text = self.voice_input.listen(timeout=5, phrase_time_limit=10)
                        if text:
                            print(f"   You said: {text}")
                            return text
                        else:
                            return ""  # No speech detected
                    except Exception as e:
                        print(f"⚠ Voice input error: {e}")
                        return input().strip()
                elif key == 't':
                    # 't' key - switch to text input
                    return input(" > ").strip()
                else:
                    # Other key - treat as text input
                    text = input(" > ").strip()
                    return key + text
            else:
                if HAS_READCHAR:
                    sys.stdout.write(prompt)
                    sys.stdout.flush()
                    return input().strip()
                else:
                    return input(prompt).strip()
                
        except (KeyboardInterrupt, EOFError):
            raise
    
    def _process_input(self, user_input: str):
        """Process user input."""
        # Handle commands
        if user_input.lower() in ["quit", "exit", "q"]:
            self.running = False
            print("👋 Goodbye!")
            return
        
        if user_input.lower() in ["help", "h", "?"]:
            self._show_help()
            return
        
        if user_input.lower() == "clear":
            os.system("clear" if os.name == "posix" else "cls")
            return
        
        if user_input.lower() == "profile":
            self._show_profile()
            return
        
        if user_input.lower() == "onboard":
            from onboarding.flow import OnboardingFlow
            flow = OnboardingFlow()
            flow.run()
            self._load_profile()
            return
        
        # Cloud sync commands
        if user_input.lower() in ["backup", "backup now"]:
            self._run_backup()
            return
        
        if user_input.lower() == "restore":
            self._run_restore()
            return
        
        if user_input.lower() == "sync":
            self._run_sync()
            return
        
        if user_input.lower() == "sync status":
            self._show_sync_status()
            return
        
        if user_input.lower() == "list backups":
            self._list_backups()
            return
        
        # Generate response
        response = self._generate_response(user_input)
        
        # Display response
        self._display_response(response)
        
        # Add to history
        self.history.append({
            "user": user_input,
            "assistant": response
        })
    
    def _generate_response(self, user_input: str) -> str:
        """Generate a response from the brain."""
        if self.brain is None or not self.brain.is_loaded:
            # Mock response for testing
            return "🤖 (No model loaded) - Install a model and try again."
        
        # Build system prompt with user context
        system_prompt = self._build_system_prompt()
        prompt = f"{system_prompt}\n\nUser: {user_input}\nAssistant:"
        
        try:
            response = self.brain.generate(
                prompt=prompt,
                max_tokens=256,
                temperature=0.7
            )
            return response
        except Exception as e:
            return f"⚠ Error: {e}"
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt with user context."""
        base_prompt = "You are PocketMind, a helpful AI assistant."
        
        # Add user preferences if available
        if self.profile:
            name = self.profile.get("name", "")
            if name:
                base_prompt += f" The user's name is {name}."
            
            # Response style
            style = self.profile.get("response_style", "")
            if style == "brief":
                base_prompt += " Keep responses concise and to the point."
            elif style == "detailed":
                base_prompt += " Provide detailed and thorough responses."
            elif style == "casual":
                base_prompt += " Use a casual, friendly tone."
            elif style == "professional":
                base_prompt += " Use a professional, formal tone."
            
            # Emoji preference
            if not self.profile.get("use_emojis", True):
                base_prompt += " Do not use emojis."
        
        return base_prompt
    
    def _display_response(self, response: str):
        """Display the AI response."""
        print(f"\n🤖 Assistant:")
        # Word wrap for long responses
        words = response.split()
        line = ""
        for word in words:
            if len(line) + len(word) > 70:
                print(f"   {line}")
                line = word
            else:
                line += " " + word if line else word
        if line:
            print(f"   {line}")
        
        # Speak response if voice output is enabled
        if self.voice_output:
            self.voice_output.speak(response, block=False)
        
        print()
    
    def _show_help(self):
        """Show help message."""
        # Check if cloud sync is available
        cloud_sync_line = ""
        try:
            from cloud_sync import CloudSync
            if CloudSync().can_use_cloud():
                cloud_sync_line = "   sync         - Sync backup to cloud\n"
            else:
                cloud_sync_line = "   sync status  - Show sync status (premium)\n"
        except Exception:
            pass
        
        print(f"""
📖 Available Commands:
   help, h, ?    - Show this help message
   quit, exit, q - Exit the program
   clear         - Clear the screen
   profile       - Show user profile
   onboard       - Run onboarding setup
   backup        - Create a local backup
   restore       - Restore from a backup
   list backups  - Show available backups
{cloud_sync_line}""")
    
    def _show_profile(self):
        """Show user profile."""
        print("\n👤 User Profile:")
        if not self.profile:
            print("   No profile set. Run --onboard to create one.")
        else:
            for key, value in self.profile.items():
                if key != "important_dates":  # Skip complex nested data
                    print(f"   {key}: {value}")
        print()
    
    def _run_backup(self):
        """Run backup command."""
        try:
            from cloud_sync import CloudSync
            sync = CloudSync()
            print("\n📦 Creating backup...")
            result = sync.create_backup()
            if result:
                print(f"✅ Backup created!")
        except Exception as e:
            print(f"❌ Backup error: {e}")
    
    def _run_restore(self):
        """Run restore command."""
        try:
            from cloud_sync import CloudSync
            sync = CloudSync()
            backups = sync.list_backups()
            if not backups:
                print("\n📭 No backups found.")
                return
            
            print("\nAvailable backups:")
            for i, b in enumerate(backups[:5], 1):
                print(f"   {i}. {b['name']}")
            
            choice = input("\nRestore which? (number or name): ").strip()
            
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(backups):
                    name = backups[idx]["name"]
                else:
                    print("❌ Invalid selection")
                    return
            else:
                name = choice
            
            confirm = input(f"Restore '{name}'? (y/N): ").strip().lower()
            if confirm == 'y':
                sync.restore_backup(name=name)
        except Exception as e:
            print(f"❌ Restore error: {e}")
    
    def _run_sync(self):
        """Run cloud sync command."""
        try:
            from cloud_sync import CloudSync
            sync = CloudSync()
            
            if not sync.can_use_cloud():
                print("\n💎 Cloud sync requires premium subscription!")
                print("   Run: python main.py --set-tier premium")
                return
            
            print("\n☁️ Syncing to cloud...")
            sync.sync_to_cloud()
        except Exception as e:
            print(f"❌ Sync error: {e}")
    
    def _show_sync_status(self):
        """Show sync status."""
        try:
            from cloud_sync import CloudSync
            sync = CloudSync()
            status = sync.get_status()
            
            tier = status["tier"].upper()
            print(f"\n☁️ Sync Status")
            print(f"   Tier: {'🟢' if status['can_cloud_sync'] else '⚪'} {tier}")
            print(f"   Provider: {status['provider']}")
            print(f"   Last sync: {status['last_sync'] or 'Never'}")
            print(f"   Backups: {status['backup_count']}")
            
            if not status['can_cloud_sync']:
                print("\n💎 Upgrade to premium for cloud sync!")
        except Exception as e:
            print(f"❌ Status error: {e}")
    
    def _list_backups(self):
        """List backups."""
        try:
            from cloud_sync import CloudSync
            sync = CloudSync()
            backups = sync.list_backups()
            
            print("\n📋 Backups:")
            if not backups:
                print("   No backups yet. Run 'backup' to create one.")
            else:
                for b in backups:
                    size_kb = b.get("size", 0) / 1024
                    created = b.get("created", "")[:19]
                    print(f"   • {b['name']} ({size_kb:.1f} KB, {created})")
        except Exception as e:
            print(f"❌ Error: {e}")
