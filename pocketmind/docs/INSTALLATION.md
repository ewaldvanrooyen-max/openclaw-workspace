# PocketMind Installation Guide

## Termux (Android) / iSH (iOS)

This guide covers installing PocketMind on mobile devices using Termux (Android) or iSH (iOS).

---

## Prerequisites

### Device Requirements

| Tier | Device | Can Run |
|------|--------|---------|
| **Minimum** | 4GB RAM (2020+) | SmolLM2-360M |
| **Recommended** | 6GB+ RAM (2022+) | Qwen2.5-0.5B |
| **Optimal** | 8GB+ RAM (2024+) | Llama3.2-1B |

---

## Option A: Install on Termux (Android)

### Step 1: Install Termux
**IMPORTANT:** Install from **F-Droid**, NOT Google Play Store (outdated).

```
F-Droid → Search "Termux" → Install
```

### Step 2: Update and Install Dependencies

```bash
# Update package list
pkg update && pkg upgrade

# Install Python and build tools
pkg install python git clang cmake make

# Install Python development headers (needed for llama-cpp-python)
pkg install python-dev

# Install OpenSSL (needed for HTTPS)
pkg install openssl openssl-dev
```

### Step 3: Install PocketMind

```bash
# Clone PocketMind repository
git clone https://github.com/your-repo/pocketmind.git
cd pocketmind

# Install Python dependencies
pip install -r requirements.txt

# Or with specific packages
pip install llama-cpp-python pyyaml
```

### Step 4: Download a Model

```bash
# Create models directory
mkdir -p models
cd models

# Download SmolLM2-360M (recommended for first test)
# Using huggingface-cli or wget
wget https://huggingface.co/TheBloke/SmolLM2-360M-Instruct-GGUF/resolve/main/smollm2-360m-instruct-q4_k_m.gguf

# Or Qwen2.5-0.5B (better quality)
wget https://huggingface.co/TheBloke/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf
```

### Step 5: Run PocketMind

```bash
cd ..
python main.py
```

---

## Option B: Install on iSH (iOS)

### Step 1: Install iSH
Get iSH from the **App Store**.

### Step 2: Update and Install Dependencies

```bash
# Update package list
apk update && apk upgrade

# Install Python and build tools
apk add python3 git alpine-sdk

# Install Python development headers
apk add python3-dev

# Install OpenSSL
apk add openssl openssl-dev
```

### Step 3: Install PocketMind

```bash
# Clone repository
git clone https://github.com/your-repo/pocketmind.git
cd pocketmind

# Install Python dependencies
pip3 install -r requirements.txt
```

### Step 4: Download Model

Same as Termux - see Step 4 above.

### Step 5: Run

```bash
python3 main.py
```

---

## Alternative: Using Pre-built llama.cpp Binary

If building from source is too slow, use pre-built binaries:

### Download Binary

```bash
# For ARM64 (most phones)
wget https://github.com/ggerganov/llama.cpp/releases/latest/download/llama-cli-android-arm64

# Make executable
chmod +x llama-cli-android-arm64
```

### Run with Binary

```bash
./llama-cli-android-arm64 -m models/smollm2-360m-instruct-q4_k_m.gguf -p "Hello" -n 50
```

---

## Troubleshooting

### Issue: `llama-cpp-python` fails to build

**Solution:** Install pre-built wheel:
```bash
pip install llama-cpp-python --only-binary=:all:
```

### Issue: Out of memory

**Solution:** Use a smaller model or quantized version:
- Try `Q3_K_M` or `Q4_K_M` quantizations
- Close other apps

### Issue: Slow inference

**Solution:** 
- Use smaller model (SmolLM2-360M)
- Use more aggressive quantization (Q2_K, Q3_K_S)
- Consider using GPU/NPU if available

### Issue: "No module named 'llama'"

**Solution:** Make sure you're in the right virtual environment:
```bash
source ~/.venv/pocketmind/bin/activate  # If using venv
```

---

## Testing Your Installation

### Quick Test

```bash
# Test Python
python --version

# Test llama-cpp-python
python -c "import llama_cpp; print('llama_cpp installed')"

# Run with simple prompt
python main.py --test
```

---

## Performance Tips

1. **Use quantized models** - Q4_K_M is a good balance
2. **Close background apps** - Free up RAM
3. **Keep phone cool** - Thermal throttling slows inference
4. **Use airplane mode** - Reduces background processes
5. **Consider GPU** - Some phones support GPU acceleration

---

## Next Steps

After installation, run onboarding:
```bash
python main.py --onboard
```

This will ask you 7 questions to build your personal profile.

---

*Last updated: 2026-03-10*
