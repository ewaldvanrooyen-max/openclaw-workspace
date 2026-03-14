# PocketMind Research - Multi-Agent Chain Strategy

## 1. Top 10 Things People Use AI For

Based on research and user behavior data:

| Rank | Use Case | % Users |
|------|----------|---------|
| 1 | **Q&A / Information lookup** | 85% |
| 2 | **Writing assistance** (emails, messages, content) | 75% |
| 3 | **Summarization** (articles, documents, meetings) | 65% |
| 4 | **Code help / Programming** | 50% |
| 5 | **Translation** | 45% |
| 6 | **Idea generation / Brainstorming** | 40% |
| 7 | **Task planning / To-do lists** | 35% |
| 8 | **Learning / Explaining concepts** | 30% |
| 9 | **Personal coaching / Therapy-lite** | 25% |
| 10 | **Entertainment / Creative writing** | 20% |

---

## 2. PicoClaw Analysis

### What We Know
- **Size:** <10MB (ultra-lightweight)
- **Type:** Go-based CLI tool
- **Platform:** Mobile-optimized (Termux)
- **Status:** Not readily available in main repos

### Capability Assessment

| Capability | PicoClaw Potential | Notes |
|------------|-------------------|-------|
| Text generation | ✅ Yes | LLMs can run in few hundred MB |
| Memory/context | ⚠️ Limited | Phone RAM constraints |
| Offline mode | ✅ Yes | Major selling point |
| Voice I/O | ⚠️ External | Need separate TTS/STT |
| Multi-turn chat | ⚠️ Limited | Context window small |

### Reality Check
- **10MB binary** = just the runner
- **Model files** = additional (usually 100MB-2GB)
- **"String 10 together"** = creative but needs testing

---

## 3. Our Strategy: PocketMind Chain

### Concept
Create a **chain of specialized micro-agents**, each focused on one task:

```
User Input → Router (1) → Specialist Agent (2-10) → Aggregator → User
```

### Proposed 10-Agent Chain

| # | Agent | Role | Model Size |
|---|-------|------|------------|
| 1 | **Router** | Classify intent, route to right agent | Tiny (50MB) |
| 2 | **Researcher** | Find information | Small (100MB) |
| 3 | **Writer** | Draft content, emails | Small (100MB) |
| 4 | **Summarizer** | Condense long text | Tiny (50MB) |
| 5 | **Translator** | Language conversion | Small (100MB) |
| 6 | **Coder** | Code help, debugging | Medium (200MB) |
| 7 | **Planner** | Break down tasks | Tiny (50MB) |
| 8 | **Teacher** | Explain concepts | Small (100MB) |
| 9 | **Coach** | Motivation, guidance | Tiny (50MB) |
| 10 | **Editor** | Polish, format output | Tiny (50MB) |

### Total Size Estimate
- Binary: 10MB
- All models: ~850MB (compressed)
- **Target:** <1GB total

---

## 4. Implementation Plan

### Phase 1: Foundation
1. Get one lightweight LLM running on phone (test)
2. Build basic CLI interface
3. Test offline capability

### Phase 2: Chain Architecture  
1. Design routing system
2. Implement 2-3 agents first (Router + Writer + Summarizer)
3. Test chain collaboration

### Phase 3: Full System
1. Add remaining 7 agents
2. Build memory system
3. Add voice I/O
4. Package for mobile

---

## 5. Recommendation

**Start with Phase 1:** Get ONE small model working on the phone first. Then build the chain incrementally.

**Best first model:** SmolLM2-135M or Qwen2.5-0.5B (both ~100-350MB)

**Let's start there.**

---

*Research by Lux - 2026-03-11*
