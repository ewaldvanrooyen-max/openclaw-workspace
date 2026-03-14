# Video Generation Skill

## Overview
Generate videos using Kaiber.ai API for ContentEngen library seeding.

## Prerequisites
- Kaiber.ai account (free tier available)
- API key from https://kaiber.ai/settings
- Free tier: ~100 credits/day

## Configuration
Store API key in: `~/.openclaw/credentials/kaiber-api.json`
```json
{
  "api_key": "your-kaiber-api-key"
}
```

## Usage

### Generate Video
```bash
kaiber-gen --prompt "Golden particles falling" --seconds 5 --style motion
```

### Seed Library (Batch)
```bash
# Generate 3 videos from manifest
kaiber-seed --count 3 --volume Kinetic_Glitch
```

## Scripts
- `scripts/kaiber-generate.py` - Single video generation
- `scripts/kaiber-seed.py` - Batch generation for library

## Cron Job (Every 2 hours)
```bash
0 */2 * * * /root/.openclaw/workspace/scripts/kaiber-seed.sh --count 3 >> /var/log/kaiber-seed.log 2>&1
```

## Styles Available
- motion (default)
- animation
- anime
- realistic

---
*Created: 2026-03-14*
