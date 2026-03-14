# Image Generation Skill

## Overview
Generate images using Leonardo.ai API for ContentEngen library seeding.

## Prerequisites
- Leonardo.ai account
- API key from https://leonardo.ai/account
- Free tier: 150 tokens/day

## Configuration
Store API key in: `~/.openclaw/credentials/leonardo-api.json`
```json
{
  "api_key": "your-leonardo-api-key"
}
```

## Usage

### Generate Image
```bash
leonardo-gen "A modern fleet management office with computers" --model lucidorigin --width 1024 --height 1024
```

### Seed Library (Batch)
```bash
# Generate 10 images from manifest
leonardo-seed --count 10 --volume Sovereign
```

## Scripts
- `scripts/leonardo-generate.py` - Single image generation
- `scripts/leonardo-seed.py` - Batch generation for library

## Cron Job (Hourly)
```bash
0 * * * * /root/.openclaw/workspace/scripts/leonardo-seed.sh --count 10 >> /var/log/leonardo-seed.log 2>&1
```

## Models Available
- lucidorigin (default)
- kino
- anime
- creative

---
*Created: 2026-03-14*
