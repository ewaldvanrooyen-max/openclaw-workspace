# 🔍 IC Application Workflow - Gap Analysis

## Current State (What's Working)

| Component | Status | Notes |
|-----------|--------|-------|
| Website (HTTPS) | ✅ Live | https://interlinkedcapital.co.za |
| Lead Form | ⚠️ Basic | Uses `mailto:` - opens email client, NO database capture |
| WhatsApp webhook | ❌ Not connected | Code exists but not running |
| Email listener | ❌ Not running | Code exists but not running |
| CRM/Lead DB | ⚠️ Exists | SQLite at `/var/www/ic-website/leads.db` but not connected to form |
| Follow-up cron | ❌ Not running | Code exists but disabled |
| SEO | ✅ Done | sitemap.xml, robots.txt, meta tags |

---

## 🚨 Critical Gaps (Block E2E Testing)

### 1. Lead Form → Database (HIGH)
- **Current:** Form submits via `mailto:apps@interlinkedcapital.co.za`
- **Problem:** Opens user's email client, NO data captured to CRM
- **Fix:** Connect form to API that saves to SQLite DB

### 2. WhatsApp Integration (HIGH)
- **Current:** Webhook code exists but not registered with Twilio
- **Problem:** Can't receive/process WhatsApp leads
- **Fix:** Register webhook URL with Twilio sandbox

### 3. Email Listener (MEDIUM)
- **Current:** `email-listener.py` not running
- **Problem:** Can't auto-capture leads from email submissions
- **Fix:** Run as systemd service or cron

### 4. Auto-Responder (MEDIUM)
- **Current:** No auto-replies configured
- **Problem:** New leads get no confirmation
- **Fix:** Implement POPIA verification flow (FINANCE-FLOW.md)

### 5. 48-Hour Follow-Up (LOW)
- **Current:** `followup-cron.py` not running
- **Problem:** No automated follow-ups for incomplete apps
- **Fix:** Run cron job at 8am SA time

---

## 📋 Recommended Fix Order (For E2E Tomorrow)

1. **Fix form submission** → Connect to lead-tracker.py API
2. **Start WhatsApp webhook** → Register with Twilio
3. **Test E2E:** Form submit → DB capture → WhatsApp notification

---

## 💰 What's It Cost to Fix?

| Item | Effort | Cost |
|------|--------|------|
| Form → DB | 1-2 hrs | R0 |
| WhatsApp webhook | 1 hr | R0 (Twilio sandbox) |
| Email listener | 1 hr | R0 |
| Follow-up cron | 30 min | R0 |

**Total:** ~4 hours, R0

---

_Last updated: 2026-03-13_
