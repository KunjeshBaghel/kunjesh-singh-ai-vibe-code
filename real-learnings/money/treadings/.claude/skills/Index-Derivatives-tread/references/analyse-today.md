# analyse-today — Pre-session market view and setup

**Loaded by:** `/Index-Derivatives-tread analyse-today`

**Also load:** [`gates.md`](gates.md) · [`brokers.md`](brokers.md) · [`check-expiry.md`](check-expiry.md) · [`dhan-api.md`](dhan-api.md) · [`kb/Market_View.md`](../../../../kb/Market_View.md)

Gather data, classify to one of the five views, identify key levels, write `market_view.md`. Takes ~15 min.

---

## Step 1: Create today's folder

```
Date: DD-MM-YYYY  e.g. 31-08-2026
Month folder: August-2026

Create:
  my-treads/<Month-YYYY>/<DD-MM-YYYY>/
    <DD-MM-YYYY>-market_view.md
    <DD-MM-YYYY>-tread.md         (start empty)
    <DD-MM-YYYY>-learning.md      (start empty)
```

Header for `tread.md`:
```markdown
# <DD-MM-YYYY> — Tread Log
## <HH:MM> — Session start: broker connection check
| Broker | Result | Verified with |
```

---

## Step 2: Verify all 3 brokers

See [`brokers.md`](brokers.md) for the three-broker table. Run in parallel, record in `tread.md`. Flag any failure before analysis.

---

## Step 3: Fetch expiry list — all 3 indexes

See [`check-expiry.md`](check-expiry.md) for the method. Never guess. Record sessions_to_expiry for each (TC §6 row 1).

---

## Step 4: Fetch live market data

**From Kite (parallel):**
```
mcp__kite__get_ltp: ["NSE:NIFTY 50", "NSE:NIFTY BANK", "BSE:SENSEX", "NSE:INDIA VIX",
                     "NSE:NIFTY IT", "NSE:NIFTY FMCG", "NSE:NIFTY AUTO", "NSE:NIFTY METAL"]
```

**Sectoral breadth check:** NIFTY bullish but IT/BANK/heavyweights weak = low conviction.

**From Kite historical (PDC/PDH/PDL — last 5 days):**
```
instrument_token=256265 (NIFTY), interval=day, from=5 trading days ago, to=yesterday
instrument_token=265    (SENSEX), same range
```

**From Kotak:**
```
mcp__kotak-neo__get_limits → available margin
```

**From Yahoo Finance (parallel via WebFetch):**
```
WebFetch: https://finance.yahoo.com/markets/world-indices/
  → US (S&P, Dow, Nasdaq, US VIX), US futures, Asia (Nikkei, Hang Seng, Shanghai), Europe (FTSE, DAX)
WebFetch: https://finance.yahoo.com/quote/CL%3DF/     → WTI Crude
WebFetch: https://finance.yahoo.com/quote/DX-Y.NYB/   → DXY
WebFetch: https://trendlyne.com/macro-data/fii-dii/latest/mf-pastmonth/
  → FII/DII cash market net (₹Cr, T-1)
```

**Verified 01-Sep-2026:** Yahoo Finance pages return all global indices, prices, % changes in one call, no login. Returns closed-market prices for US/EU when called pre-market IST.

**GIFT Nifty:** no programmatic source. Use opening 15-min candle. ⛔ GIFT is a futures price — never compare to NIFTY spot.

**MSCI rebalancing context:** FII cash selling on MSCI rebalancing days (typically last trading day of month) is mechanical, not bearish. Check if the date is MSCI-related before interpreting FII cash sells as bearish. Evidence: FII sells cash but writes puts (bullish F&O) on MSCI days — contradictory only if you miss the context.

---

## Step 5: Fetch FII/DII data (NSE archive — no X.com needed)

```bash
! python3 tools/fii-dii/fii_dii.py          # auto-fetches T-1
# OR for specific date:
! python3 tools/fii-dii/fii_dii.py 2026-09-01
```

**Source:** `https://archives.nseindia.com/content/nsccl/fao_participant_vol_DDMMYYYY.csv`
- ✅ Official NSE, no auth, exact match to @Fii_Dii_Data posts
- ⏳ Today's data available after ~4 PM IST → pre-market always fetches T-1
- ⚠️ Expiry days (Tue=NIFTY, Thu=SENSEX) inflate volume ~8×; treat T-4 cautiously if expiry

**Output:** Two tables — (1) participant-wise F&O (FII/Pro/Client/DII × Fut/CE/PE), (2) FII 5-day trend with By-Count/By-Sentiment.

**After fetching:**
- Append to `my-treads/fii_dii_data_2026.md` (use 31/08/2026 entry as template)
- Read last 3 daily entries for 3-day trend validation
- Classify the regime per [`kb/Market_View.md` §4](../../../../kb/Market_View.md)

---

## Step 6: Fetch option chain basics

For nearest expiry per index, fetch from Dhan (see [`dhan-api.md`](dhan-api.md)):
- ATM straddle (CE + PE at nearest ATM)
- PCR: total PE OI ÷ total CE OI (TC §10a)
- Top 3 CE OI (call walls = resistance)
- Top 3 PE OI (put walls = support)

**Forward basis check:** see [`basis-check.md`](basis-check.md).

---

## Step 7: Classify the market

### 7a. Build the participant table

For each participant (FII, Pro, Client, DII), from `fii_dii.py` output:

| Participant | Index Fut Net | CE Net | PE Net | Reading | Implication |
|---|---|---|---|---|---|

**Interpretation (summary — full definitions in [`kb/Market_View.md` §4](../../../../kb/Market_View.md)):**

- **FII (primary trend setter):** Short Fut+Calls+Long Puts = Strongly Bearish · Long Fut+Short Puts+Long Calls = Strongly Bullish
- **Pro (option writer — defines range):** Net short CALLS (large) = **CEILING** at those strikes · Net short PUTS (large) = **FLOOR** · Both short (large) = RANGE · Both long (large) = LONG GAMMA (expecting big move)
- **Client (contrarian):** Very bullish → slight bearish signal; very bearish → slight bullish
- **DII:** small in index F&O; flag only if exceptionally large

---

### 7a-2. ★ Gate 5 handoff — write these numbers into market_view.md

**Gates 1–4 run in find-trade. Gate 5 needs these numbers FROM HERE.**

On **02-Sep-2026** Gate 5 silently didn't run because the numbers were missing.

**Do not compute this by hand.** Run the fetcher — it reads the right file, picks T-2 correctly and
prints the verdict:

```bash
python3 tools/fii-dii/fii_dii.py <T-1 YYYY-MM-DD>     # see its GATE 5 block
```

Copy its output into market_view.md verbatim:

```
GATE 5 INPUTS   (T-1 = <date> vs T-2 = <date>)   source: fao_participant_oi_*.csv
  net_CE_short = |Opt Idx Call Short| − |Opt Idx Call Long|      ΔCE = net(T-1) − net(T-2)

           level T-1     level T-2       ΔCE          ΔPE       limit (TC §9)   verdict
  FII        <n>           <n>          <±n>         <±n>          <n>          <…>
  Pro        <n>           <n>          <±n>         <±n>          <n>          <…>

  ★ Read the limits off TC §9 as you fill this in. Do not quote them from memory.
  → Structures FORBIDDEN: <…>          (Gate 5 never MANDATES anything — see gates.md §5)
```

**★ The trigger is the ΔCE / ΔPE column, never the level.** The level clears 80,000 on ~98% of
sessions and carries no information; the *volume* file that used to feed this is retired. TC §9 has
the evidence table.

**Sign convention:** a participant who got *longer* calls has a **negative** Δ. Write the negative —
it is silence, not a floor.

⛔ **If either day's file will not fetch, write "Gate 5: NOT SCORED — <date> unavailable."**
That is a Gate 4 automatic blocker. Never estimate it.

---

### 7b. Classify FII regime

Six scenarios from [`kb/Market_View.md` §4](../../../../kb/Market_View.md):
Classic Rally · Distribution/Trap · Institutional Consensus · Option Writer's Trap · Range-Bound · Volatility/Reversal Trap

---

### 7c. Cross-check all dimensions

| Dimension | Data | Signal |
|---|---|---|
| Price vs OI | Price Δ + OI Δ | Long Buildup / Short Covering / Short Buildup / Long Unwinding |
| FII regime | From participant table | One of 6 scenarios |
| Pro desk | From table | Ceiling / floor / range |
| Client | From table | Contrarian read |
| PCR | Dhan chain | TC §10a bands — no gaps, every value classifies |
| VIX direction | India VIX | Rising = vega headwind · falling = tailwind |
| Global cues | Yahoo | US/Asia/EU direction, crude, DXY |

---

### 7d. Classify to one of five

**Strongly Bullish · Slightly Bullish · Sideways · Slightly Bearish · Strongly Bearish** (from [`kb/Market_View.md` §5](../../../../kb/Market_View.md))

**Conviction:** High (4+ agree) · Medium (2–3) · Low (<2 or conflicting)

**Always state WHICH participants support, which oppose.** A classification without participant backing is a guess.

**★ Stamp with time:** `Classification: <view> · Conviction: <level> · as of HH:MM`. Gate 5 must restate it before naming structure. Classification >60 min old is STALE (TC §7).

---

## Step 8: Write market_view.md

```markdown
# <DD-MM-YYYY> Market View

**Data Points Summary**
* NIFTY: <price> (PDC: X | PDH: X | PDL: X)
* BANKNIFTY: <price>
* SENSEX: <price> (PDC: X | PDH: X | PDL: X)
* VIX: <level> (<direction>)
* Sectoral: IT <X> · BANK <X> · FMCG <X> · AUTO <X> · METAL <X>
* PCR: <value> (bands from TC §10a)
* FII/DII (T-1 = <date>, NSE CSV):
  * FII: Fut <net> · CE <net> · PE <net> → <stance>
  * Pro: Fut <net> · CE <net> · PE <net> → <stance>
  * Client: Fut <net> · CE <net> · PE <net> → <stance>
* FII 5-day: T=<X> · T-1=<X> · T-2=<X> · T-3=<X> · T-4=<X> → By Count: <B/Be> · By Sentiment: <B/Be>
* Global (<time> IST): US <S&P% Dow% Nasdaq%> · Asia <Nikkei% Hang%> · Crude $<X> · DXY <X>
* Nearest expiries: NIFTY <date> (<N> sessions) · SENSEX <date> (<N>) · BANKNIFTY <date> (<N>)

**Missing Data — Genuine Gaps Only**
* GIFT Nifty — use opening 15-min candle
* IV/Greeks — Dhan broken (spot-based); use TC §14 substitutes
* IVP — use VIX direction as proxy
* <any other genuine gap>

**Basis Check**
| Index | F (parity) | Spot | Basis | 0.1% threshold | Verdict |

**OI Wall Map**
| Type | Strike | OI | Note |
Pinning zone: <range>

---

**Classification: <One of Five Views> · Conviction: <H/M/L> · as of HH:MM**

**Participant-by-participant (T-1 = <date>, NSE CSV):**

| Participant | Index Fut | CE | PE | Reading | Implication |
|---|---|---|---|---|---|
| FII | <net> | <net> | <net> | <stance> | <what it means> |
| Pro | <net> | <net> | <net> | <stance> | <ceiling/floor where; resistance mechanism> |
| Client | <net> | <net> | <net> | <stance> (contrarian → X) | <contrarian read> |
| DII | <net> | <net> | <net> | Negligible / <signal if large> | |

[★ GATE 5 INPUTS block goes here — see 7a-2 above]

**[Synthesis paragraph: all participants + OI + VIX + global into thesis.]**
State: which agree, which oppose, which neutral.
State: what ceiling/floor defined by Pro.
State: what invalidates intraday.

**Key Levels, Bias & Conviction**
* Bias: <Sideways/Bullish/Bearish> + <range or direction>
* Conviction: <H/M/L> + <which dimensions agree>
* NIFTY: Support <level> (<why>) · Resistance <level> (<why>) · Pin zone <range>
* SENSEX: F=<X> · Support <X> · Resistance <X>
* BANKNIFTY: <only if monthly expiry week>

**What to Watch Before Taking a Trade**
1. Opening 15-min: above/below PDC, gap direction
2. <key floor> PE OI at 9:45: dropping fast = floor removal
3. Kill switch at 9:45 per [`gates.md`](gates.md)
4. VIX post-open: rising while index falls = vega headwind
5. <index-specific trigger>
```

---

## Step 9: Data map — what is a gap vs what to track later

Pre-market completeness:

| Data | Source | Tool | Status |
|---|---|---|---|
| NIFTY/BANKNIFTY/SENSEX spot | Kite | `get_ltp` | ✅ |
| India VIX | Kite | `get_ltp` | ✅ |
| PDC/PDH/PDL | Kite | `get_historical_data` | ✅ |
| Sectoral indices | Kite | `get_ltp` | ✅ |
| Option chain | **Dhan REST** | curl, see [`dhan-api.md`](dhan-api.md) | ⚠️ REST only |
| ATM straddle / PCR / walls | Dhan | arithmetic | ✅ |
| FII/DII F&O (T-1) | NSE archive | `fii_dii.py` | ✅ T-1 EOD only |
| FII 5-day trend | NSE archive | `fii_dii.py` | ✅ |
| Global: US/Asian/EU/Crude/DXY | Yahoo Finance | `WebFetch` | ✅ |
| Margin | Kotak | `get_limits` | ✅ |
| Expiry dates | Dhan | see [`check-expiry.md`](check-expiry.md) | ✅ Never guess |
| IV / Greeks | Dhan | ⛔ Broken (TC §14) | Use TC §14 substitutes |
| IVP | No free source | ⛔ | Use VIX direction |
| GIFT Nifty | No source | ⛔ | First 15-min candle |
| FII/DII cash | Trendlyne | `WebFetch` | ✅ |
| News / macro | Manual | ⛔ | Check manually |

**To track intraday (not gaps):** PCR slope (every 30 min) · opening gap/ORH/ORL (9:30) · VWAP (kill switch) · OI change vs `oi_day_high`

**Never guess any numeric value.** Expiry dates: always fetch. FII/DII today: always T-1 (by design).

---

## Step 10: Update tread.md session header

Append broker connection table and preliminary snapshot to `tread.md`.

**Next:** user types `find-trade` or `/Index-Derivatives-tread find-trade`.
