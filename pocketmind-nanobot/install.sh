#!/bin/bash
# PocketMind-Nanobot Quick Setup Script

set -e

echo "🧠 PocketMind-Nanobot Setup"
echo "============================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.10+ first."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if nanobot is installed
if ! command -v nanobot &> /dev/null; then
    echo "📦 Installing Nanobot..."
    pip3 install nanobot-ai
else
    echo "✅ Nanobot already installed"
fi

# Create workspace directory
WORKSPACE="$HOME/.pocketmind/workspace"
echo ""
echo "📁 Creating workspace at $WORKSPACE..."

mkdir -p "$WORKSPACE/memory"
mkdir -p "$WORKSPACE/skills/pocketmind"

# Copy template files
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cp -r "$SCRIPT_DIR/workspace/"* "$WORKSPACE/"

# Create config directory
mkdir -p "$HOME/.nanobot"

# Copy config if it doesn't exist
if [ ! -f "$HOME/.nanobot/config.json" ]; then
    cp "$SCRIPT_DIR/config/config.json.example" "$HOME/.nanobot/config.json"
    echo ""
    echo "⚠️  Please edit $HOME/.nanobot/config.json and add your API key!"
else
    echo "✅ Config already exists at $HOME/.nanobot/config.json"
fi

echo ""
echo "============================"
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit ~/.nanobot/config.json and add your API key"
echo "2. Run: nanobot agent -w $WORKSPACE"
echo ""
echo "For Termux/mobile, see docs/TERMUX.md"
echo "For onboarding details, see docs/ONBOARDING.md"
