# analyse-today — Morning Setup & Market View

Full morning workflow. Takes ~15 minutes. Do every step; do not skip data points.

---

## Step 1: Create today's folder and files

```
Date format: DD-MM-YYYY  e.g. 31-08-2026
Month folder: August-2026  (derive from date)

Create:
  my-treads/<Month-YYYY>/<DD-MM-YYYY>/
    <DD-MM-YYYY>-market_view.md   ← write market view here
    <DD-MM-YYYY>-tread.md         ← append session log here (start empty)
    <DD-MM-YYYY>-learning.md      ← post-session lessons (start empty)
```

Copy the structure from `my-treads/DD-MM-YYYY/` (blank template) if it exists, otherwise create from scratch.

Write the header to `tread.md` immediately:
```markdown
# <DD-MM-YYYY> — Tread Log
## <HH:MM> — Session start: broker connection check
| Broker | Result | Verified with |
```

---

## Step 2: Verify all 3 brokers (see SKILL.md Universal Rules §1)

Run in parallel:
- `mcp__kite__get_ltp` → NIFTY + VIX
- `mcp__kotak-neo__get_limits` (sessionid required)
- `mcp__dhan__market_data_agent_tool` action=`expirylist` NIFTY

Record results in `tread.md`. If any broker fails, flag it and stop.

---

## Step 3: Fetch expiry list — all 3 indexes

Run in parallel:
```
NIFTY:    UnderlyingScrip=13, UnderlyingSeg=IDX_I
BANKNIFTY: UnderlyingScrip=25, UnderlyingSeg=IDX_I
SENSEX:   UnderlyingScrip=51, UnderlyingSeg=IDX_I
```

For each index: extract nearest expiry date and count **trading sessions** (not calendar days).

---

## Step 4: Fetch live market data (all in parallel)

From **Kite**:
```
mcp__kite__get_ltp: ["NSE:NIFTY 50", "NSE:NIFTY BANK", "BSE:SENSEX", "NSE:INDIA VIX",
                     "NSE:NIFTY IT", "NSE:NIFTY FMCG", "NSE:NIFTY AUTO", "NSE:NIFTY METAL"]
```
Sectoral indices confirm breadth — if NIFTY looks bullish but IT/BANK/heavyweights are weak, treat the move as low conviction.

From **Kite historical** (for PDC / PDH / PDL — last 5 days daily candle):
```
instrument_token=256265 (NIFTY), interval=day, from=5 trading days ago, to=yesterday
instrument_token=265   (SENSEX), same range
```

From **Kotak**:
```
mcp__kotak-neo__get_limits → available margin
```

From **Yahoo Finance + Trendlyne via WebFetch** (run in parallel with Kite calls):
```
WebFetch: https://finance.yahoo.com/markets/world-indices/
  → US indices (S&P 500, Dow, Nasdaq, US VIX), US futures, Asian (Nikkei, Hang Seng, Shanghai), European (FTSE, DAX)
WebFetch: https://finance.yahoo.com/quote/CL%3DF/
  → WTI Crude oil price and % change
WebFetch: https://finance.yahoo.com/quote/DX-Y.NYB/
  → DXY (US Dollar Index)
WebFetch: https://trendlyne.com/macro-data/fii-dii/latest/mf-pastmonth/
  → FII/DII cash market net buy/sell in ₹Cr (T-1 data, most recent date shown)
```
**MSCI rebalancing context (important):** FII cash selling on MSCI rebalancing days (typically last trading day of month) is mechanical, not bearish conviction. Check if the date is MSCI-related before interpreting FII cash sells as bearish signals. Evidence: on MSCI days FII will sell cash but simultaneously write puts (bullish F&O) — these contradict only if you miss the MSCI context.

**Proven to work (01-Sep-2026):** WebFetch on Yahoo Finance pages returns all global indices, prices, and % changes in a single call — no login required. Returns closed-market prices for US/European when called pre-market IST.

**GIFT Nifty:** Not available via WebFetch or yfinance. Use opening 15-min NIFTY candle as proxy. Remember: GIFT Nifty is a futures price — never compare to NIFTY spot.

Collect:
- NIFTY spot, BANKNIFTY spot, SENSEX spot, India VIX
- PDC / PDH / PDL (from Kite historical)
- US close: S&P 500, Dow, Nasdaq, US VIX
- Asian open: Nikkei, Hang Seng, Shanghai
- Commodities: WTI Crude, DXY
- Opening gap vs PDC (after market opens)

---

## Step 5: Fetch FII/DII data (NO X.com needed — use NSE archive directly)

Run the Python script to get T-1 data from NSE's official public archive. No login required.

```bash
! python3 tools/fii-dii/fii_dii.py          # auto-fetches yesterday (T-1)
# OR for a specific date:
! python3 tools/fii-dii/fii_dii.py 2026-09-01
```

**Output:** Two tables — (1) detailed participant-wise F&O activity (FII / Client / Pro / DII × Futures / CE / PE) and (2) FII 5-day activity trend with overall By-Count and By-Sentiment signals.

**Source:** `https://archives.nseindia.com/content/nsccl/fao_participant_vol_DDMMYYYY.csv`
- ✅ Official NSE data, no auth, free, exact match to @Fii_Dii_Data / BluechipAlgos X.com posts
- ⏳ Today's data available after ~4 PM IST — so pre-market always fetches T-1
- ⚠️ Expiry days (Tue=NIFTY, Thu=SENSEX) inflate raw trading volume ~8×; treat T-4 cautiously if it lands on an expiry

**Formula (5-day FII activity score):**
```
FII_Score = (Call Long − Call Short) − (Put Long − Put Short) + (Fut Long − Fut Short)
          = Net Call Buying + Net Put Selling + Net Futures Buying
Positive = Bullish  |  Negative = Bearish
```

**After fetching:**
- Append the output to `my-treads/fii_dii_data_2026.md` (use 31/08/2026 entry as format template)
- Read the last 3 daily entries to assess the 3-day trend (needed for FII regime validation per §Market_View.md §4)
- Classify the regime: Distribution/Trap · Classic Rally · Institutional Consensus · Option Writer's Trap · Range-Bound · Volatility/Reversal Trap

---

## Step 6: Fetch option chain basics (for preliminary view)

For the nearest expiry on each index, fetch the chain from Dhan and pull:
- ATM straddle premium (CE + PE at nearest ATM strike)
- PCR: total PE OI ÷ total CE OI in near-money range
- Max pain: strike with lowest aggregate buyer loss
- Top 3 CE OI strikes (call walls = resistance)
- Top 3 PE OI strikes (put walls = support)

**Forward basis check (§8.7.1a):** Run F = K + CE - PE at 3 strikes. If basis > 0.1% of spot → note the true ATM-forward.

---

## Step 7: Classify the market (five-view + participant synthesis)

**7a. Build the participant table — MANDATORY every session.**

For each of the 4 participants (FII, Pro, Client, DII), read from the `fii_dii.py` output:

| Participant | Index Fut Net | CE Net | PE Net | Reading | Implication |
|---|---|---|---|---|---|
| FII | +/- | +/- | +/- | … | … |
| **Pro** | +/- | +/- | +/- | … | … |
| Client | +/- | +/- | +/- | … | … |
| DII | +/- | +/- | +/- | … | … |

**Interpretation rules per participant:**

**FII (trend-setter — most important):**
- Short Futures + Short Calls + Long Puts = Strongly Bearish (Distribution/Trap)
- Long Futures + Short Puts + Long Calls = Strongly Bullish (Classic Rally)
- Short Futures + Short Puts = Range-biased / Mixed
- Short Futures + Long Calls + Short Puts = Mixed (hedge + writing puts) → Range-Bound

**Pro (dominant option writer — defines range ceiling/floor):**
- Long Futures + **Short Calls** (large) + small Long Puts = **Covered Call = CEILING defined** at short call strikes. Market expected to stay BELOW those strikes. Pro desks hold this through expiry — they resist rallies past their short calls.
- Short Futures + **Short Puts** (large) + small Long Calls = **Put Write = FLOOR defined** at short put strikes. Market expected to stay ABOVE.
- Both CE + PE Short (large) = **Iron Condor / Range** — strongest range signal. Pro earns from both sides staying within range.
- Both CE + PE Long (large) = **Long Straddle = expecting big move** — volatility event expected. Do NOT sell spreads on this day.

**Client (contrarian indicator — fade their extreme positions):**
- Very Bullish (buying calls, selling puts, long futures) → slight bearish signal
- Very Bearish (buying puts, selling calls, short futures) → slight bullish signal
- Neutral / mixed → no contrarian signal

**DII:** Generally small in index F&O. Only flag if exceptionally large divergence from FII.

---

### 7a-2. The Gate 5 handoff — write these six numbers verbatim into `market_view.md`

`find-trade`'s **Gate 5** consumes exactly six numbers. If they are not written here in this form, Gate 5 has to re-derive them mid-session — and on **02-Sep-2026 it silently didn't**, checked only Pro, missed FII's 93,282 net short calls, and a Bull Put Spread was recommended under a bearish view. **The gate cannot be skipped by omission if the numbers are already on the page.**

```
GATE 5 INPUTS (T-1 = <date>)
  FII_net_CE_short = |CE Short| − |CE Long| = <n>      FII_net_PE_short = <n>      FII_net_FUT = <n>
  Pro_net_CE_short = |CE Short| − |CE Long| = <n>      Pro_net_PE_short = <n>      Pro_net_FUT = <n>

  CEILING?  either net_CE_short > 80,000  → YES/NO   (which participant, what value)
  FLOOR?    either net_PE_short > 80,000  → YES/NO   (which participant, what value)
  LONG GAMMA? either net LONG both CE and PE > 100,000 → YES/NO
  → Structures MANDATED: <…>      Structures FORBIDDEN: <…>
```

Rules, restated so they travel with the numbers:

- **FII is read first.** CLAUDE.md: *"FII = primary trend setter."* Pro is the second read, not the only one.
- A value **below 50,000 is SILENCE, not permission for the opposite side.** It hands the decision back to the §8.5 grid; it does not vote.
- Both a ceiling and a floor firing = short strangle = **range**; the larger magnitude breaks the tie, but the winner must still be permitted by the view.
- **Long gamma (net long both legs > 100,000) → halve size or stand down.** Do not argue that an early move "already delivered" so the signal inverted — a long-gamma book re-hedges and stays long gamma.

Sign convention matters: Pro net **long** 168,089 calls means `Pro_net_CE_short = −168,089`, which is *not* a ceiling and *not* a floor. Write the negative number; do not write "n/a".

---

**7b. Classify the FII regime (6 scenarios from `kb/Market_View.md §4`):**
1. Classic Bullish Rally — FII buying futures + selling puts
2. Distribution/Trap — FII selling futures/calls while retail buys
3. Institutional Consensus — FII + Pro aligned (same direction)
4. Option Writer's Trap — FII short + writing both CE+PE (expecting range)
5. Range-Bound — FII mixed + Pro writing both sides
6. Volatility/Reversal Trap — Pro buying both CE+PE (long straddle)

**7c. Cross-check all dimensions:**

| Dimension | Data | Signal |
|---|---|---|
| Price vs OI matrix | Price change + OI change | Long Buildup / Short Covering / Short Buildup / Long Unwinding |
| FII regime | From participant table | One of 6 scenarios |
| Pro desk | From participant table | Defines ceiling (short calls) or floor (short puts) or range (both) |
| Client | From participant table | Contrarian read |
| PCR level | From Dhan chain | >1.30 bullish · 1.00–1.30 mildly bullish · 0.80–1.00 mildly bearish · <0.80 bearish. **No gaps — every value classifies.** |
| VIX direction | India VIX | Rising = vega headwind · falling = seller tailwind |
| Global cues | Yahoo Finance | US/Asian/European direction · crude · DXY |

**7d. Classify to exactly one of:** Strongly Bullish · Slightly Bullish · Sideways · Slightly Bearish · Strongly Bearish

**Conviction:** High (4+ dimensions agree) · Medium (2–3 agree) · Low (<2 agree or conflicting)

**Critical rule:** Always state WHICH participants support the thesis and WHICH oppose it. A classification without participant backing is a guess, not a view.

**Stamp the classification with the time it was made** — `Classification: <view> · Conviction: <level> · as of HH:MM`. Gate 5 must restate it before naming a structure, and a classification older than 60 minutes must be re-derived rather than reused. On 02-Sep the regime flipped twice inside one hour (kill switch 1/3 at 09:30 → 0/3 at 10:25 → bounce failing by 10:56); an unstamped view invites reuse of a stale one.

---

## Step 8: Write market_view.md

```markdown
# <DD-MM-YYYY> Market View

**Data Points Summary**
* NIFTY: <price> (PDC: X | PDH: X | PDL: X)
* BANKNIFTY: <price>
* SENSEX: <price> (PDC: X | PDH: X | PDL: X)
* VIX: <level> (<direction> — rising=headwind / falling=tailwind)
* Sectoral: IT <X> · BANK <X> · FMCG <X> · AUTO <X> · METAL <X>
* PCR (near-money range): <value> (>1.30 bullish · 1.00–1.30 mildly bullish · 0.80–1.00 mildly bearish · <0.80 bearish)
* FII/DII (T-1 = <date>, NSE official CSV):
  * FII: Fut <net> · CE <net> · PE <net> → <one-word stance>
  * Pro: Fut <net> · CE <net> · PE <net> → <one-word stance>
  * Client: Fut <net> · CE <net> · PE <net> → <one-word stance>
* FII 5-day trend: T=<X> · T-1=<X> · T-2=<X> · T-3=<X> · T-4=<X> → By Count: <B/Be> · By Sentiment: <B/Be>
* Global cues (<time> IST): US <S&P% Dow% Nasdaq%> · Asian <Nikkei% HangSeng%> · Crude $<X> · DXY <X>
* Nearest expiries: NIFTY <date> (<N> sessions) · SENSEX <date> (<N>) · BANKNIFTY <date> (<N>)

**Missing Data — Genuine Gaps Only**
* GIFT Nifty — no programmatic source; use opening 15-min candle
* IV/Greeks — Dhan broken (spot-based); use §8.7.3 straddle rule on F
* IVP — no free source; use VIX direction as proxy
* <any other genuine gap this session>

**Basis Check (§8.7.1a)**
| Index | F (parity, 3 strikes) | Spot | Basis | 0.1% threshold | Verdict |

**OI Wall Map**
| Type | Strike | OI | Note |
Pinning zone: <range> — <why>

---

**Classification: <One of Five Views>**

**Participant-by-participant view (T-1 = <date>, NSE official):**

| Participant | Index Fut | CE | PE | Reading | Implication for today |
|---|---|---|---|---|---|
| FII | <net> | <net> | <net> | <stance> | <what it means for price today> |
| Pro | <net> | <net> | <net> | <stance> | <ceiling/floor defined where; how they resist breakouts> |
| Client | <net> | <net> | <net> | Bullish/Bearish (contrarian → X signal) | <contrarian read> |
| DII | <net> | <net> | <net> | Negligible / <signal if large> | |

**[One paragraph synthesising all participants + OI + VIX + global into the thesis.]**
State: which participants agree with the thesis, which oppose, and which are neutral.
State: what ceiling and floor are defined by Pro desk positioning.
State: what would invalidate this view intraday.

**Key Levels, Bias & Conviction**
* Bias: <Sideways / Bullish / Bearish> + <specific range or direction>
* Conviction: <High/Medium/Low> + <which dimensions agree>
* NIFTY: Support <level> (<why>) · Resistance <level> (<why>) · Pin zone <range>
* SENSEX: F=<X> · Support <X> · Resistance <X>
* BANKNIFTY: <only if relevant — monthly only>

**What to Watch Before Taking a Trade**
1. Opening 15-min candle: above/below PDC, gap direction (GIFT Nifty proxy)
2. 24,000 (or key floor) PE OI at 9:45: dropping fast = floor being removed (§8.7.4)
3. §8.13 Kill switch at 9:45: VWAP one-sided + ORL/ORH break + OI confirming → 2+ fired = trend day
4. VIX direction post-open: rising above <X> while index falls = vega headwind, reduce size
5. <index-specific trigger to confirm or invalidate the thesis>
```

---

## Step 9: Missing data — what is a real gap vs what to track later

**Pre-market data map — what to get from where:**

| Data Point | Source | Tool | Status |
|---|---|---|---|
| NIFTY / BANKNIFTY / SENSEX spot | NSE via Kite | `mcp__kite__get_ltp` | ✅ Always available |
| India VIX | NSE via Kite | `mcp__kite__get_ltp` | ✅ Always available |
| PDC / PDH / PDL | NSE via Kite | `mcp__kite__get_historical_data` interval=day | ✅ Always available |
| Sectoral indices (IT, BANK, FMCG, AUTO, METAL) | NSE via Kite | `mcp__kite__get_ltp` | ✅ Always available |
| Option chain (price, OI, prev_OI, bid/ask) | **Dhan REST** (`POST /v2/optionchain`) | curl, headers `access-token` + `client-id` | ⚠️ **REST only.** MCP OAuth binding is unreliable — try once, then REST |
| ATM straddle / forward / PCR / OI walls | Dhan chain | Arithmetic (no model) | ✅ Computed |
| FII/DII F&O participant OI (T-1) | NSE archive CSV | `WebFetch` + `fii_dii.py` | ✅ T-1 EOD only (by design) |
| FII 5-day activity trend | NSE archive CSV | `fii_dii.py` | ✅ |
| Global: US indices, futures | Yahoo Finance | `WebFetch` yahoo finance/markets/world-indices | ✅ |
| Global: Asian markets | Yahoo Finance | `WebFetch` same page | ✅ |
| Global: European markets | Yahoo Finance | `WebFetch` same page | ✅ |
| WTI Crude oil | Yahoo Finance | `WebFetch` yahoo finance/quote/CL=F | ✅ |
| DXY (US Dollar Index) | Yahoo Finance | `WebFetch` yahoo finance/quote/DX-Y.NYB | ✅ |
| Available margin | Kotak MCP | `mcp__kotak-neo__get_limits` | ✅ |
| Expiry dates | **Dhan REST** `/v2/optionchain/expirylist` | curl (MCP if it happens to be bound) | ✅ Never guess — a plausible wrong date silently prices the wrong contract |
| IV / Greeks | Dhan | ⛔ Broken (spot-based, not forward) | Use §8.7.3 straddle rule |
| IVP (IV Percentile) | No free source | ⛔ | Use VIX direction as proxy |
| GIFT Nifty | No programmatic source | ⛔ | Use first 15-min candle |
| FII/DII cash market (₹Cr equity) | Trendlyne via WebFetch | `WebFetch` trendlyne.com/macro-data/fii-dii/latest/mf-pastmonth/ | ✅ Verified 01-Sep-2026 |
| News / macro events | Manual | ⛔ | Check manually before session |

**To track intraday (not pre-market gaps):**
- PCR slope (Dhan chain, every 30 min from 9:20)
- Opening gap / ORH / ORL (first 15-min candle at 9:30)
- VWAP direction (9:45 kill-switch check per §8.13)
- OI change at key strikes vs morning print

**Hard rules:**
- Never guess or assume any numeric value
- Expiry dates: always fetch, never infer
- FII/DII today: always T-1 (NSE publishes EOD, by design — not a gap)
- GIFT Nifty is a futures price — never compare to NIFTY spot

Do NOT guess or assume any numeric data point.

---

## Step 10: Update tread.md session header

Append the broker connection table and preliminary snapshot to `tread.md`.

**Next:** If the user wants to find a trade, they type `find-trade` or `/Index-Derivatives-tread find-trade`.
