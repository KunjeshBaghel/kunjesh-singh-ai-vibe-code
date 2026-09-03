# 03-09-2026 Market View

*Built 10:35–10:52 IST, Thursday. **SENSEX weekly expiry day (0-DTE).***

---

## Data Points Summary

* **NIFTY 50:** 23,973.20 · +58.75 (+0.25%) — PDC 23,914.45 | PDH 23,914.45 | PDL 23,786.80 · O 23,997.95 H 24,025.40 L 23,955.35
* **BANKNIFTY:** 57,583.20 · +411.20 (**+0.72%**) — PDC 57,172.00
* **SENSEX:** 76,747.19 · +176.84 (+0.23%) — PDC 76,570.35 | PDH 76,570.35 | PDL 76,135.72 · O 76,724.95 H 76,924.48 L 76,705.02
* **India VIX: 11.10** — PDC 11.59 → **falling −4.2%.** Seller tailwind, but note the *absolute* level is near multi-week lows (5-day range 10.57–11.59). Cheap premium is the binding problem today, not vega risk.
* **Sectoral breadth — NARROW, this is the key tell:**

| Sector | Change | % |
|---|---|---|
| NIFTY BANK | +411.20 | **+0.72%** |
| NIFTY METAL | +36.65 | +0.28% |
| NIFTY AUTO | −90.00 | −0.32% |
| NIFTY FMCG | −138.85 | −0.30% |
| NIFTY IT | −234.45 | **−0.75%** |

> The entire index gain is **BANK alone**. IT, FMCG and AUTO are all red. A green index carried by one sector is low-conviction — this is explicitly the case where the move should not be read as bullish.

* **PCR (SENSEX 0-DTE):** near-money 76,000–77,600 = **1.087** · all strikes = 1.163 → *mildly bullish* band (1.00–1.30)
* **SENSEX ATM straddle (at F):** ≈ **285 pts** (76,800: 123.55 + 157.00 = 280.55; 76,700: 293.20) → 1 SD ≈ 357 pts for the remaining session
* **Max pain: 76,800** — spot 76,747, F 76,766. **Max pain is sitting on the money.** Textbook expiry pin.
* **Global cues (~10:50 IST):** S&P 500 +0.46% · Dow +0.56% · Nasdaq +0.45% · Nikkei +0.25% · Hang Seng +0.02% · Shanghai +0.43% · FTSE −0.30% · DAX −0.50% · **WTI Crude $90.58 (−0.47%)** · **DXY 99.42 (−0.18%)**
* **Nearest expiries:** SENSEX **03-Sep = TODAY (1 session, 0-DTE)** · NIFTY 08-Sep (4 sessions) · BANKNIFTY 29-Sep (~18 sessions)

---

## Gate 1 — Feasibility (§8.11.6), all three indexes

| Index | Nearest expiry | Sessions (incl. today) | Verdict |
|---|---|---|---|
| **SENSEX** | **Thu 03-Sep** | **1 (0-DTE)** | ✅ **PASS — the only tradeable index today** |
| NIFTY 50 | Tue 08-Sep | Thu 3 · Fri 4 · Mon 7 · Tue 8 = **4** | ⛔ FAIL (needs ≤ 2) |
| BANKNIFTY | Tue 29-Sep | ~18 — monthly only | ⛔ FAIL by construction, excluded, not priced |

MAX CREDIT permitted = ₹3,500 ÷ (k−1) = **₹5,833** at k = 1.6.

---

## Gate 2 — Basis check (§8.7.1a), SENSEX

| Strike | CE | PE | F = K + CE − PE |
|---|---|---|---|
| 76,600 | 246.15 | 79.60 | 76,766.55 |
| 76,700 | 179.55 | 113.65 | 76,765.90 |
| 76,800 | 123.55 | 157.00 | 76,766.55 |
| 76,900 | 83.70 | 216.40 | 76,767.30 |

**F ≈ 76,766.5**, agreement spread **1.4 pts** across four strikes → chain is live, not stale.
Basis = F − spot = 76,766.5 − 76,757.5 = **+9.0 pts** vs 0.1% threshold of 76.8 → **basis is small and normal for 0-DTE.**
**True ATM strike = 76,800.** ⛔ Vendor Greeks/IV still not used anywhere in this view — `credit ÷ width` is the delta proxy throughout.

---

## Missing Data — Genuine Gaps Only

* **GIFT Nifty** — no programmatic source. Proxy used: opening 15-min candle (SENSEX gapped +154.6 from PDC and held).
* **IV / Greeks** — Dhan broken (spot-based, CE IV ≠ PE IV). Substituted with the §8.7.3 straddle rule on F.
* **IVP** — no free source. VIX level + direction used as proxy.
* **VWAP (kill-switch M2)** — ⚠️ Kite returns `volume: 0` for cash indices, so a true VWAP is **not computable** for SENSEX. M2 must be judged from price structure alone, or from a futures proxy. Recorded as a genuine gap, not scored green.
* **SENSEX-specific participant OI** — the NSE participant CSV covers **NSE** F&O only. Gate 5's six numbers are an NSE-positioning read applied to a BSE index. Directionally valid (the two indexes are ~0.99 correlated) but it is a proxy, and it is stated as one.

---

## OI Wall Map — SENSEX 03-Sep (0-DTE)

| Type | Strike | OI | prev OI | Note |
|---|---|---|---|---|
| **CALL WALL** | **77,000** | **9,067,120** | 3,494,880 | +5.57M built today — hard ceiling, 234 pts above F |
| Call | 76,900 | 6,135,320 | 1,279,900 | +4.86M |
| Call | 76,800 | 5,632,000 | 1,703,100 | +3.93M — at the money |
| Call | 77,100 | 4,746,460 | 1,246,580 | +3.50M |
| **PUT WALL** | **76,500** | **8,266,780** | 1,436,320 | +6.83M built today — floor, 267 pts below F |
| Put | 76,800 | 6,441,980 | 283,600 | +6.16M — at the money |
| Put | 76,700 | 6,047,260 | 294,360 | +5.75M |
| Put | 76,600 | 5,216,140 | 585,180 | +4.63M |

**Pinning zone: 76,700 – 76,900**, centred on max pain 76,800.
Writers have built heavily on **both** sides today — this is two-sided expiry writing, the strongest range signal available. Note also that **ITM calls (76,200–76,500) are unwinding** (76,300 CE: 694,340 → 368,840) while OTM calls build: consistent with pinning, not with a directional squeeze.

---

## Classification: **SIDEWAYS** · Conviction **Medium** · as of **10:52 IST**

> ⚠️ Stale after **11:52**. Gate 5 must restate this with a fresh timestamp before any strike is quoted.

### Participant table (T-1 = 02-Sep-2026, NSE official cumulative OI)

| Participant | Index Fut (net) | CE (net) | PE (net) | Reading | Implication today |
|---|---|---|---|---|---|
| **FII** | **−229,163** (short) | **−299,253** (short calls) | **+593,223** (long puts) | **Short futures + short calls + long puts = Distribution/Trap** | Textbook **Strongly Bearish** institutional book. Caps rallies hard. |
| **Pro** | +15,826 (long) | +21,925 (long calls) | +88,909 (long puts) | Mildly long both wings, small size | Near-neutral. Defines **neither** ceiling nor floor. Slight long-gamma tilt, below threshold. |
| **Client** | +200,070 (long) | +273,067 (long calls) | **−712,140 (short puts)** | Long futures + long calls + **heavy put writing** = very bullish | Retail is maximally bullish → **contrarian bearish** |
| **DII** | +13,267 | +4,260 | +30,008 | Negligible size | No signal |

### GATE 5 INPUTS (T-1 = 02-Sep-2026) — copy verbatim, do not re-derive

**Both datasets are given because the 80,000 threshold is ambiguous between them — see the ruling note below.**

```
                        DAILY CHANGE          CUMULATIVE NET OI
                        (fao_participant_vol) (fao_participant_oi)
FII_net_CE_short          +51,192               +299,253
FII_net_PE_short          +39,242               −593,223   (net LONG puts)
FII_net_FUT               + 7,131 (sold)        −229,163   (net SHORT futures)

Pro_net_CE_short          −40,683 (bought)       −21,925   (net LONG calls)
Pro_net_PE_short          + 3,651                −88,909   (net LONG puts)
Pro_net_FUT               − 1,401 (bought)       +15,826   (net LONG futures)

CEILING?     change: FII 51,192 → 50–80K = STRONG PREFERENCE (no mandate)
             cumul.: FII 299,253 > 80,000 → HARD CEILING
             ✅ BOTH point the same way: the ceiling is real, sell CALLS.

FLOOR?       change: FII 39,242 (<50K = SILENCE) · Pro 3,651 (SILENCE)
             cumul.: FII −593,223 · Pro −88,909, both net LONG puts
             ✅ BOTH agree: NO FLOOR on either reading.

LONG GAMMA?  change: Pro bought 40,683 CE but SOLD puts → not long both. NO.
             cumul.: Pro long both wings, 21,925 / 88,909, both < 100,000. NO.

→ Structures MANDATED : BEAR CALL SPREAD
→ Structures FORBIDDEN: BULL PUT SPREAD (no floor on either reading + bearish participant book)
```

> ⚠️ **Rulebook defect flagged 03-Sep-2026 — needs a ruling before a session where the two disagree.**
> Gate 5 says ">80,000 net short calls = hard ceiling" without saying *which* dataset. The precedents
> in CLAUDE.md (01-Sep "Pro net short 1,09,003 calls", 02-Sep "FII net short 93,282 calls") match the
> **daily-change** magnitudes, so 80,000 looks calibrated on **change**. If it were applied to
> cumulative OI it would breach almost every session and the gate would fire permanently — a gate that
> always fires is not a gate. **Today both readings agree, so the decision is unaffected.** Logged in
> `my-treads/fii_dii_data_2026.md` under the 02/09/2026 cumulative block.

**FII 5-day activity:** T −19,081 · T-1 −36,481 · T-2 +40,829 · T-3 +62,995 · T-4 −112,312 → **By Count Bearish (2B/3Be) · By Sentiment Bearish (net −64,050)**
**FII regime (6 scenarios): #2 Distribution / Trap Phase** — FII selling futures and calls while Client buys futures and calls and writes puts. This is the cleanest version of that pattern in the book so far.

### Synthesis

Two clocks are running in opposite directions and both readings are correct.

**The positioning clock is bearish.** FII carries a fully-consistent bearish book across all three instruments — net short 229,163 index futures, net short 299,253 calls, net long 593,223 puts — while retail sits on the exact opposite side of every one of those trades, including 712,140 net short puts. On the weekly frame SENSEX has fallen from 77,472 (26-Aug) to 76,570 (02-Sep), roughly 900 points, and the 5-day FII sentiment score is negative. Nothing in the institutional data supports upside.

**The expiry clock says pin.** It is 0-DTE, max pain is 76,800 against a forward of 76,766 — effectively zero distance — and writers piled into *both* sides this morning: +6.83M puts at 76,500 and +5.57M calls at 77,000, bracketing spot in a 500-point box. VIX is falling and near multi-week lows. Today's gap up of 154 points was bought and then immediately faded back to unchanged, with the entire index gain attributable to BANK while IT (−0.75%), FMCG and AUTO are red. That is not a rally; it is a rotation inside a range.

**Agreeing with Sideways:** two-sided OI walls, max pain on the money, falling VIX, narrow sectoral breadth, price round-tripping to the open. **Agreeing with a bearish tilt:** FII across all three instruments, Client contrarian, the weekly downtrend. **Opposing:** PCR at 1.087 (mildly bullish) and mildly positive global cues — but PCR in the 1.0–1.3 band is the weakest signal on the board, and global cues were already spent in the gap that got sold.

Resolution: on expiry day the option-structure evidence outranks the swing-positioning evidence for *today's range*, so the view is **Sideways**. But the bearish participant book decides **which side is safe to sell** — and it says the upside. Conveniently, Sideways and Slightly Bearish permit the same structure, so this classification carries no structural risk either way.

**Ceiling and floor defined by positioning:** FII's 299,253 net short calls define the ceiling. **No floor is defined by any participant** — Pro is net long puts, FII is net long puts, and the only large put writer is *retail*, who is the contrarian indicator. A floor whose sole author is Client is not a floor.

**What would invalidate this view intraday:** a sustained SENSEX close above **77,000** (the call wall) on two consecutive 15-min candles — that breaks the pin and turns the ceiling into a squeeze; or a break below **76,500** with the put wall's OI eroding against its `oi_day_high`, which would mean the floor is being removed rather than defended.

---

## Key Levels, Bias & Conviction

* **Bias:** Sideways, range **76,500 – 77,000**, with the safer edge being the **upside** (sell calls, not puts)
* **Conviction:** **Medium** — 4 dimensions favour range (OI walls both sides, max pain on money, falling VIX, narrow breadth); 3 favour bearish (FII, Client contrarian, weekly trend); 2 mildly oppose (PCR, global). No dimension argues for a bullish break.
* **SENSEX:** F = **76,766.5** · Support **76,500** (put wall 8.27M) · Resistance **77,000** (call wall 9.07M) · Pin zone **76,700–76,900** · 1 SD remaining ≈ **357 pts**
* **NIFTY:** 23,973 · Support 23,786 (PDL) · Resistance 24,025 (day high) — **not tradeable today, Gate 1 fail at 4 sessions**
* **BANKNIFTY:** 57,583, strongest sector — **excluded, monthly expiry 18 sessions out**

---

## What to Watch Before Taking a Trade

1. **77,000 call wall integrity.** 9.07M OI, 234 pts above F — that is only **0.82 × the expected move**, so it is *not* a comfortable short strike. Check its OI against `oi_day_high` before selling anything at or below it.
2. **The clock.** Entry window closes **11:15**. SENSEX hard flat is **2:15 PM**, CAS 3:15 PM. This view was built at 10:52 — there is very little runway, and a rushed 0-DTE entry is worse than no entry.
3. **Credit adequacy is the likely blocker, not direction.** With VIX at 11.1 the whole chain is cheap. Preliminary scan: 77,000/77,100 gives c/W ≈ 20.3% but only ~₹2,436 total credit at the 6-lot cap — **below the ₹2,500 minimum**. This needs to be priced properly in `find-trade`; the day may well fail on "too small" rather than "too dangerous".
4. **Kill switch at the next check.** M1 opening range (9:15–9:45) = 76,705.02 / 76,919.02; every close since has been *inside* it → **M1 not fired**. M2 not computable (no index volume — see gaps). M3 needs an OI re-pull vs `oi_day_high`.
5. **0-DTE discipline:** on expiry day the only permitted in-trade actions are **HOLD or EXIT**. §8.9 is closed. No rolling, no converting, no adding.
