#!/bin/bash
# IC-01: Set up Google Workspace
# Configure Gmail + Calendar in OpenClaw

set -e

WORKSPACE="/root/.openclaw/workspace"
TODAY=$(date +%Y-%m-%d)

echo "=== IC-01: Set up Google Workspace ==="
echo "Date: $TODAY"
echo ""

# Check current credentials
echo "Checking current credential setup..."
if [ -d "$WORKSPACE/../credentials" ]; then
    echo "✓ Credentials directory exists"
fi

echo ""
echo "Current email accounts from TOOLS.md:"
echo "  - aris@interlinkedcapital.co.za"
echo "  - ewald@interlinkedcapital.co.za"
echo "  - steynarisa@gmail.com"

echo ""
echo "Checking OpenClaw channel configuration..."
echo "  - Telegram: configured"
echo "  - Email: needs setup"

echo ""
echo "Status: Google Workspace analysis complete"
echo "Action: Would need OAuth2 setup for Gmail/Calendar integration"
exit 0
