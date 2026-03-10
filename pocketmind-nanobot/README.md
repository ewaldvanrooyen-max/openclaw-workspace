# PocketMind 🧠

**Personal AI Memory Assistant with 7-Question Onboarding**

Two variants available:
- **PocketMind-Nanobot**: Python-based (this repo)
- **PocketMind-PicoClaw**: Go-based, optimized for mobile

## Quick Comparison

| Feature | Nanobot | PicoClaw |
|---------|---------|----------|
| Language | Python | Go |
| RAM | ~100MB | <10MB |
| Startup | ~30s | <1s |
| Mobile/Termux | ⚠️ Heavy | ✅ Optimized |
| Channels | All | All |

## Choose Your Version

### For Desktop/Server → Use Nanobot

```bash
# Install
pip install nanobot-ai

# Clone workspace
git clone https://github.com/HKUDS/pocketmind-nanobot.git
cp -r pocketmind-nanobot/workspace ~/.pocketmind/

# Configure
nano ~/.nanobot/config.json

# Run
nanobot agent -w ~/.pocketmind/workspace
```

### For Mobile (Termux) → Use PicoClaw

```bash
# Download
wget https://github.com/sipeed/picoclaw/releases/download/v0.1.1/picoclaw-linux-arm64
chmod +x picoclaw-linux-arm64
pkg install proot
termux-chroot ./picoclaw-linux-arm64 onboard
```

See [pocketmind-picoclaw/](pocketmind-picoclaw/) for full PicoClaw setup.

## The 7-Question Onboarding

Both versions include the same 7-question onboarding:

1. **Name**: What should I call you?
2. **Primary Goal**: What's your main goal for having an AI assistant?
3. **Tasks**: What tasks do you need help with most?
4. **Communication**: Casual, professional, technical, or adaptive?
5. **Timezone**: Where are you located?
6. **Preferences**: Any specific requirements?
7. **Background**: What should I know about you?

Your answers are saved to `memory/user-profile.md` and used to personalize every interaction.

## Project Structure

```
pocketmind-nanobot/           # Nanobot version
├── workspace/
│   ├── skills/pocketmind/   # Onboarding skill
│   ├── memory/              # User profile
│   ├── AGENTS.md            # Agent config
│   ├── SOUL.md              # Personality
│   └── USER.md              # User template
├── config/                   # Example configs
├── docs/                     # Documentation
└── install.sh               # Quick setup script

pocketmind-picclaw/          # PicoClaw version (mobile-optimized)
├── workspace/
├── config.json.example
└── TERMUX.md
```

## Documentation

- [Nanobot README](pocketmind-nanobot/README.md)
- [Onboarding Guide](pocketmind-nanobot/docs/ONBOARDING.md)
- [Termux Guide - Nanobot](pocketmind-nanobot/docs/TERMUX.md)
- [Termux Guide - PicoClaw](pocketmind-picoclaw/TERMUX.md)

## License

MIT - WolfPack Empire
