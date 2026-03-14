# PocketMind Project - Mobile LLM Research

**Date:** 2026-03-11  
**Researcher:** Jiles 🔍  
**Focus:** Lightest, fastest way to run ~500MB model on mobile (Android/Termux)

---

## Executive Summary

After research, **llama.cpp with GGUF quantized models** is the recommended approach for running SmolLM2-1.7B on Android/Termux. It's the lightest, fastest, and most flexible option.

---

## Options Compared

### 1. llama.cpp + GGUF (⭐ RECOMMENDED)

**Best for:** Lightweight, fast, battery-friendly mobile inference

**Pros:**
- Native C/C++ - no heavy dependencies
- Multiple quantization levels (Q2-Q8)
- Excellent ARM optimization (NEON, RVV)
- Pre-built GGUF models available
- Works on CPU (slower) or GPU via Vulkan/OpenCL
- Active community, frequent updates

**Cons:**
- CLI-based (no native Android UI out of the box)
- Requires manual setup on Termux

**SmolLM2-1.7B Quantized Sizes:**
| Format | Size | Notes |
|--------|------|-------|
| Q4_K_M | ~1GB | **Recommended** - good balance |
| Q4_K_S | ~1GB | Slightly smaller, slight quality loss |
| Q3_K_M | ~860MB | Lower quality |
| Q2_K | ~670MB | Lightest option (~500MB range!) |

**Installation (Termux):**
```bash
# Install dependencies
pkg install git cmake python

# Clone and build llama.cpp
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
mkdir build && cd build
cmake .. -DLLAMA_BUILD_CLI=ON -DLLAMA_BUILD_SERVER=ON
make -j$(nproc)

# Download quantized model
# From bartowski/SmolLM2-1.7B-Instruct-GGUF on HuggingFace
# Recommended: SmolLM2-1.7B-Instruct-Q4_K_M.gguf (~1GB)

# Run
./build/bin/llama-cli -m SmolLM2-1.7B-Instruct-Q4_K_M.gguf
```

---

### 2. MLC LLM

**Best for:** Native Android app with GPU acceleration

**Pros:**
- Native Android app with GPU acceleration (OpenCL for Adreno/Mali)
- Pre-optimized models available
- Better GPU utilization than llama.cpp on Android
- OpenAI-compatible API

**Cons:**
- Heavy build process (requires Android Studio, NDK, Rust)
- Complex setup - not beginner friendly
- Requires compiling from source for custom models
- Demo APK available but outdated

**Installation (Android):**
- Option A: Use pre-built demo APK (limited model selection)
- Option B: Build from source (complex, requires Android Studio)

**Website:** https://github.com/mlc-ai/mlc-llm

---

### 3. MediaPipe LLM Inference

**Best for:** Google's ecosystem, integrated ML pipelines

**Pros:**
- Part of Google's MediaPipe framework
- Good for integration with other ML tasks
- Android/iOS/Web support

**Cons:**
- Limited model support (not all models compatible)
- Less flexible for custom use cases
- Primarily designed for on-device ML tasks, not general LLM inference

**Website:** https://google.github.io/mediapipe/solutions/text/language_detector

---

## Recommendations for E-man

### Primary Recommendation: llama.cpp on Termux

For the **lightest, fastest** approach to run a ~500MB model on mobile:

1. **Use Q2_K quantization** - ~670MB (closest to 500MB target)
2. **Or use SmolLM2-360M** - already ~400MB in Q4_K

**Setup path:**
```bash
# Quick start on Termux
pkg update && pkg install git cmake python llvm
git clone --depth 1 https://github.com/ggml-org/llama.cpp
cd llama.cpp
make -j$(nproc)

# Download model (Q2_K for ~670MB)
# HuggingFace: bartowski/SmolLM2-1.7B-Instruct-GGUF
# File: SmolLM2-1.7B-Instruct-Q2_K.gguf
```

### Alternative: Use pre-built Android apps

- **LLMFarm** - Android app with llama.cpp backend
- **Maid** - Mobile Artificial Intelligence (llama.cpp based)
- **KoboldCpp** - Has Android support

---

## Model Recommendations

| Use Case | Model | Quantization | Size |
|----------|-------|--------------|------|
| Lightest | SmolLM2-1.7B | Q2_K | ~670MB |
| Balanced | SmolLM2-1.7B | Q4_K_M | ~1GB |
| Even lighter | SmolLM2-360M | Q4_K | ~400MB |

**SmolLM2-360M** might be even better for mobile - significantly smaller while retaining decent performance for simple tasks.

---

## Test Results (if available)

*To be filled after testing on actual device*

---

## References

- llama.cpp: https://github.com/ggml-org/llama.cpp
- GGUF Models: https://huggingface.co/bartowski/SmolLM2-1.7B-Instruct-GGUF
- MLC LLM: https://llm.mlc.ai/docs/
- Termux: https://termux.com/

---

*WolfPack Empire - Research Division 🔍*
