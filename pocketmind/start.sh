#!/bin/bash
# PocketPal Startup Script
# Usage: ./start.sh [port]

PORT=${1:-5005}

echo "=========================================="
echo "🤖 PocketPal Starting on port $PORT"
echo "=========================================="

# Check for MiniMax API key
if [ -z "$MINIMAX_API_KEY" ]; then
    echo "⚠️  MINIMAX_API_KEY not set - using MockBrain"
    echo "   To enable MiniMax AI:"
    echo "   export MINIMAX_API_KEY=your_api_key_here"
    echo "   Get your key from: https://platform.minimaxi.com/"
else
    echo "✅ MiniMax API configured: $MINIMAX_MODEL"
fi

cd /root/.openclaw/workspace/pocketmind

# Start the Flask app
python3 web.py &
PID=$!

echo "🚀 PocketPal running on http://localhost:$PORT"
echo "   PID: $PID"
echo ""
echo "To stop: kill $PID"

wait $PID
