# PROJECT BLUEPRINT - PocketPal

## Project Name
**PocketPal** - Privacy-first local AI agent with Nanobot mesh

## Vision
A state-of-the-art 2026 implementation leveraging Small Language Models (SLMs) and on-device NPUs. Modular ecosystem where specialized "Nanobots" (LoRA adapters) swap in/out of a shared base model.

---

## Core Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Nanobots | 10+ | 0 |
| Response Time | <100ms | - |
| Privacy Score | 100% | - |
| Subscription Users | 1000 | 0 |

---

## Repository
- **URL:** github.com/ewaldvanrooyen-max/pocketpal
- **Live Site:** N/A (local)

---

## Architecture

### I. The Agentic Mesh - Nanobot Fleet

#### 1. Brain (Inference Engine)
- **Base Model:** Gemma-3 1B or SmolLM3 3B
- **Why:** Natively multimodal (text, voice, vision), 128k context window
- **Runtime:** LiteRT-LM (formerly TFLite)
- **Target:** Qualcomm/MediaTek NPUs (3x power efficiency)

#### 2. Nanobot Fleet (LoRA Adapters)
Specialty "Hats" loaded into base model:
- **Scribe Bot:** WhatsApp/Signal thread summarization
- **Scout Bot:** Privacy-scrubbed web search (DuckDuckGo/SearXNG)
- **Ghostwriter Bot:** Tonal mimicry for drafting replies
- **Guardian Bot:** PII scrubbing & fraud detection
- **Creative Bot:** Local image generation (SD 3.5 Turbo)
- **Translator Bot:** Real-time translation
- **Teacher Bot:** Learn & explain concepts
- **Planner Bot:** Task planning & scheduling
- **Editor Bot:** Content editing & refinement
- **Coach Bot:** Personal development & motivation

---

### II. Data & Privacy - Personal Vault

#### Vector Database
- **Tech:** ChromaDB Mobile or Qdrant (Local Mode)
- **Function:** Messages embedded into local vector store
- **Use:** "What was the name of that restaurant Sarah mentioned?"

#### PII Firewall
- Guardian Bot replaces PII with generic tokens before web search
- All web data fetched as raw text, stripped of trackers, re-synthesized locally

---

### III. Social Mesh - Ambassador Protocol

#### Communication Layer
- **Tech:** libp2p or Matrix E2EE
- **Handshake:** JSON manifests of what friends can share
- **Feature:** Zero-Knowledge Scheduling
  - "Are you free Friday?" → Ambassador checks local calendar → "Yes" (without revealing details)

---

### IV. Media - Voice & Image

#### TTS
- **Engine:** Kokoro-82M (~300MB)
- **Use:** Daily briefing summaries, voice responses

#### Image Generation
- **Engine:** Stable Diffusion 3.5 Turbo
- **Use:** Personalized stickers, journey-style art

---

### V. Business Model - Hardware-Locked Subscription

#### Token System
- User buys 30-day subscription
- Server sends Signed License Token
- Token tied to phone's Secure Enclave/TEE
- Cannot be copied to another phone

#### Decryption
- Nanobot LoRA files are encrypted
- License contains temporary decryption key
- Day 31: No new token → reverts to Basic model

---

## Implementation Roadmap

| Phase | Focus | Tools | Status |
|-------|-------|-------|--------|
| **Phase 1** | The Core | LiteRT-LM + Gemma-3 1B (Android/iOS) | - |
| **Phase 2** | The Vault | ChromaDB + index SMS/WhatsApp logs | - |
| **Phase 3** | The Voices | Kokoro-82M for local "Daily Briefings" | - |
| **Phase 4** | The Social | libp2p "Ambassador" bridge for P2P messaging | - |
| **Phase 5** | The Moat | Encrypt Nanobots + Secure Enclave license check | - |

---

## The Final Vision

**PocketPal is a "Living Mirror" of the user.**

It knows their jokes, their budget, and their friends, but it keeps that knowledge **locked in their pocket**.

---

## Tech Stack
- **Base Models:** Gemma-3 1B, SmolLM3 3B
- **Runtime:** LiteRT-LM
- **LoRA:** Custom adapters
- **Vector DB:** ChromaDB Mobile / Qdrant
- **TTS:** Kokoro-82M
- **Image:** Stable Diffusion 3.5 Turbo
- **Communication:** libp2p / Matrix
- **Security:** TEE / Secure Enclave

---

## Current Status
- Blueprint drafted
- Repo created
- Need to implement Phase 1

---

## Notes
- Focus: Privacy-first, on-device AI
- Different from cloud AI: All data stays local
- Hardware-locked subscription prevents piracy
