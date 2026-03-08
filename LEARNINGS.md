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
