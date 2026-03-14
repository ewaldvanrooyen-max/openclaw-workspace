# Open Source TTS Research - 2026

## Top Options for Local TTS

### 1. Kokoro-82M ⭐ RECOMMENDED
- **Size:** 82M parameters (~500MB with weights)
- **Quality:** Excellent - rivals ElevenLabs
- **Speed:** Very fast, ~100ms TTFA
- **Languages:** EN, ES, FR, IT, PT, ZH, JA, HI
- **Voices:** Multiple built-in voices
- **License:** Apache 2.0 (commercial friendly)
- **Install:** `pip install kokoro`

### 2. Fish Speech S2
- **Size:** ~1.2GB
- **Quality:** Premium, emotional expression
- **Features:** Natural Language Tags for emotions
- **Best for:** Creative/storytelling

### 3. GPT-SoVITS V4
- **Size:** ~1.5GB
- **Quality:** Voice cloning from 30-60s audio
- **Best for:** Personalized voices

### 4. Piper
- **Size:** ~50MB (tiny!)
- **Quality:** Decent, not great
- **Best for:** Low-power background tasks

---

## Kokoro Setup on VPS

### Installation
```bash
python3 -m venv /opt/tts-env
/opt/tts-env/bin/pip install kokoro soundfile
```

### Usage
```python
from kokoro import KPipeline
pipeline = KPipeline(lang_code='a')  # American English
generator = pipeline("Hello world!", voice='af_heart')
for gs, ps, audio in generator:
    # audio is numpy array at 24kHz
    sf.write('output.wav', audio, 24000)
```

### Available Voices
| Voice ID | Description |
|----------|-------------|
| af_heart | Female, warm |
| af_sarah | Female, clear |
| am_michael | Male, deep |
| am_fen | Male, soft |
| bf_emma | British female |
| bm_george | British male |

---

## Telegram Integration

For voice notes:
1. Generate WAV using Kokoro
2. Convert to MP3/OGG (optional)
3. Send via Telegram Bot API

---

## Testing Done
- ✅ Installed Kokoro on VPS
- ✅ Generated test audio (255KB for ~10s)
- ✅ Ready for production use

---
*Updated: 2026-03-14*
