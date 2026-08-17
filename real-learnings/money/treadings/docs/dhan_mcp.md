# Dhan MCP — Usage Guide

**Source:** [docs.dhanhq.co/mcp](https://docs.dhanhq.co/mcp)

Dhan MCP connects your Dhan account to Claude. It covers **the full stack**: option chain with pre-calculated Greeks, live market data, historical OHLCV, portfolio, order placement, and conditional alerts with auto-order triggers.

> ⚠️ **Safety rule:** Never let AI place an order without your explicit approval. Every order suggestion is a draft — you are the final executor.
> **Link** [dhan-mcp](https://docs.dhanhq.co/mcp)
---

## Capability Map (11 Tools)

```
Dhan MCP
│
├── 🔑 Auth
│   ├── login              — start consent / auth flow, returns browser URL
│   └── complete_login     — finalize session using tokenId from callback URL
│
├── 📡 Market Data
│   ├── market_data → ltp          — last traded price (bulk, multiple instruments)
│   ├── market_data → ohlc         — Open/High/Low/Close + LTP
│   ├── market_data → quote        — full quote: 5-level market depth, OI, circuit limits
│   ├── market_data → optionchain  — ★ FULL option chain: Greeks + IV + OI per strike
│   └── market_data → expirylist   — available expiry dates for any underlying
│
├── 📈 Historical Data
│   ├── historical_data → intraday  — 1/5/15/25/60-min OHLCV candles (≤90 days per call)
│   └── historical_data → historical — daily candles for any date range
│
├── 💰 Portfolio & Account
│   ├── portfolio → holdings  — demat holdings with P&L
│   ├── portfolio → positions — open intraday + F&O positions (uses costPrice, not buyPrice)
│   ├── portfolio → funds     — available margin / fund limits
│   └── portfolio → trades    — today's executed trades
│
├── 📋 Orders & Trades
│   ├── orderbook → list       — today's full order book
│   ├── orderbook → get        — specific order by order ID
│   ├── orderbook → super_list — super order book incl. all leg details
│   └── tradebook → list / by_order — execution history
│
├── ⚡ Order Execution (USE WITH CAUTION)
│   ├── trading → place        — market / limit / stop-loss / SL-market order
│   ├── trading → modify       — change price/qty of a pending order
│   ├── trading → cancel       — cancel a pending order
│   ├── trading → super_place  — bracket order: entry + target + SL + trailing stop in one shot
│   ├── trading → super_modify — modify one leg of a super order
│   └── trading → super_cancel — cancel one leg of a super order
│
├── 🧮 Margin Calculator
│   ├── margin → single — margin for a single order
│   └── margin → multi  — basket margin (multiple orders / existing positions)
│
└── 🔔 Conditional Alerts
    ├── alerts → create — conditional trigger: price or technical-indicator based
    ├── alerts → modify — update an existing alert
    ├── alerts → list   — get all active alerts
    └── alerts → delete — remove an alert
```

---

## Key Capability Deep-Dives

### ★ Option Chain (the big one)

The `optionchain` action returns a **full option chain** for any index or stock with pre-calculated values per strike:

| Field | What it means |
|-------|--------------|
| Delta | Rate of change of option price vs underlying |
| Theta | Time decay per day |
| Gamma | Rate of change of Delta |
| Vega  | Sensitivity to IV change |
| IV    | Implied Volatility per strike |
| OI    | Open Interest (number of contracts) |
| OI Change | Today's OI delta (buildup or unwinding) |

```
# Fetch NIFTY option chain for a specific expiry
"Get NIFTY option chain for 2026-08-14 expiry"
"Show me all strikes for BANKNIFTY weekly expiry with IV and OI"
"What is the PCR (Put-Call Ratio) for NIFTY right now?"
```

**Rate limit:** 1 unique request per 3 seconds (client-enforced).

---

### ★ Conditional Alerts with Auto-Order Triggers

The `alerts` tool is the closest thing to a scanner/watchdog. It monitors a condition and optionally fires an order when triggered.

**Two trigger types:**

| Type | Description |
|------|-------------|
| `PRICE_WITH_VALUE` | Fire when price crosses/equals a fixed level |
| `TECHNICAL_WITH_VALUE` | Fire when a technical indicator (SMA, EMA, RSI, MACD…) hits a value |
| `TECHNICAL_WITH_INDICATOR` | Fire when one indicator crosses another |
| `TECHNICAL_WITH_CLOSE` | Fire when indicator crosses the close price |

**Supported indicators:** SMA_5/10/20/50/100/200, EMA_5/10/20/50/100/200, RSI_14, MACD variants

**Supported operators:** CROSSING_UP, CROSSING_DOWN, CROSSING_ANY_SIDE, GREATER_THAN, LESS_THAN, GREATER_THAN_EQUAL, LESS_THAN_EQUAL, EQUAL, NOT_EQUAL

**Supported timeframes:** DAY, ONE_MIN, FIVE_MIN, FIFTEEN_MIN

**Limitation:** Alerts work on **equities and indices only** (NSE_EQ, BSE_EQ, IDX_I). No direct F&O alerts (you alert on the index, then manually place the option order).

---

### ★ Super Orders (Bracket Orders)

A single `super_place` call creates **three legs atomically**: entry + profit target + stop-loss with optional trailing stop. Ideal for systematic F&O trades.

```
super_place example for a CE buy:
  transactionType: BUY
  exchangeSegment: NSE_FNO
  securityId: <option securityId>
  price: 120.0        ← entry limit price
  targetPrice: 180.0  ← take profit
  stopLossPrice: 80.0 ← hard stop
  trailingJump: 5.0   ← trail SL by ₹5 as price moves in your favor
```

---

## Example Queries

### Option Chain & OI Analysis

```
"Get NIFTY option chain for 14 Aug 2026 expiry"
"Show me strikes from 24000 to 25000 with IV and OI for BANKNIFTY"
"What are the available expiry dates for NIFTY?"
"Which CE/PE strikes have the highest OI buildup today?"
"Calculate PCR from the current option chain data"
```

### Live Market Data

```
"Get live quote for NIFTY spot"
"Show OHLC for RELIANCE and HDFC Bank"
"Get full market depth for NIFTY 24500 CE"
"What are the circuit limits on HDFC Bank today?"
```

### Historical Data & Trend Analysis

```
"Get 15-min candles for NIFTY from 9:15 to 15:30 today"
"Show daily candles for BANKNIFTY for the last 30 days"
"Get 5-min OHLCV for RELIANCE from 2026-08-01 to 2026-08-09"
"Fetch intraday data with OI for NIFTY FUT current month"
```

### Portfolio & Account

```
"Show my Dhan available margin"
"What are my open F&O positions?"
"Show today's executed trades"
"What are my equity holdings?"
```

### Margin Calculator

```
"How much margin to sell 1 lot of NIFTY 24500 CE?"
"Calculate basket margin for this Iron Condor setup: [4 legs]"
"Check margin for selling BANKNIFTY PE + CE simultaneously"
```

### Alerts / Scanners

```
"Create an alert: notify when NIFTY crosses above 24800 on the daily chart"
"Alert me when RSI_14 crosses above 60 on RELIANCE (5-min)"
"Set an alert: when EMA_20 crosses above EMA_50 on HDFC Bank daily"
"Show all my active alerts"
"Delete the alert with ID xyz"
```

### Order Placement (confirm before executing)

```
"Place a LIMIT BUY for 1 lot NIFTY 24500 CE at ₹120"  ← AI drafts, YOU confirm
"Place a super order: buy NIFTY CE at 120, target 180, SL 80"  ← AI drafts, YOU confirm
"Cancel order ID 12345"                                 ← AI drafts, YOU confirm
```

---

## Answering Your Three Questions

### 1. Can I watch option chain and OI data via Claude Code?

**YES — this is Dhan MCP's strongest capability.**

- Full option chain with Delta, Theta, Gamma, Vega, IV, OI, OI Change per strike
- Available expiry dates for any underlying
- Live quotes with 5-level market depth
- Intraday + daily historical OHLCV with OI overlay (for tracking OI buildup over time)
- Rate limit: 1 option chain request per 3 seconds

You can ask Claude to pull the chain, compute PCR, highlight max-pain strikes, and track OI change as a session progresses — everything manually that Sensibull does, but inside Claude.

### 2. Can I do option trading via Dhan MCP?

**YES — Dhan MCP has full F&O order placement.**

Supports `NSE_FNO` and `BSE_FNO` exchange segments with LIMIT, MARKET, STOP_LOSS, STOP_LOSS_MARKET orders. Also supports **super orders** (bracket orders: entry + target + SL + trailing in one shot).

> **Note on architecture:** CLAUDE.md currently designates Dhan as "data only" with Kite for execution. Now that Dhan MCP is connected and confirmed to have trading tools, you can choose to use Dhan for execution too — or keep the separation. Dhan's super orders are a meaningful advantage for F&O (bracket orders in one call).

### 3. Can I create scanners or alerts / let Claude monitor the live market?

**PARTIALLY YES — alerts exist, live monitoring requires polling.**

**What works:**
- Conditional alerts on price (crossing levels) or technical indicators (SMA/EMA/RSI/MACD) on any timeframe
- Alerts can auto-trigger an order when fired
- Works on equities and indices (IDX_I for NIFTY/BANKNIFTY)

**Limitation — alerts don't work on F&O instruments directly.** You alert on the index (e.g., NIFTY), then the triggered order must be an equity order, not an option. To auto-trade options on an alert, you'd need a separate system outside Claude.

**For live monitoring via Claude:** Claude can't run a background loop, but you can ask it to `poll` by repeatedly calling `market_data → optionchain` or `quote` every few minutes during a session. It's manual polling, not a daemon.

---

## Dhan MCP vs Kite MCP vs Kotak Neo MCP

| Feature | Dhan MCP | Kite MCP (Zerodha) | Kotak Neo MCP |
|---------|----------|--------------------|---------------|
| Option Chain + Greeks | ✅ Pre-calculated | ❌ | ❌ |
| OI per strike | ✅ | ❌ | ❌ |
| Live Quotes | ✅ | ✅ | ✅ |
| Market Depth (5-level) | ✅ | ✅ | ✅ |
| Historical OHLCV | ✅ | ✅ | ❌ |
| Intraday OHLCV | ✅ | ✅ | ❌ |
| Holdings & Positions | ✅ | ✅ | ✅ |
| Funds / Margin | ✅ | ✅ | ✅ |
| Basket Margin Calculator | ✅ | ❌ | ❌ |
| Research Reports | ❌ | ❌ | ✅ |
| Mutual Funds | ❌ | ✅ | ❌ |
| Order Placement | ✅ ⚠️ | ✅ ⚠️ | ❌ |
| Super Orders (Bracket) | ✅ | ❌ | ❌ |
| GTT Orders | ❌ | ✅ | ❌ |
| Conditional Alerts | ✅ | ❌ | ❌ |
| Auto-order on Alert | ✅ | ❌ | ❌ |

---

## Login Flow

Dhan uses a **2-phase auth**: a one-time OAuth setup (per Claude Code install) + a per-session consent login.

### Phase 1 — One-time OAuth Setup (stored in `~/.claude.json`)

```bash
# Add Dhan as HTTP transport MCP (run once in terminal):
claude mcp add --transport http --client-id <YOUR_DHAN_CLIENT_ID> dhan https://mcp.dhan.co/mcp
# YOUR_DHAN_CLIENT_ID = your numeric Dhan account client ID (e.g. 1112807061)
# stored in .broker_creds as DHAN_CLIENT_ID

# Then authenticate via the /mcp menu in Claude Code → pick dhan → Authenticate
# Browser opens → complete Dhan consent → "Authentication successful" page appears
# If you get {"error":"invalid_client"}: remove and re-add with --client-id flag (see above)
```

Config is stored in `~/.claude.json` (NOT `.mcp.json`). The entry looks like:
```json
"dhan": {
  "type": "http",
  "url": "https://mcp.dhan.co/mcp",
  "oauth": { "clientId": "<YOUR_DHAN_CLIENT_ID>" }
}
```

### Phase 2 — Per-session Dhan Login (every Claude Code session)

```
1. Ask Claude: "Login to Dhan" or "Show my Dhan positions"
2. Claude calls mcp__dhan__login → returns a browser consent URL
   Format: https://auth.dhan.co/consent-login?consentId=...
3. Click the URL → log in with Dhan credentials in browser
4. Browser redirects to: https://mcp.dhan.co/auth/callback?tokenId=...&consentId=...
5a. If auto-binding works → "token already consumed" = SUCCESS, session active
5b. If not auto-bound → copy tokenId from callback URL → tell Claude:
    "complete_login with tokenId <value>"
6. Verify: ask "Show my Dhan funds"
```

Session is valid for the trading day. Re-login (Phase 2 only) required every new Claude Code session.

---

## Config

Dhan uses **HTTP transport** stored in `~/.claude.json` (project-scoped), **not** `.mcp.json`.

Kite and Kotak Neo use `.mcp.json` with `mcp-remote` (stdio transport). Dhan is different:

| Broker | Transport | Config file |
|--------|-----------|-------------|
| Kite (Zerodha) | stdio via `mcp-remote` | `.mcp.json` |
| Kotak Neo | stdio via `mcp-remote` | `.mcp.json` |
| Dhan | HTTP (OAuth) | `~/.claude.json` |

---

## Rate Limits (important for F&O use)

| API | Limit |
|-----|-------|
| LTP / OHLC / Quote | 1 request / second |
| Option Chain | 1 unique request / 3 seconds |
| Historical (intraday) | ≤ 90 days per call |

If you're polling the option chain every 30 seconds (the recommended OI re-check interval from CLAUDE.md), you're well within limits.

---

*Disclaimer: AI suggestions are decision-support only. Always confirm orders before execution. Dhan T&C apply.*
