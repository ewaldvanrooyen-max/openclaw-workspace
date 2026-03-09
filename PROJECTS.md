# Projects Registry

## 1. Interlinked Capital (IC)
- **Type:** Finance Origination Company (Fleet & Asset Finance)
- **Stakeholders:** E-man (70%), Mario (30%)
- **Status:** Active - Workflow in development
- **Website:** interlinkedcapital.co.za
- **Emails:** ewald@, mario@, apps@, aris@ interlinkedcapital.co.za

### Workflow: Finance Origination Smart-Flow

**Technology:**
- WhatsApp Business API (Twilio)
- Email listener
- SQLite CRM (leads.db)
- WhatsApp webhook (whatsapp-webhook.py)

**Status Types:**
- `NEW` - Just received
- `INCOMPLETE` - Missing docs
- `PENDING` - Submitted to bank
- `APPROVED` - Podium received
- `DECLINED` - Bank declined
- `CANCELLED` - Client opted out

**Key Features:**
1. **Language Detection** - Afrikaans → Reply AF+EN, English → EN only
2. **POPIA Verification (2-Step)** - Verify cell number → Confirm company name → Pull CRM record
3. **Short Codes (Consultant Use)**
   | Code | Action |
   |------|--------|
   | D1 | Decline + tier-2 offer |
   | D2 | Decline + no options |
   | I1 | Incomplete + checklist |
   | P1 | Pending + submit to bank |
   | A1 | Approved + notify parties |
4. **48-Hour Follow-Up (8am SA)** - Targets: INCOMPLETE, PENDING. Opt-out: "STOP" or "CANCEL"
5. **Channel Routing** - Response channel = Original input channel
6. **Podium Protection** - Wholesale docs to dealer only, client gets generic "Approved" msg

**CRM Fields:**
- dealer_group, preferred_channel, language, last_followup, submission_date

**Implementation Priority:**
1. WhatsApp webhook + basic CRM lookup ✅ (done)
2. Language detection ✅ (done)
3. POPIA verification flow 🔄 (next)
4. Status query automation 🔄 (next)
5. Follow-up cron (8am) ⬜
6. Short codes ⬜

---

## 2. ContentEngen
- **Type:** AI Video Content Factory
- **Stakeholders:** 
- **Status:** Phase 1 (Immediate)
- **Website:** 
- **GCP Project:** contentengen-dxp-v2

### The Vision
AI-driven content factory for Overlay Economy. Dual-core brain (Gemini), rendering engines, 4-volume aesthetic matrix, agent roster (Narrator, Teacher, Demo, Closer).

### What's Built (4 Priority Workflows)
| Workflow | Description | Status |
|----------|-------------|--------|
| Demo | Website tutorial enhancer | ✅ Functional |
| Narrator | Viral storytelling/documentary | ✅ Functional |
| Teacher | Multi-part lesson generator | ✅ Functional |
| Closer | Product review + affiliate links | ✅ Functional |

### Technical Stack
- **Brain:** Gemini 2.5 Flash via Vertex AI (connected, disabled for testing)
- **Rendering:** FFmpeg on Cloud Run (L4 GPU) ✅
- **Storage:** Cloudflare R2 ✅
- **TTS:** edge-tts (fallback)

### Roadmap

**Phase 1: Immediate**
- [x] 4 workflows built ✅
- [ ] Add Gemini API for dynamic script generation (Vertex AI connected)
- [ ] Better backgrounds/transitions (polish - later)

**Phase 2: Short-term**
- [ ] Cloud infrastructure (Cloud Run) ✅ Ready
- [ ] R2 storage ✅ Ready

**Phase 3: Medium-term**
- [ ] 4 aesthetic themes (Sovereign, Silicon Solarpunk, Haptic Sanctuary, Kinetic Glitch)
- [ ] Paddle integration (African payments) + Stripe for affiliate payouts
- [ ] Asset library - start with 500 (have some in bucket + HuggingFace cron)

**Phase 4: Later Expansion (Empire Revenue)**
- [ ] Tier 1: Affiliate Marketing (leverage IC web-audit clients)
- [ ] Tier 1: Digital Products (SEO guides, templates)
- [ ] Tier 2: Print-on-Demand (branded merchandise)
- [ ] Tier 2: Online Courses (monetize expertise)
- [ ] Tier 3: SaaS Tools (web audit automation)
- [ ] Tier 3: Dropshipping

---

## 3. GHL (GoHighLevel)
- **Type:** Marketing/CRM Automation Platform
- **Description:** AI-powered all-in-one platform combining CRM, marketing automation, sales pipelines, and customer communication
- **Stakeholders:** 
- **Status:** Research Phase
- **Pricing:** Starter ($97/mo), Unlimited ($297/mo - includes API access)

---

### What GHL Can Automate

| Category | Capabilities |
|----------|-------------|
| **Lead Capture** | Landing pages, forms, surveys, calendars, inbound phone |
| **Marketing** | Multi-channel campaigns (SMS, MMS, email, WhatsApp, FB Messenger, voicemail drops, forced calls) |
| **Sales** | Pipeline management, opportunity tracking, deal stages, contact management |
| **Communication** | Two-way SMS/WhatsApp, email marketing, Facebook Messenger, phone/voicemail |
| **Payments** | Stripe integration for collecting payments on funnels/appointments |
| **Appointments** | Built-in calendar, automated booking, appointment reminders |
| **Membership/Courses** | Create courses, membership areas, sell digital products |
| **AI Features** | AI voice calls, AI-powered conversation management, workflow automation |

---

### Limitations & What Requires Human Intervention

**GHL Limitations:**
- **Complex decision-making** - Basic if/then workflows only; complex logic needs external tools or manual intervention
- **Custom integrations** - Requires API access (Unlocked plan at $297/mo)
- **Advanced analytics** - Basic reporting built-in; deeper analysis needs export/external tools
- **Voice/WhatsApp compliance** - Regional restrictions apply, WhatsApp Business API needs separate approval
- **White-labeling** - Desktop app white-label only; mobile app requires additional fees
- **API rate limits** - Not unlimited; depends on plan tier
- **No native invoicing** - Can integrate with Stripe but no built-in invoicing engine
- **Custom objects** - Limited; enterprise needs may outgrow

**Requires Human Intervention (HITL):**
- Complex objection handling in conversations
- Negotiations and contract discussions
- High-value deal approvals
- Quality control on creative/content
- Customer complaints requiring empathy/escalation
- Strategy and campaign planning
- Financial decisions (pricing, discounts, terms)
- Technical troubleshooting beyond basic FAQs

---

### APIs & Integrations

**API Access:**
- **Starter Plan ($97)** - No API access
- **Unlimited Plan ($297)** - Full API access included

**Native Integrations:**
- Stripe (payments)
- Facebook/Instagram
- Google Calendar
- Zapier (via webhooks)
- Twilio (SMS/Voice)
- Mailgun/SendGrid (email)

**Webhook Support:**
- Outbound webhooks to trigger external actions
- Inbound webhooks to receive data
- Custom API endpoints via Private Integrations

**Custom Development:**
- REST API for CRUD operations on contacts, deals, pipelines
- Workflow automation via API
- Custom app development (white-label option)

---

### Build vs Buy Analysis

| Aspect | GHL | Custom Build (OpenClaw) |
|--------|-----|------------------------|
| **Setup Time** | Hours | Days-Weeks |
| **Cost** | $97-297/mo | Dev time + hosting |
| **Maintenance** | Managed | Self-hosted |
| **Customization** | Limited by platform | Full control |
| **Data Ownership** | GHL servers | Your servers |
| **Flexibility** | Pre-built workflows | Any logic |
| **Learning Curve** | Medium | High (build it yourself) |

**GHL Wins When:**
- Quick deployment needed
- Standard CRM + marketing flow
- Team can use GUI builders
- No complex custom logic

**Custom Build Wins When:**
- Need full data sovereignty
- Complex unique workflows
- Tight budget (self-hosted)
- Integration with proprietary systems

---

### Web Agency: What to Outsource vs Keep In-House

**Can Be Fully Autonomous (No Human Needed):**
- ✅ Lead capture forms & landing pages
- ✅ Automated follow-up sequences (email/SMS/WhatsApp)
- ✅ Appointment scheduling & reminders
- ✅ Basic lead qualification (score-based)
- ✅ Pipeline stage updates
- ✅ Payment collection (Stripe)
- ✅ Membership content delivery

**Needs Human In The Loop (HITL):**
- ⚠️ SEO audit analysis & strategy (requires expertise, judgment)
- ⚠️ Content creation (requires creativity, brand voice)
- ⚠️ Technical site builds (complex issues)
- ⚠️ Client communication & relationship management
- ⚠️ Proposal writing & pricing decisions
- ⚠️ Quality assurance on deliverables
- ⚠️ Handling objections & negotiations

**Outsource Options:**
- SEO audits → Freelance SEO experts (Fiverr, Upwork)
- Content writing → Copywriters
- Basic site builds → Templates + GHL (no-code)
- Routine follow-ups → GHL automations

**Must Stay In-House:**
- Strategic decisions
- Client relationships
- Quality control
- Complex technical implementation
- Financial/contractual decisions

---

### Recommendation for E-man

For a web agency offering SEO audits + site builds:
1. **Use GHL for:** CRM, lead capture, automated nurturing, appointment booking, basic follow-ups
2. **Outsource:** SEO audits (specialists), content writing, basic design
3. **Keep in-house:** Strategy, client relationships, complex builds, quality control
4. **Custom build only if:** Need data sovereignty, unique workflows, or budget constraints

GHL provides 80% of agency automation out-of-the-box at $297/mo vs custom build costs.

---

### 🎯 The Vision: Autonomous Business Layer

**Base:** GHL (CRM, pipelines, automation)

**Add Our Autonomy Layer (Build on top of GHL):**

| Agent | Function |
|-------|----------|
| **Lead Scraper** | Pull leads from directories, social, Google maps |
| **Verifier** | Validate leads, enrich with business data |
| **Quote Generator** | Auto-generate quotes from audit data → send via GHL |
| **Negotiator** | AI email back-and-forth (via GHL inbox) |
| **Site Builder** | Use GHL free site builder → pitch to owner for sale |

**Target:** 90% automation, 10% human intervention

**Flow:**
1. Agent finds business → scrapes site → runs audit
2. Agent sends quote via GHL email/WhatsApp
3. AI handles negotiation via email
4. Human closes (only for signing)
5. Work outsourced (Fiverr/Upwork)
6. GHL handles invoicing/payments

---

_Last updated: 2026-03-07_
