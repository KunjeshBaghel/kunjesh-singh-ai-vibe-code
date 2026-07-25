# Candlestick Reference Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a bilingual, safety-first candlestick reference that teaches the basic forms shown in the existing image without presenting them as standalone trade signals.

**Architecture:** Keep all learning content in the existing `candlestick_kb.md` page. Organize it from visual recognition, to context-aware interpretation, to a compulsory pre-trade checklist so a reader encounters risk controls before considering execution.

**Tech Stack:** Markdown, existing PNG image, ASCII text diagrams.

## Global Constraints

- Use English first and short Hindi translations in parentheses.
- Include all forms labelled in `images/basic_forms_of_candlestick.png`.
- Every reversal claim requires a preceding trend and confirmation.
- Do not give autonomous trade recommendations or describe a candle as an automatic entry.
- Require a defined stop-loss, pre-set loss limit, and at least 1:2 reward-to-risk before entry.
- Include option-specific checks: underlying direction, expiry, IV, liquidity, bid-ask spread, and theta.
- Do not commit changes unless the user explicitly requests a commit.

---

### Task 1: Replace the minimal candlestick page with the bilingual reference

**Files:**
- Modify: `kb/kb2-Candlestick/candlestick_kb.md:1-7`
- Reuse: `kb/kb2-Candlestick/images/basic_forms_of_candlestick.png`

**Interfaces:**
- Consumes: the existing `basic_forms_of_candlestick.png` image.
- Produces: linked headings that serve as the page table of contents and a self-contained candlestick-learning reference.

- [ ] **Step 1: Create the page navigation and anatomy section**

Add a linked table of contents for “Candle anatomy”, “Basic forms”, “How to read formations”, “Visual guide”, “Trading significance”, and “Pre-trade checklist”. Keep the existing image and label it as a shape catalogue, not a buy/sell signal. Add an ASCII anatomy diagram with `High`, `Open`, `Close`, `Low`, `real body`, and `upper/lower wick`, followed by this rule:

```text
One candle tells a story of one period (ek timeframe ki kahani), not the next move.
Read: trend + location + volume + confirmation + risk before trading.
```

- [ ] **Step 2: Add the complete basic-forms reference table**

Create a Markdown table with the columns `Form`, `Definition (paribhasha)`, `Usual meaning`, `Valid context`, and `Do not mistake it for`. Include these exact forms: bearish candle, bullish candle, inverted hammer, shooting star, hammer, hanging man, bullish spinning top, bearish spinning top, short bullish candle, short bearish candle, bullish marubozu, bearish marubozu, long-legged doji, dragonfly doji, gravestone doji, and four-price doji. Note that the two spinning-top colour variants count as a single shape family in the image.

- [ ] **Step 3: Add context-dependent ASCII formation diagrams**

Add compact diagrams for bullish/bearish bodies, hammer versus hanging man, inverted hammer versus shooting star, spinning top/short candle, marubozu, and the four doji forms. Each diagram must include the prerequisite location:

```text
Downtrend → Hammer near support → bullish close above hammer high = possible reversal
Uptrend   → Hanging man near resistance → bearish close below its low = possible reversal
```

Explain that the same geometry changes name and interpretation based on trend/location, and that the confirmation candle is mandatory.

- [ ] **Step 4: Add the trading-significance and safety section**

State the five evidence checks in this order: higher-timeframe trend, location at support/resistance or breakout/retest, relative volume, confirmation close, and trade math. Include clear no-trade conditions: formation in the middle of a range, no confirmation, event risk, wide stop, poor reward-to-risk, conflicting higher timeframe, or thin option liquidity. Add a step-by-step checklist requiring:

```text
Entry: only after the confirmation-candle close or planned retest.
Stop: beyond the formation extreme, never widened after entry.
Target: the next structure level and minimum 1:2 reward-to-risk.
Size: position risk must remain within the daily and per-trade loss limits.
Options: choose direction from the underlying chart; then check expiry, IV, spread, liquidity, and theta.
```

- [ ] **Step 5: Validate navigation and Markdown presentation**

Run:

```bash
rg '^## |^### |^-' "kb/kb2-Candlestick/candlestick_kb.md"
```

Expected: all table-of-contents destinations and major sections appear in the output.

Preview the Markdown in the editor. Expected: the image renders, every contents link resolves, diagrams preserve their layout, and the table remains readable without horizontal ambiguity.

- [ ] **Step 6: Check diagnostics**

Run the IDE diagnostics check for:

```text
kb/kb2-Candlestick/candlestick_kb.md
```

Expected: no introduced diagnostics.

## Plan Self-Review

- Spec coverage: Task 1 covers navigation, anatomy, all image labels, bilingual explanations, diagrams, conditional interpretation, no-trade rules, risk/reward, position sizing, and option safeguards.
- Placeholder scan: no deferred tasks, missing content, or ambiguous actions remain.
- Consistency: the only modified learning page is `kb/kb2-Candlestick/candlestick_kb.md`; all navigation and verification target that file.
