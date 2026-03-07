## VPS

- **Host:** 76.13.195.238
- **User:** root
- **SSH Key:** ~/.ssh/id_ed25519

### Services Running
- mission-control-backend (8000)
- mission-control-frontend (3000)
- postgres (5432)
- redis (6379)
- searxng (8080)
- mlc-nginx (8888)

## Credentials Location
- Local vault: ~/.openclaw/credentials/
- External backup: ~/Documents/credentials/

Skills define _how_ tools work. This file is for _your_ specifics - the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
