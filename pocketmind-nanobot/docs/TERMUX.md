# Running PocketMind on Termux (Android)

This guide covers how to run PocketMind-Nanobot on your Android device using Termux.

## Why PicoClaw for Mobile?

While this project uses Nanobot as the base framework, for **mobile (Termux) deployment**, we recommend using **[PicoClaw](https://github.com/sipeed/picoclaw)** instead because:

1. **Single Binary**: PicoClaw is a Go binary (~10MB), no Python dependencies needed
2. **Lower RAM**: Uses <10MB RAM vs Nanobot's ~100MB+
3. **Faster Startup**: Boots in <1 second
4. **Native Termux Support**: Explicitly tested on Termux

## Option 1: PicoClaw (Recommended for Termux)

### Install PicoClaw

```bash
# Update packages
pkg update && pkg upgrade

# Install required packages
pkg install git wget curl

# Download PicoClaw (choose your architecture)
# For ARM64 (most modern phones)
wget https://github.com/sipeed/picoclaw/releases/download/v0.1.x/picoclaw-linux-arm64
chmod +x picoclaw-linux-arm64

# Install proot for full Linux compatibility
pkg install proot
termux-chroot

# Run onboard
./picoclaw-linux-arm64 onboard
```

### Configure PicoClaw

Edit `~/.picoclaw/config.json`:

```json
{
  "model_list": [
    {
      "model_name": "claude-sonnet",
      "model": "anthropic/claude-sonnet-4-6",
      "api_key": "sk-or-v1-xxx"
    }
  ],
  "agents": {
    "defaults": {
      "model": "claude-sonnet",
      "workspace": "~/.picoclaw/workspace"
    }
  }
}
```

### Run PicoClaw

```bash
# Interactive mode
./picoclaw-linux-arm64 agent

# Or use termux-chroot for better compatibility
termux-chroot ./picoclaw-linux-arm64 agent
```

## Option 2: Nanobot on Termux (More Resources)

If you prefer the full Nanobot (Python) experience:

### Install Dependencies

```bash
pkg update && pkg upgrade
pkg install python git

# Install Nanobot
pip install nanobot-ai

# Clone PocketMind
git clone https://github.com/HKUDS/pocketmind-nanobot.git
cd pocketmind-nanobot
```

### Setup Workspace

```bash
# Copy workspace to Termux
mkdir -p ~/.pocketmind
cp -r workspace/* ~/.pocketmind/

# Configure
mkdir -p ~/.nanobot
cp config/config.json.example ~/.nanobot/config.json
nano ~/.nanobot/config.json  # Add your API key
```

### Run

```bash
# Set workspace
export NANOBOT_WORKSPACE=~/.pocketmind

# Interactive chat
nanobot agent -w ~/.pocketmind

# Or with config
nanobot agent -c ~/.nanobot/config.json -w ~/.pocketmind
```

## Termux Tips

### Keep Running in Background

Use `nohup` or Termux's built-in background execution:

```bash
# Run gateway in background
nanobot gateway &
```

### Wake Lock (Keep Awake)

```bash
# Install termux-api for wake lock
pkg install termux-api

# Keep device awake while running
termux-wake-lock
nanobot gateway
```

### Access from Other Devices

```bash
# Run gateway on all interfaces
nanobot gateway --host 0.0.0.0
```

Then access via your local network IP.

## Troubleshooting

### "Command not found" errors

```bash
# Add pip bin to PATH
export PATH=$PATH:$PREFIX/bin
```

### Storage Permission

```bash
# Grant storage permission if needed
termux-setup-storage
```

### Python Version Issues

```bash
# Check Python version (need 3.10+)
python --version

# If too old, install newer version
pkg install python3.11
```

## Performance Comparison

| Metric | Nanobot (Python) | PicoClaw (Go) |
|--------|-----------------|---------------|
| RAM Usage | ~100MB | <10MB |
| Startup | ~30s | <1s |
| Binary Size | N/A (pip) | ~10MB |
| Termux Support | Partial | Full |

## Recommendation

For mobile use, we strongly recommend **PicoClaw**. It's specifically designed for resource-constrained environments and works seamlessly on Termux.

To create a PicoClaw version of PocketMind:

1. Use PicoClaw as the base framework
2. Copy the `workspace/` from this project
3. Add the 7-question onboarding skill to PicoClaw's skill system

---

*Note: This project (PocketMind-Nanobot) focuses on the Nanobot framework. For Termux/mobile, PicoClaw is the better choice.*
