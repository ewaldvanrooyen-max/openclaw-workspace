# PocketMind Quick Start Guide

## Quick Start (MVP Complete! ✅)

### What's Been Built

1. **Offline-First** - Zero network calls, 100% local
2. **Error Handling** - Graceful failures, informative messages
3. **Documentation** - Complete README and installation guide
4. **GitHub Ready** - Proper repo structure with LICENSE

### Project Structure

```
pocketmind/
├── main.py              # Entry point
├── agent/
│   ├── brain.py         # Model loading & inference
│   └── __init__.py
├── onboarding/
│   ├── flow.py          # 7-question onboarding
│   └── __init__.py
├── storage/
│   ├── json_store.py    # Local JSON storage
│   └── __init__.py
├── cli/
│   ├── interface.py     # Terminal UI
│   └── __init__.py
├── docs/
│   └── INSTALLATION.md  # Full install guide
├── LICENSE              # MIT License
├── requirements.txt     # Python dependencies
├── README.md            # Main documentation
└── .gitignore           # Git ignore file
```

---

## Step 1: Test Your Installation

```bash
# Test everything is working
python main.py --test

# Run onboarding (recommended first time)
python main.py --onboard
```

---

## Step 2: Download a Model

To generate AI responses, you need a model file.

### Recommended Models

| Model | Size | RAM | Best For |
|-------|------|-----|----------|
| **SmolLM2-360M** | 180MB | ~1GB | Fastest, lightest |
| **Qwen2.5-0.5B** | 350MB | ~2GB | Balanced quality |
| **TinyLlama** | 640MB | ~3GB | Good quality |

### Download

```bash
# Create models directory
mkdir -p models
cd models

# Download SmolLM2-360M (recommended for testing)
wget https://huggingface.co/TheBloke/SmolLM2-360M-Instruct-GGUF/resolve/main/smollm2-360m-instruct-q4_k_m.gguf
```

---

## Step 3: Run PocketMind

```bash
# Run with your model
python main.py -m models/smollm2-360m-instruct-q4_k_m.gguf

# Or run without model (mock mode for testing)
python main.py --mock
```

---

## Command Reference

| Command | Description |
|---------|-------------|
| `python main.py --test` | Test installation |
| `python main.py --onboard` | Set up your profile |
| `python main.py --mock` | Run without model |
| `python main.py --info` | Show storage info |
| `python main.py -m <model>` | Specify model file |
| `python main.py -c 512` | Set context length |
| `python main.py -t 4` | Set thread count |

### In-App Commands

| Command | Description |
|---------|-------------|
| `help` | Show help |
| `quit` | Exit |
| `clear` | Clear screen |
| `profile` | Show your profile |
| `onboard` | Re-run onboarding |

---

## Offline Verification

The app is designed to run **completely offline**:
- ✅ No `requests` module required
- ✅ No `urllib` for network calls
- ✅ All inference local
- ✅ All storage local

Run `--test` to verify offline capability.

---

## Troubleshooting

**Model not found:**
- Download a GGUF model file
- Place in `models/` directory
- Run with `-m` flag

**Out of memory:**
- Use smaller model (SmolLM2-360M)
- Reduce context: `-c 256`
- Close other apps

**Slow inference:**
- Use smaller model
- Reduce context length
- Increase threads: `-t 8`

---

## What's Next (Post-MVP)

- [ ] Voice input (Whisper.cpp)
- [ ] Mobile app wrapper (Flutter)
- [ ] Better models (Qwen2.5-0.5B)
- [ ] Cloud backup sync (optional paid)

---

*MVP Ship-Ready! 🚀*
