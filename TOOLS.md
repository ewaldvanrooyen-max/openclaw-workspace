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

## Nexus (Local Machine)
- **Name:** aris-steyn-imedia-S2870
- **Connection:** Via OpenClaw node (paired & connected)
- **SSH:** aris-steyn@192.168.5.116 (local IP)
- **Health Check:** Run `openclaw nodes status` to verify connection
- **Git Sync:** 
  - Workspace: `/home/aris-steyn/openclaw-workspace/`
  - To sync: `cd /home/aris-steyn && git clone https://github.com/ewaldvanrooyen-max/openclaw-workspace.git`
  - Then `git pull` to get updates

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

## Interlinked Capital (IC) - Social Media

### Branding
- **Business Name:** Interlinked Capital
- **Tagline:** Fleet & Asset Finance Specialists
- **Website:** interlinkedcapital.co.za
- **Location:** South Africa
- **Stakeholders:** E-man (70%), Mario (30%)

### Available Credentials
- **Business Email:** aris@interlinkedcapital.co.za (password: [REDACTED])
- **Alternative Email:** ewald@interlinkedcapital.co.za (password: [REDACTED])
- **Gmail (personal):** steynarisa@gmail.com / App password: [REDACTED]

### Social Media Accounts Status

| Platform | Status | Account | Credentials |
|----------|--------|---------|-------------|
| Website | ✅ LIVE | https://interlinkedcapital.co.za | - |
| Facebook | ✅ Created | @interlinkedcapital | steynaris@gmail.com / [REDACTED] |
| Instagram | ✅ Created | @interlinkedcapital | steynaris@gmail.com / [REDACTED] |
| Twitter/X | Needs setup | - | steynaris@gmail.com (Google auth) |
| LinkedIn | Needs setup | - | steynaris@gmail.com (Google auth ready) |

### Logo
- **ic-logo.jpg** - /var/www/ic-website/ic-logo.jpg (37KB)
- **mlc-logo.png** - /var/www/ic-website/images/mlc-logo.png (173KB)
- **mlc-logo-signature.png** - /var/www/ic-website/images/mlc-logo-signature.png (390KB)

### Next Steps (Manual Action Required)
1. **Make website live** - Get interlinkedcapital.co.za running
2. **Extract/Create logo** - Pull from website or design new
3. **Create accounts manually** - Each platform requires human verification:
   - Twitter/X: x.com (business account)
   - LinkedIn: linkedin.com/company/interlinked-capital
   - Facebook: facebook.com/interlinkedcapital
   - Instagram: @interlinkedcapital
4. **Link accounts** - Add website URL and consistent bio across all platforms

---

Add whatever helps you do your job. This is your cheat sheet.
