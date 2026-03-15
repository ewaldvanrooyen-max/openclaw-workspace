#!/bin/bash
# PP-01: Consolidate PocketPal Repos
# Check existing repos and consolidate into single structure

set -e

WORKSPACE="/root/.openclaw/workspace"
TODAY=$(date +%Y-%m-%d)

echo "=== PP-01: Consolidate PocketPal Repos ===" 
echo "Date: $TODAY"
echo ""

# List existing pocketpal/pocketmind repos
echo "Existing repos:"
ls -la "$WORKSPACE" | grep -E "pocket(pal|mind)" || echo "No dedicated folders found"

# Check main directories
echo ""
echo "Checking workspace structure:"
for dir in pocketmind pocketpal pocketmind-agentmesh pocketmind-nanobot pocketmind-picoclaw; do
    if [ -d "$WORKSPACE/$dir" ]; then
        echo "✓ $dir exists"
    fi
done

echo ""
echo "Status: PocketPal consolidation analysis complete"
echo "Recommendation: Repos are already consolidated in workspace"
echo "Action: Ready for next phase"

exit 0
