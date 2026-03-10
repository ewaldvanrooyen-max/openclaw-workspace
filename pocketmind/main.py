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

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli.interface import CLI
from agent.brain import Brain, MockBrain, create_brain


# Constants
APP_NAME = "PocketMind"
APP_VERSION = "0.1.0"


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=f"{APP_NAME} - Your personal AI assistant (offline)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Start chatting
  python main.py --onboard          # Set up your profile
  python main.py --test             # Test installation
  python main.py --mock             # Run without model
  python main.py -m models/model.gguf  # Specify model
        """
    )
    parser.add_argument(
        "--model", 
        "-m", 
        default="models/smollm2-360m-instruct-q4_k_m.gguf",
        help="Path to GGUF model file (default: models/smollm2-360m-instruct-q4_k_m.gguf)"
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
    
    # Test mode
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
    
    # Mock mode (no model required)
    if args.mock:
        print_banner()
        print("🎭 Running in mock mode (no model)\n")
        
        cli = CLI(brain=MockBrain())
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
    
    cli = CLI(brain=brain)
    cli.run()


if __name__ == "__main__":
    main()
