# PROJECT BLUEPRINT - Interlinked Capital (IC)

## Project Name
**Interlinked Capital** - Fleet & Asset Finance

## Vision
South African fleet and asset finance company connecting businesses with funding. Uses automation for lead management, follow-ups, and client communication.

---

## Core Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Total Leads | - | 0 |
| Approval Rate | >60% | - |
| Follow-up Response | >40% | - |
| Pipeline Value | - | 0 |

---

## Repository
- **URL:** github.com/ewaldvanrooyen-max/interlinked-capital
- **Live Site:** interlinkedcapital.co.za

---

## Sub-Projects

### 1. website ✅
**Purpose:** Business website
**Status:** Live
**Location:** /var/www/ic-website/
**Tasks:**
- [ ] Add contact forms
- [ ] Add lead capture

### 2. workflows ✅
**Purpose:** WhatsApp CRM, lead management automation
**Status:** Built
**Location:** /root/.openclaw/workspace/ic/
**Tasks:**
- [ ] POPIA verification flow
- [ ] Status query automation
- [ ] Short codes implementation

### 3. crm ✅
**Purpose:** SQLite database for leads
**Status:** Built
**Location:** /root/.openclaw/workspace/ic/leads.db
**Tasks:**
- [ ] Connect to workflow
- [ ] Add reporting

### 4. automation ✅
**Purpose:** 48-hour follow-up, auto-responses
**Status:** Fixed
**Location:** Cron jobs
**Tasks:**
- [x] Fix IC-FOLLOWUP cron (now IC-48hr-FollowUp)
- [ ] Add more automation

---

## Tech Stack
- **Frontend:** Static HTML
- **Backend:** Python webhook
- **Database:** SQLite
- **Channels:** WhatsApp (Twilio), Telegram

---

## Integrations
| Service | Purpose | Status |
|---------|---------|--------|
| WhatsApp Business | Client communication | ✅ Connected |
| Twilio | WhatsApp API | ✅ Connected |
| Telegram | Admin alerts | ✅ Connected |

---

## Current Blockers
- None - core systems working

---

## 4-Phase Plan

### Phase 1: Automation (This Week)
- [x] Fix IC-48hr-FollowUp cron job
- [ ] Test follow-up reporting
- [ ] Add short codes (D1, I1, P1, A1, etc.)

### Phase 2: Verification (This Week)
- [ ] Implement POPIA verification flow
- [ ] Add status query automation
- [ ] Connect CRM to workflow

### Phase 3: Website (This Week)
- [ ] Add contact forms to website
- [ ] Add lead capture integration
- [ ] Connect to CRM

### Phase 4: Growth (This Week)
- [ ] Add reporting dashboard
- [ ] Set up Google Workspace
- [ ] Launch marketing campaigns

---

## Notes
- Stakeholders: E-man (70%), Mario (30%)
- Focus: Fleet finance, asset finance
- Location: South Africa
