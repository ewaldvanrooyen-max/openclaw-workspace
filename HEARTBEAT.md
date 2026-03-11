# HEARTBEAT.md

## Context Monitoring (Every 10-15 minutes during active session)
- [ ] Check session context usage via session_status
- [ ] If context > 80%: Alert E-man, finish current task, recommend new session

## Health Loop (Every 30 minutes)
### Aris checking on Nexus (VPS → Local)
- [ ] Check if Nexus is reachable via node status
- [ ] If Nexus down: Alert E-man

### What Nexus should check on Aris:
- [ ] Check VPS gateway status
- [ ] If Aris down: Nexus has write access as 2IC to handle urgent tasks
- [ ] Alert E-man if critical

## Notes
- 2IC Protocol: If Aris is down, Nexus can write to memory/docs temporarily
- Failover: Jobs continue on whichever instance is up
