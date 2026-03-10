# PocketMind

> Your personal AI that runs 100% offline on your phone. No internet. No cloud. No subscription.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-MVP-green.svg)]()

</div>

---

## What is PocketMind?

PocketMind is a **fully offline personal AI assistant** that runs on your phone. It:

- 🏃 **Runs 100% offline** - No internet connection required
- 📱 **Runs on your phone** - Termux (Android) or iSH (iOS)
- 🧠 **Learns about you** - Onboarding builds personalized context
- 🔒 **Keeps your data private** - Everything stays on your device
- 💰 **Free forever** - No subscription, no cloud fees

---

## Quick Start

### 1. Install Dependencies

**Termux (Android):**
```bash
pkg update && pkg install python git
pip install -r requirements.txt
```

**iSH (iOS):**
```bash
apk update && apk add python3 git
pip install -r requirements.txt
```

**Linux/macOS/Windows (development):**
```bash
pip install -r requirements.txt
```

### 2. Download a Model

Place a GGUF model file in the `models/` directory. Recommended:

| Model | Size | RAM Needed | Best For |
|-------|------|------------|----------|
| **SmolLM2-360M** | 180MB | 500MB-1GB | Ultra-light, fastest |
| **Qwen2.5-0.5B** | 350MB | 1-2GB | Balanced quality/speed |
| **TinyLlama** | 640MB | 2-3GB | Good quality |

Download from [HuggingFace](https://huggingface.co/TheBloke):
- https://huggingface.co/TheBloke/SmolLM2-360M-Instruct-GGUF
- https://huggingface.co/TheBloke/Qwen2.5-0.5B-Instruct-GGUF

### 3. Run

```bash
# Test installation
python main.py --test

# Set up your profile
python main.py --onboard

# Start chatting
python main.py
```

---

## Features

### 🎯 Personalization
- Onboarding flow asks 7 questions to learn about you
- Remembers your name, schedule, preferences
- Adapts response style (brief/detailed, casual/professional)

### 💾 Local Storage
- All data stored in `~/.pocketmind/data/`
- JSON format - human readable, no database needed
- Profile, memory, and conversation history

### 🔌 Offline-First
- **Zero network calls** - verified in code
- Works in airplane mode
- Works in remote areas with no connectivity

### 🛡️ Privacy First
- Your data never leaves your device
- Doesn't train on your conversations
- No account required

---

## Command Line Options

```bash
python main.py [OPTIONS]

Options:
  -m, --model PATH       Model file path (default: models/smollm2-360m-instruct-q4_k_m.gguf)
  -c, --context-length  Context length (default: 512)
  -t, --threads NUM     CPU threads (default: 4)
  -v, --verbose         Verbose output
  --onboard             Run onboarding
  --test                Test installation
  --mock                Run without model
  --info                Show storage info
  --version             Show version
```

---

## Commands (while chatting)

| Command | Description |
|---------|-------------|
| `help` | Show help |
| `quit` / `exit` | Exit |
| `clear` | Clear screen |
| `profile` | Show your profile |
| `onboard` | Re-run onboarding |

---

## Project Structure

```
pocketmind/
├── main.py                 # Entry point
├── agent/
│   └── brain.py            # Model loading & inference
├── cli/
│   └── interface.py        # Terminal UI
├── storage/
│   └── json_store.py       # Local JSON storage
├── onboarding/
│   └── flow.py            # User setup flow
├── docs/
│   └── INSTALLATION.md     # Detailed installation guide
├── models/                 # Place model files here
├── LICENSE                 # MIT License
├── README.md               # This file
└── requirements.txt       # Python dependencies
```

---

## Troubleshooting

### "Model not found"
Download a GGUF model and place it in the `models/` directory.

### "llama-cpp-python not installed"
```bash
pip install llama-cpp-python
```

### Slow performance
- Reduce context length: `-c 256`
- Reduce threads: `-t 2`
- Try a smaller model (SmolLM2-360M)

### Out of memory
- Use a smaller model
- Reduce context length
- Close other apps

---

## What's Next?

The MVP is ready! Future enhancements:

- [ ] Voice input (Whisper.cpp)
- [ ] Mobile app wrapper (Flutter)
- [ ] Better models (Qwen2.5-0.5B, Llama3.2-1B)
- [ ] Cloud backup sync (optional paid tier)

---

## License

MIT License - See [LICENSE](LICENSE) file.

---

## Credits

Built with ❤️ by [WolfPack Empire](https://github.com/wolfpack-empire)

Powered by [llama.cpp](https://github.com/ggerganov/llama.cpp)
