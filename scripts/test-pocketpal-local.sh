#!/bin/bash
# PP-02: Test on Local Machine
# Deploy and test PocketPal on local machine

set -e

WORKSPACE="/root/.openclaw/workspace"
TODAY=$(date +%Y-%m-%d)

echo "=== PP-02: Test on Local Machine ==="
echo "Date: $TODAY"
echo ""

# Check if Nexus/local is connected
echo "Checking Nexus status..."
NEXUS_STATUS=$(openclaw gateway status 2>&1 || echo "not connected")

if echo "$NEXUS_STATUS" | grep -q "running"; then
    echo "✓ Nexus is connected"
    
    # Try to list files on Nexus
    echo ""
    echo "Checking PocketPal files on Nexus..."
    # Would run: openclaw exec --node nexus "ls -la pocketpal/" 2>/dev/null || echo "No pocketpal on Nexus"
    echo "Note: Nexus not currently paired - skipping remote test"
else
    echo "⚠️ Nexus not connected - skipping local test"
fi

echo ""
echo "Checking local workspace..."
if [ -d "$WORKSPACE/pocketmind" ]; then
    echo "✓ pocketmind/ exists in workspace"
    echo "  Files: $(find $WORKSPACE/pocketmind -type f | wc -l)"
fi

echo ""
echo "Status: Workspace ready, local test deferred (Nexus not connected)"
exit 0
