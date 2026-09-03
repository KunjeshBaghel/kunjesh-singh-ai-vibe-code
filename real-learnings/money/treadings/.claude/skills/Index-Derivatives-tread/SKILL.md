---
name: Index-Derivatives-tread
description: |
  NSE/BSE F&O index options trading copilot for NIFTY50, BANKNIFTY, and SENSEX. Invoke with /Index-Derivatives-tread <sub-command>. Use this skill whenever the user says anything about today's trade, market analysis, open positions, session wrap-up, lot sizing, expiry check, or options trading workflow. Sub-commands: analyse-today | find-trade | followup | session-close | size-it | check-expiry | basis-check | no-trade. Trigger on: "analyse today's market", "what should I trade", "check my positions", "close the session", "how many lots", "when does nifty expire", "calculate sizing", "no trade today" — and any variant. This skill covers the full intraday trading lifecycle from pre-market setup to post-session learning.
---

# Index-Derivatives-tread

Professional options-trading copilot for Indian index derivatives, covering the intraday lifecycle from
pre-market setup to post-session learning.

**This file is a router. Do not answer from it.** Identify the sub-command, load exactly the files in its
row, and work from those.

---

## Sub-command → load exactly these

Paths are relative to this skill directory. `TC` = [`TRADING_CONSTANTS.md`](../../../TRADING_CONSTANTS.md)
at the repo root — **load it for every sub-command**; it holds every number and outranks every other file.

| User says | Sub-command | Load |
|---|---|---|
| `analyse-today` · "analyse today" · "market view" · "today's data" | **analyse-today** | TC · `references/analyse-today.md` · `references/brokers.md` · `references/dhan-api.md` · `references/gates.md` |
| `find-trade` · "any good trade" · "what to trade" · "best position" | **find-trade** | TC · `references/find-trade.md` · `references/gates.md` · `references/dhan-api.md` · `references/kill-switch.md` · `references/size-it.md` · `references/entry-exit-orders.md` · `references/trade-log.md` |
| `followup` · "check positions" · "how is my trade" · "recheck" | **followup** | TC · `references/followup.md` · `references/kill-switch.md` · `references/adjustments-are-closed.md` · `references/entry-exit-orders.md` · `references/dhan-api.md` |
| `session-close` · "close session" · "I closed the trade" · "wrap up" | **session-close** | TC · `references/session-close.md` · `references/trade-log.md` |
| `size-it` · "how many lots" · "lot sizing" · "sizing" | **size-it** | TC · `references/size-it.md` |
| `check-expiry` · "when does X expire" · "expiry dates" | **check-expiry** | TC · `references/check-expiry.md` · `references/dhan-api.md` |
| `basis-check` · "what is the forward" · "check basis" | **basis-check** | TC · `references/basis-check.md` · `references/dhan-api.md` |
| `no-trade` · "no trade today" · "standing down" · "decided not to trade" | **no-trade** | TC · `references/no-trade.md` · `references/trade-log.md` |

**Read the reference files immediately after identifying the sub-command. Do not proceed without them,
and do not load rows you were not asked for.**

If the ask spans two sub-commands, run them in sequence and load each row when you get to it.

---

## The two things true of every sub-command

**1 · Verify the brokers first.** Before any data fetch, verify each MCP with a call that exercises the
capability you actually need — a successful login proves nothing about the data endpoints, and a
populated field is not a verified field. Procedure: `references/brokers.md`. If a broker fails, say
exactly what is missing and what it blocks, and do not run analysis that depends on it.

**2 · Every session appends to `tread.md` and ends with `learning.md`** — including no-trade days.
Learning is part of every session, not a separate request. The four required artefacts are listed in
`references/trade-log.md`.

Everything else — every number, gate, filter, veto and lock — lives in `TRADING_CONSTANTS.md` and in the
reference file for the job at hand.
