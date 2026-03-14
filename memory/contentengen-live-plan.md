# ContentEngen Live Plan
**Created:** 2026-03-14  
**Role:** Lux (Code Execution Specialist)  
**Focus:** Minimum Viable Product to Launch

---

## 📊 Current State Assessment

### What IS Working (Contrary to Documentation)

| Component | Status | Notes |
|-----------|--------|-------|
| Next.js 16.1.6 | ✅ DONE | Already upgraded |
| vercel.json | ✅ DONE | Already migrated |
| Biome linter | ✅ DONE | Already configured |
| 4 Workflows | ⚠️ PARTIAL | Code exists, not tested end-to-end |
| FFmpeg | ✅ READY | Cloud Run configured |
| R2 Storage | ✅ READY | Configured |
| Gemini 2.5 | ⚠️ DISABLED | Connected but off for testing |

### What ISN'T Working

| Blocker | Severity | Impact |
|---------|----------|--------|
| Gemini API disabled | 🔴 HIGH | No dynamic script generation |
| No end-to-end tests | 🔴 HIGH | Can't verify anything works |
| LangGraph not implemented | 🟡 MEDIUM | Using simple sequential flow |
| No clear MVP | 🔴 HIGH | Scope too large (70+ services) |
| Too much complexity | 🔴 HIGH | Can't debug what's broken |

---

## 🎯 MVP Definition: "Ship ONE Workflow"

**Instead of 4 workflows, launch with 1.**

### Simplest Path: Website Tutorial (Demo) Workflow

**Why:**
- Most straightforward - screen recording → script → dubbed video
- Uses existing assets (no new content creation)
- Clear value proposition for users

**What it does:**
1. User submits URL or upload
2. AI generates script from content
3. AI dubs with TTS
4. Video rendered via FFmpeg
5. Download link returned

**Skip for MVP:**
- ❌ LangGraph orchestration (use simple sequential flow)
- ❌ Multiple aesthetic themes (use one default)
- ❌ Payment integration (manual for now)
- ❌ Affiliate link injection (manual for now)
- ❌ Music library (use stock/royalty-free)

---

## 🚀 Execution Plan (2-3 Days)

### Day 1: Re-enable & Verify Core

| Task | Priority | Time |
|------|----------|------|
| Re-enable Gemini API | P0 | 30 min |
| Verify env vars loaded | P0 | 15 min |
| Run local dev server | P0 | 30 min |
| Test single endpoint | P1 | 1 hour |

**Commands:**
```bash
cd /root/.openclaw/workspace/Contentengen-DXP-v2
npm run dev
```

### Day 2: E2E Test Single Workflow

| Task | Priority | Time |
|------|----------|------|
| Identify working demo endpoint | P0 | 1 hour |
| Run manual test (curl) | P0 | 30 min |
| Fix critical errors | P0 | 2 hours |
| Verify video output | P1 | 1 hour |

**Focus:** Get ONE video generated end-to-end

### Day 3: Deploy & Validate

| Task | Priority | Time |
|------|----------|------|
| Deploy to Vercel | P0 | 15 min |
| Set env vars in Vercel | P0 | 15 min |
| Test production endpoint | P0 | 30 min |
| Create simple landing page | P1 | 2 hours |

---

## 📋 Specific Blockers to Fix

### 1. Gemini API Disabled
**Check:** Look for disabled-config.json or env toggle
**Fix:** Enable in environment or config file
**File to check:** `src/lib/config/`

### 2. Missing Env Vars
**Required:**
- `GOOGLE_APPLICATION_CREDENTIALS` or Vertex AI config
- `DATABASE_URL` (Neon)
- `R2_` vars for storage
- `GEMINI_API_KEY`

### 3. FFmpeg Worker Not Responding
**Check:** Cloud Run service health
**Fallback:** Use local FFmpeg for testing

### 4. Database Schema Mismatch
**Check:** Run `npx prisma db pull` to sync
**Fix:** `npx prisma migrate deploy`

---

## 🧪 Test Checklist (Before Launch)

- [ ] Homepage loads
- [ ] Login/auth works
- [ ] Can submit a URL for processing
- [ ] Script generation works (Gemini)
- [ ] TTS generates audio
- [ ] Video renders (FFmpeg)
- [ ] Video downloadable
- [ ] No critical console errors
- [ ] Mobile responsive

---

## 🎯 Success Metrics

**MVP Launch Criteria:**
1. ✅ Working demo video generated from URL input
2. ✅ < 5 min end-to-end generation time
3. ✅ No manual intervention required
4. ✅ Deployed to Vercel with custom domain (optional)

---

## 💡 What Was Cut (MVP)

| Feature | Reason |
|---------|--------|
| LangGraph | Too complex for MVP |
| 4 workflows | Ship one, add more later |
| Payment system | Manual billing for now |
| Affiliate system | Manual links for now |
| Music library | Use default audio |
| 4 aesthetic themes | Single theme only |

---

## 🔄 Next Steps After MVP

1. **Week 2:** Add second workflow (Narrator)
2. **Week 3:** Add payment (Stripe/Paddle)
3. **Week 4:** Add affiliate link injection
4. **Month 2:** LangGraph if needed for complexity

---

**Summary:** The project is 80% built but not tested. Ship ONE working workflow, not four broken ones.

*Lux - Code Execution Specialist*
