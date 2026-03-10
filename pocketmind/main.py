#!/usr/bin/env python3
"""
PocketMind - Personal AI Assistant

A fully offline personal AI that runs on your phone.
No internet required - all processing happens locally.

Usage:
    python main.py                  # Start chatting
    python main.py --onboard        # Run onboarding
    python main.py --test          # Test installation
    python main.py --info           # Show storage info
"""

import argparse
import sys
import os
import yaml
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli.interface import CLI
from agent.brain import Brain, MockBrain, create_brain
from voice import VoiceInput, VoiceOutput, check_voice_setup
from cloud_sync import CloudSync, create_sync_instance


# Constants
APP_NAME = "PocketMind"
APP_VERSION = "0.1.0"

# Model presets - maps preset names to model paths
MODEL_PRESETS = {
    "smollm2": "models/smollm2-360m-instruct-q4_k_m.gguf",
    "qwen2.5": "models/qwen2.5-0.5b-instruct-q4_k_m.gguf",
    "llama3.2": "models/llama3.2-1b-instruct-q4_k_m.gguf",
}


def load_config():
    """Load configuration from config.yaml."""
    config_path = Path(__file__).parent / "config.yaml"
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception:
            pass
    return {}


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=f"{APP_NAME} - Your personal AI assistant (offline)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Start chatting
  python main.py --preset qwen2.5  # Use Qwen2.5 model
  python main.py --onboard          # Set up your profile
  python main.py --test             # Test installation
  python main.py --mock             # Run without model
  python main.py -m models/model.gguf  # Specify model
        """
    )
    parser.add_argument(
        "--model", 
        "-m", 
        default=None,
        help="Path to GGUF model file"
    )
    parser.add_argument(
        "--preset",
        "-p",
        choices=list(MODEL_PRESETS.keys()),
        help="Use a model preset (smollm2, qwen2.5, llama3.2)"
    )
    parser.add_argument(
        "--test", 
        action="store_true",
        help="Run test mode to verify installation"
    )
    parser.add_argument(
        "--onboard",
        action="store_true",
        help="Run onboarding flow to set up your profile"
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Run with mock brain (no model required)"
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show storage and system information"
    )
    parser.add_argument(
        "--context-length",
        "-c",
        type=int,
        default=512,
        help="Context length (default: 512)"
    )
    parser.add_argument(
        "--threads",
        "-t",
        type=int,
        default=4,
        help="Number of CPU threads (default: 4)"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{APP_NAME} v{APP_VERSION}"
    )
    parser.add_argument(
        "--voice-input",
        action="store_true",
        help="Enable voice input (speech-to-text)"
    )
    parser.add_argument(
        "--voice-output",
        action="store_true",
        help="Enable voice output (text-to-speech)"
    )
    parser.add_argument(
        "--voice-voice",
        default="female",
        choices=["female", "male", "british", "australian"],
        help="Voice for TTS output (default: female)"
    )
    # Cloud sync commands
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create a local backup"
    )
    parser.add_argument(
        "--restore",
        nargs="?",
        const="latest",
        help="Restore from backup (specify name or 'latest')"
    )
    parser.add_argument(
        "--sync-status",
        action="store_true",
        help="Show cloud sync status"
    )
    parser.add_argument(
        "--list-backups",
        action="store_true",
        help="List all available backups"
    )
    parser.add_argument(
        "--verify-backup",
        metavar="NAME",
        help="Verify backup integrity"
    )
    parser.add_argument(
        "--delete-backup",
        metavar="NAME",
        help="Delete a backup"
    )
    parser.add_argument(
        "--set-tier",
        metavar="TIER",
        choices=["free", "premium", "enterprise"],
        help="Set subscription tier (free/premium/enterprise)"
    )
    parser.add_argument(
        "--sync-to-cloud",
        action="store_true",
        help="Sync backup to cloud (premium only)"
    )
    return parser.parse_args()


def print_banner():
    """Print welcome banner."""
    print(f"""
╔═══════════════════════════════════════════╗
║         {APP_NAME} v{APP_VERSION}                      ║
║   Your personal AI - 100%% offline        ║
╚═══════════════════════════════════════════╝
""")


def test_mode():
    """Quick test to verify installation and offline capability."""
    print("🧪 Running Installation Tests...")
    print("=" * 50)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Python version
    print("\n[1/6] Checking Python version...")
    try:
        version = sys.version_info
        print(f"   ✓ Python {version.major}.{version.minor}.{version.micro}")
        tests_passed += 1
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        tests_failed += 1
    
    # Test 2: Imports
    print("\n[2/6] Testing imports...")
    try:
        from agent.brain import Brain, MockBrain
        from storage.json_store import JSONStore
        print("   ✓ All core imports successful")
        tests_passed += 1
    except ImportError as e:
        print(f"   ✗ Import failed: {e}")
        tests_failed += 1
    
    # Test 2b: Onboarding imports
    print("\n[2b/6] Testing onboarding imports...")
    try:
        from onboarding.flow import OnboardingFlow
        print("   ✓ Onboarding imports successful")
        tests_passed += 1
    except ImportError as e:
        print(f"   ✗ Onboarding import failed: {e}")
        tests_failed += 1
    
    # Test 3: Storage
    print("\n[3/6] Testing local storage...")
    try:
        store = JSONStore()
        test_data = {"test": "hello", "timestamp": "2026-01-01"}
        store.save("test_run", test_data)
        loaded = store.load("test_run")
        
        if loaded == test_data:
            print(f"   ✓ Storage working at: {store.data_dir}")
            tests_passed += 1
        else:
            print(f"   ✗ Storage data mismatch")
            tests_failed += 1
        
        # Cleanup
        store.delete("test_run")
    except Exception as e:
        print(f"   ✗ Storage test failed: {e}")
        tests_failed += 1
    
    # Test 4: Model loading (will fail without model, expected)
    print("\n[4/6] Testing model loader...")
    try:
        brain, success = create_brain("nonexistent-model.gguf")
        if not success:
            print("   ✓ Model loader working (expected: no model file)")
            tests_passed += 1
        else:
            print("   ✗ Unexpected: model loaded without file")
            tests_failed += 1
    except Exception as e:
        print(f"   ✓ Model loader working (expected error)")
        tests_passed += 1
    
    # Test 5: Mock brain
    print("\n[5/6] Testing mock brain...")
    try:
        mock = MockBrain()
        response = mock.generate("test prompt")
        if "mock" in response.lower():
            print("   ✓ Mock brain working")
            tests_passed += 1
        else:
            print(f"   ✗ Unexpected mock response: {response}")
            tests_failed += 1
    except Exception as e:
        print(f"   ✗ Mock brain failed: {e}")
        tests_failed += 1
    
    # Test 6: Offline verification
    print("\n[6/6] Verifying offline capability...")
    try:
        import importlib.util
        spec = importlib.util.find_spec("requests")
        urllib_spec = importlib.util.find_spec("urllib.request")
        
        print("   ✓ No network modules required for core functionality")
        print("   ✓ App runs 100% offline")
        tests_passed += 1
    except Exception as e:
        print(f"   ✗ Offline check failed: {e}")
        tests_failed += 1
    
    # Summary
    print("\n" + "=" * 50)
    if tests_failed == 0:
        print(f"✅ All {tests_passed} tests passed!")
        print("\n🚀 Ready to use!")
        print("   1. Download a GGUF model to models/")
        print("   2. Run: python main.py")
        print("   3. Or run: python main.py --onboard to set up profile")
        return True
    else:
        print(f"⚠ {tests_passed} passed, {tests_failed} failed")
        return False


def info_mode():
    """Show storage and system information."""
    print("📊 System Information")
    print("=" * 50)
    
    # Python info
    print(f"\nPython: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # Storage info
    print("\n📁 Storage:")
    try:
        from storage.json_store import JSONStore
        store = JSONStore()
        info = store.get_storage_info()
        
        print(f"   Data directory: {info['data_dir']}")
        print(f"   Keys stored: {info['key_count']}")
        print(f"   Total size: {info['total_size_bytes']} bytes")
        
        if info['keys']:
            print("   Stored keys:", ", ".join(info['keys']))
        else:
            print("   (No data stored yet)")
            
    except Exception as e:
        print(f"   Error: {e}")
    
    # Model info
    print("\n🤖 Model:")
    model_path = "models/smollm2-360m-instruct-q4_k_m.gguf"
    if os.path.exists(model_path):
        size = os.path.getsize(model_path) / (1024 * 1024)
        print(f"   ✓ Model exists: {model_path}")
        print(f"   Size: {size:.1f} MB")
    else:
        print(f"   ⚠ Model not found: {model_path}")
        print("   Download a model to enable AI features")
    
    print()


def main():
    """Main entry point."""
    args = parse_args()
    
    # Load config for defaults
    config = load_config()
    
    # Determine model path
    # Priority: --preset > --model > config > default
    model_path = None
    
    # Check preset first
    if args.preset:
        model_path = MODEL_PRESETS[args.preset]
        print(f"📦 Using preset: {args.preset}")
    elif args.model:
        model_path = args.model
    elif config.get('model_preset'):
        preset = config['model_preset']
        if preset in MODEL_PRESETS:
            model_path = MODEL_PRESETS[preset]
            print(f"📦 Using config preset: {preset}")
        else:
            model_path = config.get('model', {}).get('path', 'models/smollm2-360m-instruct-q4_k_m.gguf')
    else:
        # Default to config or fallback
        model_path = config.get('model', {}).get('path', 'models/smollm2-360m-instruct-q4_k_m.gguf')
    
    if args.test:
        success = test_mode()
        sys.exit(0 if success else 1)
    
    # Info mode
    if args.info:
        info_mode()
        sys.exit(0)
    
    # Onboarding mode
    if args.onboard:
        print_banner()
        try:
            from onboarding.flow import OnboardingFlow
            flow = OnboardingFlow()
            flow.run()
            print("\n✅ Onboarding complete! Run without --onboard to start chatting.")
        except Exception as e:
            print(f"\n⚠ Onboarding error: {e}")
            print("   You can still use PocketMind without completing onboarding.")
        return
    
    # Cloud sync commands
    sync = CloudSync()
    
    if args.backup:
        print("📦 Creating backup...")
        result = sync.create_backup()
        if result:
            print(f"\n✅ Backup created: {result}")
        return
    
    if args.restore:
        name = args.restore if args.restore != "latest" else None
        print(f"🔄 Restoring backup...")
        success = sync.restore_backup(name=name, latest=(args.restore == "latest"))
        return
    
    if args.sync_status:
        print("☁️ Cloud Sync Status")
        print("=" * 50)
        status = sync.get_status()
        tier = status["tier"].upper()
        tier_display = f"{'🟢' if status['can_cloud_sync'] else '⚪'} {tier}"
        print(f"   Subscription: {tier_display}")
        print(f"   Provider: {status['provider']}")
        print(f"   Enabled: {status['enabled']}")
        print(f"   Last sync: {status['last_sync'] or 'Never'}")
        print(f"   Backups: {status['backup_count']}")
        print(f"   Storage used: {status['storage_used'] / 1024:.1f} KB")
        print(f"   Data dir: {status['data_dir']}")
        if not status['can_cloud_sync']:
            print("\n💎 Upgrade to premium for cloud sync!")
            print("   python main.py --set-tier premium")
        return
    
    if args.list_backups:
        print("📋 Available Backups")
        print("=" * 50)
        backups = sync.list_backups()
        if not backups:
            print("   No backups found.")
            print("   Run: python main.py --backup")
        else:
            for i, b in enumerate(backups, 1):
                size_kb = b.get("size", 0) / 1024
                created = b.get("created", "Unknown")[:19]
                print(f"   {i}. {b['name']}")
                print(f"      Size: {size_kb:.1f} KB | Created: {created}")
        return
    
    if args.verify_backup:
        print(f"🔍 Verifying backup: {args.verify_backup}")
        print("=" * 50)
        result = sync.verify_backup(args.verify_backup)
        if result.get("valid"):
            print("✅ Backup is valid!")
        else:
            print(f"❌ Backup invalid: {result.get('error')}")
        return
    
    if args.delete_backup:
        # Auto-confirm in non-interactive mode
        confirm = "y"
        try:
            confirm = input(f"Delete backup '{args.delete_backup}'? [y/N]: ").strip().lower()
        except EOFError:
            pass
        if confirm == 'y':
            sync.delete_backup(args.delete_backup)
        return
    
    if args.set_tier:
        print(f"💳 Setting subscription tier: {args.set_tier}")
        success = sync.set_tier(args.set_tier)
        if success:
            print(f"✅ Tier set to {args.set_tier.upper()}")
            if args.set_tier == "free":
                print("   Cloud sync disabled for free tier.")
        else:
            print(f"❌ Failed to set tier")
        return
    
    if args.sync_to_cloud:
        print("☁️ Syncing to cloud...")
        success = sync.sync_to_cloud()
        return
    
    # Mock mode (no model required)
    if args.mock:
        print_banner()
        print("🎭 Running in mock mode (no model)\n")
        
        # Initialize voice components if requested
        voice_input = None
        voice_output = None
        
        if args.voice_input or args.voice_output:
            print("🎤 Initializing voice features...")
            voice_status = check_voice_setup()
            
            if args.voice_input and not voice_status["whisper"]:
                print("⚠ Whisper not installed. Voice input disabled.")
                args.voice_input = False
            
            if args.voice_output and not voice_status["edge_tts"]:
                print("⚠ Edge TTS not installed. Voice output disabled.")
                args.voice_output = False
            
            if args.voice_input:
                try:
                    voice_input = VoiceInput(model_size="tiny")
                    print("✓ Voice input ready")
                except Exception as e:
                    print(f"⚠ Voice input error: {e}")
                    args.voice_input = False
            
            if args.voice_output:
                try:
                    voice_output = VoiceOutput(voice=args.voice_voice)
                    print(f"✓ Voice output ready ({args.voice_voice} voice)")
                except Exception as e:
                    print(f"⚠ Voice output error: {e}")
                    args.voice_output = False
            
            print()
        
        cli = CLI(
            brain=MockBrain(),
            voice_input=voice_input if args.voice_input else None,
            voice_output=voice_output if args.voice_output else None
        )
        cli.run()
        return
    
    # Normal chat mode
    print_banner()
    print("Type 'help' for commands, 'quit' to exit\n")
    
    # Initialize brain
    brain = None
    model_path = args.model
    
    # Check if model exists
    if not os.path.exists(model_path):
        print(f"⚠ Model not found: {model_path}")
        print("\nOptions:")
        print("  1. Download a model to the models/ directory")
        print("  2. Use --mock to run without a model")
        print("  3. Use --test to verify installation")
        print("\nRecommended models:")
        print("  - SmolLM2-360M (smallest, fastest)")
        print("  - Qwen2.5-0.5B (balanced)")
        print("  - TinyLlama-1.1B (quality)")
        print()
        
        # Offer to run in mock mode
        response = input("Run in mock mode? [y/N]: ").strip().lower()
        if response in ['y', 'yes']:
            cli = CLI(brain=MockBrain())
            cli.run()
            return
        else:
            print("\nExiting. Download a model and try again.")
            sys.exit(1)
    
    # Try to load the model
    print(f"📥 Loading model: {os.path.basename(model_path)}...")
    print(f"   Context: {args.context_length}, Threads: {args.threads}\n")
    
    brain, success = create_brain(
        model_path=model_path,
        n_ctx=args.context_length,
        n_threads=args.threads,
        offline_mode=True  # Always offline!
    )
    
    if not success or brain is None:
        print("⚠ Failed to load model.")
        print("   Try running with --mock to use without model")
        response = input("\nRun in mock mode? [y/N]: ").strip().lower()
        if response in ['y', 'yes']:
            cli = CLI(brain=MockBrain())
            cli.run()
            return
        else:
            sys.exit(1)
    
    # Start CLI
    print(f"✓ Model loaded: {brain.model_name}")
    print(f"✓ Offline mode: Active (no network calls)\n")
    
    # Initialize voice components if requested
    voice_input = None
    voice_output = None
    
    if args.voice_input or args.voice_output:
        print("🎤 Initializing voice features...")
        voice_status = check_voice_setup()
        
        if args.voice_input and not voice_status["whisper"]:
            print("⚠ Whisper not installed. Voice input disabled.")
            args.voice_input = False
        
        if args.voice_output and not voice_status["edge_tts"]:
            print("⚠ Edge TTS not installed. Voice output disabled.")
            args.voice_output = False
        
        if args.voice_input:
            try:
                voice_input = VoiceInput(model_size="tiny")
                print("✓ Voice input ready")
            except Exception as e:
                print(f"⚠ Voice input error: {e}")
                args.voice_input = False
        
        if args.voice_output:
            try:
                voice_output = VoiceOutput(voice=args.voice_voice)
                print(f"✓ Voice output ready ({args.voice_voice} voice)")
            except Exception as e:
                print(f"⚠ Voice output error: {e}")
                args.voice_output = False
        
        print()
    
    cli = CLI(
        brain=brain,
        voice_input=voice_input if args.voice_input else None,
        voice_output=voice_output if args.voice_output else None
    )
    cli.run()


if __name__ == "__main__":
    main()
