# PocketPal - Complete Project Specification
## Your AI Mate That Actually Gives a Damn

**Version:** 1.0
**Date:** March 11, 2026
**Last Updated:** March 12, 2026
**Built by:** WolfPack Empire 🐺

---

## PROJECT STATUS: UI POLISH IN PROGRESS

### Completed:
- ✅ Web UI (pocketpal-web.html) - Functional MVP
- ✅ Onboarding flow (8 steps)
- ✅ 14 Nanobots spec
- ✅ Memory system design
- ✅ Privacy-first architecture

### In Progress:
- 🟡 UI Modernization (2026 trends)
- 🟡 Glassmorphism + glow effects
- 🟡 Spring animations

### Next:
- ⬜ Onboarding polish
- ⬜ Bento grid features section
- ⬜ Mobile optimization

---

## Core Identity

| Attribute | Value |
|-----------|-------|
| **Name** | PocketPal |
| **Tagline** | Your AI mate that actually gives a damn! |
| **Vibe** | Witty, encouraging, helpful mate |
| **Tone** | Casual, friendly, uses emojis naturally |
| **Languages** | English, Afrikaans, Zulu, Xhosa, Sotho |
| **Platform** | Mobile-first (Android/Termux), Desktop later |
| **Privacy** | 100% local, offline, your data stays yours |

---

## The 14 Nanobots (Team)

| # | Nanobot | Role |
|---|---------|------|
| 1 | **Router** | Intent classification, routes to specialist |
| 2 | **Scribe** | Summarizes messages, threads |
| 3 | **Ghostwriter** | Tonal mimicry - writes like YOU |
| 4 | **Guardian** | Financial monitoring, intervention |
| 5 | **Secretary** | Calendar, tasks, reminders |
| 6 | **Filter** | Spam, priority detection |
| 7 | **Teacher** | Explains concepts |
| 8 | **Translator** | Language conversion |
| 9 | **Coder** | Programming help |
| 10 | **Memory Keeper** | Shadow memory, context |
| 11 | **Scout** | Safe internet access |
| 12 | **Firewall** | PII scrubbing, data anonymization |
| 13 | **Ambassador** | Social bridge to other PocketPals |
| 14 | **Voice** | TTS, voice cloning |

---

## Live Now

### ✅ Website
- **URL:** https://interlinkedcapital.co.za/pocketpal/
- **Features:** Landing page + onboarding flow (8 steps)

### ✅ Onboarding Flow
1. Language selection (5 SA languages)
2. Personal info (name, job, location)
3. What they need help with
4. Important people (family, friends)
5. Keywords for reminders
6. Memory check & limits explanation
7. Ready to go!

---

## Phase Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| 1 | Foundation | ✅ Live |
| 2 | Shadow Memory | 📋 Researched |
| 3 | Ghostwriter | 📋 Researched |
| 4 | Financial Guardian | 📋 Researched |
| 5 | Adaptive UX | 📋 Researched |
| 6 | Vision | 📋 Researched |
| 7 | Privacy Bridge | 📋 Researched |
| 8 | Voice & Creative | 📋 Researched |
| 9 | Social Mesh | 📋 Researched |

---

## Key Features (All Documented)

### Memory System
- SQLite + sqlite-vec for vector search
- ~50MB total including models
- "Remember when" functionality
- Weekly check-ins for important people

### Privacy Features
- Privacy Firewall (PII scrubbing)
- Scout for safe web access
- 100% offline operation

### Social Features
- Ambassador Nanobot (A2A protocol)
- PocketPal Circle
- Ghost Group Chats
- Federated Learning

### Business Model
- **Free:** PocketPal Companion (for everyone)
- **Paid:** Premium (all features)
- **Impact:** Social mission - no one should be alone

---

## Research Documents

- `memory/pocketpal-spec-001.md` - This file
- `memory/pocketpal-memory-research.md` - Jiles' research
- `memory/methodology.md` - WolfPack methodology

---

## Business Model: Local-First Subscription

### The "Subscription-as-a-Key" Workflow
Instead of the app asking a server for permission every time it runs, the permission is baked into a local, encrypted file.

- **The Purchase:** When the user pays for 30 days, your server sends a signed digital license to the phone.
- **The Expiration:** This license has a hard-coded "Death Date" (e.g., April 12th).
- **Local Enforcement:** Every time the user opens the app, the Orchestrator checks the current system time against the license date. If expired, the "premium" Nanobots refuse to load.

### The "Encrypted Gate" (Technical Moat)
To prevent hacking:
- **LoRA Locking:** Keep the "Core" model weights open, but encrypt the specialized "Nanobot" weights (LoRA files)
- **Decryption at Runtime:** The license key contains a portion of the decryption key needed to load premium Nanobots into RAM
- No valid license = Nanobots remain scrambled/unusable

### Tiered Functionality

| Tier | Status | What Happens |
|------|--------|--------------|
| Basic (Free) | Always On | Basic chat, simple reminders, local weather |
| Premium (Paid) | License Gated | WhatsApp Summarizer, Journey Image Gen, Scout (Internet) |
| Expired | Fallback | Premium bots "go to sleep" — "I'm feeling tired, can still chat but can't summarize until recharge" |

### Hardware Locking (Anti-Piracy)
- Bind license to phone's unique hardware ID (IMEI or Android ID)
- License file only works on that specific device

### Grace Period
- 72-hour grace period after expiration
- "Your subscription expired, but I've kept the lights on for 3 more days!"

| Agent | Task |
|-------|------|
| **Lux** | Build core runner, integrate llama.cpp |
| **Max** | Project structure, GitHub repos |
| **Jiles** | Research memory systems, optimal storage |
| **Aris** | Orchestrate, manage roadmap |

---

## Links

- **Website:** https://interlinkedcapital.co.za/pocketpal/
- **GitHub:** https://github.com/ewaldvanrooyen-max/pocketmind-agentmesh
- **IC Website:** https://interlinkedcapital.co.za

---

*WolfPack Empire 🐺 - Building the future of compassionate AI*
