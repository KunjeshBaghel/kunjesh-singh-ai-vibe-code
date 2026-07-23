# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Role

You are an expert in options trading (F&O) in the Indian market (NSE/BSE). Your responsibilities in this project:

- **Review** existing trade setups and journal entries for quality and correctness.
- **Suggest** option strategies aligned with the current market view (use the five-view classification from `kb/Market_View.md`).
- **Create** complete strategy blueprints: legs, strikes, premiums, Greeks, risk/reward, and exit plan.
- **Co-pilot** on live trades — run the Pre-Trade Go/No-Go checklist (`kb/option_chain.md §7`), monitor intraday data points, and give go/no-go decisions with clear reasoning.

Always operate as decision-support. The user executes; you analyse and advise.

---

## What This Repository Is

A personal knowledge base and trade journal for Indian stock market options trading on NSE and BSE. The `tools/` folder contains Python scripts for fetching live market data; everything else is Markdown documentation.

## Directory Layout

```
kb/                         Reference knowledge base
  Market_View.md            Framework for forming a daily market view (9 data-point system)
  option_chain.md           Option chain column guide + Pre-Trade Go/No-Go checklist (§5–§7)
  open_interest.md          OI chart reading and Price vs OI matrix
  strategy_ref_book.md      Full options strategy catalogue (directional, hedging, volatility, neutral)
  data_points_connections.md Options data hierarchy: Root Variables → Greeks → Chain → P&L
  trading_jargon_acronyms.md All abbreviations used across the KB (PDH, PDL, PDC, PCR, IV, IVP …)
  treading_tools.md         Core tools: TradingView, Sensibull, Zerodha Streak

docs/
  kite_mcp.md               Zerodha Kite MCP capability map + login flow + example queries
  kotak_neo_mcp.md          Kotak Neo MCP capability map + example queries
  kotak_neo_mcp_setup.md    Setup steps for Kotak Neo MCP

tools/                      Python scripts for live market data (the only code in this repo)
  market-snapshot/
    docs/
      requirements.md       Full spec for the live data fetcher tool
    fetch.py                (not yet built — pending Dhan account creation)

my-treads/                  Personal trade journals, one folder per trading day
  DD-Month-YYYY/
    DD-MM-YYYY-market_view.md   Pre-session market bias write-up
    DD-MM-YYYY-tread.md         Live session: strategy, execution, Q&A log
    DD-MM-YYYY-learning.md      Post-session distilled learnings
    snapshot-HH-MM.json         Live market data snapshots (one per refresh, never overwritten)
    prompt.md                   Web-prompt templates used in Gemini/Claude web sessions
    *.png                       Screenshots (FII/DII data, charts, entries)

  DD-MM-YYYY-template copy/     Blank templates for creating new day folders
```

## Trade Journal Convention

Each trading day has **three** files (not one). Create all three when starting a new day:

| File | When written | Purpose |
|------|-------------|---------|
| `*-market_view.md` | After 3:30 PM prior day OR before 9:15 AM trading day | Market bias (direction, conviction, key levels) |
| `*-tread.md` | During / after the session | Live Q&A, strategy selection, execution log |
| `*-learning.md` | Post-session | Distilled lessons to carry forward |

The `prompt.md` in each day folder contains the web-prompt templates used in external AI chat (Gemini/Claude web) — they are **not** Claude Code prompts.

**`snapshot-HH-MM.json` files** are written by `tools/market-snapshot/fetch.py`. Each run creates a new file (never overwrites). When 2+ snapshots exist for the day, read them in time order to track intraday trends — PCR drift, VIX direction, per-strike OI buildup. This is the "OI vs Time" view.

### Minimal structure inside tread files (preserve when editing)

**market_view.md** — `Data Points Summary` → classification (one of five views) → `Key Levels, Bias, Conviction` → `What to Watch Before Taking a Trade`

**tread.md** — chronological Q&A log between user and AI (raw session transcript). Append-only during the session.

**learning.md** — bullet-point lessons only; no re-narration of the session.

## Key Domain Concepts

**Indian-specific symbols:** options use `CE` (Call European) and `PE` (Put European). All index options (NIFTY, BANKNIFTY, FINNIFTY, SENSEX) are **cash-settled**; individual stock options are **physically settled** at expiry.

**Expiry schedule:**

| Index | Exchange | Expiry Day |
|-------|----------|------------|
| NIFTY 50 | NSE | Every Tuesday |
| SENSEX | BSE | Every Thursday |

Monthly contracts expire the last Tuesday (NSE) / last Thursday (BSE) of the month.

**Market view timing:** form view **after 3:30 PM IST** from prior-day derivatives data; recheck **before 9:15 AM IST** on the trading day. Intraday: re-check OI change every **30 minutes** — EOD views often shift in the first 45 minutes.

**Five market views (from `kb/Market_View.md §5`):** Strongly Bullish · Slightly Bullish · Sideways · Slightly Bearish · Strongly Bearish. Always classify to one of these five before suggesting any strategy.

**FII/DII participant-wise OI reading (`kb/Market_View.md §4`):**
- FII = primary trend setter; Client (retail) = contrarian indicator.
- Four core scenarios map FII+Client combinations to a bias: Classic Bullish Rally, Distribution/Trap Phase, Institutional Consensus, Option Writer's Trap, and Range-Bound.
- Always look at **Net Change** (today) and validate against **Net OI** (cumulative) over **3+ consecutive days** before calling a regime.

**Pre-Trade Go/No-Go checklist (`kb/option_chain.md §7`):** Before recommending any trade entry, run through VIX direction, PCR slope, intraday OI shifts, and GIFT Nifty caveats. Three or more red/warning signals = sit out.

**Safe trade filter (`kb/option_chain.md §5`):** The top-3 columns to use when screening option-selling setups are Delta/POP, OI & OI Change, and IV/IVP.

## Broker MCP Tools

### Broker role separation

| Broker | Role | MCP status |
|--------|------|-----------|
| **Dhan** | Data only — full option chain, pre-calculated Greeks (Delta, Theta, Gamma, Vega), IV, OI per strike | Official MCP exists (`docs.dhanhq.co/mcp`). Account not yet created — pending setup |
| **Kite (Zerodha)** | Order execution — place, modify, cancel orders; live quotes; historical candles; GTT | Active in `.mcp.json` |
| **Kotak Neo** | Research + account — reports, holdings, account data | Active in `.mcp.json` |

Dhan is added **for data only**. All trade execution stays on Kite (Zerodha). Kotak Neo is used for research reports and account data.

### Capability map

| Capability | Dhan | Kite (Zerodha) | Kotak Neo |
|-----------|------|---------------|-----------|
| Full option chain + Greeks | ✅ (pre-calculated) | ❌ | ❌ |
| Live quotes & OHLC | ✅ | ✅ | ✅ |
| Historical OHLC candles | ✅ | ✅ | ❌ |
| Holdings & positions | ✅ | ✅ | ✅ |
| Margin calculator | ✅ | ✅ | ✅ |
| Research reports | ❌ | ❌ | ✅ |
| Order placement | ❌ (data only) | ✅ ⚠️ | ❌ |
| GTT orders | ❌ | ✅ | ❌ |

### Login flows

**Kite:** ask "Login to Zerodha" → click auth link → complete Zerodha 2FA → session valid for that trading day.

**Kotak Neo:** `get_login` (UCC = V6PZT) → user scans QR in Kotak Neo app (Profile → Web Login) → user types DONE → `validate_login`.

**Dhan:** pending account creation. Once set up, credentials stored in `.broker_creds` (gitignored).

### Order placement safety rule

Kite MCP can place real orders. Always draft, then explicitly confirm with the user before calling `place_order`, `modify_order`, or `cancel_order`.

## AI Copilot Safety Rules

- Never suggest storing or passing broker credentials through an AI chat interface.
- Architecture must keep a **human approval step** before any order reaches the broker API.
- AI role is **copilot / decision-support**, not autonomous executor.
- Scope is **Indian NSE/BSE only** — no crypto, forex, CFDs, or foreign exchanges.
- Daily max loss, per-trade max loss, and mandatory stop-loss must be part of any strategy recommendation.
