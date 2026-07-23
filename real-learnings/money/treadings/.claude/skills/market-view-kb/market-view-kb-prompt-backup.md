# market-view-kb — Original Creation Prompt Backup

Created: 22-July-2026
Invoked via: `/skill-creator:skill-creator`

---

## Original Prompt (verbatim summary)

**Skill name:** `market_view_kb`

**Core purpose:**
- Daily market view validator for Indian NSE/BSE F&O trading
- Runs once per day — not repeatedly
- Acts as a critical second-opinion reviewer of the `dd-mm-yyyy-market_view.md` written by another agent
- Takes 2 parameters: today's date + file path to the market_view.md

**Role context:**
> "You are finance master in Indian stock market and best option trader, who is expert making profit with safe and creative strategies. You are my NSE/BSE options trading copilot."

**Data collection requirements:**
- Use Dhan / Zerodha / Kotak Neo MCPs first for live data
- Fall back to trusted financial platforms: Yahoo Finance, NSE/BSE website, Mint, Moneycontrol, etc.
- No assumptions on numbers. No guessing. Strictly verified data only.
- Follow `Market_View.md` framework for market view classification

**Classification output:** One of:
- Strongly Bullish · Slightly Bullish · Sideways · Slightly Bearish · Strongly Bearish

**Evidence to use:**
- Price + OI: Long Buildup / Short Covering / Short Buildup / Long Unwinding
- FII stance vs Client (retail) — FII leads; validate Net Change over 3+ days
- Option chain: PCR, heavy CE/PE writing, max pain
- VIX, global cues, PDH/PDL/PDC

**Outcome / workflow:**
1. Read the existing `dd-mm-yyyy-market_view.md` (already created by primary agent)
2. Validate the market view independently
3. If discrepancy found → show the difference first, do NOT modify the file
4. Only after user approves → append understanding under a new heading (do not modify existing content)

**File output rule:**
> "Once I approve then only append, your understanding under a new heading on the doc my-treads/DD-MM-YYYY/dd-mm-yyyy-market_view.md but do not modify the existing content just append it."

**Technical requirements:**
- Create skill folder inside the current project (`.claude/skills/`)
- Default model: Sonnet 4.6 (1M context) — `claude-sonnet-4-6`
- Read all `*.md` docs from the `kb/` folder to understand existing data points
- Add ALL data points (including ones missing from the original framework)
- Make it multi-dimensional — like a pro trader's full checklist

**Pro trader data points requested to be included:**
- Whatever data points are in `Market_View.md` (9 dimensions)
- Plus anything missing that pro traders use
- Check trusted financial sites to understand what experts use
- Goal: "I want to be like a pro in this skill and be like a pro trader when deciding how is the market today"

---

## What Was Built

### Data Dimensions Added (beyond existing Market_View.md framework)

The following 12 dimensions were identified as missing from the existing KB and added to the skill:

| # | Added Dimension | Why it matters |
|---|----------------|----------------|
| 1 | Opening Range High/Low (ORH/ORL) | First 15-min candle — key intraday reference level |
| 2 | VWAP (Volume Weighted Average Price) | Above VWAP = institutional intraday bullish bias |
| 3 | ATM Straddle Premium (CE + PE) | Market's priced-in expected daily range |
| 4 | Dollar Index (DXY) | Stronger DXY = FII outflow risk for India |
| 5 | US 10Y Treasury Yield | Rising yields = EM capital outflows, bearish India |
| 6 | Gold price | Risk-off signal (gold up = equity fear) |
| 7 | Volatility Skew | OTM Put IV vs OTM Call IV — shows downside fear premium |
| 8 | Futures Premium/Discount to Spot | Cost of carry signal (premium = bullish carry) |
| 9 | BANKNIFTY vs NIFTY Divergence | Divergence = low conviction, both aligned = high conviction |
| 10 | Advance/Decline Ratio | Broad market breadth vs narrow move in heavyweights |
| 11 | Delivery % validation | Breakouts on low delivery are traps |
| 12 | Expiry week special rules | Max Pain gravity stronger, Gamma risk high, Theta accelerates |

### Files Created

```
.claude/skills/market-view-kb/
  SKILL.md                         ← Main skill (186 lines)
  market-view-kb-prompt-backup.md  ← This file
  references/
    data_points.md                 ← Complete 10-dimension data checklist (207 lines)
    sources.md                     ← Where to find each data point (58 lines)
```

### Skill Usage

```
/market_view_kb 22-07-2026 my-treads/22-July-2026/22-07-2026-market_view.md
```

---

## Future Improvement Ideas (captured from session)

- Once Dhan account is created and Dhan MCP is configured, the skill can use live option chain data (Delta, Theta, Gamma, Vega per strike) directly from Dhan without web scraping
- Consider adding BANKNIFTY as a separate classification parameter if user starts trading BANKNIFTY options
- Skill could be extended to auto-generate strategy suggestions once the market view is validated (hook into `strategy_ref_book.md`)
