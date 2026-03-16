# Architecture of Autonomous Agency: Comparative Evaluation
**Date:** 2026-03-16

---

## Executive Summary

This document evaluates three approaches to building autonomous AI agents:
1. **Genspark Claw** - Managed "AI employee" ecosystem ($200M ARR)
2. **OpenClaw** - Open-source autonomous framework (316k GitHub stars)
3. **MiniMax M2.5 + Coding Plan** - Economic disruption via subscription

---

## Key Finding

**OpenClaw + MiniMax $20 Coding Plan is the superior choice** for "no monthly limit" autonomous agents.

| Factor | Genspark | OpenClaw + MiniMax |
|--------|----------|-------------------|
| Cost | $25-250/mo (credit-based) | $20-70/mo (fixed) |
| Speed | ~33 TPS | 50-100 TPS |
| Tool Calling | 63.3% | 76.8% |
| Privacy | Shared infrastructure | Local-first |
| Limits | Credit-based | Rate-limited only |

---

## The Stack

```
┌─────────────────────────────────────────────┐
│           AUTONOMOUS AGENT STACK             │
├─────────────────────────────────────────────┤
│                                             │
│  MESSAGING LAYER                            │
│  WhatsApp, Telegram, Slack, Discord         │
│           ↓                                  │
│  OPENCLAW GATEWAY                           │
│  - Sessions, Cron, Skills                    │
│           ↓                                  │
│  MINIMAX M2.5 (Coding Plan)                 │
│  - $20/mo = 300 prompts / 5 hours          │
│  - 80.2% SWE-Bench                         │
│  - 76.8% BFCL Tool Calling                 │
│  - 50-100 TPS                              │
│           ↓                                  │
│  LOCAL TOOLS                                │
│  - FFmpeg, Whisper, Browser                 │
│  - No data leaves unless needed             │
└─────────────────────────────────────────────┘
```

---

## Cost Comparison

| Usage | Genspark | OpenClaw + MiniMax |
|-------|----------|-------------------|
| Personal (Light) | $25/mo | ~$26/mo |
| Business (Moderate) | $250/mo | ~$35/mo |
| Agency (Heavy) | $1,000+ | ~$70/mo |
| "Limitless" | ❌ Not available | ✅ Fixed cost |

---

## Replication: "AI Employee" Workflows

| Genspark Feature | OpenClaw Equivalent |
|-----------------|-------------------|
| Deep Research | Tavily + Summarize |
| AI Slides | Felo Slides / AiPPT |
| Call for Me | Twilio + Voice |
| AI Drive | Local Storage |
| Task Scheduling | Cron / Heartbeat |

---

## The $20 Coding Plan

| Tier | Cost | Prompts/5hr | Use Case |
|------|------|-------------|----------|
| Starter | $10 | 100 | Light loads |
| Plus | $20 | 300 | Professional |
| Max | $50 | 1,000 | High-volume |
| Plus-Highspeed | $40 | 300 | 100 TPS |

**Key:** 1 prompt ≈ 15 model requests

---

## Implementation Steps

1. **Connect MiniMax** → OAuth in OpenClaw onboarding
2. **Create Telegram Bot** → @BotFather → Pair with Gateway
3. **Install Skills** → ClawHub (13,000+ skills)
4. **Set up Cron** → Morning research routines
5. **Deploy** → VPS ($6-10/mo)

---

## Daily Example: Competitive Intelligence

1. **7 AM** - Cron wakes agent
2. **Search** - Tavily web search (competitors)
3. **Synthesize** - M2.5 analyzes 200k token context
4. **Generate** - Felo Slides creates 10-slide PPT
5. **Notify** - Voice call via Twilio
6. **Archive** - Memory file for reference

**Cost:** 2-3 prompts = negligible

---

## Pros & Cons

### OpenClaw + MiniMax
✅ 90% cheaper than Claude Opus
✅ Data sovereignty
✅ No credit limits
✅ 100 TPS speed
❌ Technical setup required
❌ Self-maintenance

### Genspark Claw
✅ Out-of-the-box
✅ Professional outputs
✅ Managed infrastructure
❌ Credit-based limits
❌ More expensive
❌ Less customization

---

## Strategic Implication

For the WolfPack Empire:
- Use OpenClaw + MiniMax as the foundation
- Build custom skills for GHL, ContentEngen, etc.
- Achieve "limitless" automation at fixed cost

**This is exactly what we're building.**
