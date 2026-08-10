# Bull Call Spread Learnings Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a practical Bull Call Spread learning subsection and a matching navigation entry without duplicating existing knowledge-base material.

**Architecture:** Modify the existing strategy-reference Markdown file only. Insert one nested table-of-contents link beneath the existing Bull Call Spread entry, and insert its matching subsection immediately after the Bull Call Spread heading and before its existing definition.

**Tech Stack:** Markdown; GitHub-style heading anchors.

## Global Constraints

- Preserve all existing Bull Call Spread content.
- Do not use current market data or make a live trade recommendation.
- Treat examples as educational; point outcomes require multiplication by the current live lot size.
- Do not prescribe a universal strike distance, fixed Delta, or guaranteed profitability.
- Do not create a git commit unless the user explicitly requests one.

---

### Task 1: Add practical Bull Call Spread learnings

**Files:**
- Modify: `real-learnings/money/treadings/kb/kb1/strategy_ref_book.md:30`
- Modify: `real-learnings/money/treadings/kb/kb1/strategy_ref_book.md:495-496`
- Test: Markdown heading-anchor and diagnostics validation

**Interfaces:**
- Consumes: Existing `##### 1.3 Bull Call Spread` heading and table-of-contents link.
- Produces: A `###### Practical Learnings: Selection, Execution & Defence` subsection with a matching `#practical-learnings-selection-execution--defence` navigation anchor.

- [ ] **Step 1: Add the nested navigation entry**

Insert this line directly below the existing `1.3 Bull Call Spread` table-of-contents entry:

```markdown
        - [Practical Learnings: Selection, Execution & Defence](#practical-learnings-selection-execution--defence)
```

- [ ] **Step 2: Insert the practical learning subsection**

Immediately below `##### 1.3 Bull Call Spread`, add a `###### Practical Learnings: Selection, Execution & Defence` heading and content covering:

```markdown
- Target, deadline, maximum rupee loss, and executable liquidity before strike selection.
- ATM/slightly-ITM long CE as a starting shape; short CE at a realistic target.
- Net Delta, Theta, Gamma, Vega/IV, OI, volume, and premium priority.
- One labelled hypothetical selection example.
- No-go checks, exit/time-stop rules, and rolling as a new-trade decision.
- NSE index cash-settlement distinction and the limited but professional role of the strategy.
```

Use cross-references to `trading_jargon_acronyms.md` and other existing knowledge-base sections for concepts already documented. Include trusted-source URLs for additional claims.

- [ ] **Step 3: Verify navigation and placement**

Inspect the modified lines and ensure:

```text
The table of contents contains exactly one new nested learning entry.
The generated anchor text matches the inserted heading.
The learning subsection appears before the existing “Basic definition” bullet.
```

- [ ] **Step 4: Run diagnostics**

Run: `ReadLints` for `real-learnings/money/treadings/kb/kb1/strategy_ref_book.md`

Expected: no new Markdown diagnostics.

- [ ] **Step 5: Inspect the final diff**

Run: `git diff -- real-learnings/money/treadings/kb/kb1/strategy_ref_book.md`

Expected: only the navigation entry and the new Bull Call Spread learning subsection are changed.
