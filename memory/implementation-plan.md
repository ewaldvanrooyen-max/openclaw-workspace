# Implementation Plan: Agent HQ + Mission Control

**Date:** 2026-03-15

---

## What We Have

### 1. Mission Control (VPS :8082) ✅ RUNNING
- Dashboard, Chat, Workshop
- Cron Monitor, Cost Tracker
- Agent Hub, Skills
- Problem: Config points to wrong paths

### 2. Agent HQ Skill
- Found in ~/.openclaw/skills/skills/thibautrey/agent-hq/
- Just metadata, not full install

---

## Implementation Plan

### Phase 1: Fix Mission Control (Today)
- [ ] Update config to use VPS paths
- [ ] Connect Nexus when it comes online
- [ ] Verify Agent Hub sees both agents

### Phase 2: Build Agent HQ Features (This Week)
Create our own task board:

| Feature | Implementation |
|---------|---------------|
| Task tracking | SQLite database in /workspace |
| Cron monitor | Already in Mission Control |
| Telegram alerts | Use existing cron → Telegram |
| Agent status | Gateway API |

### Phase 3: Connect Nexus (Today)
- [ ] You start OpenClaw on Nexus
- [ ] Both agents visible in Mission Control

---

## What E-man Needs To Do
1. Start OpenClaw on Nexus/local machine
2. Test Mission Control at http://76.13.195.238:8082

---

## What Aris Will Do
1. Fix Mission Control config
2. Set up SQLite task board
3. Configure Telegram notifications

---

## Files Created
- /memory/organization-plan.md
- /memory/skills-research.md  
- /memory/task-list.md
- /PREPLY_CHECKLIST.md
