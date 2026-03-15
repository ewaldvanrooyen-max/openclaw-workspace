#!/bin/bash
# PP-03: Phone Edition Deployment
# Set up phone edition with WebUI

set -e

WORKSPACE="/root/.openclaw/workspace"
TODAY=$(date +%Y-%m-%d)

echo "=== PP-03: Phone Edition Deployment ==="
echo "Date: $TODAY"
echo ""

# Check existing web interface
echo "Checking existing web interfaces..."
if [ -d "$WORKSPACE/pocketmind" ]; then
    echo "✓ pocketmind/ found"
    
    # Check for web files
    if [ -f "$WORKSPACE/pocketmind/index.html" ] || [ -f "$WORKSPACE/pocketmind/pocketpal-web.html" ]; then
        echo "✓ Web interface files exist"
    fi
fi

echo ""
echo "Checking mission-control for PocketPal integration..."
if [ -d "$WORKSPACE/mlc-website" ]; then
    echo "✓ mlc-website/ found (potential integration point)"
fi

echo ""
echo "Status: Phone edition analysis complete"
echo "Recommendation: Consider deploying as sub-module in mission-control"
exit 0
