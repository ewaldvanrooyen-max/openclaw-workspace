#!/bin/bash
# PocketMind Install Script for Termux
# Run: bash install.sh

set -e

echo "🐺 PocketMind Agentic Mesh Installer"
echo "===================================="
echo ""

# Update
echo "📦 Updating packages..."
pkg update -y

# Install Python
echo "🐍 Installing Python..."
pkg install -y python git

# Install llama.cpp (or use pre-built)
echo "🔧 Installing llama.cpp..."
pkg install -y cmake llvm

# Create directories
echo "📁 Creating directories..."
mkdir -p ~/.pocketmind/models
mkdir -p ~/.pocketmind/nanobots

# Download model (SmolLM2-360M - lightest!)
echo "📥 Downloading model..."
cd ~/.pocketmind/models
if [ ! -f "smollm2-360m-q4_k_m.gguf" ]; then
    wget -O smollm2-360m-q4_k_m.gguf \
        "https://huggingface.co/TheBloke/SmolLM2-360M-Instruct-GGUF/resolve/main/smollm2-360m-instruct-q4_k_m.gguf"
fi

# Clone nanobots
echo "🤖 Setting up nanobots..."
cd ~/.pocketmind
git clone https://github.com/ewaldvanrooyen-max/pocketmind-agentmesh.git .

echo ""
echo "✅ Installation complete!"
echo ""
echo "🚀 Run PocketMind:"
echo "   cd ~/.pocketmind"
echo "   python main.py"
echo ""
