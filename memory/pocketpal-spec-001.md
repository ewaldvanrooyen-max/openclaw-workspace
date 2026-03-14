# PocketPal - Project Specification
## Your AI Mate That Actually Gives a Damn

**Version:** 1.0
**Date:** March 11, 2026
**Built by:** WolfPack Empire 🐺

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

## The 10 Nanobots (Team)

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

---

## Phase 1: Foundation (This Week)

### 1.1 Onboarding Flow
- [x] Language selection (5 SA languages)
- [x] Personal info (name, job, location)
- [x] Important people (family, friends)
- [x] Keywords for reminders
- [x] Memory check & explain limits

### 1.2 Basic Chat UI
- [x] Web version (instant, no install)
- [ ] CLI version for Termux
- [ ] Mobile app shell

### 1.3 Basic Responses
- [ ] Keyword-based responses
- [ ] Simple conversation flow

---

## Phase 2: Shadow Memory (Core)

### 2.1 Memory Architecture
| Component | Technology | Size |
|-----------|-----------|------|
| Storage | SQLite + sqlite-vec | Built-in |
| Embeddings | all-MiniLM-L6-v2 | ~40MB |
| Search | Hybrid (semantic + keyword) | - |

### 2.2 Memory Types
- **Conversation** - Recent chats
- **Fact** - Preferences, important info
- **People** - Family, friends, colleagues
- **Event** - Calendar items, deadlines

### 2.3 "Remember When" Feature
- Temporal queries via timestamps
- Parse natural language time references
- Combine with semantic search

### 2.4 Weekly Check-ins
- Cron job: Check in with important people
- "How's your brother Sam doing?"
- Remember events and follow up

---

## Phase 3: Social Ghostwriter

### 3.1 Tonal Mimicry
- Analyze sent messages locally
- Learn slang, emoji usage, response patterns
- Draft in YOUR voice

### 3.2 Message Analysis
- Detect writing style
- Identify patterns (punctuation, length, tone)
- Store as user profile

### 3.3 Draft Generation
- Generate responses in user's style
- User can edit or send as-is

---

## Phase 4: Financial Guardian

### 4.1 Banking Integration
- Monitor local notifications/SMS
- Track spending vs budget
- Detect due dates

### 4.2 Intervention
- Proactive alerts: "Hey, rent is due tomorrow"
- Spending warnings
- Financial health tips

### 4.3 Privacy
- All processing local
- No bank credentials stored
- Notifications read only

---

## Phase 5: Adaptive UX

### 5.1 Time-Based Modes
| Mode | Time | Display |
|------|------|---------|
| **Morning Briefing** | 6-9 AM | Goals, weather, messages |
| **Work Focus** | 9-5 PM | Minimal, urgent only |
| **Evening Wind Down** | 5-10 PM | Soft UI, tomorrow's plan |
| **Night Mode** | 10PM-6AM | Do Not Disturb |

### 5.2 Shape-Shifting Interface
- UI adapts to time of day
- Context-aware bubbles
- Priority notifications only

---

## Phase 6: Vision (Future)

### 6.1 On-Device Camera
- Process images locally (no cloud)
- Delete after processing

### 6.2 Use Cases
- Menu scanning (dietary needs)
- Document scanning
- Object recognition

---

## Technical Architecture

```
┌─────────────────────────────────────────────┐
│              PocketPal Core                  │
├─────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────────────┐ │
│  │   Router    │  │  Memory Keeper     │ │
│  │  (Intent)  │  │  (Vector DB)       │ │
│  └─────────────┘  └─────────────────────┘ │
│                                             │
│  ┌─────────────────────────────────────┐  │
│  │        Nanobot Team                 │  │
│  │  Scribe | Ghostwriter | Guardian  │  │
│  │  Secretary | Filter | Teacher      │  │
│  │  Translator | Coder | Memory      │  │
│  └─────────────────────────────────────┘  │
│                                             │
│  ┌─────────────────────────────────────┐  │
│  │     Local Storage (SQLite)          │  │
│  │  Conversations | Facts | People    │  │
│  └─────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## Internal Dialogue Log

Users can see nanobots collaborating:

```
🔍 The Scribe: "Summarized 42 messages from Family Group"
🔔 The Filter: "Flagged Mom as urgent - keyword 'help'"
📅 The Secretary: "Drafted calendar invite for Sunday"
🛡️ The Guardian: "Rent due tomorrow - notified user"
```

---

## Memory System Specs

| Metric | Value |
|--------|-------|
| Storage needed | ~50MB total |
| Embedding model | 40MB |
| SQLite database | ~5MB base |
| Conversations stored | ~100 before summarization |
| Compression | 50-75% via quantization |

---

## Roadmap

| Phase | Focus | Timeline |
|-------|-------|----------|
| 1 | Foundation | This week |
| 2 | Shadow Memory | Week 2 |
| 3 | Ghostwriter | Week 3 |
| 4 | Financial Guardian | Week 4 |
| 5 | Adaptive UX | Week 5 |
| 6 | Vision | Future |

---

## Research Links

- Memory: `memory/pocketpal-memory-research.md`
- Methodology: `memory/methodology.md`

---

*WolfPack Empire 🐺 - Building the future of personal AI*

---

## Phase 7: Privacy-First Bridge

### 7.1 The Scout Nanobot
- Only ONE nanobot has internet access
- "Double-blind" search - generic query, personal results
- Uses privacy-focused search (DuckDuckGo or SearXNG)
- Never shares your location/identity

### 7.2 Privacy Firewall
- PII (Personally Identifiable Information) scrubber
- Replaces names, addresses, phone numbers with placeholders
- Swaps back after answer returns

### 7.3 Offline Vault (RAG)
- Upload your PDFs (lease, car manual, health records)
- 100% offline search via natural language
- "What's my tire pressure?" "Can I have pets under my lease?"

### 7.4 Ghost Notifications
- Intercept all pings
- Hourly "Human Pulse" summary
- "3 friends planning Friday, boss update (not urgent), mom called twice"

### 7.5 Social Mediator
- Group chat analysis
- Conflict resolution suggestions
- Knows YOUR preferences

### 7.6 Mood Ring
- Smartwatch integration (local Bluetooth)
- Heart rate / stress monitoring
- Suggests breaks when tense

---

## Privacy Architecture

User Device:
- Privacy Firewall: PII scrubber, data anonymizer
- Scout: Internet gatekeeper, generic queries only
- Offline Vault: Your docs, 100% local search

---

## Phase 8: Voice & Creative

### 8.1 Voice Nanobot (TTS)
- **Model:** Kokoro-82M or Piper
- **Size:** <100MB
- **Features:**
  - Human-like voice
  - Voice cloning from sample
  - SSML for emotion/pauses
  - Night mode: softer "library voice"

### 8.2 Creative Tier
- **Stable Diffusion 3.5 Turbo:** Image generation (5-10 sec)
- **ControlNet:** Sketch to logo
- **Moondream 2:** Vision/camera AI

### 8.3 Time Traveler
- "What was I worried about exactly one year ago today?"
- Year-in-review from local data
- Deep personal insights (cloud AI can't do this)

---

## PocketPal Tiers (Product)

| Tier | Features | RAM |
|------|----------|-----|
| **Core** | WhatsApp, Email, Basic Search | 4GB |
| **Pro** | + Voice TTS, Memory Keeper | 8GB+ |
| **Creative** | + Image Gen, Video Summarization | High-end |


---

## Business Model

### The Vision
> "A companion for everyone - especially those who need it most."

### Free Tier: PocketPal Companion
- **For:** Friends, lonely people, elderly
- **Features:** Basic chat, memory, voice
- **Cost:** FREE
- **Why:** Social impact, give back, humanity first

### Paid Tier: PocketPal Premium
- **For:** Power users, professionals
- **Features:** All nanobots, creative tier, cloud sync
- **Cost:** Low monthly subscription (updates, servers)
- **Why:** Sustainable development

### International Expansion
- Each country gets localized version
- Local languages, slang, cultural context
- "Local lingo" taught to the AI

---

## Social Impact

### Mission
> "No one should be alone. Everyone deserves a companion who listens."

### Use Cases
- Elderly isolation
- Mental health support (not replacement for professionals)
- Language learning
- Kids education
- Accessibility (vision/hearing impaired)

---

## The Dream
> "In 2026, AI doesn't have to mean surveillance. 
> PocketPal proves that technology can be personal, private, and kind."

---

*WolfPack Empire 🐺 - Building the future of compassionate AI*

---

## Phase 9: Social Mesh

### 9.1 Ambassador Nanobot
- Only bot authorized to "leave the house"
- Uses Matrix Protocol or Nostr for E2EE
- Direct peer-to-peer handshake
- Zero-knowledge proofs

### 9.2 PocketPal Circle
- **Vibe Matching:** Compare music/taste, suggest connections
- **Collective Memory:** Stitch photos/notes from group events (local only)
- **Trust Scores:** Warn about bots/scams from friends' blocks
- **Ghost Group Chats:** Evaporate when you leave physical location

### 9.3 Sync (Federated Learning)
- Bots learn from each other without sharing private data
- Share "lessons" (weights) not data

### 9.4 Creative Social
- **Co-Dream:** Collaborative image generation with friends
- **Mood Avatars:** Avatar changes expression based on detected mood

---

## The Vision: Private Digital Life

> "In 2026, AI doesn't have to mean surveillance. 
> PocketPal proves that technology can be personal, private, and kind."

---

## The Ambassador Handshake

Rules when PocketPals meet:

1. Introduction: "Hi, I'm [Name]'s PocketPal"
2. Permission: "Can I share X with you?"
3. Exchange: Encrypted data transfer
4. Goodbye: Clear all temp data

