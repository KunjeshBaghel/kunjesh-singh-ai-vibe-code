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

Gate 1 blocks when sessions_to_expiry ≥ 3.
```

**Holidays:** derive from gaps in the fetched expiry list + the NSE calendar. **If a day's status is uncertain, COUNT it as a trading day** — the conservative direction.

This convention was previously implicit and differed by one between files, which flips the gate in both directions. On Fri 28-Aug-2026: NIFTY 01-Sep (**2**), SENSEX 03-Sep (**4**), BANKNIFTY 29-Sep (**22**) — no 0-DTE instrument existed anywhere, which alone decided the session.

## Output format

```
| Index | Nearest expiry | Calendar days | Sessions | Gate 1 verdict |
|---|---|---|---|---|
| NIFTY 50 | <date> | <N> | <M> | <verdict> |
| SENSEX | <date> | <N> | <M> | <verdict> |
| BANKNIFTY | <date> (monthly) | <N> | <M> | <verdict> |

Gate 1 (§8.11.6) verdicts — a BINARY gate:
  sessions = 1  (expiry day)  → ✅ TRADEABLE. Full theta today.
  sessions = 2  (expiry eve)  → ⚠️ TRADEABLE ONLY with a Gate-5-clean directional view.
                                 Delta-driven, not theta-driven. State the required move in POINTS.
  sessions >= 3               → ⛔ NO TRADE on this index. Hard stop.
```

⛔ **Do not attach a quoted return to any verdict.** The old table said "2–3 DTE: 0.5–0.75% realistic" — which turned a hard STOP into a tradeable ⚠️ with a number attached to reach for. At 3+ sessions intraday theta is a rounding error; there is no smaller percentage that makes it a trade.

## BANKNIFTY is never the fallback

**BANKNIFTY fails Gate 1 by construction on all but the final ~2 sessions of the expiry month.** Screen it, state `BANKNIFTY: N sessions → Gate 1 ⛔, excluded` in one line, and do not price it.

⛔ **It is never the fallback when NIFTY and SENSEX are both blocked.** Two blocked indexes plus a structurally blocked third is a **no-trade day**, not a BANKNIFTY day.

Both majors blocked = **no trade today**, which is the correct and common answer (~75% of sessions).

---

## Logging

After completing, append to today's tread.md:

```
09:20 — check-expiry: NIFTY 1 session ✅, SENSEX 3 sessions ⛔, BANKNIFTY 22 sessions ⛔ → NIFTY only
```
