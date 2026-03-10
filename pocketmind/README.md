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

**Option A: Use the download script (recommended)**
```bash
# Interactive selection
python download_model.py

# Or specify a model directly
python download_model.py --preset qwen2.5
python download_model.py --preset smollm2
python download_model.py --preset llama3.2
```

**Option B: Manual download**
Place a GGUF model file in the `models/` directory.

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

## Model Options

PocketMind supports multiple models. Choose based on your device's RAM:

| Model | Preset | Size | RAM Needed | Best For |
|-------|--------|------|------------|----------|
| **SmolLM2-360M** | `smollm2` | 180MB | 500MB-1GB | Ultra-light, fastest |
| **Qwen2.5-0.5B** | `qwen2.5` | 350MB | 1-2GB | ✅ **Recommended** - Balanced |
| **Llama3.2-1B** | `llama3.2` | 640MB | 2-3GB | Best quality |

### Model Selection

```bash
# Using preset (recommended)
python main.py --preset qwen2.5

# Using manual path
python main.py -m models/qwen2.5-0.5b-instruct-q4_k_m.gguf

# Or edit config.yaml
# model_preset: "qwen2.5"
```

### Performance Notes

- **SmolLM2**: Fastest startup, lowest RAM. Good for older phones.
- **Qwen2.5**: Best balance. Recommended for most users.
- **Llama3.2**: Best response quality. Slower on mobile.

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
  -m, --model PATH       Model file path
  -p, --preset NAME      Use preset (smollm2, qwen2.5, llama3.2)
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
├── download_model.py       # Model downloader
├── config.yaml             # Configuration
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
```bash
# Use the downloader
python download_model.py --preset qwen2.5

# Or manually download a GGUF model to models/
```

### "llama-cpp-python not installed"
```bash
pip install llama-cpp-python
```

### Slow performance
- Use a smaller model: `python main.py --preset smollm2`
- Reduce context length: `-c 256`
- Reduce threads: `-t 2`

### Out of memory
- Use SmolLM2 preset (lowest RAM)
- Reduce context length: `-c 256`
- Close other apps

---

## Configuration

Edit `config.yaml` to customize defaults:

```yaml
# Model preset: smollm2, qwen2.5, or llama3.2
model_preset: "qwen2.5"

model:
  path: "models/qwen2.5-0.5b-instruct-q4_k_m.gguf"
  context_length: 512
  threads: 4
  gpu_layers: 0

generation:
  max_tokens: 256
  temperature: 0.7
```

---

## License

MIT License - See [LICENSE](LICENSE) file.

---

## Credits

Built with ❤️ by [WolfPack Empire](https://github.com/wolfpack-empire)

Powered by [llama.cpp](https://github.com/ggerganov/llama.cpp)
