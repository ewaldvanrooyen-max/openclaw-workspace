# Learnings

A record of lessons learned, mistakes made, and things to remember.

---

## 2026-03-08

### System Architecture
- **Sequential agent spawning** works better than parallel - prevents context drift
- **30-minute intervals** = sweet spot - prevents hallucinations, maximizes throughput
- **Task rotation** across agents ensures no single agent gets overloaded

### What Worked
- Git-based workspace sync between Aris and Nexus
- BLACKBOARD.json as single source of truth
- Discord webhooks for notifications
- Forum channels for project organization

### What Didn't Work
- Agent spawning with `--url` flag (version mismatch)
- Parallel agent spawning caused context issues
- Port 80 blocking on VPS (website issue)

### Mistakes Made
- Added PATH to scripts but forgot initially - cron jobs failed
- Multiple cron entries caused conflicts
- Tried to spawn too many agents at once

### To Implement
- [ ] Task weighting system (short vs long tasks)
- [ ] Auto-pause for complex tasks
- [ ] Better error handling in spawner

---

## Older Learnings
(To be added)

### 2026-03-09 Morning - Task Review Session

Completed:
- INCOME-001: Affiliate marketing, digital products approved (Tier 1)
- PHONE-001: MTN SIM + cheap Android approved
- BROWSER-001: Playwright default, SecretAgent skill to build
- HF-IMAGE-001: Free credits minimal, need paid provider
- CE-AUDIT-001: 4 workflows functional, needs GCP creds
- CE-GEMINI-001: Integration ready, API key needed
- GHL-RESEARCH-001: Autonomous layer approved

New Tasks Created:
- SA-TIME-001: Configure agents for SA timezone
- SIM-SA-001: Get MTN Superflex
- DEVICE-001: Cheap Android for social
- NANOBOT-001: Android automation for notifications
- PLAYWRIGHT-001: Install on VPS
- SECRETAGENT-SKILL-001: Build skill
- VIDEO-002: Re-run video limits
- CLAWHUB-001: Search VoltAgent skills
- GHL-SCRAPER-001, GHL-VERIFIER-001, GHL-QUOTE-001, GHL-NEGOTIATOR-001

GOAL: IC Application Process 90% by Friday
