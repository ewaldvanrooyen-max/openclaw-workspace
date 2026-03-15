# Contentengen Workflow Audit Plan

**Date:** 2026-03-15
**Status:** In Progress

---

## Current State

| Component | Status | Notes |
|-----------|--------|-------|
| Next.js 16.1.6 | ✅ | Running on localhost:3000 |
| vercel.json | ✅ | Configured with crons |
| Biome | ✅ | Linter configured |
| Ollama gemma:2b | ✅ | Configured |
| Test User | ✅ | create@contentengen.com |

---

## Workflow Test Results

| Workflow | Status | Draft Created | Issue |
|----------|--------|---------------|-------|
| **Story** | ✅ Works | Yes | Safety audit needs GCP |
| **Product Review** | ✅ Works | Yes | Safety audit needs GCP |
| **How-To** | ⚠️ Partial | Yes | Instructor agent error |
| **Tutorial** | ❌ Fails | No | manifest undefined |
| **Website Tutorial** | Not tested | - | - |

---

## Blockers

1. **GCP Credentials** - Safety audit fails without them
2. **FFmpeg Worker** - Not running (need to build Docker)
3. **Tutorial Mode** - Code bug (manifest undefined)
4. **How-To Mode** - Instructor agent error

---

## Execution Plan

### Phase 1: Fix GCP Credentials
- [ ] Obtain GCP service account JSON
- [ ] Add to .env.local
- [ ] Test safety audit passes

## Execution Plan

### Phase 1: Fix GCP Credentials (pending)
- [ ] Obtain GCP service account JSON

### Phase 2: FFmpeg Worker ✅ COMPLETED
- [x] Build Docker - Skipped, running Node.js directly
- [x] Run worker on port 8081 ✅ LIVE
- [ ] Test full render end-to-end

### Phase 3: Fix Code Bugs
- [ ] Fix Tutorial mode (manifest undefined) - Lux working on it
- [ ] Fix How-To mode (instructor agent error)

### Phase 3: Fix Code Bugs
- [ ] Fix Tutorial mode (manifest undefined)
- [ ] Fix How-To mode (instructor agent error)

### Phase 4: Final Audit
- [ ] Document each workflow: inputs, outputs, quality rating
- [ ] List remaining blockers

---

## Resources Needed
- Docker (available ✅)
- FFmpeg (check if installed)
- GCP credentials (blocking)

---

## Estimated Timeline
- Phase 1-2: 1-2 hours
- Phase 3: 1 hour
- Phase 4: 30 min
- **Total: ~3 hours**
