# PocketPal MiniMax Setup Guide

## Current Status

✅ **PocketPal is running on port 5005**
✅ **MiniMax API integration is complete**
⚠️ **MiniMax API key is NOT configured**

## What Was Done

1. **Located PocketPal**: The Flask app is at `/root/.openclaw/workspace/pocketmind/`
2. **Added MiniMax API support**: Created `MiniMaxBrain` class that connects to MiniMax API
3. **Updated configuration**: Environment variables control API connection
4. **Added health endpoint**: Available at `/api/health`

## How to Enable MiniMax

### Option 1: Set Environment Variable (Quick)

```bash
export MINIMAX_API_KEY=your_api_key_here
```

Then restart PocketPal:
```bash
pkill -f 'python3 web.py'
cd /root/.openclaw/workspace/pocketmind
python3 web.py &
```

### Option 2: Permanent Setup

Add to `/root/.bashrc`:
```bash
export MINIMAX_API_KEY=your_api_key_here
export MINIMAX_MODEL=MiniMax-M2.5
```

Then restart your shell and PocketPal.

## Getting a MiniMax API Key

1. Go to https://platform.minimaxi.com/
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and use it above

## Testing

After setting the API key:

```bash
# Check health
curl http://localhost:5005/api/health

# Test chat
curl -X POST http://localhost:5005/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"message": "Hello!"}'
```

## Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| MINIMAX_API_KEY | (none) | Your API key from minimaxi.com |
| MINIMAX_BASE_URL | https://api.minimax.io/v1 | API endpoint |
| MINIMAX_MODEL | MiniMax-M2.5 | Model to use |

## Fallback

Without MINIMAX_API_KEY, PocketPal uses MockBrain (test mode).
