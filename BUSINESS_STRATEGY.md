# Business Strategy — Idle-Time Initiative Selection

**Date:** 2026-03-07  
**Council:** Lux (Strategy) + Jiles (Product) — Joint Decision

---

## Executive Summary

After evaluating three seed initiatives, the Business Council recommends **pursuing the Automated Web-Asset Auditor** as the first idle-time revenue initiative.

---

## Initiative Scores

| Initiative | Setup Cost | Revenue Potential | Scalability | Alignment | **TOTAL** |
|------------|:----------:|:-----------------:|:-----------:|:---------:|:--------:|
| Web-Asset Auditor | 8 | 7 | 9 | 8 | **32** |
| AI Newsletter Engine | 9 | 5 | 6 | 4 | **24** |
| Arbitrage Monitoring | 3 | 8 | 4 | 2 | **17** |

---

## Rationale

### Winner: Automated Web-Asset Auditor

1. **Token/Prompt ROI (Lux):** Near-zero incremental infrastructure cost. Runs on existing VPS. Uses current LLM capacity efficiently — generates actionable reports without heavy inference spend.

2. **Commercial Viability (Jiles):** Clear value proposition: "We scan your website, find what broke your SEO, and give you a fix report." Agencies pay $200-2000/month for this. SMBs pay $50-200 one-off. Lead-gen funnel is straightforward.

3. **Scalability:** Fully automated. Add more target websites = linear revenue. No marginal human effort once built.

4. **Business Alignment:** Fits Interlinked Capital's target market (SMBs). Could feed leads into ContentEngen's content pipeline. GHL integration potential for automated reporting delivery.

### Why Not The Others

- **Newsletter:** Low cost but slow monetization. Audience compounding takes 6-12 months minimum. Subscription fatigue limits revenue ceiling.
- **Arbitrage:** High returns potential, but high operational overhead, capital requirements, and zero alignment with IC's core business. Risk profile doesn't fit a bootstrap operation.

---

## First Action Step

**Build the MVP scanner:**
- Identify 3-5 target SEO metrics (broken links, missing meta tags, load speed, mobile usability)
- Create a lightweight crawler using existing tools (or simple HTTP requests)
- Generate a PDF/HTML report template
- Test on 10 local businesses (free) to validate value

**Owner:** Lux  
**Timeline:** 2 weeks to MVP  
**Success Metric:** At least 1 paid pilot customer

---

## Notes

- Council consensus: unanimous (Lux + Jiles aligned)
- Re-evaluate in 30 days post-MVP launch
