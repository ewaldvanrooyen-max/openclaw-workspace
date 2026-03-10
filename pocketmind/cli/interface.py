"""
PocketMind CLI Interface

The main terminal interface for interacting with PocketMind.
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
    """
    
    def __init__(self, brain=None):
        """
        Initialize the CLI.
        
        Args:
            brain: Brain instance for generating responses
        """
        self.brain = brain
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
            prompt = f"\n[{name}] > "
            
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
        print()
    
    def _show_help(self):
        """Show help message."""
        print("""
📖 Available Commands:
   help, h, ?    - Show this help message
   quit, exit, q - Exit the program
   clear         - Clear the screen
   profile       - Show user profile
   onboard       - Run onboarding setup
""")
    
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
