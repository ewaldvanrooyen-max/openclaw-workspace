#!/bin/bash
# PocketMind Termux Installation Script
# Run from Termux on Android

set -e

echo "🤖 Installing PocketMind..."
echo "=============================="

# Update packages
echo "[1/6] Updating packages..."
pkg update -y
pkg upgrade -y

# Install dependencies
echo "[2/6] Installing dependencies..."
pkg install -y python git curl wget unzip

# Install Python packages
echo "[3/6] Installing Python packages..."
pip install --upgrade pip
pip install mediapipe numpy

# Clone or setup PocketMind
echo "[4/6] Setting up PocketMind..."
if [ -d "$PREFIX/lib/pocketmind" ]; then
    echo "PocketMind already installed. Updating..."
    cd "$PREFIX/lib/pocketmind"
    git pull
else
    mkdir -p "$PREFIX/lib/pocketmind"
    # Create basic structure
    mkdir -p "$PREFIX/lib/pocketmind"/{src,models,configs}
    
    # Copy basic files (if running from cloned repo)
    if [ -f "$(dirname "$0")/src/core/engine.py" ]; then
        cp -r "$(dirname "$0")/src" "$PREFIX/lib/pocketmind/"
    fi
fi

# Download base model
echo "[5/6] Downloading base model..."
MODEL_DIR="$PREFIX/lib/pocketmind/models"
mkdir -p "$MODEL_DIR"

# Download SmolLM2-1.7B (placeholder - implement with actual download)
echo "Downloading SmolLM2-1.7B..."
echo "Note: Model download requires additional storage (~3GB)"
echo "Run 'python -m pocketmind download-model' after install"

# Create alias
echo "[6/6] Creating alias..."
echo "alias pocketmind='python -m pocketmind'" >> ~/.bashrc

echo ""
echo "✅ Installation complete!"
echo ""
echo "To start PocketMind:"
echo "  python -m pocketmind"
echo ""
echo "Or use the alias (restart terminal first):"
echo "  pocketmind"
echo ""
