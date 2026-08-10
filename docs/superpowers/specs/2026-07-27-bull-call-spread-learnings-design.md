# Bull Call Spread Learnings Design

## Goal

Expand the existing Bull Call Spread entry with research-backed practical guidance without duplicating its definition, payoff example, or the canonical option-chain and Greek definitions elsewhere in the knowledge base.

## Scope

Insert one subsection immediately below `##### 1.3 Bull Call Spread` in `real-learnings/money/treadings/kb/kb1/strategy_ref_book.md`. Add a corresponding nested entry in the document's table of contents.

## Content

The subsection will:

- identify the appropriate market view and unsuitable conditions;
- establish target, deadline, risk, and liquidity before strike selection;
- explain strike width, net Delta, Theta, Gamma, Vega/IV, OI, volume, and premium priority;
- provide one clearly labelled hypothetical selection example;
- define pre-entry no-go checks, exit/defence rules, and rolling discipline;
- distinguish NSE cash-settled index-option expiry mechanics from stock-option settlement;
- clarify that professionals use the structure as one defined-risk tool, not as a guaranteed-profit strategy;
- cite existing KB sections for material that is already documented, and cite trusted external sources for new claims.

## Constraints

- Preserve all existing Bull Call Spread content.
- Do not use current market data or make a live trade recommendation.
- Treat all examples as educational and multiply point outcomes by the current live lot size only when trading.
- Do not prescribe a universal strike distance, fixed Delta, or guaranteed profitability.

## Verification

After editing, verify the table-of-contents anchor matches the inserted heading, the new subsection remains under Bull Call Spread, and the edited Markdown has no linter diagnostics.
