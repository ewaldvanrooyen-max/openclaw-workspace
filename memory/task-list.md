# WolfPack Empire - Task List

**Date:** 2026-03-15
**Status:** Organization System Setup

---

## 🎯 Today's Priorities

### Skills Installation (Aris)
- [ ] ~~Install: agent-brain~~ - NOT AVAILABLE in repo
- [ ] ~~Install: alex-session-wrap-up~~ - NOT AVAILABLE in repo
- [ ] ~~Install: agent-task-tracker~~ - NOT AVAILABLE in repo
- [ ] ~~Install: active-maintenance~~ - NOT AVAILABLE in repo
- [x] **BUILD OURS:** Use built-in OpenClaw tools (memory, cron, subagents)

### Implementation - ✅ DONE
- [x] Configure health loop: Aris ↔ Nexus (cron every 30 min)
- [x] Set up daily memory ritual (cron: 8am SA)
- [x] Create pre-reply checklist (PREPLY_CHECKLIST.md)
- [ ] Document all projects in PROJECTS.md

### Infrastructure (E-man - YOU)
- [ ] Fix Nexus connection (check if your machine is online)
- [ ] Set up Tailscale on Nexus if not running
- [ ] Verify SSH access from VPS to Nexus

---

## 📋 What You Need to Do

1. **Check your machine** - Is Nexus/your PC online? Can you access it locally?
2. **Tailscale** - Make sure Tailscale is running on your machine
3. **SSH test** - Try SSH: `ssh aris-steyn@192.168.5.116`
4. **Review plan** - Read /memory/organization-plan.md

---

## ❓ What's Mission Control?

Found on VPS:
- Port 8000: Chroma DB (PocketPal)
- Port 3000: Contentengen  
- Port 8081: FFmpeg worker

Is it something else? Let me know.

---

## System Status

| Component | Status |
|-----------|--------|
| Contentengen | Working, 3/4 workflows |
| FFmpeg worker | Running :8081 |
| Health cron | ✅ Every 30 min |
| Daily standup | ✅ 8am SA |
| Pre-reply checklist | ✅ PREPLY_CHECKLIST.md |
| Nexus | ❌ Disconnected |
