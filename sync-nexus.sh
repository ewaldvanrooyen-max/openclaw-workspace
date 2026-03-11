#!/bin/bash
# WolfPack Empire - Workspace Sync Script
# Run this on Nexus to sync with VPS

REPO_URL="https://github.com/ewaldvanrooyen-max/openclaw-workspace.git"
SYNC_DIR="/home/aris-steyn/openclaw-workspace"

echo "🐺 WolfPack Empire Sync"
echo "======================"

# Clone or pull
if [ -d "$SYNC_DIR/.git" ]; then
    echo "📥 Pulling latest changes..."
    cd "$SYNC_DIR"
    git pull
else
    echo "📦 Cloning workspace..."
    cd /home/aris-steyn
    git clone "$REPO_URL" openclaw-workspace
    cd openclaw-workspace
fi

echo "✅ Sync complete!"
echo ""
echo "📁 Files synced:"
ls -la *.md 2>/dev/null | head -10

# Sync key files to memory folder for agent access
echo ""
echo "📋 Syncing to memory..."
mkdir -p memory
cp -n *.md memory/ 2>/dev/null
echo "✅ Done!"
