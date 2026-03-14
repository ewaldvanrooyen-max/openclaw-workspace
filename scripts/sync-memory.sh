#!/bin/bash
# Memory Sync Script for Nexus
# Pulls latest memory files from VPS (via GitHub)
# Run via cron: */15 * * * * /usr/local/bin/sync-memory.sh

WORKSPACE_DIR="$HOME/openclaw-workspace"
LOG_FILE="$HOME/.memory-sync.log"

echo "=== Memory Sync: $(date) ===" >> $LOG_FILE

# If workspace doesn't exist, clone it
if [ ! -d "$WORKSPACE_DIR" ]; then
    echo "Cloning workspace..." >> $LOG_FILE
    git clone https://github.com/ewaldvanrooyen-max/openclaw-workspace.git "$WORKSPACE_DIR" >> $LOG_FILE 2>&1
fi

# Pull latest changes
cd "$WORKSPACE_DIR"
git fetch origin >> $LOG_FILE 2>&1
git pull origin master >> $LOG_FILE 2>&1

# Check if memory files updated
if [ -d "$WORKSPACE_DIR/memory" ]; then
    echo "Memory files synced successfully" >> $LOG_FILE
    ls -la "$WORKSPACE_DIR/memory/" | head -5 >> $LOG_FILE
else
    echo "WARNING: memory directory not found" >> $LOG_FILE
fi

echo "=== End Sync ===" >> $LOG_FILE
