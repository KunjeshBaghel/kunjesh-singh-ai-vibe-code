# adjustments-are-closed.md — When it goes against you

**Loaded by:** followup (primary), find-trade (as a hard forbid reminder)

---

## The only three permitted actions

When the structure is at a loss, at any hour, on any day:

1. **Do nothing** — hold with the resting SL-LIMIT order live
2. **Close the whole structure** at market
3. **Let the resting stop fill**

That is the complete list. There is no fourth option.

---

## FORBIDDEN — no exception, no override, no "adjustment budget"

⛔ Adding lots to a position that is at or beyond its trigger.

⛔ Rolling a threatened leg to a nearer strike.

⛔ Widening, converting, or "repairing" a loser intraday.

⛔ Moving the stop further away, for any reason.

**Any order that increases short exposure in a losing structure** — roll, shift, add, average, leg into a ratio, re-enter the same side — is forbidden.

---

## War stories (the evidence)

**01-Sep-2026, 13:11** — a 9th lot was SOLD at ₹11.45, **one minute before the exit call**. The structure was already at the trigger level (₹11.00 on the 24,000 PE). That lot alone lost **₹1,589**. Total session loss: **−₹15,564** (the largest single loss in the book). The stop was computed correctly and called on time at 13:12 — but not executed. Holding instead of exiting at the trigger cost **8.3×** the trigger loss.

**24-Jul-2026** — rolled the call wing down **three times** into a 100-pt iron fly and got squeezed by the bounce.

**Other banned actions observed live:** widening a spread mid-session to "collect more credit" while it was losing; converting a losing vertical into a ratio; moving a stop further away "because it still looks fine."

---

## Why §8.9's martingale test is retired

`strategy_ref_book.md` **§8.9** is the adjustment playbook — shift the untested side, roll, hedge up, convert, cut. It includes a 4-question martingale test scoped to *"before every **roll**"*:

- **Q1:** does this roll require MORE lots?
- **Q3:** have I already rolled this side?
- **Q4:** am I rolling because of the market, or because I don't want to book the loss?

On 01-Sep-2026 at 13:11, **no leg was bought back — a 9th lot was simply sold.** That is not a roll, so Q1 and Q3 are textually inapplicable and the test does not fire.

**§8.14.3** ("Death 3 — Averaging in") names the failure and then points at this same Q1–Q4 test, which cannot catch it.

**Q4** asks the trader to self-report intent at the exact moment intent is compromised — that is decoration, not a control.

**§8.9.2** ("shift the untested side") is exempt from the test entirely, is called the workhorse adjustment, and explicitly instructs you to *collect additional credit* while a side is losing.

**Result:** the test was scoped to ONE failure mode (cascading rolls) and missed the others.

---

## Replaced by an objective test — A1–A5

Scoped to **ANY order that increases short exposure** — roll, shift, add, average, or re-enter the same side. No introspection, no judgement:

```
A1. Post-order short quantity > pre-order?          → STOP
A2. Post-order max loss (₹) > pre-order?            → STOP
A3. Position currently at negative MTM?             → STOP
A4. Any prior adjustment on this side today?        → STOP
A5. Was this order in the written pre-entry plan?   → if NO, STOP
```

**A1–A3 alone would have blocked the 13:11 fill mechanically.** No question about the market, no question about intent — just: is the short exposure increasing while the position is red? If yes, stop.

**Thresholds:** see [`TRADING_CONSTANTS.md` §12](../../../../TRADING_CONSTANTS.md).

---

## A vertical has no untested side

**§8.9.8's decision tree** branches on *"Is the OTHER side below 7Δ?"* — meaning, is the opposite wing of an iron condor or strangle safely OTM and untested by the market.

For a **one-sided credit spread** (Bull Put or Bear Call), both terminal branches of that tree are undefined. There is no "other side" — you sold one vertical, not a strangle. And 7Δ is unmeasurable here anyway (no trustworthy Greeks source).

**The tree does not apply to an intraday vertical.**

**At the stop: CUT. Zero adjustments.**

---

## On expiry day (0-DTE), §8.9 is CLOSED

**The only two permitted actions are HOLD or EXIT.**

Rolling or converting an ITM short on expiry day costs more than the original stop. On 01-Sep-2026 the 9th lot was added **six minutes after the exit trigger fired**, on expiry day, at a price above the trigger — all three failures in one order.

**§8.9's adjustment playbook is CLOSED.** It used to be described as "applies only to 2+ DTE positions, which the feasibility gate rarely permits" — an argument that leaned on Gate 1 doing the work. **Gate 1 was retired on 04-Sep-2026 (TC §6 row 1) and multi-session holds are now permitted (TC §1a), so that scaffolding is gone and the rule must stand on its own merit. It does:** adjusting a losing spread is the mechanism of the −₹15,564. A longer permitted hold means more hours staring at a red position, which makes this temptation **larger**, not smaller. **HOLD or EXIT. Nothing else, at any DTE.**

Adding lots to an expiry-day position is not "adjusting," it is martingaling.

---

## Violation consequences

Breaking any of the FORBIDDEN actions is a **behavioural violation** and triggers a **5-session halt** per [`TRADING_CONSTANTS.md` §12](../../../../TRADING_CONSTANTS.md), **even if the trade ends profitable.**

**The behavioural breaker punishes process independent of outcome, and that is deliberate.** +₹3,331 on 31-Aug and −₹15,564 on 01-Sep may well be the same behaviour with different luck. If only the losing version is punished, the record teaches you that discretion works half the time — which is precisely the lesson that produces the next −₹15,564.

Other automatic violations:
- Stop triggered and not executed within 5 minutes
- Stop moved away from the market
- Any position held past the hard exit time (see [`TRADING_CONSTANTS.md` §7](../../../../TRADING_CONSTANTS.md))
- Any trade opened with no live SL order / blank SL-order-ID in the log
- More than one structure opened in a calendar day

---

## Permitted arithmetic — not adjustments

**Put-call parity `F = K + C − P`** is arithmetic and always permitted — it does not change the position.

**§8.7.3 straddle rule** is strike selection, not an adjustment.

**A residual long option after buying back the short is safe.** When a credit spread is stopped out:
1. BUY BACK THE SHORT FIRST (always)
2. Then sell the long

You are briefly holding a cheap OTM long option — defined risk, and it pays if the move continues. That residual is **not** an adjustment and is permitted. The warning in §8.10 is about stopping *both* legs, which un-hedges you.

Reverse order (selling the long before buying back the short) leaves you momentarily naked — forbidden.

---

## Summary — the hard line

**When it goes against you:**
- The resting SL-LIMIT order is the mechanism
- You may HOLD (with the stop live) or CLOSE
- You may NOT add, roll, widen, convert, repair, or move the stop away

**On expiry day:** HOLD or EXIT only. §8.9 is closed.

**A vertical has no untested side.** The decision tree in §8.9.8 does not apply. At the stop: cut.

**Violations earn a 5-session halt, profitable or not.** The rule is about the decision, not the outcome.
