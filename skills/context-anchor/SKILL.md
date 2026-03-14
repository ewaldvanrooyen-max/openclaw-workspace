---
name: context-anchor
description: Recovers from context compaction by scanning memory files for current task, daily logs, in-progress files. Extracts decisions and open loops, generates briefing after compaction.
---

# Context Anchor Skill

## Purpose
Recover from context compaction by anchoring to existing memory and tasks.

## When to Use
- After context compaction
- At start of new session
- When uncertain about current state

## Actions

### 1. Scan Memory Files
Read recent memory files to understand current state:
- `memory/YYYY-MM-DD.md` - Today's logs
- `MEMORY.md` - Long-term memory
- Check for in-progress work

### 2. Extract Key Information
From memory, identify:
- Current active projects
- Recent decisions
- Open loops/todos
- Blockers

### 3. Generate Briefing
Create a brief summary of:
- What was in progress
- What's pending
- Next steps

## Usage
This skill runs automatically after compaction. No explicit invocation needed.
