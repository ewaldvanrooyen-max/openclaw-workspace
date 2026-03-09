# BROWSER-001: Headless Browser Research Report

## Executive Summary
Comparison of headless browsers for web scraping. Playwright recommended for general use; specialized anti-detection tools for high-value targets.

---

## Top Headless Browsers Compared

### 1. Playwright ⭐ RECOMMENDED
- **Developer:** Microsoft
- **Languages:** JavaScript, TypeScript, Python, .NET, Java
- **Browsers:** Chromium, WebKit, Firefox
- **Speed:** ⭐⭐⭐⭐⭐ Fast (out-of-process architecture)
- **Reliability:** ⭐⭐⭐⭐⭐ Excellent (auto-wait, smart retries)
- **Anti-Detection:** ⭐⭐⭐ Moderate (requires manual configuration)
- **Pros:**
  - Cross-browser, cross-platform support
  - Built-in auto-wait eliminates flakiness
  - Excellent debugging tools (inspector, trace viewer)
  - Native mobile emulation
  - Strong iframe/shadow DOM support
  - Auth state persistence
- **Cons:**
  - Larger package size
  - Anti-detection requires extra work
- **Best for:** General scraping, automation, testing

### 2. Puppeteer
- **Developer:** Google
- **Languages:** JavaScript, TypeScript
- **Browsers:** Chromium only
- **Speed:** ⭐⭐⭐⭐ Fast
- **Reliability:** ⭐⭐⭐⭐ Good
- **Anti-Detection:** ⭐⭐⭐ Moderate
- **Pros:**
  - Lightweight, fast setup
  - Excellent Chrome integration
  - Large ecosystem
  - Good documentation
- **Cons:**
  - Chrome-only
  - More manual handling than Playwright
  - Flaky tests possible without careful handling
- **Best for:** Chrome-specific automation, simpler projects

### 3. SecretAgent / Hero ⭐ ANTI-DETECTION
- **Developer:** Ulixee
- **Languages:** JavaScript, TypeScript
- **Browsers:** Chromium-based
- **Speed:** ⭐⭐⭐⭐ Good
- **Reliability:** ⭐⭐⭐⭐ Good
- **Anti-Detection:** ⭐⭐⭐⭐⭐ Built-in
- **Pros:**
  - Designed specifically for scraping
  - Built-in browser fingerprint emulation
  - TLS fingerprint evasion
  - W3C-compliant DOM in Node.js
  - Avoids detection at entire stack
- **Cons:**
  - Newer, smaller community
  - Less documentation than Playwright
- **Best for:** Hard-to-scrape sites, anti-bot protected sites

---

## Comparison Table

| Browser | Speed | Reliability | Anti-Detect | Learning Curve | Empire Use |
|---------|-------|-------------|-------------|----------------|------------|
| **Playwright** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Low | ⭐ Best general |
| **Puppeteer** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Low | Good alternative |
| **SecretAgent** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Medium | High-value targets |

---

## Anti-Detection Options

### For Playwright/Puppeteer:
1. **puppeteer-extra-plugin-stealth** - Evades detection plugins
2. **playwright-stealth** - Playwright equivalent
3. **Manual configuration:**
   - Randomize viewport/user-agent
   - Add realistic headers
   - Use residential proxies
   - Randomize timing/interactions

### Specialized Anti-Detection Browsers:
- **Undetectable Browser** - Paid, browser-based
- **Multilogin** - Paid, profile management
- **Incogniton** - Paid, anti-detect

---

## Empire Recommendation

### Tier 1 - Default: Playwright
```bash
npm install playwright
```
- Best for 80% of scraping needs
- Reliable, well-documented, active development

### Tier 2 - Hard Sites: SecretAgent
```bash
npm install @ulixee/hero
```
- For sites that block Playwright/Puppeteer
- Built-in evasion saves time on high-value targets

### Tier 3 - Proxies & Rotation
- Bright Data (residential proxies)
- SmartProxy
- Oxylabs

---

## Quick Start Code

### Playwright Example:
```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0...',
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();
  await page.goto('https://example.com');
  const data = await page.content();
  await browser.close();
})();
```

### SecretAgent Example:
```javascript
const agent = require('secret-agent');

(async () => {
  await agent.goto('https://example.com');
  const title = await agent.document.title;
  await agent.close();
})();
```

---

## Cost Comparison
- **Playwright:** Free (open source)
- **Puppeteer:** Free (open source)
- **SecretAgent:** Free (open source)
- **Anti-detect browsers:** $50-150/month

---

*Research Complete: 2026-03-09*
