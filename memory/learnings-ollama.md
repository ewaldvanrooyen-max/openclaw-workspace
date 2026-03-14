# Ollama - Local AI (Recommended)

## Why Ollama?
- ✅ Free - no API costs
- ✅ Runs locally on VPS
- ✅ No external dependencies
- ✅ Privacy-first (data stays on server)
- ✅ 12 models available

## Models Available
- llama3.3 (latest)
- qwen2.5 (various sizes)
- gemma2b (lightweight)
- mistral
- And more...

## Setup for ContentEngen

### 1. API Endpoint
```
OLLAMA_API_URL=http://127.0.0.1:11434
```

### 2. Use Ollama SDK
```javascript
import { Ollama } from 'ollama'

const ollama = new Ollama({ host: 'http://127.0.0.1:11434' })
```

### 3. Model Selection
For video generation scripts:
- **llama3.3** - Best quality, slower
- **qwen2.5:7b** - Good balance
- **mistral** - Fast, decent quality

## Benefits
- No rate limits
- No billing issues
- Instant response
- Fully controlled

## Notes
- VPS needs adequate RAM (7b models = ~8GB RAM)
- GPU recommended but CPU works for small models

---
*Updated: 2026-03-14*
