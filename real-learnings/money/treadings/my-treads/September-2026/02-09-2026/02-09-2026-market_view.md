# 02-09-2026 Market View

> **REBUILT 09:30 IST with LIVE market data.** The 07:36 pre-market version is preserved at the bottom under *Appendix — Pre-Market View (07:36)*. What changed is summarised in *§ What Changed vs Pre-Market*.

**Broker status (09:24):** Kite ✅ live · Kotak Neo ✅ live (₹6,86,627) · Dhan MCP ⚠️ OAuth `Unauthorized` → **REST fallback ✅ working** (all 3 chains pulled)

---

## Data Points Summary — live 09:25–09:30 IST

| Index | LTP | Open | Day High | Day Low | PDC | PDH | PDL | Net Chg |
|---|---|---|---|---|---|---|---|---|
| **NIFTY 50** | 23,805.10 | 23,858.00 | 23,882.95 | 23,786.80 | 24,055.80 | 24,143.15 | 23,952.55 | **−250.70 (−1.04%)** |
| **BANKNIFTY** | 56,996.70 | 57,006.45 | 57,079.90 | 56,823.20 | 57,409.60 | — | — | **−412.90 (−0.72%)** |
| **SENSEX** | 76,189.32 | 76,471.32 | 76,521.67 | 76,135.72 | 76,944.28 | 77,231.87 | 76,656.12 | **−754.96 (−0.98%)** |
| **India VIX** | **12.11** | 11.49 | 12.11 | 10.55 | 11.49 | — | — | **+0.62 (+5.40%)** ⚠️ at day high |

**Opening gap (measured, not assumed):**
* NIFTY opened **−197.8 pts (−0.82%)** below PDC and **never traded back above PDL 23,952.55**. Gap-and-hold, not gap-and-fade.
* SENSEX opened **−473 pts (−0.61%)** below PDC, now **−755**, also entirely below PDL 76,656.
* BANKNIFTY opened −403 pts; the **relative outperformer** (−0.72% vs NIFTY −1.04%).

**Sectoral breadth — 7 of 7 RED (no rotation, broad risk-off):**

| Sector | LTP | Net Chg | % |
|---|---|---|---|
| NIFTY IT | 30,704.55 | −792.15 | **−2.51%** ⚠️ worst |
| NIFTY AUTO | 27,930.70 | −560.35 | −1.97% |
| NIFTY METAL | 13,039.30 | −150.55 | −1.14% |
| NIFTY FMCG | 45,945.25 | −511.90 | −1.10% |
| NIFTY FIN SERVICE | 25,763.75 | −240.15 | −0.92% |
| NIFTY BANK | 56,996.70 | −412.90 | −0.72% |
| NIFTY PHARMA | 26,721.90 | −70.75 | −0.26% (most defensive) |

**Global cues (live 09:26 IST — Asia deepening vs the 07:20 read):**
* US (01-Sep close): S&P 500 **7,631.47 −0.71%** · Dow **52,766.90 −0.79%** · Nasdaq **26,099.77 −1.03%** · **US VIX 16.34 +9.52%** ⚠️
* Asian (live): **Nikkei 64,402.93 −2.74%** ⚠️ (worse than −2.65% at 07:20) · Hang Seng 25,069.80 **−1.03%** (worse than −0.42%) · Shanghai 3,947.26 **−0.82%** (worse than −0.38%)
* European (prev close): FTSE 10,789.28 −0.32% · DAX 25,970.11 −1.10%
* Commodities: **WTI Crude $90.67 (+0.50%)** · **DXY 99.77 (+0.09%)**

**5-session NIFTY trend (Kite daily closes):** 24,219 (24-Aug) → 24,334 (25) → 24,208 (26) → 24,091 (27) → 24,176 (28) → 24,080 (31) → 24,056 (01-Sep) → **23,805 now**. From the 25-Aug close high, **−529 pts (−2.17%) in 6 sessions.** Confirmed lower-highs downtrend.

**Nearest expiries (fetched from Dhan, never guessed) — trading sessions, not calendar days:**

| Index | Nearest expiry | Sessions away |
|---|---|---|
| **SENSEX** | **03-Sep-2026 (Thu)** | **1 — tomorrow. Today is 1-DTE.** |
| **NIFTY** | 08-Sep-2026 (Tue) | 4 |
| **BANKNIFTY** | 29-Sep-2026 (Tue, monthly) | 19 |

⚠️ **No 0-DTE instrument exists on any index today.** §8.11.6 feasibility implication is flagged below.

**Kotak margin available:** ₹6,86,627 (live)

---

## Missing Data — Genuine Gaps Only

* **GIFT Nifty** — no programmatic source. **Resolved by the actual open:** the 15-min candle (O 23,858 / H 23,882.95 / L 23,786.80) is now real data, so this gap is closed for today.
* **IV & Greeks** — Dhan computes off spot, not forward → unusable. **Substituted with §8.7.3 straddle rule on the parity forward** (below). Arithmetic only; no Black-Scholes solved.
* **IVP (IV percentile)** — no free source. **Proxy:** India VIX direction (+5.40%, sitting at its day high) = rising vega cost.
* **Dhan MCP OAuth** — `Unauthorized`; two fresh consentIds issued, not yet bound. **Not a data gap** — REST fallback delivered all 3 full chains.
* **FII/DII cash equity (Trendlyne)** — not fetched. F&O participant OI (NSE official CSV) is the primary signal; cash is secondary context only.
* **⚠️ OI-change magnitudes are provisional at 09:30.** 01-Sep was the NIFTY weekly expiry, so the Sep-08 series only became the front week yesterday — a large part of today's OI *adds* is roll-in, not fresh conviction. **The CE-vs-PE ratio of adds is the readable signal; the absolute numbers are not.** Re-check at 9:45 against `oi_day_high` per §8.13.3.

---

## Basis Check (§8.7.1a) — RUN LIVE, all 3 indexes

`F = K + CE − PE`, averaged over 5 near-ATM strikes. All agreed within ±1.2 pts → **chains are fresh, not stale.**

| Index | F (parity, 5 strikes) | Dhan spot | Basis | 0.1% threshold | Verdict |
|---|---|---|---|---|---|
| NIFTY 08-Sep | **23,875.39** | 23,814.05 | **+61.34** | 23.8 | ⛔ **HIGH — 2.6× threshold** |
| SENSEX 03-Sep | **76,309.91** | 76,221.86 | **+88.05** | 76.2 | ⛔ **HIGH — 1.16× threshold** |
| BANKNIFTY 29-Sep | **57,395.61** | 57,039.10 | **+356.51** | 57.0 | ⛔ **HIGH — 6.3× threshold** |

**Consequence: discard any vendor delta band on all three indexes.** Use §8.7.3 straddle-rule strikes centred on **F**, not spot. The true ATM is **one to four strikes above spot** on every index today.

**ATM-forward straddles (§8.7.3 — arithmetic, not a model):**

| Index | ATM-fwd strike | CE | PE | **Straddle** | Implied σ back-solved from `Straddle ≈ 0.7979·F·σ·√T` |
|---|---|---|---|---|---|
| NIFTY 08-Sep (4 sessions) | 23,900 | 129.15 | 153.80 | **282.95** | ≈ **11.8%** |
| SENSEX 03-Sep (1 session) | 76,300 | 279.40 | 270.55 | **549.95** | ≈ **14.3%** |
| BANKNIFTY 29-Sep (19 sessions) | 57,400 | 766.25 | 770.15 | **1,536.40** | ≈ **12.2%** |

**Two things this tells us that the Greeks cannot:**
1. **NIFTY implied σ (11.8%) is *below* India VIX (12.11).** There is no fear premium priced into the NIFTY weekly despite a 250-pt gap down. Cheap options = poor seller edge on NIFTY.
2. **SENSEX 1-DTE implied σ (14.3%) carries a ~2.2 vol-point premium over VIX.** That is the expiry/event premium. **If anything is worth selling today it sits in SENSEX, not NIFTY.**

**Expected-move reality check — the single most important number today:**
* NIFTY straddle 282.95 over 4 sessions → **1-day expected move ≈ 283/√4 = ±141 pts.**
* **NIFTY has already moved −251 pts from PDC — that is 1.8× a full day's implied move, before 9:30.**
* SENSEX 1-DTE straddle 549.95 = the market's expected move *through tomorrow's expiry*. **SENSEX is already −755, i.e. 1.4× that, today alone.**
> The bearish move is not "starting" — on a vol-implied basis **most of it has already been paid out.** Continuation from here requires *new* selling, not the overnight news that is already in the price.

---

## OI Wall Map (live, near-money ±5%)

### NIFTY 08-Sep — PCR 0.735 near-money · 0.668 full chain · **Max pain 24,000**

| Type | Strike | OI | OI change today | LTP | Note |
|---|---|---|---|---|---|
| **CE wall** | **24,000** | 9,297,730 | **+3,523,845** | 86.10 | **Ceiling, reinforced hard today.** Coincides with max pain. |
| CE wall | 24,200 | 9,259,575 | +1,864,915 | 33.25 | Secondary ceiling |
| CE wall | 24,100 | 7,309,510 | +889,005 | 54.80 | |
| CE wall | 24,500 | 7,569,575 | +338,520 | 7.75 | Far ceiling |
| **PE wall** | **23,800** | 6,505,265 | **+3,489,655** | 109.15 | **NEW floor forming at spot** — writers stepping in here today |
| PE wall | 23,500 | 6,888,180 | +693,420 | 33.35 | Strong support below |
| PE wall | 23,600 | 6,033,235 | +1,198,145 | 50.15 | |
| PE wall | 23,900 | 4,857,710 | +1,508,650 | 153.80 | |

**Near-money OI adds: CE +27,662,310 vs PE +16,019,315 → CE adds are 1.73× PE adds → call writing dominant → bearish confirmation.**

> **The pin zone has MOVED.** Pre-market it was 24,000–24,200. The live chain has rebuilt it at **23,800–24,000** — fresh writing of +3.52M calls at 24,000 and +3.49M puts at 23,800 in the same session is writers **bracketing a new, lower range around the gap.**

### SENSEX 03-Sep (1-DTE) — PCR 0.669 near-money · 0.643 full chain · **Max pain 76,400**

| Type | Strike | OI | OI change today | LTP | Note |
|---|---|---|---|---|---|
| **CE wall** | **76,500** | 2,016,720 | **+1,842,240** | 190.90 | **Fresh ceiling right above spot** — 311 pts up. Near-10× OI growth today. |
| CE wall | 77,000 | 3,655,200 | +1,655,440 | 64.50 | Heaviest absolute CE wall |
| CE wall | 77,500 | 1,959,480 | +517,560 | 22.25 | |
| CE wall | 78,000 | 2,404,140 | +299,700 | 9.60 | |
| **PE wall** | **76,200** | 1,820,160 | **+1,455,580** | 225.00 | **Fresh floor at spot** — 5× OI growth today |
| PE wall | 76,000 | 2,013,820 | +657,300 | 149.95 | Key round-number floor |
| PE wall | 75,500 | 1,656,560 | +659,660 | 49.45 | |
| PE wall | 75,000 | 1,586,660 | +334,540 | 18.45 | |

**Near-money OI adds: CE +14,158,900 vs PE +8,000,300 → 1.77× → call writing dominant → bearish confirmation.**
**Pin zone SENSEX: 76,000–76,500**, spot 76,189 sits inside it. Max pain 76,400 is *above* spot → mild upward pull into tomorrow's expiry.

### BANKNIFTY 29-Sep (monthly) — PCR 1.125 near-money · 1.054 full chain · **Max pain 57,500**

| Type | Strike | OI | OI change today | LTP |
|---|---|---|---|---|
| CE wall | 57,500 | 1,929,750 | **−26,550** (unwinding) | 714.15 |
| CE wall | 58,000 | 1,373,670 | +13,680 | 490.85 |
| PE wall | 57,500 | 1,943,640 | +1,740 | 814.75 |
| PE wall | 57,000 | 900,150 | +62,370 | 597.80 |
| PE wall | 56,000 | 697,380 | −5,550 | 298.10 |

**BANKNIFTY is the outlier: PCR 1.125 (neutral-to-bullish) while NIFTY/SENSEX print 0.67–0.74.** OI changes are tiny (monthly, 19 sessions out) — no fresh conviction either way. Basis +356 makes spot-based reads meaningless here. **No structure recommended; monthly-only, no weekly.**

---

## Classification: **Slightly Bearish** — bearish thesis CONFIRMED at the open, but ~1.8× already realised

**Participant table (T-1 = 01-Sep-2026, NSE official CSV — unchanged, correctly T-1):**

| Participant | Index Fut | CE | PE | Reading | Implication for today |
|---|---|---|---|---|---|
| **FII** | −12,717 | −93,282 | −69,518 | Short futures + short strangle (sold OTM CE **and** OTM PE) | Directionally bearish on futures; expects a **range** on the options side. FII score −36,481. |
| **Pro** | +3,617 | **+168,089** | **+131,998** | **LONG STRADDLE, ~300K contracts** | **Bought the straddle FII sold. Paid for a big move — and the gap-down delivered it.** ⚠️ See below. |
| Client | +8,911 | −75,332 | −62,619 | Short straddle + long futures | Contrarian → the retail short straddle is **already hurting** on a 250-pt gap. Their pain is the move's fuel. |
| DII | +189 | +525 | +139 | Negligible | No signal. |

**FII 5-day:** T=−36,481 (Be) · T-1=+40,829 (B) · T-2=+62,995 (B) · T-3=−112,312 (Be) · T-4=−45,603 (Be) → **By Count: Bearish (2B/3Be) · By Sentiment: Bearish (net −90,572)**

**Regime: Scenario 6 — Volatility/Reversal Trap** (Pro long straddle), overlaid on a confirmed downtrend.

### Synthesis

The pre-market thesis was right and the market paid it out inside the first minute. NIFTY gapped −198, extended to −251, and has **not once traded back above yesterday's low (23,952.55)**. Every one of the seven sectoral indices is red, led by IT at −2.51% — this is index-level de-risking, not rotation. Asian markets have *deepened* their losses in live trade since the 07:20 read (Nikkei −2.65% → −2.74%, Hang Seng −0.42% → −1.03%, Shanghai −0.38% → −0.82%), so the risk-off impulse is still being fed, not exhausted. The option chain agrees: near-money call OI is being added at **1.73× (NIFTY) and 1.77× (SENSEX)** the rate of put OI, and price-down-plus-call-OI-up is textbook **short buildup**.

**But three things argue firmly against chasing this lower, and they are the reason this stays *Slightly* Bearish rather than *Strongly*:**

1. **The move is 1.8× spent on a vol-implied basis.** NIFTY's own chain prices a ±141-pt day and has already delivered −251. SENSEX has delivered 1.4× its entire 1-DTE expected move today alone. Everything the overnight tape knew is in the price.
2. **Writers are bracketing a NEW range, not fleeing.** +3.52M fresh calls at NIFTY 24,000 *and* +3.49M fresh puts at 23,800 in the same session is the market building a floor and a ceiling around the gap — pin zone relocated to **23,800–24,000**. SENSEX did the identical thing: +1.84M calls at 76,500, +1.46M puts at 76,200 → **76,000–76,500**.
3. **There is no fear premium to sell into on NIFTY, and no panic anywhere.** NIFTY implied σ (11.8%) is *below* India VIX (12.11); VIX at 12.11 is a historically very low absolute level even after a +5.4% pop. Real flush days do not start with a 12 handle.

**⚠️ The Pro-desk read has flipped meaning since the pre-market view.** Pro bought a ~300K-contract straddle on 01-Sep. That position is now deeply in the money after a 250-pt gap. **A long straddle that has paid gets monetised, and monetising it means selling those options back into the market** — which is *vol-negative and mean-reverting intraday*, not vol-positive. Yesterday this signal said "expect a big move, don't sell premium." Today, with the move delivered before 9:16, it argues the opposite way: **the marginal Pro flow from here is more likely to compress the range than extend it.** This is the single biggest interpretation change vs the 07:36 view.

**Who agrees with Slightly Bearish:** FII (short futures), the CE/PE OI-add ratio on both indexes, all-red sectoral breadth, live Asia, the 6-session lower-highs downtrend, PCR 0.67–0.74, US VIX +9.5%.
**Who opposes it:** BANKNIFTY PCR 1.125, NIFTY max pain 24,000 and SENSEX max pain 76,400 both *above* spot, VIX at only 12.11, NIFTY implied σ < VIX, the fresh put wall at 23,800/76,200, and the expected-move exhaustion above.
**Who is neutral:** DII (negligible), Client (contrarian but already positioned wrong and therefore not a fresh signal).

**Ceiling defined by:** NIFTY **24,000** (CE OI 9.30M, +3.52M today, = max pain) · SENSEX **76,500** (CE OI 2.02M, +1.84M today).
**Floor defined by:** NIFTY **23,800** (PE OI 6.51M, +3.49M today) then **23,500** (6.89M) · SENSEX **76,200** (1.82M, +1.46M) then **76,000** (2.01M).

**What invalidates this view intraday:**
* **Escalates to Strongly Bearish** if NIFTY breaks and *holds* below **23,786.80** (opening-range low) with the 23,800 PE OI *falling* — that is the floor being removed, not defended (§8.7.4). Next stop 23,600, then 23,500.
* **Collapses to Sideways** if NIFTY reclaims **23,952.55 (PDL)** and holds — that would mean the gap is being filled and the whole overnight story rejected.

---

## Key Levels, Bias & Conviction

* **Bias:** **Slightly Bearish, range-building.** Base case = NIFTY chops **23,800–24,000** for the rest of the session; SENSEX chops **76,000–76,500** into tomorrow's expiry. Directional continuation is the *alternative* case, not the base case.
* **Conviction: Medium.** 6 dimensions support bearish (FII, OI-add ratio, breadth, live Asia, downtrend, PCR); 5 oppose further downside (expected-move exhaustion, fresh put walls, max pain above spot, VIX 12.11 with σ < VIX, BANKNIFTY PCR 1.125). **Direction is agreed; magnitude-from-here is not.** Never higher than Medium on a day where the two halves of the evidence point at different distances.
* **NIFTY:** Forward **F = 23,875** · Support **23,800** (PE 6.51M, +3.49M) → **23,600** → **23,500** (PE 6.89M) · Resistance **23,952 (PDL)** → **24,000** (CE 9.30M = max pain) → 24,100/24,200 · Pin zone **23,800–24,000** · ORL **23,786.80** / ORH **23,882.95**
* **SENSEX (1-DTE):** Forward **F = 76,310** · Support **76,200** (PE 1.82M) → **76,000** (2.01M) → 75,500 · Resistance **76,500** (CE 2.02M) → **77,000** (3.66M) · Pin zone **76,000–76,500** · Max pain 76,400
* **BANKNIFTY:** Forward **F = 57,396** (basis +357). Monthly-only, 19 sessions. PCR 1.125 diverges from the other two. Max pain 57,500. **No structure — stand aside.**

### §8.11.6 feasibility flag (for `find-trade`, not decided here)
Sessions to nearest expiry: **SENSEX 1 · NIFTY 4 · BANKNIFTY 19.** **No 0-DTE instrument exists today.** At `k = 1.5`, `MAX CREDIT = risk cap ÷ 0.5` and required capture = **50%** of the credit. With NIFTY implied σ (11.8%) sitting *below* VIX there is no premium richness on NIFTY to fund that. **SENSEX 1-DTE at σ ≈ 14.3% is the only place carrying a real vol premium today** — run the full gate against SENSEX first, and expect the honest answer on NIFTY to be "too thin." Run §8.11.7 (noise floor) before pricing anything: NIFTY's 30-min range is already ~96 pts.

---

## What to Watch Before Taking a Trade

1. **§8.13 kill switch at 9:45 — currently 1 of 3 fired.** ✅ *OI confirming* (price down + call OI up at 1.73× put adds = short buildup). ⬜ *ORL break*: needs a sustained close below **23,786.80**, not a wick. ⬜ *VWAP one-sided*: needs 45 min, first readable ~10:00. **2+ fired → abandon neutral structures, one-sided only.**
2. **NIFTY 23,800 PE OI at 9:45 vs the 09:30 print of 6,505,265** — and compare to `oi_day_high`, not to the morning number (§8.13.3). **Rising = floor being defended → range holds. Falling fast = floor being removed → flush to 23,600/23,500.** This is the highest-information single number today.
3. **SENSEX 76,200 PE OI (09:30 print 1,820,160) and 76,500 CE OI (2,016,720)** — both grew 5–10× today. Whichever *stops* growing first tells you which side the 1-DTE pin breaks.
4. **India VIX** — 12.11 and pinned at its day high. **Above 13 → vega headwind, cut size on any short-premium structure.** Back below 11.50 → the gap is being digested, range case strengthens.
5. **PDL reclaim test: NIFTY 23,952.55.** A reclaim-and-hold kills the bearish thesis outright and turns the day Sideways. Watch it as a level, not as a wish.
6. **Re-run the basis check before any strike is quoted.** Basis is +61 (NIFTY) / +88 (SENSEX) / +357 (BANKNIFTY) at 09:30 and is tenor-dependent — it will move. **Vendor delta bands are unusable on all three indexes today.**
7. **Asia into the IST afternoon.** Nikkei, Hang Seng and Shanghai all deepened between 07:20 and 09:26. If that continues past noon, the range case weakens and continuation becomes the base case.
8. **Exit clock (§8.3):** SENSEX target **2:15 PM** / hard **2:45 PM** · NIFTY target **2:30 PM** / hard **3:00 PM**. Nothing carried into the 3:15 CAS.

---

## What Changed vs Pre-Market (07:36)

| Dimension | 07:36 pre-market | 09:30 live | Verdict |
|---|---|---|---|
| NIFTY | 24,055 (prev close, market shut) | **23,805**, gapped −198, below PDL all session | ✅ Bearish call **correct**, and faster than expected |
| SENSEX | 76,944 | **76,189** (−755) | ✅ Correct |
| VIX | 11.49, "likely to gap up" | **12.11 (+5.40%)**, at day high | ✅ Correct — but still a very low absolute level |
| NIFTY pin zone | 24,000–24,200 | **23,800–24,000** | 🔄 **Relocated a full 200 pts lower.** Writers rebuilt the range around the gap. |
| SENSEX pin zone | 76,000–77,000 | **76,000–76,500** | 🔄 Tightened; 76,500 is now a fresh, heavy ceiling |
| Basis | "~0, F ≈ spot" (from stale pre-market LTPs = 0) | **+61 / +88 / +357 — all above the 0.1% threshold** | ❌ **Pre-market estimate was wrong.** LTPs were zero, so the "basis ≈ 0" line was an artefact of no data, not a measurement. Never carry a placeholder forward as a finding. |
| ATM straddle | NIFTY est. 311 · SENSEX est. 444 (from VIX) | **NIFTY 282.95 · SENSEX 549.95** (measured) | 🔄 NIFTY 9% *cheaper* than the VIX estimate; **SENSEX 24% richer** — the premium is in SENSEX, not NIFTY |
| PCR NIFTY | 0.69 | 0.735 near-money / 0.668 full chain | ↔ Same bearish lean |
| BANKNIFTY PCR | not computed | **1.125 — diverges from the other two** | ➕ New signal |
| Pro long straddle | "Big move expected → do NOT sell spreads" | **The move happened. A paid straddle gets monetised → vol-negative from here** | 🔄 **Signal inverted.** Same position, opposite implication once the move is delivered. |
| Expected-move context | not computed | **NIFTY already 1.8× its 1-day implied move; SENSEX 1.4× its whole 1-DTE move** | ➕ **The most important new number.** It is what holds the view at *Slightly* rather than *Strongly* Bearish. |

**Carry-forward lesson:** the pre-market basis table recorded `~0` and stamped it **✅ Low basis — forward ≈ spot** while explicitly noting LTPs were zero. That is a placeholder dressed as a verified result — the same failure mode as trusting Dhan's populated-but-wrong Greeks. **A field with no data in it must read "unknown", never a value with a green tick.**

---
---

## Appendix — Pre-Market View (07:36, superseded)

*Retained verbatim for scoring and learning. All live numbers above supersede this.*

**Data Points Summary**
* NIFTY 50: 24,055.80 (PDC: 24,055 | PDH: 24,143 | PDL: 23,952)
* BANKNIFTY: 57,409.60
* SENSEX: 76,944.28 (PDC: 76,944 | PDH: 77,231 | PDL: 76,656)
* VIX: 11.49 — LOW (pre-market; likely to gap up at open given US VIX +9.5%)
* Sectoral: IT 31,496 · BANK 57,409 · FMCG 46,457 · AUTO 28,491 · METAL 13,189
* PCR (NIFTY Sep8 full chain): 0.69 — bearish lean (<0.9 threshold)
* PCR (SENSEX Sep3 full chain): 0.69 — bearish lean
* FII/DII (T-1 = 01-Sep-2026, NSE official CSV):
  * FII: Fut -12,717 · CE -93,282 · PE -69,518 → Short futures + short strangle → Bearish lean + Range
  * Pro: Fut +3,617 · CE +168,089 · PE +131,998 → **LONG STRADDLE (very large) → Big move expected**
  * Client: Fut +8,911 · CE -75,332 · PE -62,619 → Short straddle (contrarian = neutral)
  * DII: negligible
* FII 5-day trend: T=-36,481(Be) · T-1=+40,829(B) · T-2=+62,995(B) · T-3=-112,312(Be) · T-4=-45,603(Be) → By Count: Bearish (2B/3Be) · By Sentiment: Bearish (net -90,572)
* Global cues (~07:20 IST): US S&P 7,631 (-0.71%) · Dow 52,766 (-0.79%) · Nasdaq 26,099 (-1.03%) · US VIX 16.34 (+9.52%) ⚠️ · Nikkei 64,462 (-2.65%) ⚠️ · Hang Seng 25,222 (-0.42%) · Shanghai 3,964 (-0.38%) · FTSE 10,789 (-0.32%) · DAX 25,970 (-1.10%) · WTI $91.65 (+1.59%) · DXY 99.78 (+0.10%)
* Nearest expiries: NIFTY 08-Sep · SENSEX 03-Sep · BANKNIFTY 29-Sep
* Kotak margin available: ₹6,86,627

**Pre-market classification: Slightly Bearish · Conviction Medium**
Ceiling: NIFTY 24,200 / SENSEX 77,000. Floor: NIFTY 24,000 / SENSEX 76,000. Pin zone NIFTY 24,000–24,200.
Invalidation: NIFTY opens above 24,143 (PDH) and holds → thesis collapses.
Key risk flagged: Pro long straddle (300K contracts) → a 1–2% move expected; if NIFTY starts moving it may not stop at 24,000.
