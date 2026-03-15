# 📡 Social Media Agent Blueprint

**Version:** 1.0  
**Date:** 2026-03-15  
**Location:** `/root/.openclaw/workspace/blueprints/social-media-agent.md`  
**Parent Project:** Interlinked Capital (WolfPack Empire)

---

## 🎯 Executive Vision

**Build an autonomous Social Media Agent that can manage the entire social media lifecycle for Interlinked Capital — from account creation and content posting to advertising campaign management and performance analytics.**

This agent will be the "Social Media Manager" for Interlinked Capital, handling fleet & asset finance marketing across all major platforms with minimal human oversight.

### Core Philosophy
- **Platform-First:** Native API integrations where possible, fallback to automation
- **Brand Consistency:** Unified voice across all platforms (Fleet & Asset Finance specialist)
- **Analytics-Driven:** Every action measured, optimized, and reported
- **Human-in-the-Loop:** Sensitive actions (paid ads >$100, brand-damaging content) require approval

---

## 🏗️ Core Features

### 1. Account Management
- **Multi-Platform Login:** Authenticate with Facebook, Instagram, Twitter/X, LinkedIn, TikTok, YouTube
- **Profile Setup:** Auto-fill business info, logos, bios from Interlinked Capital brand kit
- **Account Health Monitoring:** Detect suspended/disabled accounts, alert immediately
- **Session Management:** Maintain persistent sessions, handle 2FA, token refresh

### 2. Content Creation & Scheduling
- **Content Library:** Store templates, images, videos, captions
- **Smart Scheduling:** Optimal posting times based on audience analytics per platform
- **Bulk Scheduling:** Queue multiple posts across platforms
- **Content Calendar:** Visual calendar showing scheduled content
- **Template System:** Pre-built post templates for common content types:
  - New fleet financing options
  - Asset-backed loan promotions
  - Case studies / success stories
  - Industry news / insights
  - Seasonal campaigns

### 3. Advertising Campaign Management
- **Campaign Creation:** Set up ads on Facebook, Instagram, LinkedIn, TikTok
- **Audience Targeting:** Define demographics, interests, lookalike audiences
- **Budget Management:** Set daily/monthly caps, auto-pause on budget exhaustion
- **A/B Testing:** Automatically test ad variations, optimize to best performer
- **Creative Generation:** Generate ad copy and image suggestions using AI

### 4. Performance Analytics
- **Unified Dashboard:** All platforms in one view
- **Metrics Tracked:**
  - Reach, impressions, engagement rate
  - Follower growth, unfollows
  - Link clicks, conversions
  - Ad spend efficiency (CPC, CPM, ROAS)
- **Automated Reporting:** Weekly/monthly reports delivered to E-man
- **Competitor Analysis:** Benchmark against competitors (via scraping)

### 5. Engagement & Community
- **Comment Management:** Auto-reply to common questions, flag urgent for human
- **DM Handling:** Auto-respond to common queries, route leads to CRM
- **Mention Monitoring:** Track brand mentions, respond appropriately

### 6. Compliance & Safety
- **Content Moderation:** Check posts for policy violations before publishing
- **Approval Workflow:** Configurable approval thresholds
- **Audit Log:** Full history of all actions taken

---

## 🔗 Platform Integrations

### 📘 Facebook

| Feature | Method | API/SDK |
|---------|--------|---------|
| Page Management | Official API | Meta Graph API |
| Post Creation | Official API | Graph API `POST /{page-id}/feed` |
| Ads Management | Official API | Marketing API |
| Analytics | Official API | Graph API Insights |
| Comments | Official API | Graph API |

**API Requirements:**
- Meta Business Account
- Facebook Page (created)
- App ID + App Secret
- Access Token (long-lived, expires ~60 days)

**Status:** ✅ Account created (`@interlinkedcapital`), needs API setup

---

### 📸 Instagram

| Feature | Method | API/SDK |
|---------|--------|---------|
| Business Profile | Official API | Instagram Graph API |
| Post Creation | Official API | Instagram Graph API |
| Stories | Official API | Instagram Graph API |
| Reels | Official API | Instagram Graph API |
| Analytics | Official API | Instagram Insights API |
| Comments | Official API | Instagram Graph API |

**API Requirements:**
- Facebook Page (linked)
- Instagram Business Account
- Same Meta App as Facebook

**Status:** ✅ Account created (`@interlinkedcapital`), needs API setup

---

### 🐦 Twitter / X

| Feature | Method | API/SDK |
|---------|--------|---------|
| Account Management | Official API v2 | Twitter API v2 |
| Post Creation (Tweets) | Official API | POST /tweets |
| Media Upload | Official API | POST /media/upload |
| Threads | Official API | Sequential POST /tweets |
| Analytics | Official API | GET /tweets_metrics |
| Ads | Official API | Ads API v2 |

**API Requirements:**
- X Developer Account
- App ID + API Key + API Secret
- Bearer Token (App-only) or OAuth 1.0a / 2.0 (user)

**Pricing:** Basic (free), Pro ($100/mo), Enterprise (custom)

**Status:** ⚠️ Needs session creation + API key application

---

### 💼 LinkedIn

| Feature | Method | API/SDK |
|---------|--------|---------|
| Company Page | Official API | LinkedIn Marketing API |
| Post Creation | Official API | UGC Posts API |
| Analytics | Official API | Organization Stats API |
| Ads | Official API | LinkedIn Ads API |

**API Requirements:**
- LinkedIn Developer Organization
- App ID + App Secret
- Marketing API Product access (requires application)

**Note:** LinkedIn API access is restrictive; may need OAuth scraping fallback

**Status:** ⚠️ Needs session creation + API application

---

### 🎵 TikTok

| Feature | Method | API/SDK |
|---------|--------|---------|
| Video Upload | Official API | TikTok Display API |
| Content Posting | Official API | TikTok Share Kit |
| Analytics | Official API | TikTok Insights API |
| Ads | Official API | TikTok Ads API |

**API Requirements:**
- TikTok Developer Account
- App ID + App Secret
- Marketing API access

**Note:** TikTok is highly restrictive; automation often requires manual upload

**Status:** ⚠️ Needs session creation + API setup

---

### 📺 YouTube

| Feature | Method | API/SDK |
|---------|--------|---------|
| Video Upload | Official API | YouTube Data API v3 |
| Thumbnail/Cards | Official API | YouTube Data API v3 |
| Analytics | Official API | YouTube Analytics API |
| Live Streaming | Official API | YouTube Live Streaming API |

**API Requirements:**
- Google Cloud Project
- YouTube Data API v3 enabled
- OAuth 2.0 credentials
- Channel ownership verification

**Status:** ⚠️ Needs Google Cloud project + channel verification

---

## 🛠️ Tech Stack

### Primary Technologies

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Agent Framework** | OpenClaw (existing) | Orchestration, scheduling, memory |
| **HTTP Client** | Axios + Got | API requests with retry logic |
| **Browser Automation** | Playwright (stealth) | Fallback for platforms without APIs |
| **OAuth Handling** | `passport.js` + custom | Social platform authentication |
| **Scheduling** | `node-cron` + Redis | Post scheduling, queue management |
| **Database** | PostgreSQL (existing) | Content, analytics, logs |
| **Storage** | GCS + R2 | Media assets (images, videos) |
| **AI Integration** | Gemini/DeepSeek | Content generation, optimization |

### API SDKs (Official)

| Platform | SDK | npm Package |
|----------|-----|-------------|
| Facebook/Meta | Graph API SDK | `@beskythe64/facebook-nodejs-business-sdk` |
| Instagram | Graph API | (same as Facebook) |
| Twitter | Twitter API v2 | `twitter-api-v2` |
| LinkedIn | Marketing API | `linkedin-api` (unofficial) |
| TikTok | Display API | `@tiktok-share/connector` |
| YouTube | Google APIs | `googleapis` |

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOCIAL MEDIA AGENT                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │  Content    │  │  Scheduler  │  │  Analytics  │            │
│  │  Generator  │  │  (node-cron)│  │  Dashboard  │            │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘            │
│         │                │                │                   │
│  ┌──────┴────────────────┴────────────────┴──────┐            │
│  │              Platform Abstraction Layer        │            │
│  │         (Unified Interface → Platform APIs)    │            │
│  └──────┬────────────────┬────────────────┬──────┘            │
│         │                │                │                   │
│  ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐              │
│  │  Meta API   │ │ Twitter API │ │ LinkedIn    │              │
│  │  (FB/IG)    │ │   (X)       │ │  API        │              │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘              │
│         │                │                │                   │
│  ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐              │
│  │  TikTok API │ │ YouTube API │ │  Playwright │              │
│  │             │ │             │ │  (fallback) │              │
│  └─────────────┘ └─────────────┘ └─────────────┘              │
│                                                                 │
│  ┌─────────────────────────────────────────┐                   │
│  │         Storage Layer (GCS + R2)        │                   │
│  │     (Media files, assets, templates)   │                   │
│  └─────────────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔐 Credentials & API Requirements

### Current Status

| Platform | Account | Credentials | API Access |
|----------|---------|-------------|------------|
| Facebook | @interlinkedcapital | ✅ Gmail auth | ❌ Not set up |
| Instagram | @interlinkedcapital | ✅ Gmail auth | ❌ Not set up |
| Twitter/X | - | ⚠️ Need to create | ❌ Need API key |
| LinkedIn | - | ⚠️ Need to create | ❌ Need application |
| TikTok | - | ⚠️ Need to create | ❌ Need application |
| YouTube | - | ⚠️ Need to create | ❌ Need GCP project |

### Credentials to Obtain

```json
{
  "meta": {
    "app_id": "REQUIRED",
    "app_secret": "REQUIRED",
    "access_token": "REQUIRED (long-lived)",
    "business_account_id": "REQUIRED for ads"
  },
  "twitter": {
    "api_key": "REQUIRED",
    "api_secret": "REQUIRED",
    "bearer_token": "REQUIRED",
    "access_token": "OPTIONAL for user actions",
    "access_secret": "OPTIONAL"
  },
  "linkedin": {
    "client_id": "REQUIRED",
    "client_secret": "REQUIRED",
    "access_token": "REQUIRED"
  },
  "tiktok": {
    "app_id": "REQUIRED",
    "app_secret": "REQUIRED",
    "access_token": "REQUIRED"
  },
  "youtube": {
    "client_id": "REQUIRED (GCP)",
    "client_secret": "REQUIRED",
    "refresh_token": "REQUIRED"
  }
}
```

### Credential Storage

**Location:** `~/.openclaw/credentials/`

| File | Contents |
|------|----------|
| `meta-api.json` | Meta app credentials |
| `twitter-api.json` | Twitter/X API keys |
| `linkedin-api.json` | LinkedIn credentials |
| `tiktok-api.json` | TikTok API credentials |
| `youtube-api.json` | Google Cloud OAuth |
| `social-sessions.json` | Encrypted session tokens |

---

## 📊 What's Already Built vs Needs Building

### ✅ Already Built (Existing Assets)

| Component | Location | Status |
|-----------|----------|--------|
| Socials Agent IDENTITY | `/workspace/Socials/IDENTITY.md` | ✅ Done |
| Playwright Scraper Skill | `~/.openclaw/skills/playwright-scraper-skill/` | ✅ Done |
| Contentengen (video gen) | `/workspace/Contentengen-DXP-v2/` | ✅ Built |
| Credential Storage | `~/.openclaw/credentials/` | ✅ Infrastructure exists |
| Interlinked Capital Branding | TOOLS.md section | ✅ Defined |
| Gmail/Google OAuth | `credentials/google-oauth.json` | ✅ Available |

### ❌ Needs Building

| Component | Priority | Complexity |
|-----------|----------|------------|
| Meta (FB/IG) API Integration | P0 | High |
| Twitter/X API Integration | P0 | Medium |
| LinkedIn API Integration | P1 | High |
| TikTok API Integration | P1 | High |
| YouTube API Integration | P1 | High |
| Unified Platform Abstraction Layer | P0 | High |
| Content Scheduler + Queue | P0 | Medium |
| Analytics Dashboard | P1 | Medium |
| Campaign Manager | P1 | High |
| Content Template Library | P2 | Low |
| Comment/DM Automation | P2 | Medium |

---

## 🚀 4-Phase Implementation Plan

### 📍 Phase 1: Foundation & Core Platform (Weeks 1-2)

**Objective:** Get the agent running with basic posting capabilities on 2 platforms

| Task | Description | Deliverable |
|------|-------------|-------------|
| 1.1 | Set up Meta App + Business Account | App ID, Secret, Access Token |
| 1.2 | Implement Facebook/Instagram API client | Working `post()` to FB/IG |
| 1.3 | Create content storage in GCS/R2 | Media upload pipeline |
| 1.4 | Build platform abstraction interface | Unified `SocialPoster` class |
| 1.5 | Implement basic scheduling (node-cron) | Cron job for post timing |
| 1.6 | Test posting to FB + IG | 5 test posts live |

**Success Criteria:**
- [ ] Post to Facebook Page via API
- [ ] Post to Instagram via API (or linked FB)
- [ ] Schedule a post for future time
- [ ] Upload media to storage

---

### 📍 Phase 2: Multi-Platform Expansion (Weeks 3-4)

**Objective:** Add Twitter/X, LinkedIn, and fallback automation

| Task | Description | Deliverable |
|------|-------------|-------------|
| 2.1 | Apply for Twitter API (Basic tier) | API keys obtained |
| 2.2 | Implement Twitter API client | Working Twitter posting |
| 2.3 | Apply for LinkedIn Developer + Marketing API | Access granted |
| 2.4 | Implement LinkedIn API client (or OAuth fallback) | Working LinkedIn posting |
| 2.5 | Set up Playwright stealth automation | Fallback for blocked platforms |
| 2.6 | Build session manager | Persistent login handling |

**Success Criteria:**
- [ ] Post to Twitter via API
- [ ] Post to LinkedIn via API
- [ ] Fallback to browser automation if API fails
- [ ] Handle token refresh automatically

---

### 📍 Phase 3: Advertising & Analytics (Weeks 5-6)

**Objective:** Full campaign management and performance tracking

| Task | Description | Deliverable |
|------|-------------|-------------|
| 3.1 | Implement Meta Ads API | Campaign creation, audience targeting |
| 3.2 | Implement LinkedIn Ads API | Campaign management |
| 3.3 | Build analytics aggregation | Pull metrics from all platforms |
| 3.4 | Create unified dashboard UI | Web dashboard for stats |
| 3.5 | Build automated reporting | Weekly report generation |
| 3.6 | Add A/B testing framework | Auto-optimize ad creatives |

**Success Criteria:**
- [ ] Create and run ad campaign on Facebook
- [ ] Create and run ad campaign on LinkedIn
- [ ] View unified analytics dashboard
- [ ] Receive automated weekly report

---

### 📍 Phase 4: Advanced Features & Polish (Weeks 7-8)

**Objective:** Full automation, AI enhancement, and production hardening

| Task | Description | Deliverable |
|------|-------------|-------------|
| 4.1 | Integrate TikTok API (if available) | TikTok posting capability |
| 4.2 | Integrate YouTube API | Video upload capability |
| 4.3 | Build AI content generator | Generate post copy using Gemini |
| 4.4 | Implement comment/DM auto-response | Basic FAQ automation |
| 4.5 | Add approval workflow | Human-in-loop for sensitive actions |
| 6 | Production hardening | Error handling, logging, alerting |

**Success Criteria:**
- [ ] Post video to TikTok/YouTube
- [ ] AI generates post content
- [ ] Auto-reply to common comments
- [ ] Approval workflow functional

---

## 📋 Milestone Summary

| Phase | Weeks | Platforms | Key Features |
|-------|-------|-----------|--------------|
| **1** | 1-2 | Facebook, Instagram | API posting, scheduling |
| **2** | 3-4 | + Twitter, LinkedIn | Multi-platform, fallback automation |
| **3** | 5-6 | All 5 | Ads, analytics, reporting |
| **4** | 7-8 | + TikTok, YouTube | AI generation, full automation |

---

## 💰 Cost Projection

| Item | Phase | Estimated Cost |
|------|-------|----------------|
| Twitter API (Basic) | 2 | $0/mo |
| Meta (Business) | 1 | $0/mo (free tier) |
| LinkedIn (Marketing) | 2 | $0/mo (requires approval) |
| TikTok (Marketing) | 4 | $0/mo (if approved) |
| YouTube (GCP) | 4 | ~$10/mo (API quotas) |
| **Total** | All | **~$10-20/mo** |

---

## 🗺️ Next Immediate Steps

1. **Apply for Twitter API Basic** (free, takes 1-2 days)
2. **Set up Meta App** at developers.facebook.com
3. **Create @interlinkedcapital on Twitter**
4. **Create LinkedIn Company Page** for Interlinked Capital
5. **Create TikTok/YouTube accounts**
6. **Start Phase 1 development**

---

## 📚 References

- [Meta for Developers](https://developers.facebook.com/)
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api)
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [TikTok for Developers](https://developers.tiktok.com/)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [Playwright Stealth](https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth)

---

**Status:** 🟡 Blueprint Complete - Ready for Implementation

**Created by:** Aris (Lead Orchestrator)  
**For:** Interlinked Capital - WolfPack Empire
