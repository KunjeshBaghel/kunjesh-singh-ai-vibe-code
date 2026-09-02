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

## 2. Return target

| Constant | Value |
|---|---|
| **Target** | **2–4% per month = ₹14,000–28,000**, measured as a rolling 3-month mean |
| ⛔ Retired | **"~1% net per session" is DELETED.** It is ~250% annualised. Under a 0.5% stop cap it needs 200% capture of the credit — not a reachable number. Keeping it on the wall guarantees size creep at the worst possible moment. |
| Honest per-session expectancy | **₹1,274 (0.20%)** — `strategy_ref_book.md` §8.11.5 |
| First 3 months | **The target is a violation count of zero, not a rupee number.** |

## 3. Risk caps — all hard, none discretionary

| Constant | Value | Note |
|---|---|---|
| **Structural max loss, per structure** | **₹10,500 (1.5%)** | `(width − credit) × lot_size × lots`. Set EQUAL to the daily breaker so that *total failure of the stop* still lands inside the day's limit. **The only cap that does not depend on you pressing a button.** |
| **Planned stop loss, per structure** | **₹3,500 (0.5%)** | Three consecutive stops = the daily cap |
| **Daily realised loss** | **₹3,500 → day over.** **₹10,500 → day over + next session is a mandatory no-trade day** | |
| **Weekly realised loss** | **₹21,000 (3.0%)** | Week over, following week paper-only |
| **Monthly realised loss** | **₹28,000 (4.0%)** | Calendar month over |
| **Structures per calendar day** | **ONE.** Not one at a time — one per day. | Closing at 10:30 does not buy a second slot |
| **Margin cap** | 40% (₹2,80,910) | A backstop only. With the ₹10,500 structural cap this will never bind — a permitted spread blocks ~₹10–12K of margin. **Margin is not a sizing input.** |

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
| NIFTY (65) | 200 | ~₹12,546 | **0** | ⛔ **banned — cannot carry size at this capital** |
| SENSEX (20) | **100** | ~₹1,620 | 6 | ✅ best granularity in the book |
| SENSEX (20) | 200 | ~₹3,157 | 3 | ✅ |
| BANKNIFTY (30) | 200 | ~₹4,320 | 2 | ⚠️ locked — see §11 |

## 5. Permitted structures

| | |
|---|---|
| **Permitted** | **The one-sided defined-risk credit vertical. Two legs. That is the entire list.** |
| ⛔ Locked | Iron condors and every 4-leg structure — two gamma exposures you cannot measure and two stop orders to place by hand. Unlocks per §11. |
| ⛔ Never | Naked shorts · ratios · calendars · ladders · "repair" structures · martingale sizing |
| **Leg counts** | `short qty == long qty`, exactly. A mismatch is a rejected order, not a strategy. |

## 6. Entry filters — every one is a veto

| # | Filter | Threshold |
|---|---|---|
| 1 | Sessions to expiry | **≤ 2** (count sessions, never calendar days; always fetch the expiry list) |
| 2 | **Credit ÷ width** | **≥ 15%**, 20%+ preferred. *Tail control: at 3.5% max loss is 28× the credit; at 20% it is 4×.* |
| 3 | Net credit, total | **≥ ₹2,500** (round-trip friction ~₹150) |
| 4 | **Stop reachability** | **`k × credit < width`**. Above `c/W = 1/k` the premium stop sits beyond max loss and can never trigger. |
| 5 | Noise floor | `(k−1) × credit ≥ 1.5 × the SHORT leg's 30-min intra-bar swing`, opening gap bar excluded |
| 6 | Combined bid-ask, both legs | **≤ 15% of net credit** |
| 7 | Top-of-book depth | **≥ 5× your lot count**, both legs, both sides |
| 8 | India VIX level | **< 20**. ≥ 20 → HOSTILE → no trade. |
| 9 | India VIX change on the day | **≤ +8%** at entry. Above → event day, not a decay day. |
| 10 | Basis | `F = K + CE − PE` at 3–4 near-ATM strikes must agree within ~1 pt. `basis = F − spot`; **> 0.1% of spot** → discard any vendor delta, use the §8.7.3 straddle rule on `F`. |
| 11 | Go/No-Go (`option_chain_n_greeks.md` §7) | **3+ RED → sit out** |
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

> **The old "target 2:30 / hard 3:00" two-tier scheme is DELETED.** Publishing a later time
> guarantees the later time gets used on the day the position is red at 2:30 — the only day
> it matters. **One time. Set a phone alarm, not a mental note.**

## 8. Exit mechanics

| Constant | Value |
|---|---|
| **Stop multiple `k`** | **1.6** (credit vertical — the only permitted structure) |
| **Profit target** | **50% of net credit.** One exit. No scaling, no trailing. |
| **The stop does not move** for the life of the trade — except **down** (less risk). |
| **Stop order** | **SL-LIMIT, buy-to-close, SHORT LEG ONLY.** Never SL-M (§8.10: a trap on options). Never any standing order on the long leg. |
| **Trigger** | `short_leg_entry + 1.6 × (net credit per lot, in points)` — the net captures ~62% of the short leg's move; verify against the live chain and adjust the *trigger*, not the rule |
| **Limit** | `trigger + max(12% of trigger, 2 pts NIFTY/BN, 5 pts SENSEX)` |
| **Placed within** | **90 seconds of the entry fill**, plus two index alerts: one at the short strike, one at `short strike + 0.5 × width` |
| ⛔ | **No live SL order → close at market immediately.** A blank SL-order-ID in the log = an unauthorised trade regardless of P&L. |
| **Stop-out sequence** | **Buy back the SHORT first**, then sell the long. Reverse = momentarily naked. |

## 9. Direction — Gate 5 participant thresholds

`net_CE_short = |CE Short| − |CE Long|`, and the put equivalent, for **FII and Pro separately.
FII is read first — FII is the primary trend setter.**

| Reading | Meaning |
|---|---|
| **> 80,000 net short calls** (either participant) | **HARD CEILING** → Bear Call mandated, Bull Put forbidden |
| **> 80,000 net short puts** (either) | **HARD FLOOR** → Bull Put mandated |
| 50,000 – 80,000 | Strong; prefer that side |
| **< 50,000** | **SILENCE — not permission for the opposite side.** Hands the decision back to the grid. |
| Net **LONG** both CE and PE **> 100,000** | Long gamma → **halve size or stand down** |

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

**Log the no-trade days too**, with the failing filter code. ~75% of sessions are no-trades and
that decision record is currently invisible.
**Report violation count ABOVE P&L in every weekly review.** Violations lead; P&L lags.
**Frequency governor:** < 4 trades in a month → filters too tight, review at month end.
**Never loosen a filter mid-month.**
