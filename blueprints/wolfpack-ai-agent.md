# PROJECT BLUEPRINT - WolfPack AI Agent

## Project Name
**WolfPack AI Agent** - Genspark Alternative

## Vision
Build a subscription-based "unlimited" AI agent wrapper around OpenClaw. Sell to users who want Genspark-like capabilities but at lower cost with more privacy.

---

## The Concept

**Similar to:** Genspark Claw, but:
- Built on OpenClaw (open-source)
- Powered by MiniMax (cheap)
- Local-first option (PocketPal)

### Local Models (via Ollama) - Updated 2026-03-16
| Model | Size | RAM | Notes |
|-------|------|-----|-------|
| **Qwen 3 VL** | 2-4B | 4-8GB | Top pick - 128k context |
| **Gemma 3** | 4B | 8GB | Google's best |
| **Llama 3.2 Vision** | 11B | 16GB | Best quality |
| **DeepSeek-OCR** | 3B | 6GB | Document parsing |

**Key:** Must have 128k context for OpenClaw. Old models (LLaVA 7B) = too small = crashes.

**Key Feature:** "Unlimited" AI agent
- User pays $30/mo
- We pay ~$15/mo to MiniMax
- **Margin: $15/user (50%)**

---

## Pricing Model

| Tier | Price | Cost | Margin |
|------|-------|------|--------|
| Basic | $15/mo | $10/mo | $5/mo |
| **Pro** | **$30/mo** | **$15/mo** | **$15/mo** |
| Ultra | $50/mo | $20/mo | $30/mo |
| Enterprise | $100/mo | $30/mo | $70/mo |

**Target:** 100 Pro users = $1,500/mo revenue, $750 profit

---

## Features

### Core
- AI Chat (MiniMax)
- Image Generation (Leonardo)
- Video Generation (Kaiber)
- Browser Automation (Playwright)

### Premium
- Voice (TTS/STT)
- Custom Nanobots
- API Access
- Priority Support

### Competitor-Crushing Features (from research)
1. **Persistent Project Memory** - Like Claude's CLAUDE.md, auto-loads project context
2. **Cross-Session Context** - Users don't re-explain every time
3. **Workflow Recording** - Record & replay browser automation
4. **Agent Marketplace** - Pre-built templates users can share
5. **Privacy Signals** - Visible data sovereignty guarantees

### Differentiators
- Privacy-first (local option via PocketPal)
- Open-source core
- Industry-specific agents (finance, fleet)

---

## Tech Stack

```
Frontend → Next.js + Auth + Billing
     ↓
API Gateway (rate limiting, quotas)
     ↓
OpenClaw Cluster
     ↓
MiniMax API + Skills (Leonardo, Kaiber, etc.)
```

---

## 4-Phase Plan

### Phase 1: Foundation
- [ ] Set up multi-user auth
- [ ] Connect MiniMax with quota tracking
- [ ] Basic billing (Lemon Squeezy/Stripe)
- [ ] **Persistent Project Memory** (auto-load PROJECT.md)

### Phase 2: Core Features
- [ ] Image gen (Leonardo)
- [ ] Video gen (Kaiber)
- [ ] Browser automation
- [ ] **Cross-Session Context**

### Phase 3: Premium
- [ ] Voice (TTS/STT)
- [ ] Custom Nanobots
- [ ] API access
- [ ] **Workflow Recording**
- [ ] **Agent Marketplace**

### Phase 4: Scale
- [ ] Mobile app
- [ ] White-label options
- [ ] Enterprise features
- [ ] **Privacy Dashboard**

---

## Competition

| Competitor | Price | Our Advantage |
|------------|-------|---------------|
| Genspark | $29/mo | Cheaper, privacy |
| ChatGPT Plus | $20/mo | More features |
| Claude Pro | $20/mo | Images/videos included |

---

## Risks

- MiniMax price changes
- Rate limiting enforcement
- Support costs at scale

---

## Status
**Concept only** - Not started

---

## Notes
- Idea: E-man (2026-03-16)
- Pricing: $30 user / $15 MiniMax = 50% margin
