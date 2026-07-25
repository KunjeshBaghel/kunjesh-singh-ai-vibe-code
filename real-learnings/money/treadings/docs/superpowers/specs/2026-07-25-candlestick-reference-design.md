# Candlestick Reference Design

## Purpose

Expand `kb/kb2-Candlestick/candlestick_kb.md` into a beginner-friendly trading reference. English is the primary language; short Hindi explanations in parentheses help connect the concepts to the user's existing learning material.

## Scope

- Add a table of contents.
- Explain candlestick anatomy: open, high, low, close, real body, and upper/lower wick.
- Add a compact quick-reference table for all 15 forms shown in the existing image:
  bearish, bullish, inverted hammer, shooting star, hammer, hanging man, bullish spinning top, bearish spinning top, short bullish candle, short bearish candle, bullish marubozu, bearish marubozu, long-legged doji, dragonfly doji, gravestone doji, and four-price doji.
- Add text diagrams for the principal candle families and explicitly show that paired shapes change meaning with trend and location.
- Explain trading significance only as a conditional indication, never as a standalone buy/sell instruction.
- Add a detailed pre-trade safety checklist for spot/chart confirmation and options execution.

## Content Rules

1. Every reversal formation must state its prerequisite trend and required confirmation candle.
2. Candle colour is not treated as an automatic bullish or bearish signal.
3. Entries require confirmation, a defined stop-loss, a target that provides at least 1:2 risk-to-reward, and position sizing within the trader's pre-set loss limit.
4. The section must state no-trade conditions: event risk, a candle in the middle of a range, poor risk-to-reward, a stop that is too wide, and conflicting higher-timeframe structure.
5. For options, the underlying chart determines direction; expiry, implied volatility, liquidity, spread, and theta must be checked before choosing an option.

## Structure

1. Title and linked table of contents.
2. Existing basic-forms image with a note that it is a shape catalogue, not a signal catalogue.
3. Anatomy diagram and reading rule.
4. Full basic-form quick-reference table.
5. ASCII diagrams and explanations for:
   - bullish/bearish bodies;
   - hammer versus hanging man;
   - inverted hammer versus shooting star;
   - spinning top and short candles;
   - marubozu;
   - the four doji variants.
6. Trading significance and confirmation framework.
7. Pre-trade checklist and option-specific execution safeguards.

## Verification

- Confirm all labels visible in the existing image are represented in the quick-reference table.
- Confirm all Markdown links in the table of contents point to valid headings.
- Preview the Markdown to verify the diagrams remain monospaced and tables are readable.
- Check the edited Markdown for diagnostics.

## Out of Scope

- Named multi-candle patterns and price-chart patterns; these belong in their respective knowledge-base pages.
- Live market recommendations, order placement, or changes to broker tools.
