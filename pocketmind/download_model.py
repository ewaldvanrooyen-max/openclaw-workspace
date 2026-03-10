#!/usr/bin/env python3
"""
PocketMind Model Downloader

Downloads GGUF models for offline use.
Supports selecting model quality based on device capability.

Usage:
    python download_model.py              # Interactive selection
    python download_model.py --preset qwen2.5
    python download_model.py --list      # Show available models
"""

import os
import sys
import argparse
import urllib.request
import shutil
from pathlib import Path


# Model definitions
MODELS = {
    "smollm2": {
        "name": "SmolLM2-360M",
        "filename": "smollm2-360m-instruct-q4_k_m.gguf",
        "url": "https://huggingface.co/TheBloke/SmolLM2-360M-Instruct-GGUF/resolve/main/smollm2-360m-instruct-q4_k_m.gguf",
        "alt_url": "https://huggingface.co/TheBloke/SmolLM2-360M-Instruct-GGUF/resolve/main/smollm2-360m-instruct-q4_k_m.gguf?download=true",
        "size_mb": 180,
        "description": "Ultra-light, fastest - best for low RAM devices",
        "min_ram": "500MB",
    },
    "qwen2.5": {
        "name": "Qwen2.5-0.5B",
        "filename": "qwen2.5-0.5b-instruct-q4_k_m.gguf",
        "url": "https://huggingface.co/TheBloke/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf",
        "alt_url": "https://huggingface.co/TheBloke/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf?download=true",
        "size_mb": 350,
        "description": "Balanced quality and speed - recommended for most phones",
        "min_ram": "1GB",
    },
    "llama3.2": {
        "name": "Llama3.2-1B",
        "filename": "llama3.2-1b-instruct-q4_k_m.gguf",
        "url": "https://huggingface.co/TheBloke/Llama-3.2-1B-Instruct-GGUF/resolve/main/llama3.2-1b-instruct-q4_k_m.gguf",
        "alt_url": "https://huggingface.co/TheBloke/Llama-3.2-1B-Instruct-GGUF/resolve/main/llama3.2-1b-instruct-q4_k_m.gguf?download=true",
        "size_mb": 640,
        "description": "Best quality - best responses, requires more RAM",
        "min_ram": "2GB",
    },
}


def get_models_dir():
    """Get the models directory path."""
    script_dir = Path(__file__).parent.resolve()
    models_dir = script_dir / "models"
    models_dir.mkdir(exist_ok=True)
    return models_dir


def list_models():
    """List all available models."""
    print("\n📦 Available Models for PocketMind")
    print("=" * 60)
    print()
    
    for key, model in MODELS.items():
        print(f"  {key}")
        print(f"    Name:     {model['name']}")
        print(f"    Size:     ~{model['size_mb']}MB")
        print(f"    RAM:      {model['min_ram']}+")
        print(f"    Quality:  {model['description']}")
        print()
    
    print("=" * 60)
    print("\n💡 Quick Reference:")
    print("  • SmolLM2    → Fastest, lowest RAM (500MB)")
    print("  • Qwen2.5    → Best balance (recommended)")
    print("  • Llama3.2   → Highest quality, needs 2GB+ RAM")
    print()


def download_with_progress(url: str, dest_path: Path, model_name: str):
    """Download a file with progress bar."""
    print(f"\n📥 Downloading {model_name}...")
    print(f"   URL: {url}")
    print(f"   Dest: {dest_path}")
    print()
    
    # Create a simple progress reporter
    def report_progress(block_num, block_size, total_size):
        if total_size > 0:
            downloaded = block_num * block_size
            percent = min(100, (downloaded / total_size) * 100)
            # Simple progress bar
            bar_length = 30
            filled = int(bar_length * percent / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"\r   [{bar}] {percent:.1f}% ", end="", flush=True)
    
    try:
        # Download the file
        urllib.request.urlretrieve(url, dest_path, reporthook=report_progress)
        print("\n\n✅ Download complete!")
        return True
        
    except Exception as e:
        print(f"\n\n❌ Download failed: {e}")
        if dest_path.exists():
            dest_path.unlink()
        return False


def download_model(preset: str, force: bool = False):
    """Download a specific model preset."""
    if preset not in MODELS:
        print(f"❌ Unknown preset: {preset}")
        print(f"   Available: {', '.join(MODELS.keys())}")
        return False
    
    model = MODELS[preset]
    models_dir = get_models_dir()
    dest_path = models_dir / model["filename"]
    
    # Check if already exists
    if dest_path.exists() and not force:
        size_mb = dest_path.stat().st_size / (1024 * 1024)
        print(f"✅ Model already exists: {dest_path}")
        print(f"   Size: {size_mb:.1f}MB")
        response = input("\n   Redownload? [y/N]: ").strip().lower()
        if response != 'y':
            return True
        print()
    
    # Try downloading
    success = False
    
    # Try primary URL
    try:
        success = download_with_progress(model["url"], dest_path, model["name"])
    except Exception as e:
        print(f"   Primary URL failed, trying alternate...")
    
    # Try alternate URL if primary failed
    if not success and dest_path.exists() is False:
        try:
            success = download_with_progress(model["alt_url"], dest_path, model["name"])
        except Exception as e:
            print(f"   Alternate URL also failed: {e}")
    
    if success:
        print(f"\n📁 Model saved to: {dest_path}")
        print(f"\n🚀 Run PocketMind with:")
        print(f"   python main.py -m {dest_path}")
        
        # Update config.yaml if it exists
        config_path = Path(__file__).parent / "config.yaml"
        if config_path.exists():
            import yaml
            try:
                with open(config_path, 'r') as f:
                    config = yaml.safe_load(f)
                
                config['model_preset'] = preset
                config['model']['path'] = str(dest_path)
                
                with open(config_path, 'w') as f:
                    yaml.dump(config, f, default_flow_style=False)
                
                print(f"\n✅ Updated config.yaml with preset: {preset}")
            except ImportError:
                print("\n⚠ yaml not installed - config not updated")
            except Exception as e:
                print(f"\n⚠ Could not update config: {e}")
        
        return True
    
    return False


def interactive_select():
    """Interactive model selection."""
    print("\n🧠 PocketMind Model Selector")
    print("=" * 50)
    print("\nSelect a model based on your device:")
    print()
    
    options = list(MODELS.keys())
    for i, key in enumerate(options, 1):
        model = MODELS[key]
        print(f"  {i}. {model['name']}")
        print(f"     Size: ~{model['size_mb']}MB | RAM: {model['min_ram']}")
        print(f"     {model['description']}")
        print()
    
    print("  0. Cancel")
    print()
    
    while True:
        choice = input("Enter choice [1-3]: ").strip()
        if choice == '0':
            print("Cancelled.")
            return False
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                preset = options[idx]
                return download_model(preset)
        except ValueError:
            pass
        
        print("Invalid choice. Enter 1, 2, or 3.")


def main():
    parser = argparse.ArgumentParser(
        description="Download GGUF models for PocketMind",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python download_model.py --list              # Show available models
  python download_model.py --preset qwen2.5   # Download Qwen2.5-0.5B
  python download_model.py --preset smollm2   # Download SmolLM2-360M
  python download_model.py --preset llama3.2  # Download Llama3.2-1B
  python download_model.py                     # Interactive selection
        """
    )
    
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List available models"
    )
    parser.add_argument(
        "--preset", "-p",
        choices=list(MODELS.keys()),
        help="Model preset to download"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Force re-download even if model exists"
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_models()
        return
    
    if args.preset:
        success = download_model(args.preset, force=args.force)
        sys.exit(0 if success else 1)
    
    # Interactive mode
    interactive_select()


if __name__ == "__main__":
    main()
