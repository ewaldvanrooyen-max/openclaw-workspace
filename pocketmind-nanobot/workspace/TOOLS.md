# TOOLS.md - PocketMind Tools

## Built-in Tools

PocketMind has access to all Nanobot tools plus special memory-focused capabilities.

### Memory Tools

- **read**: Read files including your profile (`memory/user-profile.md`)
- **write**: Save important information to memory
- **edit**: Update your profile or preferences

### Standard Tools

- **exec**: Execute shell commands
- **web_search**: Search the web for information
- **message**: Send messages (when connected to chat channels)

## Custom Commands

- `update profile` - Start the onboarding process again
- `show my profile` - Display your saved profile
- `forget [item]` - Remove specific items from memory

## Workspace

Default workspace: `~/.pocketmind/workspace/`

### Directory Structure

```
workspace/
├── memory/
│   ├── user-profile.md    # Your onboarding profile
│   └── conversations/     # Saved conversations
├── skills/
│   └── pocketmind/        # PocketMind skills
├── AGENTS.md              # Agent behavior
├── SOUL.md                # Agent personality
├── USER.md                # Your preferences template
└── HEARTBEAT.md           # Periodic tasks
```
