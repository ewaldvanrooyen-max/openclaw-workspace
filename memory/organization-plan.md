# WolfPack Empire - Organization Plan

**Created:** 2026-03-15
**Purpose:** Fix continuity, health loops, project tracking

---

## Problems to Solve

1. Every day starts fresh - no continuity
2. VPS ↔ Nexus unstable connection  
3. No health loop - don't know when things go down
4. Projects scattered everywhere
5. No pre-reply rules

---

## Recommended Skills to Install

### Continuity & Memory
| Skill | Purpose |
|-------|---------|
| [agent-brain](https://github.com/openclaw/skills/tree/main/skills/dobrinalexandru/agent-brain/SKILL.md) | Local-first persistent memory with SQLite |
| [alex-session-wrap-up](https://github.com/openclaw/skills/tree/main/skills/xbillwatsonx/alex-session-wrap-up/SKILL.md) | End-of-session: commit work, extract learnings, persist rules |
| [agent-task-tracker](https://github.com/openclaw/skills/tree/main/skills/rikouu/agent-task-tracker/SKILL.md) | Proactive task state management |

### Health Monitoring
| Skill | Purpose |
|-------|---------|
| [active-maintenance](https://github.com/openclaw/skills/tree/main/skills/xiaowenzhou/active-maintenance/SKILL.md) | Automated system health and memory metabolism |

### Project Tracking
| Skill | Purpose |
|-------|---------|
| [agent-daily-planner](https://github.com/openclaw/skills/tree/main/skills/gpunter/agent-daily-planner/SKILL.md) | Structured daily planning and execution tracking |

---

## Solution Architecture

### 1. VPS ↔ Nexus Connection
**Current:** Tailscale (VPS can reach Nexus via 100.x.x.x)
**Problem:** Connection drops
**Solution:**
- Use Tailscale with persistent connection
- Set up SSH tunnel as backup
- Register both as nodes in OpenClaw

### 2. Health Loop Protocol
```
Aris (VPS) checks Nexus:
- Every 30 min: ping Nexus via Tailscale
- If down: alert E-man, continue operating

Nexus checks Aris:
- Every 30 min: curl gateway status  
- If down: alert E-man, pick up critical tasks
```

### 3. Daily Continuity Checklist
Before every session:
- [ ] Read memory/YYYY-MM-DD.md (yesterday)
- [ ] Read MEMORY.md (long-term)
- [ ] Check active tasks from agent-task-tracker
- [ ] Check HEARTBEAT.md for pending items

End of every session:
- [ ] Update memory/YYYY-MM-DD.md with what happened
- [ ] Update MEMORY.md with key learnings
- [ ] Mark completed tasks in tracker

### 4. Pre-Reply Rules
Before responding to user:
1. Check if it's a heartbeat → follow HEARTBEAT.md
2. Check memory for context
3. Check health status (Aris/Nexus)
4. Check active tasks

### 5. Project Organization
| Project | Location |
|---------|----------|
| Contentengen | /workspace/Contentengen-DXP-v2 |
| IC Pipeline | /workspace/ic |
| PocketMind | /workspace/pocketmind |
| Socials | /workspace/Socials |
| Skills | ~/.openclaw/skills |

---

## Implementation Steps

### Week 1: Foundation
1. [ ] Install core skills (agent-brain, session-wrap-up, active-maintenance)
2. [ ] Configure Tailscale for stable connection
3. [ ] Set up health check cron jobs
4. [ ] Create daily memory ritual

### Week 2: Tracking
1. [ ] Set up agent-task-tracker
2. [ ] Create project status dashboard
3. [ ] Document all projects in PROJECTS.md

### Week 3: Optimization
1. [ ] Fine-tune pre-reply rules
2. [ ] Add automation for routine tasks
3. [ ] Review and iterate

---

## Skills Installation Status

**Problem:** Specific skills not found in OpenClaw repo. Cloned full repo (5400+ skills) but exact matches don't exist.

**What we CAN do:**
1. Build our own using existing skills as templates
2. Use built-in OpenClaw features (memory, cron, subagents)
3. Implement organization manually (what we're doing)

**Our built-in tools:**
- ✅ Memory system (MEMORY.md + memory/YYYY-MM-DD.md)
- ✅ Cron jobs (openclaw cron)
- ✅ Subagents (Max, Lux, Jiles)
- ✅ Heartbeats

This is actually fine - we can build the system ourselves!
