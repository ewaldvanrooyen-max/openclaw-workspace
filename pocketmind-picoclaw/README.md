# PocketMind-PicoClaw 🧠

A PicoClaw-based personal AI memory assistant with 7-question onboarding system.

## What is PocketMind?

PocketMind is a personal AI assistant designed to remember everything about you through a friendly onboarding process. It uses the ultra-lightweight [PicoClaw](https://github.com/sipeed/picoclaw) framework (<10MB RAM, runs on $10 hardware).

## Features

- ⚡ **Ultra-lightweight**: Built on PicoClaw (<10MB RAM)
- 🧠 **7-Question Onboarding**: Remembers you through personalized questions
- 📱 **Mobile Ready**: Optimized for Termux (Android)
- 🔒 **Privacy-focused**: Your data stays on your device
- 🎯 **Personalized**: Learns your preferences and adapts

## Quick Start (Termux)

```bash
# Install PicoClaw
pkg update && pkg install git wget
wget https://github.com/sipeed/picoclaw/releases/download/v0.1.1/picoclaw-linux-arm64
chmod +x picoclaw-linux-arm64
pkg install proot
termux-chroot ./picoclaw-linux-arm64 onboard

# Configure
nano ~/.picoclaw/config.json

# Add your model:
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

# Run
termux-chroot ./picoclaw-linux-arm64 agent
```

## The 7-Question Onboarding

1. **Name**: What should I call you?
2. **Primary Goal**: What do you want me to help you with?
3. **Tasks**: What are your most frequent tasks?
4. **Communication**: How do you prefer to communicate?
5. **Timezone**: Where are you located?
6. **Preferences**: Any specific requirements?
7. **Background**: What should I know about you?

## Project Structure

```
pocketmind-picoclaw/
├── workspace/           # PicoClaw workspace
│   ├── memory/
│   │   └── user-profile.md
│   ├── AGENTS.md
│   ├── SOUL.md
│   └── USER.md
├── config.json.example
├── TERMUX.md
└── README.md
```

## Performance

| Metric | PicoClaw | Nanobot (Python) |
|--------|----------|------------------|
| RAM | <10MB | ~100MB |
| Startup | <1s | ~30s |
| Binary | ~10MB | N/A |

## License

MIT - WolfPack Empire
