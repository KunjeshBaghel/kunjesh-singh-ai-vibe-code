# The five gates

**Loaded by:** `analyse-today`, `find-trade`.
**Purpose:** decide *whether* to trade (Gates 1–4) and *which side* (Gate 5) — **before** any chain
analysis or strike pricing. Run them in order. Skip none. Each takes about two minutes and each was
earned the expensive way.

⛔ Every threshold below is quoted from [`TRADING_CONSTANTS.md`](../../../../TRADING_CONSTANTS.md).
If this file and that one ever disagree, **the constants file wins and this file is a bug.**

---

## Gate 1 · Feasibility — is there a trade here at all?

Procedure and the counting convention: **[`check-expiry.md`](check-expiry.md)**.

```text
□ Fetch the expiry list for all 3 indexes.  NEVER guess a date.
□ sessions_to_expiry per index (including today; expiry day = 1, expiry eve = 2).
      ⛔ sessions ≥ 3  →  NO TRADE on that index. Hard stop. No smaller-size workaround.
      sessions = 2     →  delta-driven, not theta-driven. Needs a Gate-5-clean directional view.
□ MAX CREDIT = per-structure planned stop ÷ (k − 1)        [TC §4 · §6]
      ⚠️ The numerator is the PER-STRUCTURE stop, never the daily budget.
□ REQUIRED CAPTURE = the fraction of that credit the structure must actually keep.
□ If required capture > realistic capture → no structure and no size fixes it. Report and stop.
```

Estimate realistic capture against the structure's **dominant Greek**. The DTE decay table in §8.11.6
is a *theta* table, and theta stops dominating past ~10 DTE.

> ⛔ The "1% per session" target is **DELETED** (TC §2). This gate asks whether the *structure* can pay,
> not whether a daily quota can be met.
>
> **When something is out of reach, quote the capital at risk, not the shortfall.** A ratio ends the
> discussion; an adjective invites size creep.

**BANKNIFTY fails this gate by construction** on all but the final ~2 sessions of its monthly cycle.
State `BANKNIFTY: N sessions → Gate 1 ⛔, excluded` in one line and do not price it. ⛔ It is never the
fallback when NIFTY and SENSEX are both blocked — that is a **no-trade day**.

---

## Gate 2 · Basis — can you trust anything derived?

Full procedure: **[`basis-check.md`](basis-check.md)**.

```text
□ F = K + CE − PE at 3–4 near-ATM strikes.  Must agree within ~1 pt, else the chain is stale.
□ basis = F − Spot.   > 0.1% of spot → DISCARD the vendor delta band; use §8.7.3 on F.
□ Vendor sanity: one strike + one expiry = ONE IV.  CE IV ≠ PE IV → the Greeks are broken.
```

★ **Then run the realised-vs-implied rider immediately, before pricing a single strike:**

```text
REALISED = (day_high − day_low) ÷ minutes_elapsed_since_open
IMPLIED  = (ATM-forward straddle × ~1.25) ÷ minutes_remaining_to_close
RATIO    = REALISED ÷ IMPLIED        → bands in TC §10b. Read them there.
   RATIO ≥ 1.0 → VRP negative before friction. No credit structure is paid.
                 ⛔ STOP and log the no-trade as `UNPAID` — not as "Too thin".
```

*03-Sep-2026: SENSEX realised 2.38 pts/min against an implied 1.40 — **1.7×**. All six candidates failed
at once. That is the signature of negative VRP, not of a bad strike choice, and the ratio would have
reached the verdict twenty minutes and one full chain analysis earlier.*

⚠️ **A low VIX is a low-IMPLIED signal, not a cheap-vol signal.** VIX 11.10 read as "calm" while the tape
delivered a 233-pt range. Low IV with high RV is the worst tape for a seller and looks identical to the
best one on a VIX quote alone.

★ Wherever the book asks for a delta, use **`credit ÷ width`** — as width narrows, a vertical's price
→ Δ × W exactly. Model-free, vendor-free, unbreakable.

---

## Gate 3 · Kill switch — is this a trend day?

Canonical marker definitions, escalation and re-check discipline: **[`kill-switch.md`](kill-switch.md)**.

```text
□ M1 opening-range break, sustained    □ M2 VWAP one-sided    □ M3 OI confirming
   0/3 = not a trend day    1/3 = proceed only if every filter passes with margin
   2/3 = ⛔ no new position; exit if wrong-side    3/3 = ⛔ ABORT, close at market, profitable or not
□ ⛔ VIX is NOT a marker here — it is Go/No-Go row 1. Never score a 4th marker out of 3.
□ ⛔ 0/3 means "not a trend day". It NEVER means "bullish" and is never a reason to HOLD a loser.
□ ★ M2 is unmeasurable for cash indices (Kite returns volume: 0). Log the gap; never score it green.
```

---

## Gate 4 · Go/No-Go — point-scored

Row definitions: `kb/option_chain_n_greeks.md` §7. Scoring: **TC §6**.

```text
SCORE = (2 × RED) + (1 × YELLOW).       ⛔ SCORE ≥ 4  →  SIT OUT.
   (so 2 reds, or 1 red + 2 yellows, or 4 yellows, all block)

  row 1  VIX level & direction         RED at ≥ 20, or a +8% spike
  row 2  Open vs PRIOR SPOT CLOSE      ⛔ GIFT Nifty is a futures price — never compare it to spot
  row 3  OI-wall integrity at the intended short strike, vs oi_day_high
  row 4  FII regime                    needs 3 consecutive days + Net OI validation
  row 5  PCR intraday slope

□ A row with no data is YELLOW, never green. Blank ≠ clear. Unmeasured is not benign.
□ Rows must score from DISJOINT inputs. If one observation would colour two rows, score it once in
  the LOWER-NUMBERED row and mark the other `n/a — same input as row N`.
□ AUTOMATIC BLOCKERS — reject immediately, and they do NOT count toward the score:
     no five-view classification · undefined max loss · no LIVE SL order · Gate 5's table
     not written to tread.md.
```

⚠️ **The old "3+ distinct red/warning signals" wording is RETIRED.** It counted yellows in one file and
not another, and three of the five rows shared inputs, so a single VIX tick manufactured three "distinct"
reds. `kb/option_chain_n_greeks.md` §7 still carries the retired wording in three places — **TC §6
overrides it.**

★ **Score row 3 against the day's HIGH/LOW, not against spot.** A 6.97M-contract wall that price has
already penetrated is not a wall; OI size alone was reading green on 03-Sep.

---

## Gate 5 · Structure ↔ view ↔ participants — which SIDE do we sell?

Gates 1–4 decide *whether*. This one narrows *which side*, and it has cost money twice.
Thresholds: **TC §9** — read them off the file, never from memory.
Source: `python3 tools/fii-dii/fii_dii.py <YYYY-MM-DD>`, whose `GATE 5` block prints the verdict.

⛔ **Gate 5 can only FORBID. It never authorises, never mandates.** A silent Gate 5 hands the
decision back to Gates 1–4 and the five-view — it is not a green light for either side.

```text
□ 5A  Restate the five-view classification WITH A TIMESTAMP.
      A view older than 60 minutes is STALE — re-pull it. [TC §7]
      ⛔ Bull Put Spread is FORBIDDEN under Strongly / Slightly Bearish.
      ⛔ Bear Call Spread is FORBIDDEN under Strongly / Slightly Bullish.
      No override exists — not vol state, not skew, not §8.5.4 PE-first, not participants.

□ 5B  Run the fetcher and copy its four CHANGE numbers: FII and Pro × (ΔCE, ΔPE).
      ★ The basis is the T-1 vs T-2 CHANGE in net OI, from the _oi_ file.
        The LEVEL never triggers Gate 5 — it clears 80,000 on ~98% of sessions.
        The _vol_ (trading-volume) file is RETIRED as an input. TC §9 has the evidence.
      ★ FII is read FIRST and is the primary. Pro is a VETO ONLY — it may forbid, never permit.
        ΔCE ≥ limit → ⛔ Bull Put FORBIDDEN.   ΔPE ≥ limit → ⛔ Bear Call FORBIDDEN.
        Both fire → NO TRADE.   Below limit → SILENCE, not permission for the other side.
      Net LONG both CE and PE beyond the long-gamma LEVEL → halve size or stand down.
         A long-gamma book re-hedges and stays long gamma; it does not become a seller
         because one leg paid.

□ 5C  Confirm no BANNED input is carrying the directional argument:
         morning spread P&L (a widened credit spread is a BETTER entry, not a broken thesis)
         · the last three candles · kill switch 0/3 · any rule that did not fire.

★ Write 5A's sentence and 5B's numbers into tread.md BEFORE quoting a single strike.
  An unwritten Gate 5 table is a Gate 4 automatic blocker.
  ⛔ If either day's OI file cannot be fetched, Gate 5 CANNOT be scored — say so; do not estimate it.
```

**Why Gate 5 exists — two losses, one root cause:**

- **01-Sep-2026, −₹15,564** — a Bull Put Spread under a ceiling. Pro's net-CE-short rose **+109,002**
  on 31-Aug (T-1), over its 100,000 limit → Bull Put forbidden. NIFTY then broke 24,000.
  *But be honest about it:* c/W was 3.5% against a 15% floor and structural sizing already returned
  0 lots. Three gates banned that trade; Gate 5 was not the load-bearing one (TC §9).
- **02-Sep-2026** — the view was Slightly Bearish and a **Bull Put Spread** was recommended. The rule
  inspected only **Pro**, who were net *long* calls, so nothing fired. **It was checking the wrong
  participant.** FII is now explicitly primary and read first. Caught only because the user challenged it.
