# CE-AUDIT-001: ContentEngin Workflows Audit

**Date:** 2026-03-08
**Auditor:** Lux

## Summary

ContentEngin is hosted on Google Cloud Platform (GCP project: contentengen-dxp-v2). No local code found in workspace for direct audit.

## 4 Workflows Status (from PROJECTS.md)

| Workflow | Description | Status |
|----------|-------------|--------|
| Demo | Website tutorial enhancer | ✅ Functional |
| Narrator | Viral storytelling/documentary | ✅ Functional |
| Teacher | Multi-part lesson generator | ✅ Functional |
| Closer | Product review + affiliate links | ✅ Functional |

## Technical Stack

- **Brain:** Gemini 2.5 Flash via Vertex AI (connected, disabled for testing)
- **Rendering:** FFmpeg on Cloud Run (L4 GPU) ✅
- **Storage:** Cloudflare R2 ✅
- **TTS:** edge-tts (fallback)

## What's Working

1. All 4 workflow templates exist
2. Cloud infrastructure ready (Cloud Run, R2)
3. Gemini API client documented (ce-gemini-001.md)
4. Bilingual support (English/Afrikaans)

## What's Broken / Needs Attention

1. **Gemini API** - Connected but disabled for testing (needs API key)
2. **No local codebase** - Cannot audit code without local repo
3. **Missing aesthetic themes** - 4 themes not yet implemented

## What's Needed for Local Testing

### Prerequisites
1. Node.js environment
2. FFmpeg installed locally
3. GCP service account credentials (for Vertex AI + R2)
4. Gemini API key from https://aistudio.google.com/app/apikey

### Local Setup Requirements
```
npm install @google/generative-ai
npm install @ffmpeg-installer/ffmpeg
# Configure GCP credentials
# Mount R2 bucket for asset storage
```

### Testing Steps
1. Clone/deploy ContentEngin from GCP
2. Set environment: GEMINI_API_KEY, GCP_PROJECT, R2 credentials
3. Run workflow tests with sample inputs
4. Verify FFmpeg rendering

## Recommendation

To properly audit the 4 workflows in detail, either:
- **Option A:** Access the GCP Cloud Run endpoints directly
- **Option B:** Clone the ContentEngin repo to local workspace
- **Option C:** Request E-man provide access/credentials for local deployment

---

**Status:** AUDIT COMPLETE - Limited by no local access
**Next Step:** Obtain ContentEngin codebase or GCP access for deeper audit
