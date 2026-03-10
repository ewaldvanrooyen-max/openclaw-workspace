# PocketMind - Privacy-First Personal AI
## Concept Brief v2.0 (Battery-Optimized)

---

## The Vision

**PocketMind** is your private, always-available AI that lives on your devices, stores YOUR data locally, and NEVER sends your personal info to the cloud.

Think: *Your personal AI assistant that you actually own.*

---

## Core Value Proposition

| Feature | Cloud AI (ChatGPT/Claude) | PocketMind |
|---------|---------------------------|-------------|
| **Data Privacy** | Your data trains their models | 100% local, never leaves your devices |
| **Availability** | Needs internet | Works offline (with local model) |
| **Personality** | Generic | Learns YOUR preferences, context, history |
| **Cost** | Subscription ($20+/mo) | One-time hardware + running costs |
| **Customization** | Limited | Full control over model, prompts, behavior |

---

## The Problem (v1.0)

Running local LLMs directly on a phone **destroys battery** — the GPU/CPU load for inference is massive. E-man loved the concept but this was a dealbreaker.

---

## The Solution: Hybrid Hub Architecture

### How It Actually Runs ⚡🔋

**The Fix:** Phone is a *dumb terminal*. Heavy lifting happens on a local hub.

```
┌─────────────┐      WiFi       ┌──────────────────┐
│   PHONE     │ ◄──────────────►│   LOCAL HUB      │
│             │   (lightweight) │  (Laptop/Pi/PC)  │
│ - UI only   │                 │ - Full LLM       │
│ - Queries   │                 │ - Vector DB      │
│ - Responses  │                 │ - Your data      │
│ - Display   │                 │ - Processing     │
└─────────────┘                 └──────────────────┘
       │                                 │
       │ Battery-friendly ✅            │ Always plugged in ✅
       │ (idle except when in use)      │ (no battery concern)
```

### Battery Impact: <5% per day (vs 50%+ for local LLM)

| Component | Battery Drain |
|-----------|---------------|
| Display (occasional) | ~3-4% |
| WiFi radio (send/receive) | ~1% |
| Background (near zero) | ~0.5% |
| **Total** | **~5%/day** |

---

## Architecture Options

### Option A: Hybrid Hub (Recommended) 🏆
**Best for:** Home/Office users who want full functionality

| Component | Device | Role |
|-----------|--------|------|
| **Hub** | Raspberry Pi 5 (8GB) / Old Laptop / Mac Mini | Runs LLM + Vector DB |
| **Phone** | Any smartphone | Dumb terminal (UI + communication) |
| **Connection** | Local WiFi (home network) | Low-latency, secure |

**Running Costs:** ~$5-15/month (electricity for Pi) or free (laptop already on)

### Option B: Short-Burst Mode
**Best for:** Minimal setup, occasional use

- Optimized prompt compression (extract intent in <50 tokens)
- Tiny local model on phone for simple tasks (like Llama 3.2 1B)
- Fast completion, phone sleeps in between
- Heavy tasks queue to hub when available

**Battery:** ~15-20% per day (still better than full local)

### Option C: Background Sync (Agent Forwarding)
**Best for:** Desktop-centric workflow

- Agent runs on laptop/desktop 24/7
- Phone sends queries via Telegram/Signal
- Agent processes, sends back lightweight response
- Phone just displays text — no LLM locally

**Battery:** ~3-5% per day (minimal)

---

## Recommended: Option A (Hybrid Hub)

### Hardware Stack

| Tier | Setup | Cost | Performance |
|------|-------|------|--------------|
| **Budget** | Raspberry Pi 5 (8GB) + SSD | ~$150 one-time | ~5-10 tok/sec |
| **Mid** | Old MacBook / Intel NUC | $0-200 | ~15-25 tok/sec |
| **Pro** | Mac Mini M-series | $400+ | ~40-60 tok/sec |

### Software Stack

| Layer | Technology |
|-------|------------|
| **LLM** | Ollama + Qwen2.5:7B (or Llama3:8B) |
| **Vector DB** | ChromaDB or LlamaIndex |
| **Sync Protocol** | WebSocket over local WiFi |
| **Phone App** | Flutter (cross-platform) or PWA |
| **Encryption** | TLS + local network only |

### Data Flow

```
1. User speaks/types on phone
2. Phone sends compressed query → Hub (WiFi)
3. Hub processes with full LLM + personal context
4. Hub returns response → Phone
5. Phone displays, learns from interaction
```

---

## Features

### Phase 1: Core (MVP)
- [ ] Local LLM running on hub (Ollama)
- [ ] Phone app connects via WebSocket
- [ ] Basic Q&A with personal context
- [ ] Conversation history stored locally

### Phase 2: Memory
- [ ] Vector database for your documents
- [ ] RAG pipeline (retrieve → augment → generate)
- [ ] Import from: Notes, Emails, Files
- [ ] Semantic search across your data

### Phase 3: Agents
- [ ] Background agents for automation
- [ ] Scheduled tasks (daily briefing, reminders)
- [ ] API integrations (calendar, tasks, email)
- [ ] Proactive suggestions

### Phase 4: Voice
- [ ] Whisper for speech-to-text (local)
- [ ] edge-tts for text-to-speech (or local if possible)
- [ ] Natural conversation flow

---

## Privacy Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    POCKETMIND                           │
│                                                         │
│   ┌─────────────┐      ┌──────────────────────────┐   │
│   │   PHONE     │ ───► │         HUB              │   │
│   │  (UI Only)  │ WiFi │   (Processing)          │   │
│   └─────────────┘      │                          │   │
│                        │  ┌────────────────────┐  │   │
│                        │  │   Local LLM        │  │   │
│                        │  │   (Ollama)         │  │   │
│                        │  └────────────────────┘  │   │
│                        │                          │   │
│                        │  ┌────────────────────┐  │   │
│                        │  │   Vector DB        │  │   │
│                        │  │   (Your Data)      │  │   │
│                        │  └────────────────────┘  │   │
│                        │                          │   │
│                        │  ┌────────────────────┐  │   │
│                        │  │   Encrypted        │  │   │
│                        │  │   Storage          │  │   │
│                        │  └────────────────────┘  │   │
│                        └──────────────────────────┘   │
│                                                         │
│   ❌ Cloud Services        ✅ Local Only               │
│   ❌ Internet Required    ✅ Works Offline            │
│   ❌ Data Leaves Device    ✅ 100% Private             │
└─────────────────────────────────────────────────────────┘
```

---

## Implementation Roadmap

### Week 1-2: MVP
- [ ] Set up Ollama on Pi/laptop
- [ ] Test with Qwen2.5:7B
- [ ] Basic WebSocket server
- [ ] Simple phone client (web-based for now)

### Week 3-4: Memory
- [ ] Add ChromaDB
- [ ] Document ingestion pipeline
- [ ] RAG working with personal context

### Week 5-6: Polish
- [ ] Phone app (Flutter/PWA)
- [ ] Voice input/output
- [ ] Encryption layer

### Week 7+: Agents & Scale
- [ ] Background agents
- [ ] API integrations
- [ ] Multiple users/household

---

## Cost Estimate

### One-Time Hardware
| Item | Budget | Mid | Pro |
|------|--------|-----|-----|
| Raspberry Pi 5 | $150 | - | - |
| SSD (500GB) | $50 | - | - |
| Old Laptop | - | $0 | - |
| Mac Mini | - | - | $600 |

### Monthly Running
| Item | Cost |
|------|------|
| Electricity (Pi) | $3-5/mo |
| Electricity (Laptop) | $5-10/mo |
| Internet (already have) | $0 |

### Software (Free)
- Ollama: Free
- ChromaDB: Free
- Whisper: Free
- Total: **$0**

---

## Why This Wins

1. **Battery Safe** — Phone does almost nothing
2. **Privacy First** — Zero cloud, 100% local
3. **Always On** — Hub runs 24/7, instant responses
4. **Personal** — Learns your context, memories, preferences
5. **Offline Capable** — Works when internet is down
6. **No Subscription** — One-time hardware cost
7. **Future-Proof** — Swap out Pi for faster hardware anytime

---

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| WiFi goes down | Bluetooth fallback, offline cache on phone |
| Hub offline | Phone shows "reconnecting", queues queries |
| Performance slow | Use smaller model on hub, upgrade when needed |
| Data loss | Regular backups to external drive |
| Complexity | Start with Pi, iterate as needed |

---

## Next Steps

1. **Test Ollama** on current hardware (laptop or VPS)
2. **Prototype** WebSocket connection between phone + laptop
3. **Choose hardware** based on budget and performance needs
4. **Start MVP** with basic Q&A

---

*Concept v2.0 — Battery-Optimized Edition*
*Addressing the core blocker: local LLMs on phone destroy battery.*
*Solution: Hybrid Hub Architecture*
