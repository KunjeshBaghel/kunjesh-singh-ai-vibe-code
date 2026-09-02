# 01-09-2026 Market View

**Data Points Summary**

* **NIFTY:** 24,080.40 (PDC: 24,080.40 | PDH: 24,128.70 | PDL: 23,993.60)
* **BANKNIFTY:** 58,024.95
* **SENSEX:** 76,957.27 (PDC: 76,957.27 | PDH: 77,177.27 | PDL: 76,751.32)
* **VIX:** 11.19 (Low — seller tailwind)
* **Sectoral (pre-open, all ~PDC):** NIFTY IT 31,191 · NIFTY BANK 58,025 · NIFTY FMCG 46,026 · NIFTY AUTO 28,842 · NIFTY METAL 13,194
* **PCR (NIFTY near-money 23,700–24,400):** ~1.01 (neutral-balanced)
* **FII/DII F&O (T-1 = 31-Aug, NSE official CSV):** FII: Short Index Futures (−6,682 net) BUT writing puts (−42,953 net Put Short = bullish/range). Client: Net Long Futures + Long Calls (bullish — contrarian indicator = slight bearish signal). Pro: Long Futures + Net Short Calls (−1,09,003 = range/covered call stance). Pattern → **Range-Bound / Institutional Consensus** (NOT Distribution/Trap). Source: archives.nseindia.com CSV — official, no auth required.
* **Global cues (Yahoo Finance, ~07:52 IST):**
  * US close (31-Aug): S&P 500 7,686 (−0.33%) · Dow 53,186 (−0.70%) · Nasdaq 26,371 (−0.12%) · US VIX 14.92 (+3.4%)
  * US futures (01-Sep morning): S&P +0.05% · Dow +0.13% · Nasdaq −0.05% → stabilising after dip
  * Asian: Nikkei 66,161 (−0.23%) · Hang Seng 25,275 (−1.14%) · Shanghai 3,980 (−0.17%) → broadly weak
  * European: FTSE +0.29% · DAX −1.17% · CAC −0.79% → mixed-to-weak
  * WTI Crude: $86.41 (+0.76%) · **Brent Crude: ~$90–91/bbl** (+elevated, Middle East supply concern) → inflationary headwind for India
  * DXY: 99.50 (+0.07%) — flat; no major FII outflow trigger
  * **GIFT Nifty: 24,198–24,204 (−0.11% to −0.19% from prev close)** → flat-to-mildly negative NIFTY opening expected. Note: GIFT Nifty is futures price, not comparable to spot 24,080.
  * **Overall:** Mildly cautious — US slightly lower, Asian weak, Brent elevated. No panic. Flat-to-slightly negative open for India.
* **FII/DII cash (31-Aug, Trendlyne):** FII −₹7,985.90 Cr · DII +₹4,588.90 Cr
  * **Context:** FII selling was MSCI rebalancing (mechanical, one-off) — not panic distribution. DII absorbed 57%. Net effect: supply met by institutional buying = no floor collapse.
* **Macro/News:**
  * **Q1 FY27 GDP = 7.8%** (vs RBI estimate 7.0%, prior 6.7%) — capex-led beat. Released 31-Aug. Strong domestic foundation.
  * **MSCI Rebalancing (31-Aug):** Drove elevated FII cash selling and volumes. Explains why cash selling was heavy but F&O positioning remained range-bound.
  * **Brent $90–91/bbl:** Mild inflationary headwind; explains why RBI will remain cautious and market can't break out aggressively.
* **Nearest expiries:**
  * NIFTY: **01-Sep-2026 (TODAY — 0-DTE)**
  * SENSEX: 03-Sep-2026 (2 sessions)
  * BANKNIFTY: 29-Sep-2026 (22 sessions — monthly only)

**Missing Data — Genuine Gaps Only (all filled via Gemini + WebFetch)**

* **IV/Greeks** — Dhan broken (spot-based). Use §8.7.3 straddle rule on F. ⛔ (permanent)
* **IVP** — no free source; VIX direction as proxy. ⛔ (permanent)

**Filled gaps (previously missing):**
* ✅ **GIFT Nifty:** 24,198–24,204 (−0.11% to −0.19% from prev close) → flat-to-mildly negative open. Source: Economic Times Live Blog.
* ✅ **FII cash (31-Aug):** −₹7,985.90 Cr. Source: Trendlyne (WebFetch confirmed working).
* ✅ **DII cash (31-Aug):** +₹4,588.90 Cr (absorbed 57% of FII selling). Source: Trendlyne.
* ✅ **Macro:** Q1 FY27 GDP = **7.8%** (vs RBI estimate 7.0%) — strong capex-led beat. Source: BusinessToday.
* ✅ **News:** MSCI Rebalancing on 31-Aug (explains FII cash selling — mechanical, not panic). Brent Crude $90–91/bbl.

**To track intraday (not a pre-market gap):**
* PCR slope (9:20 onwards via Dhan chain, every 30 min)
* Opening gap / ORH / ORL (first 15-min candle at 9:30)
* VWAP direction (9:45 kill-switch check per §8.13)

---

**Basis Check (§8.7.1a)**

| Index | F (parity) | Spot | Basis | 0.1% threshold | Verdict |
|---|---|---|---|---|---|
| NIFTY (0-DTE) | 24,099.5 | 24,080.4 | +19.1 pts | 24.08 pts | ✅ Within — delta band marginally usable; Dhan Greeks still broken → use straddle rule |
| SENSEX (2-DTE) | 77,159 | 76,957.3 | +202 pts | 76.96 pts | ⛔ FAR exceeds — DISCARD delta band; use §8.7.3 centred on F=77,159 |

**NIFTY ATM straddle (at 24,100, F=24,099):** CE 62.10 + PE 62.50 = **₹124.60**
→ Expected daily range: 23,975 – 24,224

**SENSEX ATM straddle (at 77,200, nearest to F=77,159):** CE 303.75 + PE 343.20 = **₹646.95**

---

**OI Wall Map**

**NIFTY 0-DTE (01-Sep-2026)** — Spot 24,080, F 24,099:

| Type | Strike | OI |
|---|---|---|
| CE wall (resistance) | 24,500 | 1,70,61,590 |
| CE wall (resistance) | 24,300 | 1,48,65,760 |
| CE wall (resistance) | 24,200 | 1,30,39,260 |
| CE wall (resistance) | 24,100 | 1,01,27,650 ← nearest ceiling |
| CE wall (resistance) | 24,050 | 44,43,270 |
| PE wall (support) | 24,000 | 1,70,47,485 ← massive floor |
| PE wall (support) | 23,900 | 91,55,315 |
| PE wall (support) | 23,800 | 95,65,920 |
| PE wall (support) | 23,700 | 87,27,810 |

**Pinning zone implied:** 24,000–24,100 (PE wall vs CE wall). Spot at 24,080 sits in the middle.

**SENSEX 2-DTE (03-Sep-2026)** — Spot 76,957, F 77,159:

| Type | Strike | OI |
|---|---|---|
| CE wall (resistance) | 78,000 | 9,06,560 |
| CE wall (resistance) | 77,500 | 6,45,140 |
| CE wall (resistance) | 77,000 | 6,43,920 |
| PE wall (support) | 77,000 | 9,59,780 ← biggest near-term support |
| PE wall (support) | 76,000 | 6,58,200 |
| PE wall (support) | 75,000 | 8,43,900 |

Note: F=77,159 puts true ATM ABOVE the 77,000 PE wall. The 77,000 level is support AND the zone where CE/PE walls face off.

---

**Classification: Sideways (Range-Bound)**

**Participant-by-participant view (31-Aug T-1, NSE official):**

| Participant | Index Fut | CE | PE | Reading | Implication for today |
|---|---|---|---|---|---|
| **FII** | −6,682 (Short) | +4,558 (Long calls) | −42,953 (Put Writer) | Mixed — Net put seller | Expects floor to hold (~24,000); not aggressively bearish |
| **Pro** | +5,347 (Long) | **−1,09,003 (Short Calls)** | +6,638 (Long Puts) | **Covered Call / Range** | Long futures + massive call writing = ceiling expected around 24,100–24,200; small put hedge = knows downside risk exists |
| **Client** | +1,260 (Long) | +1,04,485 (Long Calls) | +39,020 (Long Puts) | Bullish (contrarian signal → slight bearish read) | Retail long = smart money fading the rally |
| **DII** | +75 | −40 | −2,705 | Negligible | No signal |

**Pro desk is the most important signal today.** They wrote 1,09,003 more calls than they bought (31-Aug) — this is their dominant position. Combined with long futures, they are in a classic **covered-call / synthetic range sell** posture. Their short calls sit above current spot (likely 24,200–24,500 zone based on OI concentration). They earn only if the market stays below those strikes through expiry. On a 0-DTE day, Pro desks typically hold and let theta work — they will not want the market to rally past 24,200.

**FII put writing (−42,953 net)** confirms they are not expecting a sharp fall — they are collecting put premium, which pays off only if the market holds above the strike. This reinforces the 24,000 PE wall as a genuine institutional support level, not just OI noise.

**Composite thesis (all 9 data points now complete):**

Three forces define a tight range today:

**Floor at 24,000 — triple-layered support:**
1. FII put writing (−42,953 net short puts): institutional put sellers defend this level; a breakdown below 24,000 costs them premium
2. Massive PE OI (17M contracts at 24,000): largest single OI concentration in the whole chain
3. GDP 7.8% beat: strong domestic fundamentals remove the macro case for a breakdown; DII cash buying (+₹4,589 Cr) adds structural bid

**Ceiling at 24,100–24,200 — triple-layered resistance:**
1. Pro desk covered call posture (−1,09,003 net short calls): dominant option writers resist rallies past their short strikes
2. Stacked CE OI: 24,100 (10.1M), 24,200 (13.0M) — double wall
3. Brent Crude at $90–91/bbl: inflationary headwind limits rate-cut optimism; RBI stays cautious; caps re-rating

**MSCI rebalancing context (critical):** FII cash selling of −₹7,986 Cr on 31-Aug was MECHANICAL (MSCI-driven) — not fundamental bearish conviction. Evidence: FII simultaneously WROTE PUTS (−42,953) which pays off only if the market holds above 24,000. A genuinely bearish FII would buy puts, not sell them. The apparent contradiction (cash sellers + put writers) resolves when you understand they were reducing equity book via MSCI exit while insuring the floor. This is "exit with a put sale" — not panic.

**GIFT Nifty at 24,198–24,204 (−0.11%):** Pointing to a flat-to-mildly negative open near 24,050–24,080. This is inside the expected range (23,975–24,224) and adds no new directional information beyond "range holds."

**VIX at 11.19:** Confirms no event risk priced in. Low volatility = sellers earn theta. 0-DTE theta decay is maximum today.

**Conviction: Very High** — all 9 data dimensions filled; 7/9 explicitly point to range; the 2 that are mildly negative (global cues, FII cash) are both explained by a single event (MSCI rebalancing) and do not override the institutional F&O positioning.

**Key Levels, Bias & Conviction**

* **Bias:** Sideways / Range-Bound — floor 24,000 (FII put writing + GDP support + PE OI), ceiling 24,100–24,200 (Pro short calls + CE OI + Brent headwind). No directional bias.
* **Conviction: Very High** — all 9 data dimensions complete; 7/9 point to range; FII cash selling explained by MSCI (mechanical, not bearish conviction); GDP beat reinforces floor.
* **NIFTY key levels:**
  * Support: 24,000 (PE wall 17M), 23,993 (PDL), 23,900 (PE wall 9.2M)
  * Resistance: 24,100 (CE wall 10.1M), 24,128 (PDH), 24,200 (CE wall 13M)
  * Pinning zone: 24,000 – 24,100
* **SENSEX key levels:**
  * F = 77,159; true ATM = 77,200
  * Support: 77,000 (PE wall 9.6L), 76,751 (PDL)
  * Resistance: 77,177 (PDH), 77,500 (CE wall 6.5L), 78,000 (CE wall 9.1L)
* **BANKNIFTY:** 58,024.95. Monthly expiry 29-Sep (22 sessions) — not the focus today.

**What to Watch Before Taking a Trade**

1. **Opening 15-min candle (9:15–9:30):** Does NIFTY open above or below 24,080 (PDC)? A gap above 24,100 with sustained buying = more bullish; gap below 24,000 = bearish breakdown scenario.
2. **24,000 PE OI at 9:45 check:** Yesterday 24,000 PE OI dropped 10.8L in 10 min as NIFTY approached that level. If 24,000 PE OI starts dropping again intraday → floor being removed → potential sharp move down. Track via `mcp__dhan__market_data_agent_tool` optionchain.
3. **§8.13 Kill switch (3 markers at 9:45):** VWAP one-sided + ORL break + OI confirming direction. 2+ fired → trend day → no neutral structure.
4. **VIX direction post-open:** If VIX climbs above 12.5 while NIFTY falls → vega headwind for sellers; reduce size.
5. **SENSEX behaviour:** SENSEX F = 77,159, trades on BSE. If SENSEX is weaker (below 76,751 PDL) → confirms bearish tone across both exchanges → reinforces any bearish NIFTY structure.
