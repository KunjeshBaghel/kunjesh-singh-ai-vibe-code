# Entry and exit — the order mechanics

**Loaded by:** `find-trade` (before entry), `followup` (while in the trade).
**Purpose:** the exact order sequence at entry, the stop-loss order, and the exit clock.

⛔ All times, multiples and rupee figures are quoted from
[`TRADING_CONSTANTS.md`](../../../../TRADING_CONSTANTS.md) §7–§8. If they disagree, TC wins.

---

## The one rule this file exists for

> **The stop is an ORDER, not an intention.**
>
> On 01-Sep-2026 the stop was computed correctly, called on time at 13:12, and **not executed**.
> Exiting at the trigger cost **₹1,865**. Holding cost **₹15,564** — **8.3×**. Re-run the whole book
> with that one stop honoured and **−₹11,247 becomes +₹2,252.** Nothing else in this rulebook is
> worth ₹13,700.

⛔ **A position is not open until its exit order is resting at the broker. No stop order, no trade.**
⛔ **A trade whose log has a blank SL-order-ID field is an unauthorised trade, regardless of its P&L.**

---

## Entry sequence — all of it inside 90 seconds of the fill

Execution is **manual in the Kotak Neo app**. The Kotak MCP is read-only by design and has no order
tools; Kite and Dhan can place orders but require explicit user confirmation first (SI-3).

```
1. BUY the long leg (NRML) → WAIT for fill confirmation.
      ⚠️ Placing the SELL before the BUY fills makes Kotak see a naked short:  RMS:Margin Exceeds.

2. SELL the short leg → confirm fill.

3. SL-LIMIT BUY-TO-CLOSE on the SHORT LEG ONLY.  ⛔ Never SL-M — SL-M on options is a trap (§8.10).
      trigger = short_leg_entry_price + k × (net credit per lot, in points)          [k: TC §4]
                ↳ the net captures only ~62% of the short leg's move; k is the gross-up that puts
                  the SPREAD at k × credit when the leg hits the trigger.
                  Verify against the live chain before placing. Adjust the trigger, not the rule.
      limit   = trigger + max( 12% of trigger , 2 pts NIFTY/BANKNIFTY , 5 pts SENSEX )
                ↳ 12% ≈ 6–8 bid-ask spreads of headroom. A 1–2% buffer is how an SL-Limit quietly
                  fails to fill — a close cousin of the 01-Sep failure.

4. ALERT on the INDEX at the short strike                → mandatory review; close unless at target.
5. ALERT on the INDEX at short strike + 0.5 × width      → close BOTH legs immediately, no thinking.
                                                            Layer 5 exists because Layer 3 can miss.
6. LOG the SL ORDER ID and the timestamp it read "Trigger Pending".
```

⛔ **If the SL-Limit is rejected or cannot be placed for any reason — close the position at market
immediately**, even at a loss, even if the trade still looks good.

---

## Stopping out

**Stop the SHORT leg only.** §8.10's warning is about stopping *both* legs, which un-hedges you. Buying
back the short and keeping the long leaves a cheap OTM option — defined risk, and it pays if the move
continues. That residual is safe.

**On a stop-out, BUY BACK THE SHORT FIRST, then sell the long.** The reverse order leaves you
momentarily naked.

⛔ **The trigger may only ever be moved DOWN (less risk).** Moving a stop away from the market is the
exact mechanism of the −₹15,564, and it trips the behavioural breaker (TC §3) on its own.
**The stop does not move for the life of the trade.**

When it is going against you, the permitted actions are severely limited — see
**[`adjustments-are-closed.md`](adjustments-are-closed.md)** before doing anything at all.

---

## The exit clock — one time per index, a phone alarm, not a mental note

Canonical times: **TC §7**. Summary of the shape:

| | |
|---|---|
| Entry window | one window; **no new position after it closes, ever** |
| Midday time stop | if capture is below the floor, close at market |
| NIFTY / BANKNIFTY | one hard-flat time |
| SENSEX | one hard-flat time, earlier |
| CAS | nothing ever survives into it |

⛔ **There is no later "hard" time.** The old two-tier *target 2:30 / hard 3:00* scheme is **DELETED**.
Publishing a later time guarantees the later time gets used on the day the position is red at the first
one — the only day it matters. *20-Jul-2026 exited ~3:16 PM, inside the CAS, using exactly that latitude,
and it was never flagged. 01-Sep exited 14:51 against a 2:30 plan.*

**Why the midday time stop:** a spread that has not decayed by midday is pinned near your short strike —
maximum gamma for expired theta, the worst risk-per-rupee on the board. It does not improve after lunch.

**Scope after 04-Sep-2026 (TC §1a, §7):** the midday time stop and the hard-flat times bind on
**intraday-declared** trades, and on the **final session** of a multi-session hold. They do not bind on
the intermediate sessions of a hold that was declared multi-session *at entry*. Nothing here licenses
converting an intraday trade into a hold because it is red at 2:30 — **that is a §12 violation (g)**,
and it is precisely the latitude the deleted two-tier scheme used to grant.

---

## ⚠️ The stop does not survive the night

**An SL-Limit order does not rest overnight and cannot fire on a gap.** On any hold that crosses a
session boundary this is the single most important fact about your risk:

| | Intraday hold | Multi-session hold |
|---|---|---|
| Planned stop ₹3,500 (TC §3) | enforceable all day | **enforceable only during market hours** |
| Structural cap ₹10,500 (TC §3) | backstop | **the real overnight backstop — and it holds** |

It holds because a defined-risk vertical's loss is bounded at `(width − credit) × lot × lots` no matter
how far the index gaps. TC §3 set the structural cap **equal to** the daily breaker specifically so that
*total failure of the stop* still lands inside the day's limit — and an overnight gap **is** total
failure of the stop. That scenario was sized for before it was permitted.

**What this means in practice, every session of an open hold:**

```
□ At 9:15, before anything else: check the open hold's mark against the gap.
□ RE-PLACE the SL-Limit order at the open. It is NOT still there from yesterday.
      A hold sitting through a session with no live SL order = §12 violation (e).
□ Run that session's kill-switch checks (TC §7). Deferring the EXIT is permitted;
      deferring the MONITORING is not — §12 violation (h).
□ Do NOT widen the stop because the gap moved it closer. Widening is the mechanism
      of the -Rs15,564 (TC §11: k > 2.0 is never unlocked).
```

**Sizing already assumes the gap.** Do not size a multi-session hold against the ₹3,500 stop and
reassure yourself with the ₹10,500 cap. Size so that **the structural cap itself is acceptable**, because
on a gap night that is the number you get. Empirically (1 yr NIFTY, TC §1a): median overnight gap 56 pts,
p90 192 pts, worst **731.5 pts**.

---

## Taking profit — ONE exit, no scaling, no trailing

Close at the target capture (TC §8) or at a time stop, whichever comes first.

> *Adjudication:* the textbook-optimal rule for a disciplined trader is scale half at 40%, then trail the
> remainder to breakeven. **It is rejected here.** Scaling and trailing add two more manual decisions
> under P&L pressure in a mobile app, and this book's demonstrated failure mode is freezing on exactly
> one such decision. A breakeven trail also contradicts §8.15.1 ("the stop should sit 1.5× beyond typical
> MAE"), and §8.11.7's own case study shows a spread reaching **95% of its stop and finishing +1.25**.
> Revisit scale-outs after 20 clean trades — the unlock is in TC §3.
