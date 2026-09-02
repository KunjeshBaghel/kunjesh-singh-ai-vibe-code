# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Role

You are an expert in options trading (F&O) in the Indian market (NSE/BSE). Your responsibilities in this project:

- **Review** existing trade setups and journal entries for quality and correctness.
- **Suggest** option strategies aligned with the current market view (use the five-view classification from `kb/Market_View.md §5`).
- **Create** complete strategy blueprints: legs, strikes, premiums, Greeks, risk/reward, and exit plan.
- **Co-pilot** on live trades — run the Pre-Trade Go/No-Go checklist (`kb/option_chain_n_greeks.md §7`), monitor intraday data points, and give go/no-go decisions with clear reasoning.

Always operate as decision-support. The user executes; you analyse and advise.

---

## 🔒 Precedence — read this before quoting any number

**Every number used in a live trading decision lives in [`TRADING_CONSTANTS.md`](TRADING_CONSTANTS.md) and nowhere else.**

```
TRADING_CONSTANTS.md  →  SKILL.md  →  CLAUDE.md  →  strategy_ref_book.md §8  →  everything else
```

If any file contradicts `TRADING_CONSTANTS.md`, **the constants file wins and the other file is a bug.**
Never copy a number out of it into another document — **link to the row instead.** A number that
exists in two places eventually exists in two versions, and the looser version always wins the
argument on a losing day. That is not hypothetical: on **01-Sep-2026** the daily cap said ₹10,500
and the sizing rule offered a "Standard ₹15–20K stop" eleven lines later. The loss was ₹15,564.

`strategy_ref_book.md` §1–§7 is textbook background and **never** governs a live decision.

Your working manual is **`TRADING_CONSTANTS.md` + `kb/kb1/strategy_ref_book.md` §8**. Start there, not at the top of the strategy book. Jump to the right doc with the ⚡ Fast Load table below.

---

## What This Repository Is

A personal knowledge base and trade journal for Indian stock market options trading on NSE and BSE. Everything is Markdown documentation. (`tools/market-snapshot/` currently holds **only a spec** — `docs/requirements.md`. There is no working fetcher; `src/` is empty.)

---

## ⚡ Fast Load — read only what the task needs

Do **not** read the whole `kb/` tree. Pick the row that matches the ask:

| If the user asks for… | Read, in this order |
|---|---|
| **★ Any number at all — a cap, a target, a time, a threshold, a lot size** | **[`TRADING_CONSTANTS.md`](TRADING_CONSTANTS.md). Only that file. Stop there.** |
| **Today's trade / "what should I trade" / "find best trade positions"** | **[`TRADING_CONSTANTS.md`](TRADING_CONSTANTS.md) §3–§7 FIRST** → the five gates below → `docs/mcp-usage-log.md` §1 (what data actually works) → today's `my-treads/<Month>/<DD-MM-YYYY>/*-market_view.md` → `my-treads/fii_dii_data_2026.md` → `kb/kb1/strategy_ref_book.md` **§8.5** (regime grid) → **§8.6** (the structure) → `kb/option_chain_n_greeks.md` §7 (Go/No-Go). **Always pull option chain + Go/No-Go for all three indexes: NIFTY50 (NSE, Tue expiry), BANKNIFTY (NSE, **monthly only**), and SENSEX (BSE, Thu expiry).** Compare all three before picking the best opportunity. Never analyse only one index when looking for trade positions. |
| **A strategy blueprint / which structure** | `strategy_ref_book.md` **§8.5 → §8.6 → §8.7 → §8.10 → §8.11**. §1–§7 is textbook reference only — §8 supersedes it wherever they disagree |
| **Market view / bias for tomorrow** | `kb/Market_View.md` (9 data points + five views + FII/DII scenarios) → `my-treads/fii_dii_data_2026.md` → prior day's `*-tread.md` |
| **Greeks, IV, option-chain columns** | `kb/option_chain_n_greeks.md` — but first check `docs/mcp-usage-log.md` §2.1: **IV and Greeks are currently unavailable from every MCP** |
| **Broker connection / login / "is X connected"** | `docs/broker-session-startup.md` (how) → `docs/mcp-usage-log.md` (what actually works) |
| **Rules, CAS, SEBI, expiry, lot sizes** | `kb/rules_n_regulations/rules_constrints.md` + `strategy_ref_book.md` §8.2–§8.4 |
| **In-trade: it's going against me** | **FIRST:** `references/followup.md` exit triggers. **On expiry day (0-DTE) the only two permitted actions are HOLD or EXIT — §8.9 is CLOSED.** Rolling or converting an ITM short on expiry costs more than the original stop, and *adding* is never an option (01-Sep: a 9th lot was sold six minutes after the exit trigger fired). §8.9's adjustment playbook applies **only** to 2+ DTE positions, which the feasibility gate rarely permits — so in practice §8.9 is almost never the answer. Then **§8.13** (kill switch) |
| **An abbreviation I don't know** | `kb/kb1/trading_jargon_acronyms.md` |
| **Charts / candles / indicators** | `kb/kb2-Candlestick/` · `kb/kb3-indicators/` |
| **Post-session write-up** | today's folder → write `*-learning.md`; append the session row to `docs/mcp-usage-log.md` §4 |

**The single most important file is `kb/kb1/strategy_ref_book.md` §8** (~2,300 lines). It is the live operating manual, written against the post-CAS / post-2024-SEBI regime. See "The §8 map" below.

---

### 🚦 The FIVE gates — run all of them, in order, BEFORE any chain analysis

Every one was earned the expensive way. Each takes about two minutes. **All thresholds below are
quoted from [`TRADING_CONSTANTS.md`](TRADING_CONSTANTS.md) — if they ever disagree, that file wins.**

**Gate 1 · Feasibility (§8.11.6) — is there a trade here at all?**

```text
□ Fetch the expiry list for all 3 indexes.  NEVER guess a date.
□ Sessions (not calendar days) to nearest expiry, per index.   Need ≤ 2.
□ MAX CREDIT = ₹3,500 ÷ (k − 1),  k = 1.6   →   REQUIRED CAPTURE = 60% of the credit
□ If required capture > realistic capture → no structure and no size fixes it. Report and stop.
```
> ⛔ **The "1% per session" target is DELETED** (`TRADING_CONSTANTS.md` §2). The target is **2–4% per
> month**. This gate now asks whether the *structure* can pay, not whether a daily quota can be met.
> When something is out of reach, **quote the capital at risk, not the shortfall** — a ratio ends the
> discussion; an adjective invites size creep.

**Gate 2 · Basis (§8.7.1a) — can you trust anything derived?**

```text
□ F = K + C − P at 3–4 near-ATM strikes.   Must agree within ~1 pt (else the chain is stale).
□ basis = F − Spot.        > 0.1% of spot → DISCARD the vendor delta band, use §8.7.3 on F.
□ Vendor sanity: one strike + one expiry = ONE IV.  CE IV ≠ PE IV → Greeks are broken.
```
> ⛔ **Dhan's Greeks are broken exactly this way** (spot-based, not forward-based) — see Current State.
> Parity is **arithmetic and permitted**; recomputing Δ/Γ/Θ/V locally is **not**.
> ★ Wherever the book asks for a delta, use **`credit ÷ width`** — as width narrows a vertical's price
> → Δ × W exactly. Model-free, vendor-free, unbreakable.

**Gate 3 · Kill switch (§8.13) — is this a trend day?**

```text
□ Opening-range break, sustained (not a wick)?   □ VWAP one-sided 45+ min?   □ OI confirming?
□ 2+ of 3 fired → no neutral structure.   1 of 3 → halve size, do NOT stop.
⛔ 0 of 3 means "not a trend day". It NEVER means "bullish" and is not a reason to HOLD a loser.
```

**Gate 4 · Go/No-Go (`kb/option_chain_n_greeks.md` §7) — point-scored.**

```text
□ SCORE = (2 × RED) + (1 × YELLOW).      ⛔ SCORE ≥ 4 → SIT OUT.
□ A row with no data is YELLOW, never green.  Blank ≠ clear.
□ Rows must use DISJOINT inputs — one VIX tick may colour one row only.
□ Automatic blockers are separate and do not count toward the score: no five-view
  classification · undefined max loss · no stop-loss defined before entry.
```
> The old "3+ distinct red/warning" wording is retired. See L358 for the full rule — the two must never diverge again.

**Gate 5 · Structure ↔ view ↔ participants — which SIDE do we sell?**

Gates 1–4 decide *whether*. This one decides *which side*, and it has cost money twice.

```text
□ Restate the five-view classification WITH A TIMESTAMP. A view >60 min old is stale; re-pull.
□ ⛔ Bull Put Spread is FORBIDDEN under Strongly/Slightly Bearish.
  ⛔ Bear Call Spread is FORBIDDEN under Strongly/Slightly Bullish.
  No override exists — not vol state, not skew, not §8.5.4 PE-first, not participants.
□ Extract SIX participant numbers, not one:
  FII and Pro × (net CE short, net PE short, net futures).  FII is checked FIRST.
□ EITHER participant > 80,000 net short calls → HARD CEILING → Bear Call Spread mandated.
  EITHER > 80,000 net short puts        → HARD FLOOR   → Bull Put Spread mandated.
  50,000–80,000 = strong preference.   < 50,000 = SILENCE, never a vote for the opposite side.
□ FII or Pro net LONG both CE and PE > 100,000 → long gamma → halve size or stand down.
  A long-gamma book re-hedges and stays long gamma; it does not become a seller because one leg paid.
□ Banned as directional evidence: morning spread P&L (a widened credit spread is a BETTER entry,
  not a broken thesis) · the last 3 candles · kill switch 0/3 · any rule that didn't fire.
```
> **01-Sep-2026 (−₹15,564):** Pro net short 1,09,003 calls = hard ceiling; a Bull Put Spread was recommended anyway.
> **02-Sep-2026:** view was Slightly Bearish and a **Bull Put Spread** was recommended. FII was net short **93,282 calls** — over the threshold — but the rule inspected only **Pro**, who were net *long* calls, so nothing fired. **The rule was checking the wrong participant.** Caught only because the user challenged it. Full detail: `.claude/skills/Index-Derivatives-tread/references/find-trade.md` Gate 5.

---

## Directory Layout

```
TRADING_CONSTANTS.md              ★★★ THE SINGLE SOURCE OF TRUTH. Every number used in a live
                                  decision — caps, target, k, c/W floor, times, lot sizes,
                                  thresholds, what is locked and its unlock key. Outranks every
                                  other file including this one. Never copy from it; link to it.

kb/                               Reference knowledge base
  Market_View.md                  9-data-point system + five-view classification + FII/DII scenarios
  open_interest.md                OI chart reading and Price vs OI matrix
  option_chain_n_greeks.md        Option chain column guide + Greeks deep-dive + Pre-Trade Go/No-Go checklist (§7)
  rules_n_regulations/
    rules_constrints.md           CAS (3:15 PM) rule + SEBI regulations affecting positions
  kb1/
    strategy_ref_book.md          ★★ 3,587 lines. §1–§7 = textbook catalogue.
                                  §8 = THE LIVE OPERATING MANUAL (~2,300 lines) — see "The §8 map"
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
  fii-dii/
    fii_dii.py                    ★ Fetches NSE participant-wise F&O OI (T-1) from
                                  archives.nseindia.com/content/nsccl/fao_participant_vol_DDMMYYYY.csv
                                  No auth needed. SOLE source of Gate 5's six numbers.
                                  ⚠️ MUST BE COMMITTED — currently untracked. Gate 5 cannot run
                                  without it, and one `git clean` deletes it.
  market-snapshot/
    docs/requirements.md          Spec ONLY — the fetcher was never built
    src/                          Empty. There is no fetch.py

my-treads/                        Personal trade journals (one folder per trading day)
  fii_dii_data_2026.md            ★ Persistent tracker — FII/DII data across all 2026 sessions
  July-2026/                      13, 14, 20, 21, 22, 23, 24, 28
  August-2026/                    03, 04, 05, 10, 17, 20, 24, 26, 27, 28
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
| **8.5** | **Volatility state (RICH / NORMAL / CHEAP / HOSTILE) + the 5-view × 4-state regime grid + §8.5.4 PE-first principle** | **First stop every session** — it decides whether to trade at all. §8.5.4: default to PE selling (puts are expensive due to skew); override to CE selling only for explicitly bearish views with call OI wall visible |
| **8.6** | **The 14 structures**, each with full worked Indian numbers: 8.6.1–8.6.7 core; 8.6.8 skew-aware condor; 8.6.9 positional 25–40 DTE condor; 8.6.10 0-DTE hedged fly under CAS; 8.6.11 IV-crush event harvest; 8.6.12 double calendar + the Feb-2025 margin trap; 8.6.13 the ladder (a repair, never an entry); 8.6.14 the rolling wing bank | Once the grid says "trade" |
| 8.7 | Strike selection — delta band · expected move · **the straddle rule (works with zero Greeks)** · OI walls. **§8.7.1a: the forward-basis check — `F = K + C − P`; if basis > 0.1% of spot, discard the vendor delta band. One strike + one expiry = ONE IV; CE IV ≠ PE IV means the Greeks are broken** | Picking strikes — **§8.7.1a runs before any delta is quoted** |
| 8.8 | Entry timing — intraday clock (9:20–9:45 primary) + weekly calendar | Timing the fill |
| **8.9** | **Adjustment playbook** — shift the untested side, roll, hedge up, convert, cut; the 4-question martingale test; the adjustment budget; full decision tree | Position is under pressure |
| 8.10 | Stop-loss architecture — combined-premium SL is the default; per-leg SL un-hedges you; why SL-M on options is a trap. **§8.10.5: an abort condition must match the structure's dominant Greek — a VIX-based abort on a directional credit vertical exits winners** | Before entry, always |
| **8.11** | ⚠️ **Sizing is SUPERSEDED by [`TRADING_CONSTANTS.md`](TRADING_CONSTANTS.md) §4 — two caps, the smaller wins.** §8.11's own single-cap formula bounds the loss *at the stop* and never the payoff, which is how 01-Sep's ₹12,546/lot structure passed. §8.11.5 is the honest expectancy check (₹1,274/session). **§8.11.6: the feasibility gate — `MAX CREDIT = ₹3,500 ÷ (k−1)`, k=1.6 → required capture 60%** (+ estimate capture with the structure's **dominant Greek** — the DTE table is a *theta* table and theta stops dominating past ~10 DTE). **§8.11.7: the noise-floor test — `(k−1)×credit` vs the SPREAD's own 30-min INTRA-BAR swing, opening gap bar excluded; under 1.5× the stop is inside one candle → no trade at any size** | **§8.11.6 at 9:15, before chain analysis** · **§8.11.7 on every candidate before pricing it further** |
| 8.12 | 14 named patterns (Monday Gap Fade, Expiry-Day Pin, Range-Compression Squeeze, …). **§8.12.6a: the compression "Trade Nothing" veto applies to NEUTRAL premium only — a one-sided credit vertical leaning the way the market leans is paid by the break** | Pattern recognition |
| **8.13** | **Trend-day kill switch** — 3 markers, 0-1-2-3 escalation, fixed check times. **§8.13.3: every check re-pulls spot/VWAP · VIX · ATM straddle · OI *and* `oi_day_high` at the short strikes and walls. OI is not optional — compare it to its day high, not to the morning print** | Intraday, at 9:45 / 10:30 / 11:30 / 1:30 |
| 8.14 | Six ways sellers die, with real Indian gap dates | Sanity check |
| 8.15 | Metrics that matter — and why win rate is a vanity metric. **§8.15.4: score at the *mandated exit time* (§8.3), never a mid-session snapshot, and always report MAE / exit-mark / MFE at max permitted size — including candidates you rejected in analysis and never wrote up** | Journalling · scoring a no-trade day |
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
Step 1 → Kite (Zerodha)  → "Login to Zerodha" → auth link → 2FA → verify with get_ltp NIFTY + VIX
Step 2 → Kotak Neo       → "Login to Kotak Neo" (UCC = V6PZT) → QR scan → "DONE" → get_limits
Step 3 → Dhan            → call `mcp__dhan__login` → browser URL → Dhan login → paste callback URL if needed
                           If token expired → call `mcp__dhan__login` AGAIN (fresh consentId)
                           If redirect shows "Authentication completed" → auto-bound ✅
                           If not auto-bound → paste full callback URL → call `mcp__dhan__complete_login` with tokenId
                           Verify with: `mcp__dhan__market_data_agent_tool` action=`expirylist`
Step 4 → FII/DII data    → run: ! python3 tools/fii-dii/fii_dii.py   (fetches T-1 from NSE archive, no login)
                           Append output to my-treads/fii_dii_data_2026.md
Step 5 → Record the outcome in docs/mcp-usage-log.md §4, then proceed
```

**Verify each MCP with a call that exercises the capability you actually need** — a successful login proves nothing about the data endpoints.

Three gotchas that have already cost a session:
- **Dhan `invalid_client` → call `mcp__dhan__login` again (ONCE).** ⚠️ There is **no `mcp__dhan__authenticate` tool** — the Dhan MCP exposes `login`, `complete_login` and the agent tools, nothing else. Earlier versions of this file and of SKILL.md named a tool that does not exist, in the *first step of every session*. The server generates a new OAuth client_id per call, so a second call is safe **when the URL has already failed**; do NOT retry while the user is mid-login on a valid URL. **If the second attempt fails, stop and switch to REST** — do not spend market hours on consent URLs.
- **Never verify Dhan with `funds`/`fundlimit`** — they return data even when unauthenticated. Use `mcp__dhan__market_data_agent_tool` action=`expirylist`.
- **Kite missing `NFO`/`BFO` blocks orders only, not data.** Don't abandon Kite as a data source over it.

Flag any red MCP before analysing. If IV/Greeks are needed and Dhan is down, **say so and ask** — see Current State below.

---

## Current State / Known Blockers

*Last verified: 31-Aug-2026. Full detail + evidence in `docs/mcp-usage-log.md`.*

| Fact | Consequence |
|---|---|
| ⛔ **Dhan's Greeks and IV are computed off SPOT, not the FORWARD** (found 28-Aug-2026, `mcp-usage-log.md` §2.5). Proof: same strike + same expiry returns CE IV 11.47 vs PE IV 6.41 — arithmetically impossible. Deep-ITM legs return IV/Δ/Θ = 0. | **We have NO trustworthy Greeks source.** The fields are populated and plausible, so this fails silently. Dhan's Δ=0.50 sits ~85 pts below the true ATM-forward on NIFTY. **Run §8.7.1a before quoting any delta; fall back to §8.7.3 centred on the parity forward `F`.** |
| **Near-term basis is large and tenor-dependent** — 28-Aug: NIFTY +82 (4d), SENSEX +283 (6d), BANKNIFTY +382 (32d). | **The true ATM is the forward, not spot** — often more than one strike away. Recheck each session; never reuse yesterday's basis. **GIFT Nifty is a futures price — never compare it to spot.** |
| ⚠️ **Dhan MCP OAuth binding REGRESSED (02-Sep-2026)** — failed **twice in one morning** (07:17, 09:27). `login` issues a fresh consentId, the user completes consent, `complete_login` replies `token_id already consumed for this session`, and every agent tool still returns `API Error: Unauthorized`. A second fresh consentId did not fix it. **`"token already consumed"` is NOT proof of binding.** | **Try the MCP once, then go straight to REST.** Do not spend market hours on consent URLs. **Dhan REST (`access-token` + `client-id` headers) is the reliable path** and pulled all 3 full chains on 02-Sep. Verify either path with `expirylist`, never `funds`. |
| Dhan Data API subscription **is** active (20-Aug-2026); token in `.broker_creds` as `DHAN_ACCESS_TOKEN`. **Prices, OI, `previous_oi` and bid/ask are trustworthy.** | Dhan is the best full-chain source. **Only its derived analytics (IV/Greeks) are broken.** |
| **Do not compute Greeks locally.** The user explicitly rejected a local Black-Scholes fallback. | State the gap and ask — never silently substitute. **Permitted:** `F = K + C − P` (put-call parity) and the ATM-forward straddle relation — these are arithmetic, not models. **Not permitted:** solving for Δ/Γ/Θ/V, or presenting a derived number as a vendor number. |
| **Kite (Zerodha) has ₹500 and no `NFO`/`BFO`** in `get_profile.exchanges`. | Kite = **data source only**. Cannot execute. Data (spot, VIX, OI, `oi_day_high/low`, 5-level depth, historicals) is fully working. |
| **Trading capital is ₹7,02,275 in Kotak Neo**, and the Kotak MCP is **read-only by design** (no order tools). | **All execution is manual in the Kotak Neo mobile app.** Claude gives structure, strikes, sizing, levels; the user places the orders. |
| Whether **F&O is enabled on Kotak Neo** is unknown — `get_limits` doesn't expose segment entitlements. | Open question for the user. |

**Effective architecture today:** Kite = spot/VIX/OI/depth/historicals/futures/option minute-bars · **Dhan MCP** = full option chain prices + OI + `previous_oi` + bid/ask (REST fallback also available) · **Greeks/IV = none trustworthy → §8.7.3 straddle rule on the parity forward** · Kotak = margin + research · Claude = analysis · **Kotak app = manual execution**.

**Open items** (mirrored in `docs/mcp-usage-log.md` §6):
1. 🔴 Raise the **spot-vs-forward Greeks defect** with Dhan support. Delta-band strike selection is re-blocked until fixed.
2. 🔴 **Dhan MCP OAuth binding — REOPENED 02-Sep-2026.** Fixed 31-Aug, broken again by 02-Sep (2 failures in one morning). Raise with Dhan alongside item 1. Workaround: REST.
3. Confirm F&O entitlement on Kotak Neo.
4. Decide the permanent execution venue: fund + activate F&O on Zerodha, fund Dhan, or accept manual Kotak execution.

---

## Key Domain Concepts

**Indian-specific symbols:** options use `CE` (Call European) and `PE` (Put European). All index options (NIFTY, BANKNIFTY, FINNIFTY, SENSEX) are **cash-settled**; individual stock options are **physically settled** at expiry.

**Expiry schedule:**

| Index | Exchange | Expiry Day |
|-------|----------|------------|
| NIFTY 50 | NSE | Every Tuesday |
| SENSEX | BSE | Every Thursday |
| **BANKNIFTY** | NSE | ⚠️ **MONTHLY ONLY — no weekly** (last Tuesday). Post-2024-SEBI. |

⚠️ **Always fetch the expiry list; never assume or infer a date.** A guessed date returns *Invalid Expiry Date* (Dhan) and, worse, a *plausible* wrong one silently prices the wrong contract.

**★ COUNTING CONVENTION — canonical, used by every gate. Count trading sessions, not calendar days:**

```
sessions_to_expiry = trading sessions remaining INCLUDING TODAY, up to and including expiry.
    Expiry day itself  →  1     (= "0-DTE")
    Expiry eve         →  2     (= "1-DTE")
Gate 1 blocks when sessions_to_expiry ≥ 3.
Holidays: derive from gaps in the fetched expiry list + the NSE calendar. If a day's status is
uncertain, COUNT it as a trading day — the conservative direction.
```
> This convention was previously implicit and differed by one between files, which flips the gate in both directions. On Fri 28-Aug-2026: NIFTY 01-Sep (**2**), SENSEX 03-Sep (**4**), BANKNIFTY 29-Sep (**22**) — no 0-DTE instrument existed anywhere, which alone decided the session.

**BANKNIFTY is monthly-only**, so on all but the final ~2 sessions of the expiry month it fails Gate 1 by construction. Screen it, state `BANKNIFTY: N sessions → Gate 1 ⛔, excluded` in one line, and do not price it. ⛔ **It is never the fallback when NIFTY and SENSEX are both blocked** — two blocked indexes plus a structurally blocked third is a **no-trade day**, not a BANKNIFTY day.

Monthly contracts expire the last Tuesday (NSE) / last Thursday (BSE) of the month. A holiday shifts expiry to the previous trading day.

**Market view timing:** form view **after 3:30 PM IST** from prior-day derivatives data; recheck **before 9:15 AM IST** on the trading day. Intraday: re-check OI change every **30 minutes** — EOD views often shift in the first 45 minutes.

**Five market views (`kb/Market_View.md §5`):** Strongly Bullish · Slightly Bullish · Sideways · Slightly Bearish · Strongly Bearish. Always classify to one of these five before suggesting any strategy.

**CAS rule (`kb/rules_n_regulations/rules_constrints.md`):** From 3:15 PM onward the market enters the Closing Auction Session — premium decay stalls and positions become risky for retail. Exit or reduce exposure before 3:15 PM.

**FII/DII participant-wise OI (`kb/Market_View.md §4`):**
- FII = primary trend setter; Client (retail) = contrarian indicator.
- Six scenarios map FII+Client combinations to a bias (Classic Bullish Rally, Distribution/Trap Phase, Institutional Consensus, Option Writer's Trap, Range-Bound, Volatility/Reversal Trap).
- Always look at **Net Change** (today) and validate against **Net OI** (cumulative) over **3+ consecutive days** before calling a regime.
- Persistent FII/DII data: `my-treads/fii_dii_data_2026.md`.

**Pre-Trade Go/No-Go checklist (`kb/option_chain_n_greeks.md §7`):** Before any trade entry, run VIX level/direction, gap vs GIFT, OI-wall integrity at the intended short strike, FII 3-day regime, and PCR slope.

- **Scoring: RED = 2 points, YELLOW = 1 point. Total ≥ 4 → sit out.** (So 2 reds, or 1 red + 2 yellows, or 4 yellows, all block.) The old "3+ distinct red/warning" wording is retired — it counted yellows in one file and not another, and three of the five rows shared inputs, so a single VIX tick manufactured three "distinct" reds.
- **Rows must score from disjoint inputs.** If one observation would colour two rows, score it once in the lower-numbered row and mark the other `n/a — same input as row N`.
- **A row with no data is YELLOW, never green.** Blank ≠ clear.
- **Automatic blockers** — reject immediately, outside the score: no five-view classification · undefined max loss · no live SL order · Gate 5's table not written to `tread.md`.

**Safe trade filter — REVISED for the current data reality.** Greeks and IV are **unavailable** (`TRADING_CONSTANTS.md` §14), so the old "Delta/POP · OI · IV/IVP" screen is two-thirds unsourceable. Screen on:
1. **`credit ÷ width`** — the arithmetic delta proxy. Floor 15%, 20% preferred.
2. Distance from the **parity forward `F`** in expected-move units (§8.7.3 straddle rule).
3. **OI and OI erosion** at the candidate short strike, measured against `oi_day_high`.
4. **VIX level and direction** as the vol-state proxy.

⛔ Do **not** substitute Dhan's populated Δ or IV for the missing inputs — that is exactly the "a populated field is not a verified field" failure. Never use `POP = 1 − |Delta|`.

**Risk parameters — ★ canonical values live in [`TRADING_CONSTANTS.md`](TRADING_CONSTANTS.md) §1–§4. Summary only, do not quote from here:**

| | |
|---|---|
| Capital | ₹7,02,275 (Kotak Neo) · manual execution |
| Target | **2–4% per month.** ⛔ The "~1% per session" target is **DELETED** — see `TRADING_CONSTANTS.md` §2 |
| **Structural max loss, per structure** | **₹10,500 (1.5%)** — `(width − credit) × lot_size × lots`. The only cap that does not depend on a human pressing a button. |
| **Planned stop, per structure** | **₹3,500 (0.5%)** |
| Daily / weekly / monthly | ₹3,500 day-over · **₹10,500 day-over + mandatory next-session no-trade** · ₹21,000 · ₹28,000 |
| **Structures per calendar day** | **ONE.** Not one at a time — one per day. Closing at 10:30 does not buy a second slot. |
| Margin | Never a sizing input. The ₹10,500 structural cap binds long before margin does. |

**Sizing — compute both caps, the smaller wins** (`TRADING_CONSTANTS.md` §4):

```
Cap A  lots_A = floor( 10,500 ÷ ((width − credit) × lot_size) )          ← structural
Cap B  lots_B = floor(  3,500 ÷ ((k − 1) × credit × lot_size) )   k=1.6  ← planned stop
       LOTS   = min(lots_A, lots_B)
       ⛔ LOTS < 2 → narrow the width and recompute. Still < 2 → NO TRADE.
```

**Width is chosen AFTER the cap, never before.** Present in this order, always:
**max profit → breakeven → structural max loss → planned stop → lots.** Never quote a lot count before the max loss.

> **Why both caps exist (01-Sep-2026, −₹15,564):** the structure was NIFTY 200-wide at ~7 pts credit → `(200 − 6.99) × 65 = ₹12,546` of max loss **per lot**. Cap A gives `floor(10,500 ÷ 12,546) = 0` — the structure was **banned outright, not downsized**. The rule in force that day capped only the *stop*, never the payoff, so 8 lots looked compliant. A cap that binds only when a human executes on time is not a cap.
>
> **And why the 31-Aug "size by conviction" rewrite is retired:** it was inferred from one profitable session (5 lots → ₹3,331; "20 lots would have made ₹12,500"). The very next session, the same latitude produced −₹15,564. n=1 in the winning direction is not evidence.

**There is no obligation to trade.** §8.11.5 records the honest expectancy: **≈₹1,274 (0.20%) per traded session**. ~75% of sessions are correctly no-trades. If the setup is unclear, the stop is undefined, or `LOTS < 2`, do not trade.

**For the first three months the target is a violation count of zero, not a rupee number.**

**Three distinct reasons to stand down — say which one, they generalise differently:**

| Reason | Diagnosis | What changes it |
|---|---|---|
| **Too dangerous** | Kill switch fires, 3+ Go/No-Go reds, compression squeeze, gap risk | Wait for the **regime** to change (17-Aug, 27-Aug-2026) |
| **Too small** | Day is clean but no permitted size reaches the target — §8.11.6 | Wait for the **calendar** to change (24-Aug, 28-Aug-2026) |
| **Too thin** | Credit so small the stop sits inside one candle — §8.11.7. `(k−1)×credit` < 1.5× the **SPREAD's** 30-min intra-bar swing | Pick a **different structure**: closer strikes or wider width. More size makes it worse, not better |

Conflating them buries the fixable cause. On 28-Aug-2026 the kill switch was 0/3, Go/No-Go 0 red, VRP positive and VIX falling — a **clean** day on which the then-target still needed 20–33 lots (**14.9–24.7% of capital**). **When something is out of reach, quote the capital at risk, not the shortfall.** A ratio ends the discussion; an adjective invites size creep.

**Timing — ★ canonical in [`TRADING_CONSTANTS.md`](TRADING_CONSTANTS.md) §7. One number each, no "target vs hard":**

| | |
|---|---|
| **Entry window** | **9:30 – 11:15.** ⛔ No new position after 11:15, ever. |
| **Midday time stop** | **12:30** — capture < 25% → close at market |
| **NIFTY / BANKNIFTY hard flat** | **2:30 PM** |
| **SENSEX hard flat** | **2:15 PM** |
| **CAS** | 3:15 PM — nothing ever survives into it |

> **The old two-tier "target 2:30 / hard 3:00" scheme is DELETED.** Publishing a later time guarantees the later time gets used on the day the position is red at 2:30 — the only day it matters. One time, one phone alarm. *(20-Jul-2026 exited ~3:16 PM — inside CAS — and it was never flagged. 01-Sep exited 14:51 against a 2:30 plan.)*

> ⚠️ **Pointer correction:** exit times were previously cited as `strategy_ref_book.md §8.3`. **§8.3 is the CAS/cost sheet and contains no times.** The times live in `TRADING_CONSTANTS.md` §7 and nowhere else.

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
| Full option chain (price/OI/bid-ask) | ✅ **REST only** | ❌ | ❌ | **Dhan via curl** |
| Greeks (Δ Γ Θ V) | ⚠️ populated but **computed off spot** | ❌ | ❌ | ⛔ **none** → §8.7.3 straddle rule |
| Implied Volatility | ⚠️ **CE IV ≠ PE IV**, unusable | ❌ | ❌ | ⛔ **none** → VIX + ATM-fwd straddle |
| Forward / basis | ✅ parity from chain | ✅ futures via `get_quotes` | ⬜ | **parity, cross-checked vs Kite** |
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
- **No silent substitutes for missing data.** If Dhan's Greeks/IV are unavailable **or unreliable**, say so and ask. Do not back out Greeks locally.
  - ✅ **Permitted (arithmetic, not models):** put-call parity `F = K + C − P`; the ATM-forward straddle relation `≈ 0.7979 × F × σ√T`; HV from Kite candles; §8.7.3 straddle-rule strikes.
  - ⛔ **Not permitted:** solving Black-Scholes for Δ / Γ / Θ / V, or presenting any derived figure as if it came from the vendor.
- **A populated field is not a verified field.** Dhan's Greeks returned plausible-but-wrong numbers for four sessions before anyone checked. Verify with a call that exercises the capability **and** a sanity check on the value (§8.7.1a: one strike + one expiry = one IV).

---

## Keeping this file current

This file is the repo index — there is no README. Whenever any of these change, update **here** as well as in the source doc:

| What changed | Update |
|---|---|
| An MCP endpoint starts/stops working | `docs/mcp-usage-log.md` §1 + §2, then the "Current State" table above |
| Dhan Data API gets activated | `mcp-usage-log.md` §1/§2.1/§6, `docs/dhan_mcp.md`, "Current State" above, the capability map's *Actually usable* column |
| A trading session happens | append a row to `docs/mcp-usage-log.md` §4 |
| A new §8 chapter or structure is added | the "§8 map" table above + the §8 index block at the top of `strategy_ref_book.md` |
| **A vendor's data is found to be wrong (not just missing)** | `mcp-usage-log.md` §2 (new root-cause subsection) + §1 matrix + §7 substitutes, then "Current State" above + the capability map. **Downgrade the ✅ — a populated field is not a verified field.** |
| **A session earns a KB amendment** | the target §/filter, its parent index block, the `§4` session row in `mcp-usage-log.md`, and the day's `*-learning.md`. If it changes the *routing*, also the ⚡ Fast Load table and the gates block above. |
| A new file or folder is added to the repo | the Directory Layout above |
| Capital or execution venue moves | "Current State" above + the memory note on where capital sits |
