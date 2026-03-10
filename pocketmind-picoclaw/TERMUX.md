# PocketMind on Termux - PicoClaw Guide

This is the recommended way to run PocketMind on mobile (Android/Termux).

## Why PicoClaw?

- <10MB RAM usage
- Single binary (~10MB)
- Boots in <1 second
- Native Termux support

## Installation

### 1. Install Termux

Get Termux from F-Droid (recommended) or Google Play.

### 2. Install PicoClaw

```bash
# Update packages
pkg update && pkg upgrade

# Install required packages
pkg install git wget curl proot

# Download PicoClaw (ARM64)
wget https://github.com/sipeed/picoclaw/releases/download/v0.1.1/picoclaw-linux-arm64
chmod +x picoclaw-linux-arm64
```

### 3. Setup

```bash
# Enter Linux environment
termux-chroot

# Initialize (creates ~/.picoclaw/)
./picoclaw-linux-arm64 onboard
```

### 4. Configure

```bash
nano ~/.picoclaw/config.json
```

Add your model:

```json
{
  "model_list": [{
    "model_name": "claude-sonnet",
    "model": "anthropic/claude-sonnet-4-6",
    "api_key": "sk-or-v1-xxx"
  }],
  "agents": {
    "defaults": {
      "model": "claude-sonnet"
    }
  }
}
```

### 5. Run

```bash
# Interactive mode
termux-chroot ./picoclaw-linux-arm64 agent

# Or just
./picoclaw-linux-arm64 agent
```

## Keeping PocketMind Running

### Option 1: Background

```bash
nohup ./picoclaw-linux-arm64 gateway &
```

### Option 2: Wake Lock

```bash
pkg install termux-api
termux-wake-lock
./picoclaw-linux-arm64 gateway
```

## 7-Question Onboarding

The first time you run PocketMind, it will ask you 7 questions:

1. What should I call you?
2. What's your primary goal?
3. What tasks do you need help with?
4. How do you prefer to communicate?
5. What's your timezone?
6. Any preferences I should know?
7. What should I know about you?

Your answers are saved to `memory/user-profile.md`.

## Troubleshooting

### "Command not found"
Use `termux-chroot` before running PicoClaw.

### API Errors
Check your API key in `~/.picoclaw/config.json`.

### Network Issues
Make sure Termux has network permissions.

---

*That's it! PocketMind is now running on your phone.*
