# HEARTBEAT.md

## Context Monitoring (Every 10-15 minutes during active session)
- [x] Check session context usage via session_status
- [x] If context > 80%: Alert E-man, finish current task, recommend new session

## System Health (Every 30 minutes)
- [x] Check gateway status (openclaw status) - ✅ Running on port 18789
- [x] Check Mission Control running (port 8082) - ✅ HTTP 200
- [x] Check Chrome automation running (port 9222) - Not checked (optional)
- [x] Report status if anything down

## Current Architecture (VPS-Only)
- No Nexus - VPS handles everything
- Chrome automation on VPS for business operations
- Mission Control dashboard for monitoring

## Recent Tasks Completed
- ✅ Built PocketPal Android APK (3.6MB)

## Notes
- Gateway: 76.13.195.238:18789
- Mission Control: 76.13.195.238:8082
- Chrome DevTools: localhost:9222
- PocketPal APK: /root/.openclaw/workspace/pocketpal-android.apk
