# Contentengen Tech Update & Pivot Plan
**Date:** 2026-03-12
**Status:** 85% Complete | Target: May/June Launch

---

## Current Stack (Feb 2026)

| Component | Current |
|-----------|---------|
| **Frontend** | Next.js (version unclear) |
| **AI Brain** | DeepSeek V3 + Gemini 2.5 Flash Lite |
| **Video** | Remotion + FFmpeg |
| **Database** | Neon Postgres |
| **Storage** | Google Drive + Cloudflare R2 |
| **Agents** | 5 (Teacher, Narrator, Closer, Demo, Atmosphere) |

---

## March 2026 Tech Updates (What Changed)

### 🔥 Vercel / Next.js
- **Next.js 16.1** — React 19 stable, `cacheLife` / `cacheTag` now stable
- **Vercel DevTools MCP** — AI agents can directly debug/migrate code
- **Vercel Queues (Beta)** — Durable event streaming for background orchestration
- ⚠️ **Deadline:** `now.json` deprecated March 31, 2026 → must migrate to `vercel.json`

### 🧠 Gemini / Vertex AI
- **Gemini 3.1 Pro** — 15% reasoning improvement
- **Gemini 3 Flash-Lite** — Ultra-efficient for high-frequency tasks
- **Agentic Vision** — Model can "Think-Act-Observe", execute code to investigate images
- **Veo 3.1** — Portrait mode (9:16), 3 image references for character consistency

### 🛠️ DX & Orchestration
- **Multi-Agent Orchestration** — LangGraph, Vercel Workflows for "long-running agents"
- **Biome** — Rust linter (10x faster than ESLint/Prettier)
- **MCP (Model Context Protocol)** — IDE as hub connecting AI agents to tools

---

## Recommended Pivots & Improvements

### 1. Migrate to Next.js 16.1 + Vercel Workflows
| Action | Priority |
|--------|----------|
| Upgrade to Next.js 16.1 | 🔴 Urgent |
| Migrate `now.json` → `vercel.json` | 🔴 Urgent |
| Implement Vercel Queues for video rendering pipeline | 🟡 Medium |
| Add Vercel DevTools MCP for debugging | 🟢 Nice-to-have |

### 2. Keep Gemini 2.5 (COGS Decision)
| Action | Priority |
|--------|----------|
| **SKIP Gemini 3.1 upgrade** | ✅ Decision: Stick with 2.5 for cost control |
| Monitor API costs closely | 🟡 Ongoing |

### 3. Agentic Architecture Overhaul
**Current:** 5 standalone agents
**Recommended:** Multi-agent orchestration with LangGraph

| Component | Current | New |
|-----------|---------|-----|
| Orchestration | None | LangGraph / Vercel Workflows |
| State Management | Per-agent | Shared graph state |
| Error Recovery | Basic | Long-running with retries |

### 4. Infrastructure Optimizations
| Action | Priority |
|--------|----------|
| Switch linter: ESLint → Biome | 🟢 Quick win |
| Keep Neon Postgres (already correct) | ✅ Done |
| Evaluate Vercel Queues for render queue | 🟡 Medium |

---

## Rollout Plan

### Week 1: Foundation (Mar 12-18)
- [ ] Upgrade Next.js → 16.1
- [ ] Migrate now.json → vercel.json ⚠️ DEADLINE: MAR 31
- [ ] Run Biome migration
- [ ] **SKIP** Gemini upgrade (sticking with 2.5 for COGS)

### Week 2: Agentic Refactor (Mar 19-25)
- [ ] Scope down LangGraph (simplify, not full overhaul)
- [ ] Local end-to-end testing
- [ ] Error recovery & retry logic

### Week 3: Feature Polish (Mar 26-Apr 1)
- [ ] Pipeline stress testing
- [ ] End-to-end local demo
- [ ] Final bug fixes

### Week 4: Beta Prep (Apr 2-8)
- [ ] Load testing
- [ ] Pricing finalization
- [ ] Launch May 1 Beta

---

## E-man's Decisions (Mar 12)
- ✅ Next.js 16.1 + vercel.json migration
- ✅ Biome linter
- ❌ NO Gemini 3.1 (sticking with 2.5 for COGS)
- ❌ NO Veo (building own library)
- 🟡 LangGraph: Simplified, test locally first
- 💰 No budget - bootstrap mode

---

## Open Questions

1. **Budget:** Any constraints on Vercel Pro / Cloud Run?
2. **Team:** Can Lux take the lead on Next.js + LangGraph migration?
3. **Neon:** Is the current Postgres instance sufficient for multi-agent state?
4. **Link Sentinel:** Still needed? Can we use our new Playwright capabilities?

---

*WolfPack Empire 🐺*
