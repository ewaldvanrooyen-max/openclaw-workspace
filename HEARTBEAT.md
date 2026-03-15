# HEARTBEAT.md

## Context Monitoring (Every 10-15 minutes during active session)
- [ ] Check session context usage via session_status
- [ ] If context > 80%: Alert E-man, finish current task, recommend new session

## System Health (Every 30 minutes)
- [ ] Check gateway status (openclaw status)
- [ ] Check Mission Control running (port 8082)
- [ ] Check Chrome automation running (port 9222)
- [ ] Report status if anything down

## Current Architecture (VPS-Only)
- No Nexus - VPS handles everything
- Chrome automation on VPS for business operations
- Mission Control dashboard for monitoring

## Notes
- Gateway: 76.13.195.238:18789
- Mission Control: 76.13.195.238:8082
- Chrome DevTools: localhost:9222
