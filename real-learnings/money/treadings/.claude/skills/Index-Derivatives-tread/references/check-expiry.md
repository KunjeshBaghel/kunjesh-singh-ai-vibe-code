**Sub-command:** check-expiry

Expiry resolution and calendar feasibility (Gate 1).

---

## Trigger

"when does NIFTY expire", "check expiry", "expiry dates", "how many sessions left"

## Method

⛔ **Always fetch the expiry list; never guess or infer a date.** A guessed date returns *Invalid Expiry Date* (Dhan) and — far worse — a *plausible* wrong one silently prices the wrong contract.

Fetch expiry lists for all 3 indexes in parallel (see `references/dhan-api.md` for the call):

```
NIFTY:     UnderlyingScrip=13, UnderlyingSeg=IDX_I
BANKNIFTY: UnderlyingScrip=25, UnderlyingSeg=IDX_I
SENSEX:    UnderlyingScrip=51, UnderlyingSeg=IDX_I
```

## Expiry schedule

| Index | Exchange | Expiry Day |
|---|---|---|
| NIFTY 50 | NSE | Every Tuesday |
| SENSEX | BSE | Every Thursday |
| **BANKNIFTY** | NSE | ⚠️ **MONTHLY ONLY — last Tuesday** (post-2024 SEBI) |

**Monthly contracts** expire the last Tuesday (NSE) / last Thursday (BSE) of the month. A holiday shifts expiry to the **PREVIOUS trading day**.

From [`TRADING_CONSTANTS.md` §13](../../../../TRADING_CONSTANTS.md).

## ★ The canonical counting convention

Count trading **sessions**, not calendar days.

```
sessions_to_expiry = trading sessions remaining INCLUDING TODAY, up to and including expiry.

    Expiry day itself  →  1     (= "0-DTE")
    Expiry eve         →  2     (= "1-DTE")

sessions_to_expiry is an INPUT, not a gate. It sets the holding period N.
⛔ The old "Gate 1 blocks when sessions_to_expiry ≥ 3" is RETIRED (04-Sep-2026, TC §6 row 1).
```

**Holidays:** derive from gaps in the fetched expiry list + the NSE calendar. **If a day's status is uncertain, COUNT it as a trading day** — the conservative direction.

This convention was previously implicit and differed by one between files, which flips the gate in both directions. On Fri 28-Aug-2026: NIFTY 01-Sep (**2**), SENSEX 03-Sep (**4**), BANKNIFTY 29-Sep (**22**) — no 0-DTE instrument existed anywhere, which alone decided the session.

## Output format

```
| Index | Nearest expiry | Calendar days | Sessions | Max holding period |
|---|---|---|---|---|
| NIFTY 50 | <date> | <N> | <M> | <M sessions, to <date>> |
| SENSEX | <date> | <N> | <M> | <M sessions, to <date>> |
| BANKNIFTY | <date> (monthly) | <N> | <M> | <min(M,10) sessions, to <date>> |

Sessions is an INPUT. It bounds the declarable holding period; it does not pass or fail an index.
  sessions = 1  (expiry day)  → intraday by necessity. Full theta today.
  sessions = 2  (expiry eve)  → declare intraday OR hold to expiry.
  sessions >= 3               → declare intraday OR hold N sessions. NOT a block.

  ⛔ MAX DECLARED HOLD = 10 sessions (TC §11 slot limit — one open structure at a time).
     If sessions > 10, the hold is capped at 10 and you exit BEFORE expiry.
     → model EV to the DECLARED EXIT, not to expiry: partial decay, and you pay to close.
     This bites BANKNIFTY most (monthly only, typically 15-22 sessions out).

⛔ Whether ANY of these is tradeable is decided by the vol-band / VRP gate, not by this table.
   NIFTY, SENSEX: India VIX outside 13-20 → no trade.        [TC §6 rows 1a / 8]
   BANKNIFTY:     its OWN sigma_ATM outside 16-25 → no trade. India VIX does NOT apply.
```

⛔ **Do not attach a quoted return to any verdict.** The old table said "2–3 DTE: 0.5–0.75% realistic" — a number attached to reach for. State the required move in POINTS and the declared holding period; never a promised percentage.

> **What changed, 04-Sep-2026.** This file used to say *"At 3+ sessions intraday theta is a rounding
> error."* That was true **and irrelevant** — it was an argument against holding a 3-DTE structure
> *intraday*, which nobody now proposes. With multi-session holds permitted (TC §1a), the structure
> is held until its theta actually arrives. Measured: holding period moves EV by ~2 points; VIX moves
> it by ~20. The block was on the wrong axis.

## No index is "the fallback"

**All three indexes are tradeable and all three are screened every session** — BANKNIFTY was unlocked
04-Sep-2026 ([`TRADING_CONSTANTS.md` §11a](../../../../TRADING_CONSTANTS.md), CLAUDE.md SI-7a).
Screen them together, from the start, each on its own gates.

⛔ **Never reach for an index *because* the others failed.** "Fallback" reasoning is how a structure
gets taken for wanting a trade rather than for having an edge. Run BANKNIFTY's gate and let it answer
the same way it would have if NIFTY had passed.

**All three blocked = no trade today**, which is the correct and common answer (~75% of sessions).

---

## Logging

After completing, append to today's tread.md:

```
09:20 — check-expiry: NIFTY 02-Sep (1 sess, hold<=1) · SENSEX 04-Sep (3, hold<=3) ·
        BANKNIFTY 29-Sep (22, hold capped at 10) → all three carried to the vol-band gate
```
