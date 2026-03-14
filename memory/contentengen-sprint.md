# Contentengen Sprint Plan

**Created:** 2026-03-12  
**For:** Lux (Code Execution)  
**Context:** E-man approved tech plan - Bootstrap Mode

---

## 📋 Tech Plan Decisions

| Decision | Status | Notes |
|----------|--------|-------|
| Next.js 16.1 + vercel.json | ✅ | DEADLINE: MAR 31 |
| Biome linter | ✅ | |
| Gemini 3.1 | ❌ | Stick with 2.5 for COGS |
| Veo | ❌ | Build own library |
| LangGraph | 🟡 | Simplified, test locally first |

---

## 🎯 Sprint Goal (1-2 Weeks)

**Primary Objective:** Get Contentengen foundation ready for development - migration, linting, and core architecture without spending money.

---

## 📌 Task List

### P0 - Critical (Must Complete)

#### 1. Next.js 16.1 Upgrade + vercel.json Migration
- **Priority:** P0
- **Dependencies:** None (fresh start)
- **Time Estimate:** 4-6 hours
- **Done When:**
  - [ ] Next.js upgraded to 16.1
  - [ ] vercel.json created with proper config
  - [ ] App builds successfully `npm run build`
  - [ ] Dev server runs without errors `npm run dev`
  - [ ] No console errors on homepage

#### 2. Biome Linter Setup
- **Priority:** P0
- **Dependencies:** Task 1 complete
- **Time Estimate:** 2-3 hours
- **Done When:**
  - [ ] Biome installed and configured
  - [ ] Pre-commit hook set up (if applicable)
  - [ ] `npm run lint` passes with no errors
  - [ ] CI/CD lint check in place (if applicable)

---

### P1 - High Priority

#### 3. Project Cleanup & Structure Review
- **Priority:** P1
- **Dependencies:** Task 1 complete
- **Time Estimate:** 2 hours
- **Done When:**
  - [ ] Unused dependencies removed
  - [ ] Folder structure follows Next.js 14+ App Router conventions
  - [ ] Environment variables documented in `.env.example`
  - [ ] README updated with setup instructions

#### 4. Gemini 2.5 Integration (Keep Current)
- **Priority:** P1
- **Dependencies:** Task 1 complete
- **Time Estimate:** 1-2 hours
- **Done When:**
  - [ ] Confirmed Gemini 2.5 API integration works
  - [ ] Costs monitored (set up usage tracking)
  - [ ] Fallback/error handling in place

---

### P2 - Medium Priority

#### 5. LangGraph - Local First Testing
- **Priority:** P2
- **Dependencies:** Tasks 1-3 complete
- **Time Estimate:** 4-6 hours
- **Done When:**
  - [ ] LangGraph installed locally (no cloud service)
  - [ ] Basic agent flow working (at least one test case)
  - [ ] No external API calls (fully local)
  - [ ] Document what simplified LangGraph looks like

#### 6. Content Library Architecture (Veo Alternative)
- **Priority:** P2
- **Dependencies:** Tasks 1-3 complete
- **Time Estimate:** 3-4 hours
- **Done When:**
  - [ ] Architecture doc created for "own library" approach
  - [ ] Basic storage structure defined (local file system or DB)
  - [ ] No external video API dependencies

---

### P3 - Nice to Have

#### 7. Documentation & Runbook
- **Priority:** P3
- **Dependencies:** All above
- **Time Estimate:** 1-2 hours
- **Done When:**
  - [ ] SETUP.md with fresh install steps
  - [ ] ARCHITECTURE.md explaining decisions
  - [ ] TROUBLESHOOTING.md for common issues

---

## 🔗 Dependency Graph

```
[START]
    │
    ▼
┌─────────────────┐
│ Task 1: Next.js │──────► [Task 2: Biome]
│    16.1         │              │
└─────────────────┘              │
    │                            │
    ▼                            ▼
┌─────────────────┐     ┌─────────────────┐
│ Task 3: Cleanup │─────►│ Task 4: Gemini │
└─────────────────┘     └─────────────────┘
    │                            │
    ▼                            ▼
┌─────────────────┐     ┌─────────────────┐
│ Task 5: LangGraph│◄────│ (parallel)      │
└─────────────────┘     └─────────────────┘
    │
    ▼
┌─────────────────┐
│ Task 6: Library │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│ Task 7: Docs    │
└─────────────────┘
```

---

## ⏱️ Time Summary

| Phase | Tasks | Time |
|-------|-------|------|
| P0 Critical | 1-2 | 6-9 hours |
| P1 High | 3-4 | 3-4 hours |
| P2 Medium | 5-6 | 7-10 hours |
| P3 Nice | 7 | 1-2 hours |
| **TOTAL** | **7** | **17-25 hours** |

---

## ✅ Definition of Done (Sprint)

- [ ] Next.js 16.1 running with vercel.json
- [ ] Biome linter configured and passing
- [ ] Project cleaned and structured properly
- [ ] Gemini 2.5 confirmed working
- [ ] LangGraph tested locally (documented findings)
- [ ] Own library architecture defined
- [ ] Basic documentation in place

---

## 🚨 Risks / Blocker Flags

- **Next.js 16.1 breaking changes:** May need to refactor app directory
- **LangGraph complexity:** Keep it SIMPLE - if too complex, document and move on
- **No budget:** Everything must run locally or use free tiers

---

## 📝 Notes for Lux

1. **Bootstrap mode = prioritize speed over perfection**
2. **If stuck > 30 min, flag it - don't spin wheels**
3. **Document everything** - future you will thank present you
4. **Test incrementally** - build after each major change

---

*Max - Task breakdown complete. Passing to Lux for execution.*
