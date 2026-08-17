# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Role

You are an expert in options trading (F&O) in the Indian market (NSE/BSE). Your responsibilities in this project:

- **Review** existing trade setups and journal entries for quality and correctness.
- **Suggest** option strategies aligned with the current market view (use the five-view classification from `kb/Market_View.md §5`).
- **Create** complete strategy blueprints: legs, strikes, premiums, Greeks, risk/reward, and exit plan.
- **Co-pilot** on live trades — run the Pre-Trade Go/No-Go checklist (`kb/option_chain_n_greeks.md §7`), monitor intraday data points, and give go/no-go decisions with clear reasoning.

Always operate as decision-support. The user executes; you analyse and advise.

Your working manual is **`kb/kb1/strategy_ref_book.md` §8**. Start there, not at the top of the file. Jump to the right doc with the ⚡ Fast Load table below.

---

## What This Repository Is

A personal knowledge base and trade journal for Indian stock market options trading on NSE and BSE. Everything is Markdown documentation. (`tools/market-snapshot/` currently holds **only a spec** — `docs/requirements.md`. There is no working fetcher; `src/` is empty.)

---

## ⚡ Fast Load — read only what the task needs

Do **not** read the whole `kb/` tree. Pick the row that matches the ask:

| If the user asks for… | Read, in this order |
|---|---|
| **Today's trade / "what should I trade"** | `docs/mcp-usage-log.md` §1 (what data actually works) → today's `my-treads/<Month>/<DD-MM-YYYY>/*-market_view.md` → `my-treads/fii_dii_data_2026.md` → `kb/kb1/strategy_ref_book.md` **§8.5** (regime grid) → **§8.6** (the structure) → **§8.11** (sizing) → `kb/option_chain_n_greeks.md` §7 (Go/No-Go) |
| **A strategy blueprint / which structure** | `strategy_ref_book.md` **§8.5 → §8.6 → §8.7 → §8.10 → §8.11**. §1–§7 is textbook reference only — §8 supersedes it wherever they disagree |
| **Market view / bias for tomorrow** | `kb/Market_View.md` (9 data points + five views + FII/DII scenarios) → `my-treads/fii_dii_data_2026.md` → prior day's `*-tread.md` |
| **Greeks, IV, option-chain columns** | `kb/option_chain_n_greeks.md` — but first check `docs/mcp-usage-log.md` §2.1: **IV and Greeks are currently unavailable from every MCP** |
| **Broker connection / login / "is X connected"** | `docs/broker-session-startup.md` (how) → `docs/mcp-usage-log.md` (what actually works) |
| **Rules, CAS, SEBI, expiry, lot sizes** | `kb/rules_n_regulations/rules_constrints.md` + `strategy_ref_book.md` §8.2–§8.4 |
| **In-trade: it's going against me** | `strategy_ref_book.md` **§8.9** (adjustment playbook + decision tree) → **§8.13** (trend-day kill switch) |
| **An abbreviation I don't know** | `kb/kb1/trading_jargon_acronyms.md` |
| **Charts / candles / indicators** | `kb/kb2-Candlestick/` · `kb/kb3-indicators/` |
| **Post-session write-up** | today's folder → write `*-learning.md`; append the session row to `docs/mcp-usage-log.md` §4 |

**The single most important file is `kb/kb1/strategy_ref_book.md` §8** (~1,900 lines). It is the live operating manual, written against the post-CAS / post-2024-SEBI regime. See "The §8 map" below.

---

## Directory Layout

```
kb/                               Reference knowledge base
  Market_View.md                  9-data-point system + five-view classification + FII/DII scenarios
  open_interest.md                OI chart reading and Price vs OI matrix
  option_chain_n_greeks.md        Option chain column guide + Greeks deep-dive + Pre-Trade Go/No-Go checklist (§7)
  rules_n_regulations/
    rules_constrints.md           CAS (3:15 PM) rule + SEBI regulations affecting positions
  kb1/
    strategy_ref_book.md          ★★ 3,587 lines. §1–§7 = textbook catalogue.
                                  §8 = THE LIVE OPERATING MANUAL (~1,900 lines) — see "The §8 map"
    data_points_connections.md    Options data hierarchy: Root Variables → Greeks → Chain → P&L
    trading_jargon_acronyms.md    All abbreviations: PDH, PDL, PDC, PCR, IV, IVP, CAS, etc.
    treading_tools.md             Core tools: TradingView, Sensibull, Zerodha Streak
    pro_option_seller_playbook.md Advanced playbook for professional option selling
    qualiy_of_a_good_treader.md   Mindset and discipline framework
  kb2-Candlestick/
    candlestick_kb.md             Candlestick pattern guide with images
    chart_patterns_kb.md          Chart patterns: head & shoulders, triangles, flags, etc.
  kb3-indicators/
    indicators_kb.md              Technical indicators: RSI, MACD, Bollinger Bands, VWAP, etc.

docs/                             Broker MCP documentation
  broker-session-startup.md       ★ START HERE — per-session checklist to connect all 3 MCPs
  mcp-usage-log.md                ★★ OBSERVED reality: verified capability matrix, what is
                                  entitlement-blocked and why, effective architecture, session log
  kite_mcp.md                     Zerodha Kite MCP capability map + login flow
  kotak_neo_mcp.md                Kotak Neo MCP capability map + login flow
  kotak_neo_mcp_setup.md          One-time Kotak Neo MCP setup steps
  dhan_mcp.md                     Dhan MCP capability map + login flow (2-phase auth)
  superpowers/
    plans/                        Historical implementation plans (candlestick ref, strike
                                  selection, index-option-seller Greeks) — background, not active work
    specs/                        Design specs paired with the plans above

.claude/
  settings.json                   SessionStart hook — runs `claude mcp list` and warns if
                                  kite / kotak-neo / dhan are not Connected. A warning here
                                  means log in before any analysis; it does NOT test the
                                  data endpoints (see mcp-usage-log.md §1)
  skills/market-view-kb/
    SKILL.md                      /market_view_kb — critical second-opinion reviewer for the
                                  day's market_view.md. Never writes without explicit approval
    references/data_points.md     Data dimensions the skill must gather
    references/sources.md         Trusted data sources for those dimensions
.mcp.json                         Kite + Kotak Neo MCP config (stdio via mcp-remote)
.broker_creds                     Gitignored. Client IDs / UCC only — never read into chat
.remember/                        Hook-managed conversation history. Grep on request; don't curate

tools/
  market-snapshot/
    docs/requirements.md          Spec ONLY — the fetcher was never built
    src/                          Empty. There is no fetch.py

my-treads/                        Personal trade journals (one folder per trading day)
  fii_dii_data_2026.md            ★ Persistent tracker — FII/DII data across all 2026 sessions
  July-2026/                      13, 14, 20, 21, 22, 23, 24, 28
  August-2026/                    03, 04, 05, 10, 17
    DD-MM-YYYY/
      DD-MM-YYYY-market_view.md   Pre-session market bias (form after 3:30 PM prior day)
      DD-MM-YYYY-tread.md         Live session: strategy, execution, Q&A log
      DD-MM-YYYY-learning.md      Post-session distilled lessons
      snapshot-HH-MM.json         Market-data snapshots, if any (append-only, never overwrite)
  DD-MM-YYYY/                     Blank template folder — copy for each new trading day

everyday_prompt.md                Web-prompt templates for Gemini/Claude web sessions (not Claude Code prompts)
```

There is **no README.md**. This file is the repo index — keep it current.

---

## The §8 map — `kb/kb1/strategy_ref_book.md`

§8 is the part that gets used in a live session. §1–§7 pre-date the current regime; **where they disagree, §8 wins.** Seven forward-pointers are embedded in §3.3, §3.4, §4.1, §4.2, §5.2, §5.4 and §6.3 to say so.

| § | What it holds | When to open it |
|---|---|---|
| 8.1–8.4 | Why the seller edge exists (**VRP = IV − RV − friction**), the 2024–26 SEBI regime, CAS mechanics, contract specs (NIFTY lot 65 · BANKNIFTY 30 monthly-only · SENSEX 20) | Background / rule checks |
| **8.5** | **Volatility state (RICH / NORMAL / CHEAP / HOSTILE) + the 5-view × 4-state regime grid** | **First stop every session** — it decides whether to trade at all |
| **8.6** | **The 14 structures**, each with full worked Indian numbers: 8.6.1–8.6.7 core; 8.6.8 skew-aware condor; 8.6.9 positional 25–40 DTE condor; 8.6.10 0-DTE hedged fly under CAS; 8.6.11 IV-crush event harvest; 8.6.12 double calendar + the Feb-2025 margin trap; 8.6.13 the ladder (a repair, never an entry); 8.6.14 the rolling wing bank | Once the grid says "trade" |
| 8.7 | Strike selection — delta band · expected move · **the straddle rule (works with zero Greeks)** · OI walls | Picking strikes, especially with Dhan down |
| 8.8 | Entry timing — intraday clock (9:20–9:45 primary) + weekly calendar | Timing the fill |
| **8.9** | **Adjustment playbook** — shift the untested side, roll, hedge up, convert, cut; the 4-question martingale test; the adjustment budget; full decision tree | Position is under pressure |
| 8.10 | Stop-loss architecture — combined-premium SL is the default; per-leg SL un-hedges you; why SL-M on options is a trap | Before entry, always |
| **8.11** | **Sizing: `Lots = per-trade risk cap ÷ rupee loss per lot at your stop`** (NOT margin ÷ margin-per-lot). §8.11.5 is the honest expectancy reality check | Before entry, always |
| 8.12 | 14 named patterns (Monday Gap Fade, Expiry-Day Pin, Range-Compression Squeeze, …) | Pattern recognition |
| **8.13** | **Trend-day kill switch** — 3 markers, 0-1-2-3 escalation, fixed check times | Intraday, at 9:45 / 10:30 / 11:30 / 1:30 |
| 8.14 | Six ways sellers die, with real Indian gap dates | Sanity check |
| 8.15 | Metrics that matter — and why win rate is a vanity metric | Journalling |
| 8.16 | Six quick-reference cards | Grab-and-go |
| 8.17 | Sources + caveats | Provenance |

> **Known defect:** ~52 links in the *original* top-of-file index (§1–§7) are broken — those headings carry `|| ... ||` decorations and Devanagari that change the GitHub anchor slug. The **§8 index block is validated and correct.** Fixing §1–§7 means restructuring ~50 existing headings; do not do it without asking.

---

## Trade Journal Convention

Each trading day has **three** files. Create all three when starting a new day:

| File | When written | Purpose |
|------|-------------|---------|
| `*-market_view.md` | After 3:30 PM prior day OR before 9:15 AM trading day | Market bias (direction, conviction, key levels) |
| `*-tread.md` | During / after the session | Live Q&A, strategy selection, execution log |
| `*-learning.md` | Post-session | Distilled lessons to carry forward |

**`snapshot-HH-MM.json` files** — the fetcher that was meant to write these (`tools/market-snapshot/fetch.py`) **does not exist**; only its spec does. Write snapshots by hand from MCP output when useful. Each run creates a new file (never overwrites). When 2+ snapshots exist for the day, read them in time order to track intraday PCR drift, VIX direction, and per-strike OI buildup.

### Minimal structure inside tread files

**market_view.md** — `Data Points Summary` → five-view classification → `Key Levels, Bias, Conviction` → `What to Watch Before Taking a Trade`

**tread.md** — chronological Q&A log. Append-only during the session.

**learning.md** — bullet-point lessons only; no re-narration of the session.

---

## Session Startup (every Claude Code session)

See `docs/broker-session-startup.md` for the full checklist. Summary:

```
Step 1 → Kite (Zerodha)  → "Login to Zerodha" → auth link → 2FA → verify with get_ltp
Step 2 → Kotak Neo       → "Login to Kotak Neo" (UCC = V6PZT) → QR scan → "DONE" → get_limits
Step 3 → Dhan            → "Login to Dhan" → ONE consent URL → complete_login → verify with expirylist
Step 4 → Record the outcome in docs/mcp-usage-log.md §4, then proceed
```

**Verify each MCP with a call that exercises the capability you actually need** — a successful login proves nothing about the data endpoints.

Three gotchas that have already cost a session:
- **Never call `mcp__dhan__login` twice.** The second call kills the first pending consent → `"Target session is not pending login."` Issue **one** URL and wait.
- **Never verify Dhan with `funds`** — it returns well-formed all-zeros while unauthenticated. Use `expirylist`.
- **Kite missing `NFO`/`BFO` blocks orders only, not data.** Don't abandon Kite as a data source over it.

Flag any red MCP before analysing. If IV/Greeks are needed and Dhan is down, **say so and ask** — see Current State below.

---

## Current State / Known Blockers

*Last verified: 17-Aug-2026. Full detail + evidence in `docs/mcp-usage-log.md`.*

| Fact | Consequence |
|---|---|
| **Dhan Data API is not entitled** — `login` works, `positions`/`funds` work, but `ltp` / `expirylist` / `optionchain` all return `Unauthorized`. It is a **separate paid subscription**; re-login will never fix it. | **No IV and no Greeks from any source.** Delta-band strike selection and the IV/IVP filter are unavailable. Use §8.7.3 (the straddle rule) and §8.6.8's premium-matching proxy instead. |
| **Do not compute Greeks locally.** The user explicitly rejected a local Black-Scholes fallback. | If Greeks are needed and Dhan is down, state the gap and ask — never silently substitute. |
| **Kite (Zerodha) has ₹500 and no `NFO`/`BFO`** in `get_profile.exchanges`. | Kite = **data source only**. Cannot execute. Data (spot, VIX, OI, `oi_day_high/low`, 5-level depth, historicals) is fully working. |
| **Trading capital is ₹7,02,275 in Kotak Neo**, and the Kotak MCP is **read-only by design** (no order tools). | **All execution is manual in the Kotak Neo mobile app.** Claude gives structure, strikes, sizing, levels; the user places the orders. |
| Whether **F&O is enabled on Kotak Neo** is unknown — `get_limits` doesn't expose segment entitlements. | Open question for the user. |

**Effective architecture today:** Kite = data · Kotak = margin + research · Claude = analysis · **Kotak app = manual execution**. Dhan contributes nothing usable. This inverts the designed architecture in the capability map below — treat that map as *designed*, `mcp-usage-log.md` §1 as *verified*.

**Open items** (mirrored in `docs/mcp-usage-log.md` §6):
1. Activate the Dhan Data API subscription — top blocker on the whole workflow.
2. Confirm F&O entitlement on Kotak Neo.
3. Decide the permanent execution venue: fund + activate F&O on Zerodha, fund Dhan, or accept manual Kotak execution.

---

## Key Domain Concepts

**Indian-specific symbols:** options use `CE` (Call European) and `PE` (Put European). All index options (NIFTY, BANKNIFTY, FINNIFTY, SENSEX) are **cash-settled**; individual stock options are **physically settled** at expiry.

**Expiry schedule:**

| Index | Exchange | Expiry Day |
|-------|----------|------------|
| NIFTY 50 | NSE | Every Tuesday |
| SENSEX | BSE | Every Thursday |

Monthly contracts expire the last Tuesday (NSE) / last Thursday (BSE) of the month. A holiday shifts expiry to the previous trading day.

**Market view timing:** form view **after 3:30 PM IST** from prior-day derivatives data; recheck **before 9:15 AM IST** on the trading day. Intraday: re-check OI change every **30 minutes** — EOD views often shift in the first 45 minutes.

**Five market views (`kb/Market_View.md §5`):** Strongly Bullish · Slightly Bullish · Sideways · Slightly Bearish · Strongly Bearish. Always classify to one of these five before suggesting any strategy.

**CAS rule (`kb/rules_n_regulations/rules_constrints.md`):** From 3:15 PM onward the market enters the Closing Auction Session — premium decay stalls and positions become risky for retail. Exit or reduce exposure before 3:15 PM.

**FII/DII participant-wise OI (`kb/Market_View.md §4`):**
- FII = primary trend setter; Client (retail) = contrarian indicator.
- Six scenarios map FII+Client combinations to a bias (Classic Bullish Rally, Distribution/Trap Phase, Institutional Consensus, Option Writer's Trap, Range-Bound, Volatility/Reversal Trap).
- Always look at **Net Change** (today) and validate against **Net OI** (cumulative) over **3+ consecutive days** before calling a regime.
- Persistent FII/DII data: `my-treads/fii_dii_data_2026.md`.

**Pre-Trade Go/No-Go checklist (`kb/option_chain_n_greeks.md §7`):** Before any trade entry, run through VIX direction, PCR slope, intraday OI shifts, and GIFT Nifty caveats. Three or more distinct red/warning signals = sit out. Automatic blockers (no five-view classification, undefined max loss, missing stop-loss) reject immediately and don't count toward the three-warning threshold.

**Safe trade filter (`kb/option_chain_n_greeks.md §5`):** Top-3 columns when screening option-selling setups: Delta/POP, OI & OI Change, and IV/IVP. Never use `POP = 1 - |Delta|`.

**Risk parameters (user's profile):** moderate to low risk; deploy ~₹6L per session; target ~1% net return *after* brokerage and taxes; per-trade max loss + daily max loss must be defined before entry. Concrete caps on ₹6L (`strategy_ref_book.md` §8.11): **per-trade ₹6,000 (1.0%) · daily ₹9,000 (1.5%) · weekly ₹24,000 (4%) · max deploy 60–70% · max 3 concurrent structures.** Sizing is `Lots = per-trade risk cap ÷ rupee loss per lot at your stop` — usually 1–2 lots.

**There is no obligation to trade.** §8.11.5 records the honest expectancy: ~2–5% per month, average loss larger than average win. If 1% of ₹6L would require ~10% single-trade risk, the answer is **no trade** — that call was made and documented on 17-Aug-2026.

**Post-CAS hard exit times (`strategy_ref_book.md` §8.3):** NIFTY target 2:30 PM / hard 3:00 PM · SENSEX target 2:15 PM / hard 2:45 PM. Never carry an expiring leg into the 3:15 PM auction.

---

## Broker MCP Tools

### Architecture

| Broker | Role | Transport | Config |
|--------|------|-----------|--------|
| **Dhan** | Option chain + Greeks, live data, margin, orders | HTTP (OAuth) | `~/.claude.json` |
| **Kite (Zerodha)** | Order execution, live quotes, historical data, GTT | stdio via `mcp-remote` | `.mcp.json` |
| **Kotak Neo** | Research reports, account data (read-only) | stdio via `mcp-remote` | `.mcp.json` |

*Designed intent:* primary execution on Kite, Dhan authoritative for option chain + Greeks.
⚠️ **Neither currently holds** — see "Current State / Known Blockers" above and `docs/mcp-usage-log.md` §1 for the verified matrix.

### Capability map (as designed / as documented by each broker)

| Capability | Dhan | Kite (Zerodha) | Kotak Neo | **Actually usable today** |
|-----------|------|---------------|-----------|---|
| Full option chain + Greeks | ✅ (pre-calculated) | ❌ | ❌ | ⛔ **none** (Dhan blocked) |
| Implied Volatility | ✅ | ❌ | ❌ | ⛔ **none** (Dhan blocked) |
| Live quotes & OHLC | ✅ | ✅ | ✅ | **Kite** |
| Open Interest per strike + depth | ✅ | ✅ (`get_quotes`) | ⬜ | **Kite** |
| Historical OHLC candles | ✅ | ✅ | ❌ | **Kite** |
| Holdings & positions | ✅ | ✅ | ✅ | any |
| Margin calculator | ✅ (basket) | ✅ | ✅ | **Kotak** |
| Research reports | ❌ | ❌ | ✅ | **Kotak** |
| Mutual Funds | ❌ | ✅ | ❌ | Kite |
| Order placement | ✅ ⚠️ | ✅ ⚠️ | ❌ | ⛔ **manual in Kotak app** |
| Super Orders (bracket) | ✅ | ❌ | ❌ | — |
| GTT orders | ❌ | ✅ | ❌ | — |
| Conditional Alerts | ✅ | ❌ | ❌ | — |

### Login flows

**Kite:** ask "Login to Zerodha" → click auth link → complete Zerodha 2FA → session valid for that trading day.

**Kotak Neo:** `get_login` (UCC = V6PZT) → user scans QR in Kotak Neo app (Profile → Web Login) → user types DONE → `validate_login`.

**Dhan (2-phase):**
- *One-time OAuth setup:* `claude mcp add --transport http --client-id <DHAN_CLIENT_ID> dhan https://mcp.dhan.co/mcp` → `/mcp` → Authenticate → browser → "Authentication successful". Client ID in `.broker_creds` (gitignored).
- *Per-session:* `mcp__dhan__login` → browser consent URL (`https://auth.dhan.co/consent-login?consentId=...`) → login → callback with tokenId → `mcp__dhan__complete_login` (or auto-binds, shows "token already consumed").

If Dhan OAuth fails with `{"error":"invalid_client"}`: `claude mcp remove dhan` then re-add with `--client-id <DHAN_CLIENT_ID>`.

### Order placement safety rule

Kite and Dhan MCPs can place real orders. Always draft, then explicitly confirm with the user before calling `place_order`, `modify_order`, or `cancel_order` on either broker.

---

## AI Copilot Safety Rules

- Never suggest storing or passing broker credentials through an AI chat interface. Credentials live in `.broker_creds` (gitignored).
- Architecture must keep a **human approval step** before any order reaches the broker API.
- AI role is **copilot / decision-support**, not autonomous executor.
- Scope is **Indian NSE/BSE only** — no crypto, forex, CFDs, or foreign exchanges.
- Daily max loss, per-trade max loss, and mandatory stop-loss must be part of every strategy recommendation.
- **CAS rule:** always flag if a position is likely to be held past 3:15 PM — the user should exit before the Closing Auction Session.
- **No silent substitutes for missing data.** If Dhan's Greeks/IV are unavailable, say so and ask. Do not back out Greeks locally.

---

## Keeping this file current

This file is the repo index — there is no README. Whenever any of these change, update **here** as well as in the source doc:

| What changed | Update |
|---|---|
| An MCP endpoint starts/stops working | `docs/mcp-usage-log.md` §1 + §2, then the "Current State" table above |
| Dhan Data API gets activated | `mcp-usage-log.md` §1/§2.1/§6, `docs/dhan_mcp.md`, "Current State" above, the capability map's *Actually usable* column |
| A trading session happens | append a row to `docs/mcp-usage-log.md` §4 |
| A new §8 chapter or structure is added | the "§8 map" table above + the §8 index block at the top of `strategy_ref_book.md` |
| A new file or folder is added to the repo | the Directory Layout above |
| Capital or execution venue moves | "Current State" above + the memory note on where capital sits |
