# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A personal knowledge base and trade journal for Indian stock market options trading on NSE and BSE. There is no code, no build system, and no tests — everything is Markdown documentation.

## Directory Layout

```
kb/           Reference knowledge base
  options_ref_book.md   Full options strategy reference for NSE/BSE
  Market_View.md        Framework for forming a daily market view
  treading_tools.md     Core tools (TradingView, Sensibull, Zerodha Streak)

my-treads/    Personal trade journals, one folder per trading day
  DD-month-YYYY/
    DD-MM-YYYY_tread.md   Trade setup and post-session learnings
    *.png                 Screenshots (FII/DII data, charts, entries)
```

## Trade Journal Convention

Each `_tread.md` file follows this structure:
- **Data points/Links** — market data sources used that day
- **Market View** — macro and derivatives context (global cues, FII/DII stance, VIX, PCR)
- **What Have You Done Here?** — exact legs entered (strike, CE/PE, lot count, avg price)
- **Why Would You Take This Trade?** — rationale (chart structure, option chain, scenario)
- **Learnings** — post-trade notes and lessons

When helping add or improve a trade journal entry, preserve this structure.

## Key Domain Concepts

**Indian-specific symbols:** options use `CE` (Call European) and `PE` (Put European). All index options (NIFTY, BANKNIFTY, FINNIFTY, SENSEX) are **cash-settled**; individual stock options are **physically settled** at expiry.

**Expiry schedule:**
- NIFTY 50 — weekly, every **Tuesday** (NSE)
- SENSEX — weekly, every **Thursday** (BSE)
- Monthly contracts expire the last Tuesday (NSE) / last Thursday (BSE) of the month.

**Market view timing:** form view **after 3:30 PM IST** from prior-day derivatives data; recheck **before 9:15 AM IST** on the trading day.

**FII/DII participant-wise OI reading:** FII is the primary trend setter; Client (retail) is typically contrarian. The four scenarios documented in `kb/Market_View.md` map FII+Client combinations to a market bias. Always look at **Net Change** (today's flow) and validate against **Net OI** (cumulative) over 3+ consecutive days before calling a regime.

## AI Copilot Safety Rules (from kb/options_ref_book.md §7)

When helping with any AI-assisted trading workflow, respect these constraints that are documented in the knowledge base:

- Never suggest storing or passing broker credentials (API key, TOTP seed, access token, OTP) through an AI chat interface.
- Architecture must keep a **human approval step** before any order reaches the broker API.
- AI role is **copilot / decision-support**, not autonomous executor.
- Scope is **Indian NSE/BSE only** — no crypto, forex, CFDs, or foreign exchanges.
- Daily max loss, per-trade max loss, and mandatory stop-loss must be part of any Python copilot plan.
