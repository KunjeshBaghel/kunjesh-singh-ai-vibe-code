# Long Call Strike-Selection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the Long Call reference with a practical, Indian-market framework for selecting a strike when the intent is to close the option for profit before expiry.

**Architecture:** Add one self-contained subsection beneath the existing Long Call strategy. It will separate intraday and positional use cases, rank option-chain fields by purpose, and give scenario calculations without presenting a fixed delta range as a guarantee.

**Tech Stack:** Markdown; external educational references from NSE and Zerodha Varsity.

## Global Constraints

- Modify only `kb/kb1/strategy_ref_book.md`.
- Preserve the existing Long Call definition and basic payoff example.
- State that the content is educational decision-support, not a profit guarantee or a live-trade recommendation.
- Use Indian option terminology: CE, OI, IV, and NSE/BSE.
- Do not prescribe order placement or a real trade.

---

### Task 1: Add the long-call strike-selection reference

**Files:**
- Modify: `kb/kb1/strategy_ref_book.md:414-427`
- Test: rendered Markdown inspection of the edited subsection

**Interfaces:**
- Consumes: the existing `##### 1.1 Long Call CE (buy CE)` entry and its current payoff example.
- Produces: a `###### Selecting a Long Call ...` subsection that follows the Long Call entry and precedes `##### 1.2 Long Put PE (buy PE)`.

- [ ] **Step 1: Add the decision principle and column priority**

Insert content that says a long-call buyer closing before expiry must define the target, deadline, IV outlook, and risk budget before choosing a strike. Specify that delta selects directional exposure; theta, IV/vega, liquidity, OI/volume, and premium filter the candidate strikes.

- [ ] **Step 2: Add the trader-category matrix**

Document these non-guaranteed ranges and reasons:

```markdown
| Trader category | Typical holding period | Usual CE moneyness / delta | Primary reason |
|---|---:|---|---|
| Intraday momentum or breakout | Minutes to a day | ATM to slightly OTM / 0.40–0.60 | Balances fast response and leverage. |
| Intraday trend continuation | Hours | ATM to slightly ITM / 0.50–0.70 | Prioritises dependable directional response. |
| Short swing | 2–5 sessions | ATM to slightly ITM / 0.55–0.70 | Reduces dependence on a sudden, very large move as theta accumulates. |
| Positional bullish | 1–3 weeks | ITM / 0.65–0.80 | More underlying-like exposure and less dependence on extrinsic value. |
| Event / catalyst | Before or after a defined event | ATM to slightly ITM / 0.50–0.65 | Requires an explicit IV and implied-move plan. |
| Low-premium speculation | Any | Far OTM / below 0.30 | High-convexity speculation, not a standard income approach. |
```

- [ ] **Step 3: Add strike-selection calculations and filters**

Include the approximate pre-expiry scenario formula:

```text
Option P&L ≈ (Delta × underlying move) + (0.5 × Gamma × underlying move²)
             + (Vega × IV change in percentage points) + (Theta × days held)
             − bid–ask cost − charges
```

Clarify that Greeks and IV change continuously, so this is a planning estimate, not a prediction. Include the NIFTY 22,000 comparison example of an ITM 0.65-delta, ATM 0.50-delta, and slightly OTM 0.32-delta CE, clearly labelling all premiums and Greeks as hypothetical.

- [ ] **Step 4: Add trade-management requirements and sources**

Add a pre-entry checklist: target and deadline; expiry; delta/moneyness; IV context; narrow bid–ask spread and adequate live liquidity; maximum rupee loss; underlying-level invalidation; premium stop; target; and time stop. State that OI/volume provide context and liquidity confirmation, but do not independently choose a strike. Link to NSE Greeks education and Zerodha Varsity on delta, theta, and strike selection.

- [ ] **Step 5: Verify Markdown structure**

Run:

```bash
sed -n '412,560p' kb/kb1/strategy_ref_book.md
```

Expected: the Long Call section retains its original definition and payoff example; the new subsection begins after the existing sources; `##### 1.2 Long Put PE (buy PE)` remains the next strategy heading; Markdown tables, formulas, and links are readable.

- [ ] **Step 6: Review editing diagnostics**

Run the editor diagnostics for `kb/kb1/strategy_ref_book.md`.

Expected: no new Markdown diagnostics caused by the added reference section.
