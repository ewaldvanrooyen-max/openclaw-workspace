# PROJECT BLUEPRINT - Interlinked Capital (IC)

## Project Name
**Interlinked Capital** - Fleet & Asset Finance

## Vision
South African fleet and asset finance company connecting businesses with funding. Uses automation for lead management, follow-ups, and client communication.

---

## Core Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Total Leads | - | TBD |
| Approval Rate | >60% | TBD |
| Follow-up Response | >40% | TBD |
| Pipeline Value | - | TBD |

---

## Repository
- **URL:** github.com/ewaldvanrooyen-max/interlinked-capital
- **Live Site:** interlinkedcapital.co.za

---

## Sub-Projects

### 1. website
**Purpose:** Business website
**Status:** Live
**Location:** /var/www/ic-website/
**Tasks:**
- [ ] Add contact forms
- [ ] Add lead capture

### 2. workflows
**Purpose:** WhatsApp CRM, lead management automation
**Status:** Built
**Location:** /root/.openclaw/workspace/ic/
**Tasks:**
- [ ] POPIA verification flow
- [ ] Status query automation
- [ ] Short codes implementation

### 3. crm
**Purpose:** SQLite database for leads
**Status:** Built
**Location:** leads.db
**Tasks:**
- [ ] Connect to workflow
- [ ] Add reporting

### 4. automation
**Purpose:** 48-hour follow-up, auto-responses
**Status:** Partial
**Location:** Cron jobs
**Tasks:**
- [ ] Fix IC-FOLLOWUP cron
- [ ] Add more automation

---

## Tech Stack
- **Frontend:** Static HTML
- **Backend:** Python (webhook)
- **Database:** SQLite
- **Channels:** WhatsApp (Twilio), Telegram

---

## Integrations
| Service | Purpose | Status |
|---------|---------|--------|
| WhatsApp Business | Client communication | Connected |
| Twilio | WhatsApp API | Connected |
| Telegram | Admin alerts | Connected |

---

## Current Blockers
- IC-FOLLOWUP cron job failing
- No live CRM dashboard (building in Mission Control)

---

## Next 7 Days
1. Fix IC-FOLLOWUP cron
2. Connect CRM to workflow
3. Set up Google Workspace (email/calendar)

---

## Notes
- Stakeholders: E-man (70%), Mario (30%)
- Focus: Fleet finance, asset finance
- Location: South Africa
