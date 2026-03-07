# DEON'S OPERATIONAL MEMORY

## The Team

- **E-man** - Partner, Fleet & Asset Finance Veteran. The boss.
- **Max** - Orchestrator (me, Qwen 3b). Breaking down tasks, delegating.
- **Lux** - Heavy-duty coder (qwen2.5:3b). Writes the actual code.
- **Aris** - VPS instance, runs on 76.13.195.238. Always-on backend.

## Workspace Structure

```
~/Eman_Records/           # Main workspace
├── projects/
│   ├── mlc-crm/          # MLC CRM system
│   ├── contentengen/      # Content generation
│   ├── email-pipeline/    # Email automation
│   ├── business-intelligence/
│   ├── meeting-sync/
│   └── mlc-dealership/
├── knowledge/             # Knowledge base
├── memory/               # Session memories
├── mlc/                  # MLC docs
├── skills/               # OpenClaw skills
└── backups/

~/openclaw/               # OpenClaw source (Aris's main repo)
```

## VPS (Aris)

- **Host:** 76.13.195.238
- **User:** root
- **SSH:** ~/.ssh/id_ed25519
- **Services:**
  - OpenClaw gateway
  - Ollama (local models)
  - Postgres, Redis
  - SearxNG
  - MLC Nginx

## Current Models

- **Local (me):** qwen2.5:3b (1.9GB)
- **VPS:** codellama:7b (tool issues), qwen2.5:0.5b fallback
- **Available locally:** llama3.2:3b, phi3.5:3.8b, gemma2:2b

## Credentials

- ~/Documents/credentials/
- ~/.openclaw/credentials/

## Key Commands

- SSH to VPS: `ssh -i ~/.ssh/id_ed25519 root@76.13.195.238`
- Check VPS gateway: `ps aux | grep openclaw`
- Restart VPS gateway: `systemctl --user restart openclaw-gateway`

## Active Tasks

- VPS Telegram still broken (tool issues with codellama)
- Need to configure MCP on VPS for tool support
- Agent Zero setup for Twilio/MCL workflow (not yet implemented)

---

_Updated: 2026-03-03_
