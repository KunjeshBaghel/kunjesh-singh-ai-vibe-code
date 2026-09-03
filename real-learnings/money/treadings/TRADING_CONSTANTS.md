# TRADING_CONSTANTS.md — the single source of truth

**Created 02-Sep-2026.** Every number used in a live trading decision lives here and **nowhere else**.

## The rule about this file

> **If any other file in this repo states a number that contradicts this one, THIS FILE WINS —
> and the other file is a bug that must be fixed, not a judgement call to weigh.**
>
> Never copy a number out of here into another document. **Link to the row instead.** A number
> that exists in two places will eventually exist in two versions, and the looser version always
> wins the argument at 13:12 on a losing day. That is not a hypothetical: on 01-Sep-2026 the
> daily cap said ₹10,500 and the sizing rule offered a "Standard ₹15-20K stop" eleven lines
> later. The loss was ₹15,564.

**Order of precedence, repo-wide:** `TRADING_CONSTANTS.md` → `SKILL.md` → `CLAUDE.md` →
`strategy_ref_book.md §8` → everything else. §1–§7 of `strategy_ref_book.md` is textbook
background and **never** governs a live decision.

---

## 1. Account

| Constant | Value |
|---|---|
| Trading capital | **₹7,02,275** (Kotak Neo) |
| Execution | **Manual, Kotak Neo mobile app.** All APIs are read-only or unfunded. |
| Data | Kite = spot/VIX/OI/depth/candles · Dhan REST = full chain · Kotak = margin |
| Mandate | **Intraday only.** No overnight position, ever, for any reason. |

> ⚠️ **PENDING USER RULING — capital verification 03-Sep-2026**
>
> Documented capital: **₹7,02,275**
> Live `get_limits` (03-Sep-2026): **₹6,86,627.79**
> Delta: **−₹15,647** (≈ the 01-Sep loss)
>
> Caps at the true figure: structural max loss (1.5%) = **₹10,299** · planned stop (0.5%) = **₹3,433**
>
> **Until the user rules, the CURRENT published caps (₹10,500 / ₹3,500) stand.** The ₹10,500 structural cap is stricter in rupee terms (more conservative); the ₹3,500 daily cap is marginally looser but remains the correct order of magnitude.

## 2. Return target

| Constant | Value |
|---|---|
| **Target** | **2–4% per month = ₹14,000–28,000**, measured as a rolling 3-month mean |
| ⛔ Retired | **"~1% net per session" is DELETED.** It is ~250% annualised. Under a 0.5% stop cap it needs 200% capture of the credit — not a reachable number. Keeping it on the wall guarantees size creep at the worst possible moment. |
| Honest per-session expectancy | **₹1,274 (0.20%)** — `strategy_ref_book.md` §8.11.5 |
| First 3 months | **The target is a violation count of zero, not a rupee number.** |

> **Two winning trades are already AT expectancy:** +₹2,951 and +₹3,131. There is no returns problem in this account — there is a loss-size problem.

## 3. Risk caps — all hard, none discretionary

| Constant | Value | Note |
|---|---|---|
| **Structural max loss, per structure** | **₹10,500 (1.5%)** | `(width − credit) × lot_size × lots`. Set EQUAL to the daily breaker so that *total failure of the stop* still lands inside the day's limit. **The only cap that does not depend on you pressing a button.** |
| **Planned stop loss, per structure** | **₹3,500 (0.5%)** | Three consecutive stops = the daily cap |
| **Daily realised loss** | **₹3,500 → day over.** **₹10,500 → day over + next session is a mandatory no-trade day** | 01-Sep-2026: breached by **₹5,030** (total −₹15,564); the next session began at **07:17** hunting a trade — no cool-off occurred. |
| **Weekly realised loss** | **₹21,000 (3.0%)** | Week over, following week paper-only |
| **Monthly realised loss** | **₹28,000 (4.0%)** | Calendar month over |
| **Structures per calendar day** | **ONE.** Not one at a time — one per day. | Closing at 10:30 does not buy a second slot |
| **Margin cap** | **40% (₹2,80,910)** — revised down from 60–70% on **02-Sep-2026** | A backstop only. With the ₹10,500 structural cap this will never bind — a permitted spread blocks ~₹10–12K of margin. **Margin is not a sizing input.** |

## 4. Sizing — compute both, the smaller wins

```
Cap A — STRUCTURAL
  lots_A = floor( 10,500 ÷ ((width − credit) × lot_size) )

Cap B — PLANNED STOP                                  k = 1.6
  lots_B = floor(  3,500 ÷ ((k − 1) × credit × lot_size) )

  LOTS = min(lots_A, lots_B)
  ⛔ LOTS < 2 → narrow the width, recompute. Still < 2 → NO TRADE.
```

**Width is chosen AFTER the cap, never before.** Present numbers in this order, always:
**max profit → breakeven → structural max loss → planned stop → lots.** Never quote a lot
count before the max loss.

| Index | Width | Max loss/lot | Lots | |
|---|---|---|---|---|
| NIFTY (65) | **50** | ~₹2,340 | 4 | ✅ default NIFTY trade |
| NIFTY (65) | 100 | ~₹5,070 | 2 | ✅ |
| NIFTY (65) | 200 | ~₹12,546 | **0** | ⛔ **banned — cannot carry size at this capital** — 01-Sep-2026: Bull Put 24,000/23,800, credit 6.99 → `(200−6.99)×65 = ₹12,546` → `lots_A = floor(10,500÷12,546) = 0`. The structure was **banned outright, not downsized**. 8 lots were placed. |
| SENSEX (20) | **100** | ~₹1,620 | 6 | ✅ best granularity in the book |
| SENSEX (20) | 200 | ~₹3,157 | 3 | ✅ |
| BANKNIFTY (30) | 200 | ~₹4,320 | 2 | ⚠️ locked — see §11 |

> **31-Aug-2026 sizing bands — RETIRED:** "Standard ₹15–20K" / "Aggressive ₹25–35K" against a ₹10,500 cap = up to **3× the daily maximum** in a single trade. Written the evening after ONE winning trade. **n=1 in the winning direction is not evidence.**

## 5. Permitted structures

| | |
|---|---|
| **Permitted** | **The one-sided defined-risk credit vertical. Two legs. That is the entire list.** |
| ⛔ Locked | Iron condors and every 4-leg structure — two gamma exposures you cannot measure and two stop orders to place by hand. **24-Jul-2026:** condor rolled into an iron fly, three adjustments, **−₹1,965**, 100-pt iron fly, squeezed by the bounce. Unlocks per §11. |
| ⛔ Never | Naked shorts · ratios · calendars · ladders · "repair" structures · martingale sizing |
| **Leg counts** | `short qty == long qty`, exactly. A mismatch is a rejected order, not a strategy. **20-Jul-2026:** ran **260 short / 130 long puts = 2 lots NAKED**, journalled as "defined max loss". **01-Sep-2026:** ran 8 short / 10 long. |

## 6. Entry filters — every one is a veto

| # | Filter | Threshold |
|---|---|---|
| 1 | Sessions to expiry | **≤ 2**. Count trading sessions remaining **INCLUDING TODAY**, up to and including expiry. Expiry day itself = 1 ("0-DTE"), expiry eve = 2 ("1-DTE"). **Gate 1 blocks when `sessions_to_expiry ≥ 3`.** Holiday tie-break: derive from gaps in the fetched expiry list + the NSE calendar; **if a day's status is uncertain, COUNT it as a trading day** (the conservative direction). Always fetch the expiry list — never guess or infer a date. |
| 2 | **Credit ÷ width** | **≥ 15%**, 20%+ preferred. *Tail control: at 3.5% max loss is 28× the credit; at 20% it is 4×.* **01-Sep-2026:** c/W was **3.5%** → breakeven win rate **96.5%**. Every trade in this book at ≥17% made money; 13-Jul at 2.5% was never even scored. |
| 3 | Net credit, total | **≥ ₹2,500** (round-trip friction ~₹150) |
| 4 | **Stop reachability** | **`k × credit < width`**. Above `c/W = 1/k` the premium stop sits beyond max loss and can never trigger. **02-Sep-2026:** 4-DTE condor with credit > width/2 — the premium stop sat beyond max loss and could never have triggered. |
| 5 | Noise floor | `(k−1) × credit ≥ 1.5 × the SPREAD's own 30-min intra-bar swing`, opening gap bar excluded. **Method:** pull 30-min bars for BOTH legs and price the spread at each bar's index extremes. **Run it, do not cite it.** Evidence (03-Sep-2026): measured on real legs, spread swing was **16.30 pts** vs index-proxy eyeball ~11 pts, flipping test from 1.35× (pass) to **0.92× (fail)** against 1.5× floor. |
| 6 | Combined bid-ask, both legs | **≤ 15% of net credit** |
| 7 | Top-of-book depth | **≥ 5× your lot count**, both legs, both sides |
| 8 | India VIX level | **< 20**. ≥ 20 → HOSTILE → no trade. |
| 9 | India VIX change on the day | **≤ +8%** at entry. Above → event day, not a decay day. |
| 10 | Basis | `F = K + CE − PE` at 3–4 near-ATM strikes must agree within ~1 pt. `basis = F − spot`; **> 0.1% of spot** → discard any vendor delta, use the §8.7.3 straddle rule on `F`. |
| 11 | Go/No-Go (`option_chain_n_greeks.md` §7) | **SCORE = (2 × RED) + (1 × YELLOW). SCORE ≥ 4 → SIT OUT.** (So 2 reds, or 1 red + 2 yellows, or 4 yellows all block.) **A row with no data is YELLOW, never green. Blank ≠ clear.** **Rows must score from DISJOINT inputs** — if one observation would colour two rows, score it once in the **lower-numbered row** and mark the other `n/a — same input as row N`. **Automatic blockers (separate, NOT counted toward the score):** no five-view classification · undefined max loss · **no live SL order** (a live SL order ≠ a stop-loss defined) · Gate 5's table not written to `tread.md`. Note: `kb/option_chain_n_greeks.md` §7 still carries retired "3+ distinct warnings" wording at L472/L667/L701 — **this row overrides it.** |
| 12 | Kill switch (`strategy_ref_book.md` §8.13) | **2+ of 3 markers → no neutral structure** |
| 13 | Gate 5 participant check | see §8 below |

## 7. Timing — one number each, no "target vs hard"

| Constant | Value |
|---|---|
| **Entry window** | **9:30 – 11:15.** ⛔ No new position after 11:15, ever. |
| **Midday time stop** | **12:30** — if capture < 25%, close at market. *A spread that hasn't decayed by midday is pinned at your short strike: maximum gamma for expired theta. It does not improve after lunch.* |
| **NIFTY / BANKNIFTY hard flat** | **2:30 PM** |
| **SENSEX hard flat** | **2:15 PM** |
| **CAS** | 3:15 PM. Nothing ever survives into it. *20-Jul-2026 exited at ~3:16 PM — a breach never flagged.* |
| **Kill-switch check times** (`strategy_ref_book.md` §8.13) | **9:45 / 10:30 / 11:30 / 1:30** — re-pull spot/VWAP · VIX · ATM straddle · OI *and* `oi_day_high` at each check |
| **Market-view staleness limit** | **A five-view classification older than 60 minutes is STALE — re-pull.** Restate the classification WITH A TIMESTAMP before Gate 5. |

> **The old "target 2:30 / hard 3:00" two-tier scheme is DELETED.** Publishing a later time
> guarantees the later time gets used on the day the position is red at 2:30 — the only day
> it matters. **One time. Set a phone alarm, not a mental note.**

## 8. Exit mechanics

> **01-Sep-2026 — stop called at 13:12, not executed.**
>
> Exit at the trigger: **₹1,865 loss**. Exit as placed: **₹15,564 loss** = **8.3× the call.**
> Re-running the entire book with that one stop honoured turns **−₹11,247 into +₹2,252** — a
> ₹13,700 swing. **Nothing else in this rulebook is worth ₹13,700.**

| Constant | Value |
|---|---|
| **Stop multiple `k`** | **1.6** (credit vertical — the only permitted structure) |
| **Profit target** | **50% of net credit.** One exit. No scaling, no trailing. **Why scaling out / trailing is rejected:** it contradicts §8.15.1's "stop should sit 1.5× beyond typical MAE"; §8.11.7's own case shows a spread reaching **95% of its stop and finishing +1.25**. Revisit after 20 clean trades. |
| **The stop does not move** for the life of the trade — except **down** (less risk). |
| **Stop order** | **SL-LIMIT, buy-to-close, SHORT LEG ONLY.** Never SL-M (§8.10: a trap on options). Never any standing order on the long leg. |
| **Trigger** | `short_leg_entry + 1.6 × (net credit per lot, in points)` — the net captures ~62% of the short leg's move; verify against the live chain and adjust the *trigger*, not the rule |
| **Limit** | `trigger + max(12% of trigger, 2 pts NIFTY/BN, 5 pts SENSEX)` |
| **Placed within** | **90 seconds of the entry fill**, plus two index alerts: one at the short strike, one at `short strike + 0.5 × width` |
| ⛔ | **No live SL order → close at market immediately.** A blank SL-order-ID in the log = an unauthorised trade regardless of P&L. |
| **Stop-out sequence** | **Buy back the SHORT first**, then sell the long. Reverse = momentarily naked. |

### 8a. In-trade monitoring thresholds

Used by the `followup` sub-command at every 30-minute check. The *procedure* lives in
`references/followup.md`; **these numbers live only here.**

```
stop_distance = entry_credit × (k − 1)                 ← NOT the stop threshold
BUFFER %      = (entry_credit × k − current_spread) ÷ stop_distance × 100
```
At entry BUFFER % = **100**; at the stop it = **0**. Above 100 the trade is in profit — report that
as capture, not buffer.

| Buffer % | State | Action |
|---|---|---|
| **> 60%** | 🟢 Safe | Hold. The resting stop does the work. |
| **30 – 60%** | 🟡 Watch | Hold. Confirm the SL order is still live. |
| **15 – 30%** | 🟠 Alert | Do not adjust (§12). Prepare to close. |
| **< 15%** | 🔴 Exit | Close at market now — do not wait the last points for the SL to fill. |

| Constant | Value |
|---|---|
| **Short-strike OI erosion** | **> 20% below `oi_day_high`** → the wall you sold against is going. **Measure against `oi_day_high`, never against the previous check** — the 01-Sep evidence for why is in `references/followup.md` Step 6. |
| **Sustained break** | **two consecutive 15-min CLOSES** through the short strike. A wick is not a break. |
| **Monitoring cadence** | first check at **fill + 30 min**, then **every 30 min** to the hard flat (§7) |

## 9. Direction — Gate 5 participant thresholds

> ### ★ Ruled 03-Sep-2026 — the data source changed. Read this before using the table.
>
> Gate 5 previously read `fao_participant_`**`vol`**`_DDMMYYYY.csv`. That file is
> *"Participant wise **Trading Volume**"* — contracts **traded** in a day. It is **not a position**,
> and it is **retired as a Gate 5 input.**
>
> **Why.** Volume net is the residual of two near-equal giant numbers (on 02-Sep, Client traded
> 11.82M calls long against 11.81M short — a **0.09%** residual), so same-day round-trips dominate it.
> Checked against the real position file over the same sessions:
>
> | Session | FII: true OI position change | FII: old volume net | |
> |---|---:|---:|---|
> | 27-Aug | +29,971 | +29,971 | agrees |
> | 28-Aug | −35,836 | −35,836 | agrees |
> | **01-Sep** | **+22,599** | **+93,282** | **4.1× overstated** |
> | 02-Sep | +51,192 | +51,192 | agrees |
>
> For **Pro on 01-Sep the two disagree in sign**: true position change **+44,229** (got *shorter*
> calls) vs volume net **−168,089** (reads as *buying* calls). The old input pointed the wrong way
> on the day it mattered most.

**Basis: the day-over-day CHANGE in cumulative net OI**, from
`https://archives.nseindia.com/content/nsccl/fao_participant_oi_DDMMYYYY.csv`.

```
net_CE_short(day) = |Option Index Call Short| − |Option Index Call Long|     ← from the _oi_ file
ΔCE = net_CE_short(T-1) − net_CE_short(T-2)         ← THIS is the Gate 5 number
```

⛔ **The LEVEL never triggers Gate 5.** Across 86 sessions (May–Sep 2026) the FII level exceeded
80,000 on **97.7%** of days for calls and **100%** for puts. A gate that fires every day carries no
information. Record the level as context; trigger on the change.

| Participant | Forbid threshold on \|Δ\| | Fires on | Role |
|---|---|---|---|
| **FII** | **65,000** | ~15% of sessions | **Primary — read first.** Slow, directional book (median \|Δ\| 26,923). |
| **Pro** | **100,000** | ~30% of sessions (CE) | **Veto only.** Deliberately below its own p85 — see note. |
| DII · Client | — | — | Context. Never triggers. |

**Semantics — FORBID only. A breach never mandates a structure.**

| Reading | Effect |
|---|---|
| `ΔCE ≥ +threshold` (net *selling* calls) | **CEILING** → ⛔ **Bull Put FORBIDDEN.** Does *not* authorise a Bear Call — that still has to pass every other gate. |
| `ΔPE ≥ +threshold` (net *selling* puts) | **FLOOR** → ⛔ **Bear Call FORBIDDEN.** |
| **Both fire** | ⛔ **Both forbidden → NO TRADE.** The old "mandated" wording left this case undefined. |
| Below threshold | **SILENCE — not permission for the opposite side.** Hands the decision back to the grid. |
| Net **LONG** both CE and PE **> 100,000** *(level, not change)* | Long gamma → **halve size or stand down** |

> **Why Pro sits at 100,000 rather than its own p85 of 147,007.** Pro's book is 2.5× more volatile
> than FII's (median \|Δ\| 68,530) and flips sign constantly — +68,530, −162,095, +109,002, +44,229,
> −40,683 across five consecutive sessions. That is market-maker inventory, not a directional view.
> A *mandate* keyed to it would be reading noise, which is precisely the 02-Sep failure. A **veto**
> keyed to it costs only a skipped trade — cheap in an account where ~75% of sessions are correctly
> no-trades, while a wrong-side trade is not. **Pro may veto; Pro may never authorise.**

> **Honest note on the 01-Sep-2026 precedent.** The old rule is credited with catching it via "Pro net
> short 1,09,003." That figure is **31-Aug's** (correct T-1 usage), and on the new basis it is
> **+109,002** — still over Pro's 100,000, so the catch survives. But Gate 5 was **never the
> load-bearing defence there**: c/W was 3.5% against a 15% floor (§6 row 2) and structural sizing
> returned `lots_A = 0` (§4). Two hard gates already banned that trade. Gate 5 is calibrated for
> **direction** and must not be bent to re-catch a loss three other rules already kill.
>
> **02-Sep-2026** stands unchanged as a lesson: the rule inspected Pro when FII was the signal.
> FII is now explicitly the primary and is read first.

**The hard forbid, no override:** ⛔ Bull Put under any bearish view. ⛔ Bear Call under any
bullish view. Not vol state, not skew, not §8.5.4 PE-first, not participants.

## 10. Volatility state — measurable definitions only

| State | India VIX |
|---|---|
| CHEAP | < 12 |
| NORMAL | 12 – 16 |
| RICH | 16 – 20 |
| **HOSTILE** | **≥ 20, or VIX up > 8% on the day → NO TRADE** |

> ⛔ **The old `IV − HV20 < 0 → HOSTILE` definition is DELETED.** It needs an IV feed that does
> not exist here, and its tenor is wrong regardless: you sell 0–2 session options against
> **20 days** of trailing realised vol, so after any shock it goes most negative precisely at
> the setup §8.12.7 calls the best-paid of the year. Two rules that could not both be obeyed.

## 10a. PCR — the authority bands

Put OI ÷ Call OI, whole chain, nearest expiry. **These bands, and no others.**

| PCR | Read |
|---|---|
| **> 1.30** | Bullish |
| **1.00 – 1.30** | Mildly bullish |
| **0.80 – 1.00** | Mildly bearish |
| **< 0.80** | Bearish |

**No gaps — every value classifies.** That is the point of the row. Five mutually incompatible PCR
schemes were in this repo on 02-Sep-2026 (`Market_View.md` alone carried three), and between them
they left **0.70–0.90 unclassified** — so a PCR of 0.85 could be read as neutral, mildly bearish, or
nothing at all depending on which file was open. A band scheme with a hole in it is not a filter; it
is a place to put whatever you already wanted to believe.

**How to use it — three constraints:**

- **PCR is a Gate 4 input, never a direction on its own.** It colours one row of the Go/No-Go score.
  It does not classify the five-view.
- **The slope matters more than the level.** A PCR falling through the day is call writers arriving;
  the absolute number tells you much less than its direction since 9:30.
- ⛔ **A PCR reading may colour exactly one Go/No-Go row.** It shares inputs with the OI rows, and
  the disjoint-input rule (§6) exists precisely so one number cannot manufacture three "distinct" reds.

> **Expiry week caveat:** PCR compresses toward 1.0 as OI concentrates into the expiring series.
> Inside the last two sessions, treat 0.90–1.10 as uninformative rather than as "mildly" anything.

## 10b. VRP — the "am I being paid at all" test  *(ruled 03-Sep-2026)*

Same-session, same-tenor, so it avoids the tenor mismatch that killed the `IV − HV20` rule above.
**Procedure** (how to measure it) is `references/basis-check.md`; the numbers are here.

```
realised (pts/min) = (day high − day low) ÷ minutes elapsed since 9:15
implied  (pts/min) = ATM straddle × 1.25 ÷ minutes remaining to expiry close
RATIO              = realised ÷ implied
```

| RATIO | State | Effect |
|---|---|---|
| **≥ 1.0** | **NEGATIVE VRP** | ⛔ **NO TRADE — reason code `UNPAID`.** Stop before pricing any strike. |
| 0.8 – 1.0 | THIN | Permitted, but the §6 c/W and noise-floor filters will usually kill it anyway |
| < 0.8 | PAID | Normal premium-selling conditions |

**Run this BEFORE pricing strikes**, not after. *03-Sep-2026: SENSEX realised 2.38 pts/min against
implied ~1.40 — a ratio of **1.7** — and all six candidates failed simultaneously. Ninety minutes
went into testing structures that were all failing for the same reason.*

> **Why this earns its own code.** A credit seller is long IV and short RV; the edge *is* the variance
> risk premium, and it is normally positive (Carr & Wu 2009). When realised exceeds implied the
> premium is negative and the structure is underpaid for risk it is definitely taking. Nothing about
> the strike, the width or the size fixes that — which is exactly why it must not be logged as
> `Too thin`. See §15 and `references/no-trade.md`.

## 11. What is locked, and the key for each

Current status: **one recorded instance of a stop being reached. It was not honoured.**

| Locked | Unlock |
|---|---|
| Caps above §3 | 20 consecutive trades, zero behavioural violations, positive rolling-20 net → structural cap to 2%. At 40 trades → 2.5%. **Ceiling 3% forever.** |
| 4-leg structures | 30 completed verticals, ≤1 violation, median entry-to-SL-live ≤ 90s over the last 10 |
| Scaling out / trailing stops | 20 trades with every exit coded TARGET / STOP / TIME |
| BANKNIFTY | 30 net-positive NIFTY/SENSEX trades, then final 5 sessions of the monthly cycle only, 1 lot for the first 10 |
| Two structures in one day | Not at this capital. Revisit at ₹20L+. |
| Discretionary early exit | 20 trades with zero discretionary closes, then one/month logged as `DISC` and scored |
| `k` wider than 2.0 | ⛔ **Never.** Widening the stop is the mechanism of the −₹15,564. |
| The 1%-per-session target | ⛔ **Never.** See §2. |

## 12. Behavioural circuit-breaker — 5-session halt, even if the trade was PROFITABLE

Any one of: **(a)** stop triggered, not executed within 5 min · **(b)** stop moved away from the
market · **(c)** any order increasing short exposure · **(d)** position held past the hard flat
time · **(e)** trade opened with no live SL order · **(f)** more than one structure in a day.

> **01-Sep-2026, violation (c):** 9th lot sold at ₹11.45 at **13:11** — one minute before the exit
> call. That lot alone **−₹1,589**. Gates A1–A3 (now §6 rows 1–4) would have blocked it mechanically.

> Punishing process independent of outcome is deliberate. +₹3,331 on 31-Aug and −₹15,564 on
> 01-Sep may be the same behaviour with different luck. Punish only the losing version and the
> record teaches you that discretion works half the time — the exact lesson that produces the next one.

## 13. Contract specs and friction

| Index | Exchange | Lot | Expiry |
|---|---|---|---|
| NIFTY 50 | NSE | **65** | Every Tuesday |
| SENSEX | BSE | **20** | Every Thursday |
| BANKNIFTY | NSE | **30** | ⚠️ **Monthly only** — last Tuesday |

⚠️ **Always fetch the expiry list. Never guess or infer a date.**

| Friction | Value |
|---|---|
| Entry slippage | **0.5 pt/leg** — limit order at mid, calm tape |
| **Stop-exit slippage** | **2.0 pt/leg** — fast tape, manual, cross-application. *Use this one in the feasibility and noise-floor gates.* Observed 01-Sep: **23.85 pts** between the exit call and the fill. |
| Charges, round trip, 2-leg | ~**₹150** |

## 14. Greeks and IV

| | |
|---|---|
| ⛔ **Unavailable** | Δ Γ Θ V and IV. Dhan computes them off **spot, not the forward**; CE IV ≠ PE IV at the same strike. **No delta band may be quoted anywhere.** |
| ✅ **Permitted (arithmetic, not models)** | `F = K + C − P` · ATM-forward straddle `≈ 0.7979 × F × σ√T` · HV from Kite candles · §8.7.3 straddle-rule strikes |
| ⛔ **Not permitted** | Solving Black-Scholes for Δ/Γ/Θ/V, or presenting a derived figure as a vendor figure |
| ★ **The substitute** | **`credit ÷ width` ≈ the short strike's delta.** As width narrows a vertical's price → Δ × W exactly. It is model-free, vendor-free, and nobody can break it. **Use it wherever the book asks for a delta.** |

**Chain-price substitutes for every delta trigger in §8:**

| Book says | Use instead |
|---|---|
| Sell the 16Δ strike | §8.7.3 straddle rule on the parity forward `F` |
| Untested short "below 7Δ" | Untested short's mark ≤ **25%** of its entry premium |
| Short "reaches 30Δ" | Tested short's mark ≥ **2.5×** its entry premium |
| Net position delta > ±0.15/lot | Tested short's mark ≥ **3×** the untested short's mark |
| Deep-ITM rows showing Δ=0 / IV=0 | **Discard the row** — missing data, not zero risk |

## 15. Per-trade log — mandatory fields

`date · index · expiry · sessions-to-expiry · entry HH:MM · exit HH:MM · short strike · long
strike · width · lots · credit/lot · net credit ₹ ·` **`credit÷width`** `· spot · F · VIX · ATM
straddle ·` **`planned stop (spread price, short-leg trigger, ₹, % capital) recorded BEFORE
entry`** `· structural max loss ₹ and % ·` **`SL ORDER ID + "Trigger Pending" timestamp`** `·
exit code ·` **`MAE · MFE`** `· gross/costs/net/% · R-multiple · which filter failed`

**Exit code — exactly one, no free text:** `TARGET` / `STOP` / `TIME` / `VIOLATION`.
*Free text is where rationalisation lives; a closed vocabulary means `VIOLATION` cannot be
relabelled "discretionary exit based on price action."*

**No-trade code — exactly one, no free text:** `Too dangerous` / `Too small` / `Too thin` /
**`UNPAID`** *(adopted 03-Sep-2026, §10b)*. Each names a **different thing that must change** —
regime · calendar · structure · vol pricing. Pick by what would fix it, not by how the day felt.
Detail in `references/no-trade.md`.

**Log the no-trade days too**, with the failing filter code. ~75% of sessions are no-trades and
that decision record is currently invisible.
**Report violation count ABOVE P&L in every weekly review.** Violations lead; P&L lags.
**Frequency governor:** < 4 trades in a month → filters too tight, review at month end.
**Never loosen a filter mid-month.**
