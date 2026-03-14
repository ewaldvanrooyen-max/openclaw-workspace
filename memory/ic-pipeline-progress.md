# IC Pipeline Progress Report

**Date:** 2026-03-14  
**Agent:** Max (Task Breakdown Specialist)  
**Status:** IN PROGRESS

---

## Current Pipeline Status

| Component | Status | Notes |
|-----------|--------|-------|
| WhatsApp webhook | ✅ Done | Code written, NOT RUNNING |
| Language detection | ✅ Done | Implemented in webhook |
| POPIA verification flow | 🔄 TODO | Not implemented in webhook |
| Status query automation | 🔄 TODO | Basic STATUS command exists |
| Follow-up cron (8am SA) | 🔄 TODO | Written, NOT RUNNING |
| Short codes | ✅ Done | D1, D2, I1, P1, A1 implemented |

---

## 🚨 What's Blocking Live Testing

1. **WhatsApp webhook not running** - Need systemd service
2. **Follow-up cron not running** - Need systemd timer or cron setup
3. **POPIA verification flow missing** - Need to add verification step
4. **Twilio webhook URL** - Needs public HTTPS URL

---

## 📋 Prioritized TODO List

### P0 - Critical (Blocks Live Testing)
- [ ] 1. Create systemd service for WhatsApp webhook (port 8443)
- [ ] 2. Start WhatsApp webhook service
- [ ] 3. Configure Twilio to point to public webhook URL
- [ ] 4. Set up follow-up cron as systemd timer

### P1 - Important (Feature Completion)
- [ ] 5. Implement POPIA verification flow in webhook
- [ ] 6. Add company name verification step
- [ ] 7. Improve status query automation

### P2 - Nice to Have
- [ ] 8. Add short code security (consultant password)
- [ ] 9. Add email listener for incoming leads

---

## 🔧 What's Been Done Today

1. Reviewed /opt/mlc-crm/ codebase
2. Identified WhatsApp webhook code exists but not running
3. Identified followup-cron.py exists but not scheduled
4. Confirmed Twilio sandbox is connected (config.json)
5. Mapped database schema (leads table with language field)

---

## ⏭️ Next Action

**Starting on P0 Item #1:** Create systemd service for WhatsApp webhook

