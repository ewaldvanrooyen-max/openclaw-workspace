# PROJECT BLUEPRINT - ContentEngen

## Project Name
**ContentEngen** - AI Video Content Factory for Overlay Economy

## Vision
AI-driven content factory that generates professional marketing videos using dual-core brain (Gemini), rendering engines, and 4-volume aesthetic matrix. Target: affiliate marketing and content creators.

---

## Core Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Workflows Built | 4 | 4 |
| Videos Generated | - | 0 |
| API Costs | <$50/mo | TBD |
| Aesthetic Themes | 4 | 0 |

---

## Repository
- **URL:** github.com/ewaldvanrooyen-max/contentengen
- **Live Site:** contentengen-dxp-v2 (GCP)

---

## Sub-Projects

### 1. workflows
**Purpose:** Core video generation workflows
**Status:** Functional (4 workflows built)
**Location:** /root/.openclaw/workspace/Contentengen-DXP-v2/
**Tasks:**
- [ ] Connect Gemini API for dynamic scripts
- [ ] Test all 4 workflows end-to-end

### 2. infrastructure  
**Purpose:** Cloud infrastructure for rendering
**Status:** Ready
**Location:** GCP Cloud Run, R2 Storage
**Tasks:**
- [ ] Deploy to production
- [ ] Set up monitoring

### 3. scripts
**Purpose:** TTS, Gemini integration scripts
**Status:** Built
**Location:** /src/lib/
**Tasks:**
- [ ] Add error handling
- [ ] Optimize for cost

### 4. library
**Purpose:** Asset library, backgrounds, templates
**Status:** In progress
**Location:** R2 Bucket
**Tasks:**
- [ ] Upload initial 500 assets
- [ ] Categorize by theme

### 5. free-media
**Purpose:** Free video & image generation scripts
**Status:** Planned
**Location:** /scripts/free-media/
**Tasks:**
- [ ] Set up cron jobs for image generation
- [ ] Set up cron jobs for video generation
- [ ] Add free media generation scripts

---

## Tech Stack
- **Frontend:** Next.js 16.1
- **AI:** Gemini 2.5 Flash via Vertex AI
- **Rendering:** FFmpeg on Cloud Run (L4 GPU)
- **Storage:** Cloudflare R2
- **TTS:** edge-tts (fallback)

---

## Integrations
| Service | Purpose | Status |
|---------|---------|--------|
| Gemini 2.5 | Script generation | Disconnected (testing) |
| Cloud Run | Video rendering | Ready |
| R2 Storage | Asset storage | Connected |
| Vertex AI | AI API | Connected |

---

## Current Blockers
- Gemini API disconnected (testing mode)
- No production deployment yet

---

## Next 7 Days
1. Reconnect Gemini API
2. Test all 4 workflows
3. Deploy to production
4. Set up free-media cron jobs

---

## Notes
- Originally cloned from contentengen-dxp-v2 (kept original as backup)
- Using Ollama as fallback for local AI
