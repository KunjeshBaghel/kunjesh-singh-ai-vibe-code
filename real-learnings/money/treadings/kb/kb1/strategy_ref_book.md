# Options treading in BSE/NSE markets.

> 🔒 **PRECEDENCE — read this before taking any number from this file.**
>
> `TRADING_CONSTANTS.md` → skill `SKILL.md` → `CLAUDE.md` → **this file, §8 only** → everything else.
>
> - **[`TRADING_CONSTANTS.md`](../../TRADING_CONSTANTS.md) holds every cap, target, time and threshold.**
>   If a number here disagrees with it, that file wins and this one is a bug. Don't copy numbers out
>   of it — link to the row.
> - **§1–§7 below is a textbook catalogue and NEVER governs a live decision.** It predates CAS and the
>   2024 SEBI regime. §8 supersedes it wherever they disagree.
> - **§8 is the reasoning; the constants file is the parameters.** Read §8 to understand *why* a rule
>   exists, then take the actual number from the constants file.

## Index

- [1. Tools which will help during the treads](#1-tools-which-will-help-during-the-treads)
  - [Margin calculator](#margin-calculator)
  - [FII and DII directions](#fii-and-dii-directions)
- [2. Twitter profiles to follow](#2-twitter-profiles-to-follow)
- [3. learn charts](#3-learn-charts)
  - [3.1 plces from where you can learn the charts](#31-plces-from-where-you-can-learn-the-charts)
- [4. Options basics & terminology](#4-options-basics--terminology)
- [5. learn Strategies](#5-learn-strategies)
  - [5.1 Best trusted Indian sources to learn options strategies](#51-best-trusted-indian-sources-to-learn-options-strategies)
  - [5.2 Indian market rules to remember before any strategy](#52-indian-market-rules-to-remember-before-any-strategy)
  - [5.3 Strategy list to learn for NSE/BSE](#53-strategy-list-to-learn-for-nsebse)
    - [Strategies by cash market view](#strategies-by-cash-market-view)
    - [1. Sideways / Range-Bound Market](#1-sideways--range-bound-market)
    - [2. Slightly Bullish Market](#2-slightly-bullish-market)
    - [3. Strongly Bullish Market](#3-strongly-bullish-market)
    - [4. Slightly Bearish Market](#4-slightly-bearish-market)
    - [5. Strongly Bearish Market](#5-strongly-bearish-market)
    - [Summary reference table](#summary-reference-table)
  - [5.4 Point-wise strategy reference for NSE/BSE options](#54-point-wise-strategy-reference-for-nsebse-options)
    - [How to read this section](#how-to-read-this-section)
    - [Trusted sources used for this strategy list](#trusted-sources-used-for-this-strategy-list)
    - [Common example assumptions](#common-example-assumptions)
    - [1. Directional strategies basic](#1-directional-strategies-basic)
      - [1.1 Long Call CE](#11-long-call-ce)
      - [1.2 Long Put PE](#12-long-put-pe)
      - [1.3 Bull Call Spread](#13-bull-call-spread)
        - [Practical Learnings: Selection, Execution & Defence](#practical-learnings-selection-execution--defence)
      - [1.4 Bear Put Spread](#14-bear-put-spread)
      - [1.5 Bull Put Spread](#15-bull-put-spread)
      - [1.6 Bear Call Spread](#16-bear-call-spread)
      - [1.7 Covered Call on stock holding](#17-covered-call-on-stock-holding)
      - [1.8 Protective Put / Married Put on stock holding](#18-protective-put--married-put-on-stock-holding)
    - [2. Hedging strategies](#2-hedging-strategies)
      - [2.1 Protective Put](#21-protective-put)
      - [2.2 Collar](#22-collar)
      - [2.3 Covered Call](#23-covered-call)
      - [2.4 Synthetic Long Futures / Synthetic Long Stock](#24-synthetic-long-futures--synthetic-long-stock)
      - [2.5 Synthetic Short Futures / Synthetic Short Stock](#25-synthetic-short-futures--synthetic-short-stock)
      - [2.6 Delta Hedging](#26-delta-hedging)
    - [3. Volatility strategies](#3-volatility-strategies)
      - [3.1 Long Straddle](#31-long-straddle)
      - [3.2 Long Strangle](#32-long-strangle)
      - [3.3 Short Straddle](#33-short-straddle)
      - [3.4 Short Strangle](#34-short-strangle)
      - [3.5 Long Call Butterfly](#35-long-call-butterfly)
      - [3.6 Long Put Butterfly](#36-long-put-butterfly)
      - [3.7 Long Iron Butterfly](#37-long-iron-butterfly)
    - [4. Range-bound / neutral strategies](#4-range-bound--neutral-strategies)
      - [4.1 Iron Condor](#41-iron-condor)
      - [4.2 Iron Butterfly](#42-iron-butterfly)
      - [4.3 Call Condor](#43-call-condor)
      - [4.4 Put Condor](#44-put-condor)
      - [4.5 Short Straddle](#45-short-straddle)
      - [4.6 Short Strangle](#46-short-strangle)
    - [5. Spread strategies advanced](#5-spread-strategies-advanced)
      - [5.1 Vertical Spreads](#51-vertical-spreads)
      - [5.1.1 Bull Call Spread](#511-bull-call-spread)
      - [5.1.2 Bear Put Spread](#512-bear-put-spread)
      - [5.1.3 Bull Put Spread](#513-bull-put-spread)
      - [5.1.4 Bear Call Spread](#514-bear-call-spread)
      - [5.2 Calendar Spread](#52-calendar-spread)
      - [5.3 Diagonal Spread](#53-diagonal-spread)
      - [5.4 Ratio Spread](#54-ratio-spread)
      - [5.5 Backspread Call / Put](#55-backspread-call--put)
      - [5.6 Butterfly Spread](#56-butterfly-spread)
      - [5.7 Box Spread / Conversion-Reversal Arbitrage](#57-box-spread--conversion-reversal-arbitrage)
    - [6. Income / theta strategies](#6-income--theta-strategies)
      - [6.1 Covered Call](#61-covered-call)
      - [6.2 Cash-Secured Put on physically settled stock options](#62-cash-secured-put-on-physically-settled-stock-options)
      - [6.3 Credit Spreads](#63-credit-spreads)
      - [6.4 Short Straddle](#64-short-straddle)
      - [6.5 Short Strangle](#65-short-strangle)
      - [6.6 Iron Condor](#66-iron-condor)
      - [6.7 Iron Butterfly](#67-iron-butterfly)
    - [7. High-risk strategies: learn, but avoid as beginner](#7-high-risk-strategies-learn-but-avoid-as-beginner)
      - [7.1 Naked Short Call](#71-naked-short-call)
      - [7.2 Naked Short Put](#72-naked-short-put)
      - [7.3 Short Straddle](#73-short-straddle)
      - [7.4 Short Strangle](#74-short-strangle)
      - [7.5 Ratio Spread with extra short option](#75-ratio-spread-with-extra-short-option)
      - [7.6 Stock option positions held to expiry without delivery planning](#76-stock-option-positions-held-to-expiry-without-delivery-planning)
- [6. Best references to learn (Books/Blogs/Videos/Websites/Courses)](#6-best-references-to-learn-booksblogsvideoswebsitescourses)
  - [Beginner Level](#beginner-level)
  - [Intermediate Level](#intermediate-level)
  - [Advanced Level](#advanced-level)
  - [India-Specific Options Trading](#india-specific-options-trading)
- [7. AI usage on treading](#7-ai-usage-on-treading)
  - [7.1 Scope: only Indian markets](#71-scope-only-indian-markets)
  - [7.2 Important regulation and safety notes](#72-important-regulation-and-safety-notes)
  - [7.3 Best ready-made tools for option trading guidance](#73-best-ready-made-tools-for-option-trading-guidance)
  - [7.4 Brokers and APIs that can connect Python/live data/order placement](#74-brokers-and-apis-that-can-connect-pythonlive-dataorder-placement)
  - [7.5 Can Claude/OpenAI be connected to broker account and live market feed?](#75-can-claudeopenai-be-connected-to-broker-account-and-live-market-feed)
  - [7.6 What the AI copilot should guide live](#76-what-the-ai-copilot-should-guide-live)
  - [7.7 Python implementation plan for personal copilot](#77-python-implementation-plan-for-personal-copilot)
  - [7.8 Good first practical setup](#78-good-first-practical-setup)
  - [7.9 Prompt template for live option copilot](#79-prompt-template-for-live-option-copilot)
  - [7.10 Final recommendation](#710-final-recommendation)
- [**8. The Real-World Option Seller's Book — NIFTY 50 / BANKNIFTY / SENSEX (2026 regime)**](#8-the-real-world-option-sellers-book--nifty-50--banknifty--sensex-2026-regime)
  - [8.0 Scope, non-duplication map, and reconciliation](#80-scope-non-duplication-map-and-reconciliation)
  - [8.1 Where the money actually comes from — the Volatility Risk Premium](#81-where-the-money-actually-comes-from--the-volatility-risk-premium)
  - [8.2 The 2024–2026 rule changes that decided which strategies still work](#82-the-20242026-rule-changes-that-decided-which-strategies-still-work)
  - [8.3 The real cost sheet — charges, slippage, and the friction floor](#83-the-real-cost-sheet--charges-slippage-and-the-friction-floor)
  - [8.4 Instrument selection — NIFTY vs BANKNIFTY vs SENSEX](#84-instrument-selection--nifty-vs-banknifty-vs-sensex)
  - [**8.5 The seller's regime grid — Direction × Volatility × DTE**](#85-the-sellers-regime-grid--direction--volatility--dte)
  - [**8.6 The structure library — what real sellers actually put on**](#86-the-structure-library--what-real-sellers-actually-put-on)
    - [8.6.1 Intraday Delta-Neutral Hedged Short Straddle — "the 9:20 structure"](#861-intraday-delta-neutral-hedged-short-straddle--the-920-structure)
    - [8.6.2 The Delta-Banded Hedged Strangle — the weekly workhorse](#862-the-delta-banded-hedged-strangle--the-weekly-workhorse)
    - [8.6.3 Jade Lizard (hedged) — the put-skew harvester](#863-jade-lizard-hedged--the-put-skew-harvester)
    - [8.6.4 Big Lizard — the aggressive cousin](#864-big-lizard--the-aggressive-cousin)
    - [8.6.5 Reverse Jade Lizard (Twisted Sister) — and why it is harder in NIFTY](#865-reverse-jade-lizard-twisted-sister--and-why-it-is-harder-in-nifty)
    - [8.6.6 Broken-Wing Butterfly (BWB) — the credit structure with zero risk on one side](#866-broken-wing-butterfly-bwb--the-credit-structure-with-zero-risk-on-one-side)
    - [8.6.7 Unbalanced (Ratio'd) Iron Condor — lean the view without a naked leg](#867-unbalanced-ratiod-iron-condor--lean-the-view-without-a-naked-leg)
    - [8.6.8 Skew-Aware Delta-Matched Condor — stop measuring in points](#868-skew-aware-delta-matched-condor--stop-measuring-in-points)
    - [8.6.9 Positional 25–40 DTE Iron Condor — the compounding engine](#869-positional-2540-dte-iron-condor--the-compounding-engine)
    - [8.6.10 0-DTE Hedged Iron Fly under CAS — expiry day done properly](#8610-0-dte-hedged-iron-fly-under-cas--expiry-day-done-properly)
    - [8.6.11 IV-Crush Event Harvest — RBI policy, Budget, big results](#8611-iv-crush-event-harvest--rbi-policy-budget-big-results)
    - [8.6.12 Double Calendar / "Batman" — and the February-2025 margin trap](#8612-double-calendar--batman--and-the-february-2025-margin-trap)
    - [8.6.13 The Ladder — a repair, never an entry](#8613-the-ladder--a-repair-never-an-entry)
    - [8.6.14 The Rolling Wing Bank — margin efficiency as a strategy](#8614-the-rolling-wing-bank--margin-efficiency-as-a-strategy)
  - [8.7 Strike selection — the four methods and when each wins](#87-strike-selection--the-four-methods-and-when-each-wins)
    - [**8.7.1a The forward-basis check — run this before you trust any delta**](#871a-the-forward-basis-check--run-this-before-you-trust-any-delta-added-28-aug-2026)
  - [8.8 Entry timing — the intraday premium and IV curve](#88-entry-timing--the-intraday-premium-and-iv-curve)
  - [**8.9 The adjustment playbook — decision tree**](#89-the-adjustment-playbook--decision-tree)
  - [8.10 Stop-loss architecture — four types and which to use](#810-stop-loss-architecture--four-types-and-which-to-use)
  - [**8.11 Position sizing — two caps, take the smaller**](#811-position-sizing--two-caps-take-the-smaller)
    - [**8.11.6 The feasibility gate — can today's target be reached at all?**](#8116-the-feasibility-gate--can-todays-target-be-reached-at-all-added-28-aug-2026)
    - [**8.11.7 The noise-floor test — is your stop inside one candle?**](#8117-the-noise-floor-test--is-your-stop-inside-one-candle-added-28-aug-2026)
  - [8.12 The pattern library — recurring setups a seller trades](#812-the-pattern-library--recurring-setups-a-seller-trades)
  - [**8.13 Trend-day detection — the seller's kill switch**](#813-trend-day-detection--the-sellers-kill-switch)
  - [8.14 Blow-up autopsy — the six ways sellers die](#814-blow-up-autopsy--the-six-ways-sellers-die)
  - [8.15 Metrics that actually matter](#815-metrics-that-actually-matter)
    - [**8.15.4 Scoring the day — mark at the mandated exit, report MAE and MFE**](#8154-scoring-the-day--mark-at-the-mandated-exit-and-always-report-mae-and-mfe-added-28-aug-2026)
  - [8.16 Quick-reference cards](#816-quick-reference-cards)
  - [8.17 Sources for Section 8](#817-sources-for-section-8)

## 1. Tools which will help during the treads
### Margin calculator 
- https://zerodha.com/margin-calculator/SPAN/

### FII and DII directions.
- `https://web.sensibull.com/fii-dii-data`

### Stratigy visualization 
- Sensibull login with Zerodha.
  - 
- 

## 2. Twitter profiles to follow 
### profiles 
- FII DII & GIFT NIFTY 
  - link - `https://x.com/FII_DII_Nifty`

- Ajay Bagga
  - link - `https://x.com/Ajay_Bagga`

- भाऊ
  - link - `https://x.com/PatilBankNifty`

- Kapil Dhama
  - link - `https://x.com/kapildhama`

- Sarang Sood
  - link - `https://x.com/SarangSood`

- Jegathesan Durairaj (Jegan)
  - link - `https://x.com/itjegan`

## 3. learn charts 

### 3.1 plces from where you can learn the charts

#### 3.1.1 Youtube channels

##### 3.1.1.1 


## 4. Options basics & terminology

Option basics, acronyms, Greeks, and Indian market terms are maintained in one place:

→ **[trading_jargon_acronyms.md](./trading_jargon_acronyms.md)**

**Source PDF for deeper study:** `@src/f/treading/options/docs/Module 5_Options-Theory-for-Professional-Trading.pdf`


## 5. learn Strategies

### 5.1 Best trusted Indian sources to learn options strategies

Use Indian official/regulatory sources first, because NSE/BSE rules, expiry, settlement, margin, STT, taxes, and contract availability can be different from US markets.

1. **NSE Academy: Options Trading Strategies Module**
   - Link: https://www.nseindia.com/static/learn/self-study-ncfm-modules-intermediate-options-trading-strategies
   - Why use it: NSE says this module is for learning option strategies, payoff concepts, objectives, and risks of different strategies.

2. **NISM-Series-VIII: Equity Derivatives Certification Examination**
   - Link: https://www.nism.ac.in/equity-derivatives/
   - Curriculum link: https://www.nism.ac.in/curriculum-equity-derivatives-certification-examination/
   - Why use it: NISM is established by SEBI. The curriculum covers Indian equity derivatives, options, Greeks, option strategies, clearing, settlement, risk management, legal/regulatory environment, taxation, and investor protection.

3. **SEBI Investor: Understanding Derivatives**
   - Link: https://investor.sebi.gov.in/understanding_derivatives.html
   - Why use it: SEBI explains derivatives, hedging, speculation, arbitrage, leverage risk, liquidity risk, and the warning that 9 out of 10 individual traders in equity F&O incurred net losses in SEBI's study.

4. **NSE contract specifications and settlement rules**
   - Contract specifications: https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications
   - Individual stock F&O: https://www.nseindia.com/static/products-services/equity-derivatives-individual-securities
   - Settlement mechanism: https://www.nseclearing.in/clearing-settlement/equity-derivatives/settlement-mechanism
   - Why use it: This is where you check the current underlying, lot size, expiry day, strike scheme, tick size, settlement, and physical/cash settlement rules.

5. **BSE official derivatives data**
   - Option chain: https://www.bseindia.com/markets/Derivatives/DeriReports/DeriOptionchain.html
   - Why use it: Use BSE pages to check live BSE derivative contracts, liquidity, expiry, strike availability, and traded volume before planning any BSE option strategy.

> Safe learning rule for NSE/BSE: first check whether the exact underlying, expiry, strike, lot size, liquidity, margin, and settlement rule exists in India. Do not copy US option examples directly.

### 5.2 Indian market rules to remember before any strategy

1. **NSE/BSE option symbols use `CE` and `PE`** — see [trading_jargon_acronyms.md](./trading_jargon_acronyms.md#acronyms--quick-reference). European style means exercise is at expiry, not whenever you want.

2. **Index options and stock options do not settle the same way**
   - Index options like `NIFTY`, `BANKNIFTY`, `FINNIFTY`, `MIDCPNIFTY`, `NIFTYNXT50`, and BSE index options are cash-settled because an index cannot be delivered.
   - NSE states options on individual securities are European style and physically settled.
   - Meaning: if you hold an in-the-money stock option till expiry, it can create a delivery obligation in shares. This is very important for `Covered Call`, `Protective Put`, `Collar`, and short option strategies.

3. **Check expiry and lot size every time**
   - NSE expiry day and contract specifications can change by circular.
   - NSE currently lists Tuesday expiry in its equity derivatives contract specification page.
   - Lot size can change, so always check the latest NSE/BSE contract file or broker contract details.

4. **Option selling needs margin and strict risk control**
   - Selling calls/puts, credit spreads, straddles, strangles, iron condors, and iron butterflies can lose much more than the premium received.
   - SEBI warns that derivatives can multiply profits and losses because only a smaller amount is paid compared with the underlying value.

5. **Liquidity matters in India**
   - Many stock options have poor liquidity and wide bid-ask spreads.
   - For beginners, learn and paper-trade using liquid index options first. Trade stock options only after checking volume, open interest, bid-ask spread, physical settlement risk, and margin.

### 5.3 Strategy list to learn for NSE/BSE

```bash (list)
Option Strategies for Indian Stock Market (NSE/BSE)
│
├── 1. Directional Strategies (Basic)
│   ├── Long Call CE
│   ├── Long Put PE
│   ├── Bull Call Spread
│   ├── Bear Put Spread
│   ├── Bull Put Spread
│   ├── Bear Call Spread
│   ├── Covered Call on stock holding
│   └── Protective Put / Married Put on stock holding
│
├── 2. Hedging Strategies
│   ├── Protective Put
│   ├── Collar
│   ├── Covered Call
│   ├── Synthetic Long Futures / Synthetic Long Stock
│   ├── Synthetic Short Futures / Synthetic Short Stock
│   └── Delta Hedging
│
├── 3. Volatility Strategies
│   ├── Long Straddle
│   ├── Long Strangle
│   ├── Short Straddle
│   ├── Short Strangle
│   ├── Long Call Butterfly
│   ├── Long Put Butterfly
│   └── Long Iron Butterfly
│
├── 4. Range-Bound / Neutral Strategies
│   ├── Iron Condor
│   ├── Iron Butterfly
│   ├── Call Condor
│   ├── Put Condor
│   ├── Short Straddle
│   └── Short Strangle
│
├── 5. Spread Strategies (Advanced)
│   ├── Vertical Spreads
│   │   ├── Bull Call Spread
│   │   ├── Bear Put Spread
│   │   ├── Bull Put Spread
│   │   └── Bear Call Spread
│   ├── Calendar Spread
│   ├── Diagonal Spread
│   ├── Ratio Spread
│   ├── Backspread (Call / Put)
│   ├── Butterfly Spread
│   └── Box Spread / Conversion-Reversal Arbitrage
│
├── 6. Income / Theta Strategies
│   ├── Covered Call
│   ├── Cash-Secured Put on physically settled stock options
│   ├── Credit Spreads
│   ├── Short Straddle
│   ├── Short Strangle
│   ├── Iron Condor
│   └── Iron Butterfly
│
└── 7. High-Risk Strategies: learn, but avoid as beginner
    ├── Naked Short Call
    ├── Naked Short Put
    ├── Short Straddle
    ├── Short Strangle
    ├── Ratio Spread with extra short option
    └── Stock option positions held to expiry without delivery planning
```

#### Strategies by cash market view

Based on the trusted educational frameworks of the Indian options market (such as **SEBI/NISM curriculum** and **Zerodha Varsity**), here is the structured categorization of option strategies across five specific cash market movement areas.

In India, these are specifically tailored around European-style options (`CE` for Calls, `PE` for Puts) and account for index cash-settlement versus individual stock physical-settlement rules.

#### 1. Sideways / Range-Bound Market

*The cash market index or stock is expected to consolidate within a tight horizontal channel with low volatility.*

**Top Strategies**

- **Defined-Risk (Recommended):** Iron Condor, Iron Butterfly
- **Undefined-Risk (Advanced):** Short Straddle, Short Strangle

**When to Use & Why**

- **Iron Condor / Iron Butterfly:** These are the **best choices for retail traders** in India. Because you sell ATM or OTM premiums and simultaneously buy further OTM "wings" (protection), your maximum risk is capped.
- **The Indian Market Edge:** Under NSE/BSE margin frameworks, deploying hedged structures like Iron Condors drastically reduces your required **SPAN + Exposure margin**. Furthermore, overnight gap risk (common in Nifty/Bank Nifty due to global cues) is completely hedged.
- **Short Straddle / Strangle:** Better left to institutions with high capital. They perform well when Implied Volatility (IV) is exceptionally high (e.g., right before earnings or major macro events) and is expected to crash (*IV Crush*), accelerating time decay (**Theta**).

#### 2. Slightly Bullish Market

*The market has a positive bias, likely tracking a slow upward channel or firmly holding onto a major support level.*

**Top Strategies**

- **Debit Strategy:** Bull Call Spread
- **Credit Strategy:** Bull Put Spread
- **Income Strategy:** Covered Call *(Applicable to stock holdings)*

**When to Use & Why**

- **Bull Call Spread (Buy ATM CE + Sell OTM CE):** Better when you expect a gradual crawl upward. Buying a naked call loses value quickly if the market moves too slowly due to Theta decay. Selling the higher strike CE offsets this decay cost and cheapens your total trade entry.
- **Bull Put Spread (Sell ATM/ITM PE + Buy OTM PE):** Better when you are highly confident that a specific support level will not break. It is a net credit strategy; as long as the cash market stays above your sold strike or rises slightly, you keep the full premium.
- **Covered Call:** Excellent for individual Indian stock investors. If you hold a long-term stock portfolio, selling an OTM CE allows you to generate yield.
- *Crucial Indian Market Note:* In India, individual stock options are **physically settled at expiry**. You must ensure your stock holding quantity exactly matches the exchange's contract lot size to avoid severe auction penalties if assigned.

#### 3. Strongly Bullish Market

*The cash market exhibits strong momentum, breaking out of crucial resistance levels on heavy volume, or reacting to highly positive news.*

**Top Strategies**

- **Directional Buy:** Long Call (Naked CE Buy)
- **Advanced Breakout:** Call Ratio Backspread
- **Futures Replica:** Synthetic Long Futures

**When to Use & Why**

- **Long Call (Buy CE):** Better when the upward velocity is extremely fast. Since you expect an explosive move, you want uncapped upside via **Delta** acceleration. In a fast breakout, directional profits outrun time decay effortlessly. Risk is strictly limited to the premium paid.
- **Call Ratio Backspread (Sell 1 ATM CE + Buy 2 OTM CE):** Better when you anticipate a massive upside explosion but want a safety net. If the market surprises you and violently crashes instead of breaking out, the strategy actually turns a small profit or results in zero loss (depending on entry pricing). It only loses money if the market gets stuck sideways.

#### 4. Slightly Bearish Market

*The market is exhibiting structural weakness, distribution at highs, or facing strong structural resistance.*

**Top Strategies**

- **Debit Strategy:** Bear Put Spread
- **Credit Strategy:** Bear Call Spread

**When to Use & Why**

- **Bear Put Spread (Buy ATM PE + Sell OTM PE):** Better for a steady, grinding downward move. Because markets don't always fall instantly, buying a naked put can be expensive due to premium decay. Selling the lower strike PE funds the trade and caps risk while giving you an optimal target zone.
- **Bear Call Spread (Sell ATM/ITM CE + Buy OTM CE):** Highly effective in slightly bearish environments. It acts as a net credit strategy. If the cash market fails to break resistance and stays below your short call, you capture the premium. The long call wing ensures that if an unexpected positive global cue gaps the Indian market up, your losses are strictly restricted.

#### 5. Strongly Bearish Market

*The market faces panic selling, systemic breakdowns, or severe negative macro event shocks.*

**Top Strategies**

- **Directional Buy:** Long Put (Naked PE Buy)
- **Advanced Breakdown:** Put Ratio Backspread

**When to Use & Why**

- **Long Put (Buy PE):** The **absolute best strategy** during a sharp market crash. In the Indian stock market, fear causes the India VIX (Volatility Index) to shoot up drastically. When VIX spikes, **Implied Volatility (IV) expands rapidly**, adding huge value to your option premiums via the **Vega** Greek. A naked long put gains value from both the downward price crash and the soaring fear index simultaneously.
- **Put Ratio Backspread (Sell 1 ATM PE + Buy 2 OTM PE):** Ideal for a highly anticipated downside breakdown. If the crash occurs, the two long puts make exponential gains. If the market suddenly reverses and rallies hard (due to short-covering or emergency regulatory interventions), the sold PE covers the cost, leaving you completely safe from losses on the upside.

#### Summary reference table

| Cash Market View | Best Strategy | Nature | Key Reason for Indian Markets |
| --- | --- | --- | --- |
| **1. Sideways** | **Iron Condor** | Net Credit | Optimizes SPAN margins; fully protects against overnight global gap risks. |
| **2. Slightly Bullish** | **Bull Call Spread** | Net Debit | Mitigates time decay (Theta) while riding a slow, capped upward move. |
| **3. Strongly Bullish** | **Long Call (CE)** | Net Debit | Capitalizes on fast Delta acceleration; absolute capped risk if breakout fails. |
| **4. Slightly Bearish** | **Bear Call Spread** | Net Credit | Profits from the market failing to breach overhead psychological resistance. |
| **5. Strongly Bearish** | **Long Put (PE)** | Net Debit | Explodes in value due to the dual impact of downward price action and expanding IV (Vega). |

### 5.4 Point-wise strategy reference for NSE/BSE options

#### How to read this section

- This is a learning reference, not a trade recommendation.
- Examples use simple numbers like `NIFTY spot = 22,000` or `stock = 1,000` only to explain payoff logic. Always check live price, premium, lot size, strike availability, liquidity, bid-ask spread, margin, STT/taxes, and settlement before trading.
- For NSE/BSE Indian market context, learn the rule framework from **NSE**, **BSE**, **NISM/SEBI**, and learn practical payoff examples from **Zerodha Varsity Module 5 and Module 6**.
- For stock options, remember Indian individual stock derivatives are physically settled at expiry. Do not hold ITM stock option positions into expiry unless you understand delivery obligation, margin, and auction risk.
- For index options, settlement is cash-settled because an index cannot be delivered.
- For BSE options, the payoff logic is the same as NSE, but liquidity can be very different. Before using any strategy on BSE, confirm volume, open interest, bid-ask spread, and contract availability on the BSE derivative pages.

#### Trusted sources used for this strategy list

- **NSE Academy / NCFM Options Trading Strategies Module**
  - Best for: Indian exchange-oriented strategy learning, payoff diagrams, risk-reward, and exam-style structure.
  - Link: https://www.nseindia.com/static/learn/self-study-ncfm-modules-intermediate-options-trading-strategies
- **NISM-Series-VIII Equity Derivatives**
  - Best for: Indian derivatives market structure, options basics, clearing, settlement, margins, risk management, regulation, and taxation.
  - Link: https://www.nism.ac.in/equity-derivatives/
- **SEBI Investor - Understanding Derivatives**
  - Best for: risk awareness, leverage, hedging/speculation/arbitrage explanation, and investor protection.
  - Link: https://investor.sebi.gov.in/understanding_derivatives.html
- **NSE contract specifications and settlement mechanism**
  - Best for: expiry, lot size, settlement type, strike scheme, and current contract rules.
  - Links:
    - https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications
    - https://www.nseclearing.in/clearing-settlement/equity-derivatives/settlement-mechanism
- **BSE derivatives pages**
  - Best for: checking whether the same strategy is practically tradable on BSE contracts.
  - Link: https://www.bseindia.com/markets/Derivatives/DeriReports/DeriOptionchain.html
- **Zerodha Varsity Module 5: Options Theory**
  - Best for: Indian examples of call, put, intrinsic value, time value, Greeks, volatility, and payoffs.
  - Link: https://zerodha.com/varsity/module/option-theory/
- **Zerodha Varsity Module 6: Option Strategies**
  - Best for: practical Indian examples of spreads, straddles, strangles, ratio back spreads, synthetic long, arbitrage, and iron condor.
  - Link: https://zerodha.com/varsity/module/option-strategies/

#### Common example assumptions

- `CE` and `PE` — see [trading_jargon_acronyms.md](./trading_jargon_acronyms.md#acronyms--quick-reference). For Greeks, option-chain columns, and IV, use the canonical definitions in [Greeks](./trading_jargon_acronyms.md#greeks), [Option Chain Columns](./trading_jargon_acronyms.md#option-chain-columns), and [Volatility & Sentiment](./trading_jargon_acronyms.md#volatility--sentiment).
- Ignore brokerage, exchange charges, GST, STT, stamp duty, slippage, and taxes in simple examples. Real trades must include all costs.
- In all examples, profit/loss is shown per unit. Multiply by the current NSE/BSE lot size for actual rupee impact.
- `Net premium paid` means debit strategy. `Net premium received` means credit strategy.
- Break-even formulas are approximate educational formulas before charges.

#### 1. Directional strategies basic

##### 1.1 Long Call CE (buy CE)

- **Basic definition:** Buy one `CE` when you expect the underlying to rise above the strike plus premium before or by expiry.
- **Market view:** Bullish; works best when price rises quickly and/or implied volatility rises after entry.
- **Basic example:** 
  - `NIFTY = 22,000`. 
    - Buy `22,100 CE` at premium `80`. Maximum loss = `80`. 
    - Break-even = `22,100 + 80 = 22,180`. 
    - If expiry is `22,300`, intrinsic value = `200`, net profit = `200 - 80 = 120`.
- **Risk and reward:** Loss is limited to premium paid. Profit can be large if the index/stock rises strongly.
- **Indian market note:** For stock options, avoid holding ITM calls into expiry unless you are ready for physical delivery obligation. Index calls are cash-settled.
- **From where to learn:** Zerodha Varsity Module 5 call option basics, NSE Academy options strategies module, NISM Equity Derivatives.
- **Best source:** Start with Zerodha Varsity Module 5 for payoff understanding, then use NSE/NISM for Indian rules.
- `https://web.sensibull.com/learn-options-strategies/long-call-option`

###### Selecting a Long Call strike when the plan is to exit before expiry

> **Educational framework, not a profit guarantee or a live-trade recommendation.** A bullish view alone is insufficient for a long call: the expected move must be large and fast enough to overcome the premium, time decay, and any fall in IV. The objective here is to resell the CE before expiry; the expiry break-even remains a risk reference, not the only way to make a profit.

**Professional-style selection order:** define the underlying price target, deadline, expected IV direction, and maximum rupee loss first. Then choose expiry and strike. Use [Delta and the other Greeks](./trading_jargon_acronyms.md#greeks) to compare directional exposure and decay; use [option-chain columns](./trading_jargon_acronyms.md#option-chain-columns) to assess liquidity and cost; and use [IV context](./trading_jargon_acronyms.md#volatility--sentiment) to judge whether the option may already price a large move. No single field is sufficient.

**The sub-category determines the usual delta range.** The ranges below are starting points, not rules. A trader should move to a higher-delta call when the expected move is slower or less explosive, and should not use a lower-delta call merely to reduce the premium.

| Trader sub-category | Typical holding period | Usual CE moneyness / delta | Why this category chooses it |
|---|---:|---|---|
| **Intraday momentum / breakout** | Minutes to one day | ATM to slightly OTM; `0.40–0.60` | Balances immediate response with leverage. Requires a clear breakout, liquid strike, and predefined exit. |
| **Intraday trend continuation** | Hours | ATM to slightly ITM; `0.50–0.70` | Gives more reliable directional response than a far-OTM CE while the underlying trend is the main thesis. |
| **Short swing** | 2–5 sessions | ATM to slightly ITM; `0.55–0.70` | Reduces dependence on a sudden, very large move as negative theta accumulates over several days. |
| **Positional bullish** | 1–3 weeks; normally use an expiry with adequate time remaining | ITM; `0.65–0.80` | Behaves more like the underlying and has less dependence on purely extrinsic value than an OTM CE. Compare a bull call spread if the target is capped or IV is elevated. |
| **Defined catalyst / event** | Before or immediately after a defined event | ATM to slightly ITM; `0.50–0.65` | Requires an explicit IV and implied-move plan; a post-event IV crush can offset a modest bullish move. |
| **Low-premium speculation** | Any | Far OTM; below `0.30` | A high-convexity speculation, not a standard income method. It needs a very large, very fast move and can lose its entire premium. |

**How a pre-expiry profit can be estimated:** model a scenario instead of relying only on expiry break-even. With signed Greeks (see [Greek definitions](./trading_jargon_acronyms.md#greeks)), a rough estimate is:

```text
Option P&L ≈ (Delta × underlying move)
             + (0.5 × Gamma × underlying move²)
             + (Vega × IV change in percentage points)
             + (Theta × days held)
             − bid–ask cost − charges
```

Greeks and IV change continuously, so this is a planning estimate—not a prediction or a substitute for checking the live option chain.

**Hypothetical comparison:** If `NIFTY = 22,000` and the target is `22,350` within 4–6 trading days, compare CEs in the same expiry instead of selecting only the cheapest premium:

| Hypothetical CE | Delta / moneyness | Premium | Initial directional estimate for a 350-point rise* | What it means |
|---|---|---:|---:|---|
| `21,900 CE` | `0.65`, ITM | `150` | `0.65 × 350 = 227.5` points | Higher capital outlay; more underlying-like response. |
| `22,000 CE` | `0.50`, ATM | `105` | `0.50 × 350 = 175` points | Balanced directional exposure. |
| `22,200 CE` | `0.32`, slightly OTM | `45` | `0.32 × 350 = 112` points | Lower initial cost, but much greater dependence on a fast, sustained rally. |

\*Before gamma, theta, IV, spread, charges, and changes in delta. The `22,200 CE` expiry break-even is `22,245`, but it may still be sold for a profit before expiry if the premium rises sufficiently.

**Pre-entry and exit discipline for a long CE:**

1. Write the price target and deadline; if the expected move is too slow or too small, do not force a long-call trade.
2. Select an expiry that gives the thesis time to work; avoid far-OTM buying close to expiry for a multi-day target.
3. Choose delta/moneyness for the trade category above, then compare at least the nearest ITM, ATM, and slightly OTM strikes.
4. Check IV against its own history and the expected event/implied move. Avoid paying elevated IV without a reason to expect a larger move or higher IV after entry.
5. Check a narrow, executable bid–ask spread, current volume, OI, and adequate quantity at the intended price. Use limit orders where appropriate.
6. Calculate `premium × current lot size` as maximum loss before charges. Risk only an amount within the daily and per-trade loss limits.
7. Define before entry: underlying-level invalidation, premium stop, profit target, and a time stop. Close before expiry by default; stock-option ITM contracts can create physical-settlement obligations.

**Source material:** [Zerodha Varsity — strike selection, time to expiry, and IV](https://zerodha.com/varsity/chapter/re-introducing-call-put-options/); [delta and strike behaviour](https://zerodha.com/varsity/chapter/delta-part-2/); [theta/time decay](https://zerodha.com/varsity/chapter/theta/); [NSE — Greeks mastery and risk management](https://www.nseindia.com/static/learn/greeks-mastery-program).

##### 1.2 Long Put PE (buy PE)

- **Basic definition:** Buy one `PE` when you expect the underlying to fall below the strike minus premium before or by expiry.
- **Market view:** Bearish; works best when price falls quickly and/or implied volatility rises after entry.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Buy `21,900 PE` at premium `70`. Maximum loss = `70`. 
  - Break-even = `21,900 - 70 = 21,830`. 
  - If expiry is `21,700`, intrinsic value = `200`, net profit = `200 - 70 = 130`.
- **Risk and reward:** Loss is limited to premium paid. Profit increases as the underlying falls, but an index/stock cannot fall below zero.
- **Indian market note:** Long put is also used as a hedge for stock holdings, but stock options can become physically settled at expiry.
- **From where to learn:** Zerodha Varsity Module 5 put option basics, NSE Academy options strategies module, NISM Equity Derivatives.
- **Best source:** Zerodha Varsity Module 5 for basics; NSE contract specs for strike/expiry rules.
- `https://web.sensibull.com/learn-options-strategies/long-put-option`

##### 1.3 Bull Call Spread || (buy In-the-Money Call -> bullish, sell Out-of-the-Money Call bearish) || net debit || option buyer 
> A bull call spread is **for an option buyer** (specifically a moderately bullish trader). It targets a trader who wants to profit from a limited price rise while lowering the upfront cost and capping the risk of buying a regular call
> **What they do:** Buy a call option at a lower strike price and simultaneously sell a call option at a higher strike price (same expiry and asset).
> **Net cash flow:** It is a `net debit` strategy because the cost of the bought call is higher than the money earned from the sold call.
> **Target outlook:** A moderately optimistic view where the asset price goes up, but only by a small or limited amount
> **Capped profit:** The maximum gain stops at the higher strike price

###### Practical Learnings: Selection, Execution & Defence

> **Use this only for a defined, moderately bullish move—not a guaranteed-profit trade or a substitute for a market view.** First classify the market using [Strategies by cash market view](#strategies-by-cash-market-view); a strong breakout with uncapped upside is usually a poor fit because the short CE caps gains.

**1. Decide the target and deadline before selecting strikes**

- Write four values before opening the chain: expected upside target, deadline, chart-based invalidation level, and maximum rupee loss. The short CE is the level where you deliberately agree to stop participating in further upside.
- Select expiry from the deadline. A move expected over several sessions needs adequate time; near-expiry spreads have rapidly accelerating Theta and Gamma risk.
- Do **not** use a fixed rule such as `OTM + 50` or `OTM + 500`. Strike distance must be judged against the underlying's expected move, volatility, support/resistance, and time remaining.

**2. Practical strike-selection framework**

- **Long CE:** A common starting shape for a swing/positional view is ATM to slightly ITM, often with a usable Delta range around `0.45–0.65`. It gives better initial directional participation than a far-OTM call and relies less on a sudden large move.
- **Short CE:** Place it at the realistic upside target or just above it—not merely at the strike with the largest premium. A Call-OI resistance zone can support this choice, but OI alone does not prove writing or direction; use the Price–OI context in [Open Interest & Price–OI Matrix](./trading_jargon_acronyms.md#open-interest--priceoi-matrix).
- **Spread width:** A wider spread behaves more like a long call: higher debit, more upside room, and higher directional exposure. A narrow spread costs less but may cap the move too early. Compare `net debit ÷ width`, break-even versus target, maximum profit versus maximum loss, and charges/slippage.
- **Far OTM long CE:** It can give a high percentage return only if a fast, unusually large move occurs. Its low Delta and time-decay dependence make it unsuitable as a default choice.

**3. Parameter priority: evaluate the combined position, not a single leg**

1. **Target, deadline, and maximum rupee loss** — these decide whether the strategy fits.
2. **Executable liquidity** — check live bid–ask, available quantity, volume, and OI for **both** legs. LTP, volume, or OI alone does not guarantee a fill. Prefer a basket/spread order or have an abort rule for a partial fill.
3. **Net Delta** — `long-call Delta − short-call Delta`; this is the spread's approximate initial directional exposure. More positive net Delta usually means earlier participation in a rally, but normally costs more.
4. **Net Theta and Gamma** — the short CE offsets part of the bought CE's negative Theta, but a debit spread can still lose when price stalls. Gamma becomes more acute near expiry, especially around ATM.
5. **IV, skew, and net Vega** — same-expiry legs partially offset Vega; they do not cancel it completely. A post-event IV fall can still hurt the spread, even if price rises modestly.
6. **Premium** — a result of the above, not the selection rule. The cheapest spread is often cheap because Delta is too low or the cap is too close.

For canonical option-chain and Greek definitions, see [Option Chain Columns](./trading_jargon_acronyms.md#option-chain-columns), [Greeks](./trading_jargon_acronyms.md#greeks), and [Volatility & Sentiment](./trading_jargon_acronyms.md#volatility--sentiment).

**4. Worked selection example — hypothetical only**
> **Buy** 1 Lot of Nifty ₹24,200 CE (`In-the-Money Call`) → Premium Paid = ₹150
> **Sell** 1 Lot of Nifty ₹24,400 CE (`Out-of-the-Money Call`) → Premium Received = ₹50
> Net Premium Cost (per share): ₹150 - ₹50 = ₹100
> Spread Width: 24,400 - 24,200 = 200 Points
> Maximum Risk (Total Capital Outlay): Net Premium * Lot Size -> ₹100 * 25 = ₹2,500
> Maximum Profit: (Spread Width - Net Premium) * Lot Size -> (200 - 100) * 25 = ₹2,500
> Breakeven Point: Lower Strike + Net Premium -> 24,200 + 100 = ₹24,300

Assume `NIFTY = 24,000`, target `24,300` within five trading sessions, and 14 calendar days remain:

- Buy `24,000 CE` at `265`: Delta `0.52`, Theta `-12/day`, Vega `9`.
- Sell `24,300 CE` at `125`: Delta `0.30`, Theta `-10/day`, Vega `7`.
- Net debit = `140` points; width = `300` points; expiry break-even = `24,140`; maximum profit = `160` points; maximum loss = `140` points, each multiplied by the **current live lot size**, plus charges.
- Approximate combined exposure: Delta `+0.22`, Theta `-2/day`, Vega `+2` per one-IV-point rise. These are model estimates that change with spot, time, and IV.

This construction matches a gradual, target-defined rise: the ATM long CE participates in the move, while the short CE is deliberately placed at the target. It is **not** automatically best: if the move is expected to be explosive beyond `24,300`, a long CE may be more suitable; if it is late or IV falls, the spread may underperform despite a correct bullish direction.

**5. Go / no-go and defence rules**

- **Go only when:** the target is near the short CE by the deadline; maximum loss (`net debit × lot size + all costs`) fits the trade and daily-loss budget; both legs are liquid; and the expected move still justifies the debit after considering IV and scheduled events.
- **No-go when:** the target lies beyond the short CE; debit is so close to the width that reward is negligible; an illiquid leg or wide bid–ask makes payoff estimates unreliable; or the thesis requires an expiry-day move.
- **Exit/defence plan before entry:** define an underlying invalidation level, spread-value loss limit, time stop, and profit-capture rule. Do not hold only because the expiry break-even remains possible.
- If the thesis fails, close the **entire spread** rather than averaging down. If the thesis remains valid but the deadline was wrong, close first and treat any later-expiry replacement as a **new trade** with a fresh target and risk budget.
- When spot reaches the short CE early, most possible value may already be captured. Do not remove the short CE casually: that creates a new naked-long-call exposure requiring new sizing and risk approval.

**6. Indian-market and professional-use notes**

- For NSE **index** options, contracts are European style and cash-settled; stock-option physical-settlement rules are separate. Still, close intentionally before expiry unless final-settlement-price exposure is part of the plan. Confirm live contract specifications, expiry, lot size, and basket margin with the exchange and broker.
- Professionals do use vertical call spreads, but not because they are “beginner-only” or inherently profitable. They model target, timing, IV, liquidity, net Greeks, costs, and portfolio loss first. Market makers generally manage aggregate Delta and volatility risk rather than selecting a retail-style strategy in isolation.
- A defined-loss payoff does not create an edge. Follow the hard risk limits in [Risk Management Rules](#72-risk-management-rules), and remember that the SEBI study cited in this book found widespread losses among individual equity F&O traders.

**Research sources:** [Zerodha Varsity — Bull Call Spread](https://zerodha.com/varsity/chapter/bull-call-spread/), [NSE — Greeks Mastery](https://www.nseindia.com/static/learn/greeks-mastery-program), [NSE — settlement mechanism](https://www.nseindia.com/products-services/equity-derivatives-settlement-mechanism), [NSE — contract specifications](https://www.nseindia.com/static/products-services/equity-derivatives-contract-specifications), [Options Industry Council — Bull Call Spread](https://www.optionseducation.org/strategies/all-strategies/bull-call-spread-debit-call-spread), and [SEBI equity F&O study](https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2024/updated-sebi-study-reveals-93-of-individual-traders-incurred-losses-in-equity-fando-between-fy22-and-fy24-aggregate-losses-exceed-1-8-lakh-crores-over-three-years%5F86906.html).

- **Basic definition:** Buy a lower strike `CE` and sell a higher strike `CE` of the same underlying and same expiry.
- **Market view:** Moderately bullish. Used when you expect upside, but not unlimited upside.
- **Basic example:** 
  - `NIFTY = 22,000`. 
    - Buy `22,000 CE` at `150`, 
    - sell `22,300 CE` at `60`. 
    - Net debit = `90`. Maximum loss = `90`. 
    - Maximum profit = strike difference `300 - 90 = 210`. 
    - Break-even = `22,000 + 90 = 22,090`.
- **Risk and reward:** Both loss and profit are limited. The short higher call reduces cost but caps profit.
- **Indian market note:** Usually easier to learn on liquid index options. Check margin benefit and liquidity for both strikes.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Bull Call Spread, NSE Academy options strategies module.
- **Best source:** Zerodha Varsity Module 6 for practical Indian payoff examples.
- **YT**
  - short 1 `https://youtube.com/shorts/sm0klOGmiY4?si=vHjZOaTIKhO0XX_X`
- `https://web.sensibull.com/learn-options-strategies/bull-call-spread`

###### YT: 
- https://youtu.be/uZAZAPnsqeo?si=VkVnoIteUwtX3D78
- https://youtu.be/GlIUbLZHVBo?si=Y987T4BXBZBrhVYp 

##### 1.4 Bear Put Spread || (Buy In-the-Money (ITM) Put and Sell Out-of-the-Money (OTM) Put) || net-debit || option buyer
> net debit = cash paid out-of-pocket
> **Viewpoint:** Moderately bearish—expects the underlying asset price to fall, but not crash drastically.
> **Risk Tolerance:** Risk-averse trader who wants capped, defined risk.
> **Goal:** Wants a cheaper alternative to buying a single put option outright by using the sold put's premium to offset the cost.
> **Action:** Buy a higher strike put + Sell a lower strike put (same expiration date).

- **Basic definition:** Buy a higher strike `PE` and sell a lower strike `PE` of the same underlying and same expiry.
- **Market view:** Moderately bearish. Used when you expect downside, but not a crash.
- **Basic example:** 
  - Assume the Nifty 50 Index is trading closely around `24,350`. You expect a moderate correction down to roughly 24,000 over the coming weeks.
  - **Buy** 1 ATM Put: `24,350` Strike Price @ ₹67.15 premium paid.
  - **Sell** 1 OTM Put: `24,100` Strike Price @ ₹17.20 premium received.
  * **Net Debit** (Cost Per Unit): ₹67.15 - ₹17.20 = ₹49.95
  * **Upfront Cost (Max Risk):** ₹49.95 × 65 = **₹3246.75**
  * **Maximum Spread:** 24,350 - 24,100 = **250 points**
  * **Maximum Profit Potential:** (Spread - Net Debit) = 250 - 49.95 = **200.05 points**
  * **Max Total Profit per Lot:** 200.05 × 65 = **₹13,003.25**
  * **Break-Even Point:** Higher Strike - Net Debit = 24,350 - 49.95 = **24,300.05**
-------------------------------------------------------------
  - `NIFTY = 22,000`. 
    - Buy `22,000 PE` at `140`, 
    - sell `21,700 PE` at `55`. Net debit = `85`. Maximum loss = `85`. 
    - strike difference `(22,000 - 21,700) - 85 = 215` => `300 - 85 = 215`
    - Maximum profit = strike difference `300 - 85 = 215`. Break-even = `22,000 - 85 = 21,915`.
- **Risk and reward:** Limited loss and limited profit. Short lower put reduces cost but caps downside profit.
- **Indian market note:** For stock options, physical settlement risk exists if positions are held to expiry.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Bear Put Spread, NSE Academy options strategies module.
- **Best source:** Zerodha Varsity Module 6 for payoff construction; NSE/NISM for settlement and risk rules.
- `https://web.sensibull.com/learn-options-strategies/bear-put-spread`

##### 1.5 Bull Put Spread || (sell a higher-strike put (OTM), buy a lower-strike (Deep-OTM) put) || option seller (credit) strategy
> **Core Action:** You sell a higher-strike put (collecting a larger premium) and simultaneously buy a lower-strike put (paying a smaller premium) for the same expiry.
> **Market Outlook:** Moderately bullish or sideways; you win if the underlying stays flat, rises, or doesn't drop past your short strike.

- **Basic definition:** Sell a higher strike `PE` and buy a lower strike `PE` of the same underlying and same expiry.
- **Market view:** Moderately bullish or not bearish. It profits if the underlying stays above the sold put strike.
- **Basic example:** 
> Assume the Nifty 50 Spot Price is trading around `24,400`. Since you expect the market to stay flat or rise, you build a protective credit spread.
> Step 1: Setting up the Trade (Lot Size = 65 Shares)
    You execute two legs with your broker
    * **Leg 1 (Short Put):** Sell `24,300` PE (Out-of-the-Money) → Collect ₹120 premium
    * **Leg 2 (Long Put):** Buy `24,100` PE (Deep Out-of-the-Money) → Pay ₹40 premium

    **Initial Cash Flow Calculations**
    * **Net Premium Credit per share:** ₹120 (Received) - ₹40 (Paid) = ₹80
    * **Net Premium Credit per lot:** ₹80 × 65 shares = ₹5,200 *(This is credited to your trading account instantly)*
> Step 2: Risk and Reward Metrics
  **Maximum Profit Potential**
    Limited strictly to the net credit collected.
  * **Max Profit:** ₹5,200 per lot
  **Maximum Loss Exposure**
      Capped at the strike width minus the net premium.
    * **Strike Width:** 24,300 - 24,100 = 200 points
    * **Max Loss per share:** 200 - ₹80 = ₹120
    * **Max Loss per lot:** 120 × 65 = ₹7,800
  **Break-Even Index Level**
    * **Break-Even:** Short Strike - Net Credit = 24,300 - 80 = **24,220**
------------------------------------------------------------------
  - `NIFTY = 22,000`. 
  - Sell `21,900 PE` at `90`, 
  - buy `21,700 PE` at `40`. **Note** - The option you buy protects you from big downmoves.
  - Net credit = `50`. Maximum profit = `50`.
  - Maximum loss = strike difference `200 - 50 = 150`. Break-even = `21,900 - 50 = 21,850`.
- **Risk and reward:** Limited profit and limited loss, but loss can still be larger than profit.
- **Indian market note:** This is an option selling strategy, so margin is required. Do not treat the received premium as free income.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Bull Put Spread, NSE Academy options strategies module, broker margin calculator.
- **Best source:** Zerodha Varsity Module 6 plus NSE/NISM risk management sections.
- `https://web.sensibull.com/learn-options-strategies/bull-put-spread`

##### 1.6 Bear Call Spread || (Sell OTM Call + Buy further OTM Call) || option seller (credit) strategy 
> **Sell a Call (Short Leg):** Choose a lower strike price closer to the current market price to collect a higher premium.
> **Buy a Call (Long Leg):** Simultaneously buy a higher strike price call to cap potential financial exposure, creating a risk-defined structure.

>> 3 Key `Risks` of Selling ITM Calls in India
* **Delta Risk:** ITM calls have a delta closer to 1.0, meaning your trade will lose money rapidly at the immediate start of any upward market move.
* **Early Assignment Risk:** While rare in cash-settled European options like Nifty index options, selling ITM options on individual stocks carries a severe risk of physical settlement and early assignment.
* **Slippage and Liquidity:** Deep ITM options often suffer from wider bid-ask spreads, making entry and exit execution more expensive.

If you are looking at a specific market setup, tell me your target Nifty index level or current market outlook so we can calculate the exact strike prices and break-even zones for your trade.

- **Basic definition:** Sell a lower strike `CE` and buy a higher strike `CE` of the same underlying and same expiry.
- **Market view:** Moderately bearish or not bullish. It profits if the underlying stays below the sold call strike.
- **Basic example:** 
  > Nifty 50 Example Trade
    >> Imagine NIFTY 50 is trading at `24,500`. You expect the market to stay range-bound or drop slightly over the next week. You execute a weekly credit spread:
    >> * **Sell:** `24,600` CE at ₹120 (lower strike, short position)
    >> * **Buy:** `24,800` CE at ₹40 (higher strike, long protection position)
    >> **Net Premium Received (Credit):** ₹120 − ₹40 = ₹80 per lot (₹80 × 65 = ₹5,200 maximum profit — NIFTY lot size is **65**, not the pre-2024 25)
    >> Scenario Outcomes at Expiry
      >>> * **Scenario A (Nifty falls to 24,300 or stays flat at 24,500):** Both options expire worthless. You keep the entire net credit of ₹2,000 (**Maximum Profit**).
      >>> * **Scenario B (Nifty rallies past 24,600 to 24,700):** Your short call loses value, but your long 24,800 CE cushions severe upward movement. The loss is calculated as the spread width (24,800 − 24,600 = 200 points) minus the credit received (80 points) = 120 points × 65 = ₹7,800 **Maximum Loss**.

------------------------------------------------------------------------------------------------
  - `NIFTY = 22,000`. 
    - Sell `22,100 CE` at `100`, 
    - buy `22,300 CE` at `45`. **Note** - The option you buy protects you from big upmoves
    - Net credit = `55`. Maximum profit = `55`. Maximum loss = strike difference `200 - 55 = 145`. Break-even = `22,100 + 55 = 22,155`.
- **Risk and reward:** Limited profit and limited loss. Short call risk is capped by the bought higher call.
- **Indian market note:** Requires margin. Check if both strikes are liquid; wide spreads can destroy expected edge.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Bear Call Spread, NSE Academy options strategies module.
- **Best source:** Zerodha Varsity Module 6 plus NSE/NISM for margin/risk context.
- `https://web.sensibull.com/learn-options-strategies/bear-call-spread`

##### 1.7 Covered Call on stock holding || (on shares holdings) || not now 

- **Basic definition:** Hold shares and sell a `CE` against those shares to earn premium.
- **Market view:** Neutral to mildly bullish on a stock you already own.
- **Basic example:** 
  - You hold shares of an F&O stock at `1,000`. 
  - Sell `1,050 CE` at `20`. 
  - If expiry is below `1,050`, you keep premium. 
  - If expiry is above `1,050`, upside beyond `1,050` is capped because the short call can create delivery obligation.
- **Risk and reward:** Premium gives small downside cushion, but stock downside remains large. Upside is capped.
- **Indian market note:** This is mainly for physically settled stock options, not index options. You must hold enough deliverable shares and understand expiry delivery.
- **From where to learn:** NISM Equity Derivatives, NSE settlement mechanism, NSE contract specs, SEBI risk material.
- **Best source:** NISM/NSE for Indian physical settlement rules; use Zerodha Varsity for call payoff basics.

##### 1.8 Protective Put / Married Put on stock holding || (on shares holdings) || not now 

- **Basic definition:** Hold shares and buy a `PE` on the same stock to protect downside.
- **Market view:** Bullish long-term on the stock but wants protection against near-term fall.
- **Basic example:** 
  - You hold an F&O stock at `1,000`. 
  - Buy `950 PE` at `25`. Your approximate protected level is `950`, but premium cost makes effective floor `950 - 25 = 925` before charges. 
  - If stock crashes to `850`, the put gains intrinsic value.
- **Risk and reward:** Downside is reduced below the put strike, but protection costs premium. Upside in stock remains open after paying the put cost.
- **Indian market note:** Works only where stock options are available and liquid. Physical settlement and lot-size mismatch must be handled carefully.
- **From where to learn:** NISM Equity Derivatives, NSE settlement mechanism, Zerodha Varsity Module 5 put option basics.
- **Best source:** NISM/NSE for Indian stock option settlement; Varsity for payoff basics.

#### 2. Hedging strategies || all not now

##### 2.1 Protective Put || (on shares holdings) || institutional portfolio managers || not now 

- **Basic definition:** Buy a `PE` to hedge an existing long stock or portfolio exposure.
- **Market view:** You want to stay invested but limit downside for a defined period.
- **Basic example:** 
  - You own a stock at `1,000` and buy `950 PE` at `25`. 
  - If stock falls to `850`, the put has `100` intrinsic value, partly offsetting the stock loss.
- **Risk and reward:** Hedge cost is the premium. Protection is strongest below the put strike.
- **Indian market note:** Exact one-to-one hedging may be difficult because option lots may not match share quantity. Portfolio hedges may use index puts if the portfolio is highly correlated with `NIFTY` or `SENSEX`.
- **From where to learn:** NISM Equity Derivatives, SEBI derivatives education, NSE Academy options strategies.
- **Best source:** NISM for hedging concepts and Indian settlement/risk framework.

##### 2.2 Collar || (on shares holdings) || institutional portfolio managers|| not now 

- **Basic definition:** Hold shares, buy a protective `PE`, and sell a higher strike `CE` to reduce hedge cost.
- **Market view:** You want downside protection and are willing to cap upside.
- **Basic example:** 
  - Stock = `1,000`. 
    - Buy `950 PE` at `25`, 
    - sell `1,080 CE` at `20`. 
    - Net hedge cost = `5`. 
    - Downside is protected below `950` approximately, while upside is capped near `1,080`.
- **Risk and reward:** Lower hedge cost than only buying a put, but profit above sold call strike is capped.
- **Indian market note:** For stock options, the sold call can create physical delivery obligation. Keep shares ready and check lot size.
- **From where to learn:** NISM Equity Derivatives, NSE Academy options strategies, NSE settlement mechanism.
- **Best source:** NISM/NSE for Indian hedging and physical settlement rules.

##### 2.3 Covered Call || (on shares holdings) || institutional portfolio managers|| not now 

- **Basic definition:** Own shares and sell a `CE` against the holding.
- **Market view:** Neutral to mildly bullish; used to generate premium income from existing stock holding.
- **Basic example:** 
  - Hold stock at `1,000`, 
    - sell `1,050 CE` at `20`. Maximum upside is roughly `1,050 - 1,000 + 20 = 70` before charges. Below `1,000`, stock loss remains, cushioned only by `20` premium.
- **Risk and reward:** Premium income is limited. Stock downside remains. Upside is capped.
- **Indian market note:** This strategy is most relevant for physically settled stock options. It is not a free income trade because the stock can fall much more than the premium.
- **From where to learn:** NISM Equity Derivatives, NSE settlement mechanism, Zerodha Varsity Module 5 call payoff.
- **Best source:** NSE/NISM for settlement and risk; Varsity for basic call mechanics.

##### 2.4 Synthetic Long Futures / Synthetic Long Stock || institutional portfolio managers|| not now 
> **Leg 1:** Buy a Call option (Bullish, unlimited upside)
> **Leg 2:** Sell a Put option (Bullish/Neutral, downside risk if price falls)
> **Core Goal:** Replicate the linear delta-1 payoff of a futures contract without trading the actual high-margin futures contract.
> If you are strictly an options trader, do not trade futures, and do not hold an underlying stock portfolio, this strategy is absolutely NOT a hedge.
> For a retail options trader, this is a highly speculative, high-risk directional bet
> **No Offsetting Positions:** A hedge requires two opposing forces to balance each other out. If you only trade this options combo by itself, you have nothing to balance.
> **Pure Downside Exposure:** You are acting as a naked option seller on the Put side. If the NIFTY 50 crashes, your long Call becomes worthless, and your short Put will lose a massive amount of money with no protection.
> **High Margin Requirement:** Because you are selling an uncovered Put, your broker will block a substantial amount of margin capital (similar to trading a future) because of the immense risk.


- **Basic definition:** Buy `CE` and sell `PE` at the same strike and same expiry to create payoff similar to a long futures position.
- **Market view:** Bullish; behaves like long futures, not like limited-risk option buying.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Buy `22,000 CE` at `150`, 
  - sell `22,000 PE` at `130`. Net debit = `20`. 
  - At expiry `22,300`, CE value = `300`, PE = `0`, net profit = `300 - 20 = 280`. 
  - At expiry `21,700`, CE = `0`, PE loss = `300`, net loss = `300 + 20 = 320`.
- **Risk and reward:** Upside and downside behave like futures. Loss can be large because of the short put leg.
- **Indian market note:** Requires margin because of the short `PE`. For stock options, physical settlement risk applies.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Synthetic Long and Arbitrage, NSE Academy options strategies, NISM Equity Derivatives.
- **Best source:** Zerodha Varsity Module 6 for Indian examples.
- `https://web.sensibull.com/learn-options-strategies/long-synthetic-future`

##### 2.5 Synthetic Short Futures / Synthetic Short Stock || institutional portfolio managers|| not now
> For a pure options trader with no underlying stock portfolio, a Synthetic Short Future is absolutely NOT a hedge—it is a highly aggressive, high-risk bearish bet.

- **Basic definition:** Buy `PE` and sell `CE` at the same strike and same expiry to create payoff similar to a short futures position.
- **Market view:** Bearish; behaves like short futures.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Buy `22,000 PE` at `140`, 
  - sell `22,000 CE` at `150`. Net credit = `10`. 
  - At expiry `21,700`, PE value = `300`, CE = `0`, net profit = `300 + 10 = 310`. 
  - At expiry `22,300`, CE loss = `300`, net loss = `300 - 10 = 290`.
- **Risk and reward:** Profit if underlying falls; loss can be large if underlying rises.
- **Indian market note:** Requires margin because of the short call. Naked short call risk is high, even when paired synthetically.
- **From where to learn:** Zerodha Varsity Module 6 synthetic long/arbitrage chapter for put-call parity logic, NSE Academy options strategies, NISM.
- **Best source:** Zerodha Varsity Module 6 plus NISM for risk.
- `https://web.sensibull.com/learn-options-strategies/short-synthetic-future`

##### 2.6 Delta Hedging ||  institutional portfolio managers || not now
> To delta hedge a single option position, you must trade an underlying asset (like NIFTY futures or an exact basket of NIFTY stocks) to offset the delta. If you refuse to trade futures or hold a stock portfolio, you cannot perform true delta hedging

- **Basic definition:** Adjust stock/futures/options positions so the net delta of the portfolio is close to the desired level, often near zero for market-neutral hedging.
- **Market view:** Risk management method, not one fixed directional strategy.
- **Basic example:** You have an options position with total delta `+500` shares equivalent. To reduce directional exposure, you may short futures or sell shares equivalent to about `500` delta, then rebalance as price and Greeks change.
- **Risk and reward:** Reduces directional risk but introduces transaction cost, slippage, basis risk, and rebalancing risk. Gamma and volatility can still cause losses.
- **Indian market note:** Retail traders must be careful because frequent rebalancing in NSE/BSE contracts can increase costs. Lot size and liquidity make exact hedging difficult.
- **From where to learn:** NISM Equity Derivatives for Greeks and risk management, Zerodha Varsity Module 5 Greeks, NSE Academy options strategies.
- **Best source:** NISM for Indian derivatives risk framework; Varsity Module 5 for Greeks.

#### 3. Volatility strategies

##### 3.1 Long Straddle (पैर फैलाकर बैठना) || net debit  || option buyer ||
> The target trader is a volatility trader who expects a massive price swing in NIFTY 50 in either direction (up or down) but does not know which way it will go.
> Time decay (Theta) will hurt your position very fast if the market stays still. This is rarely used for a standard straddle because the risk-reward is poor.
> **Maximum Loss:** Limited to the total premium paid (happens if NIFTY stays right at the strike price at expiry).
> **Maximum Profit:** Unlimited if NIFTY surges or crashes heavily.
> **Time Decay:** Time is the buyer's enemy; if NIFTY moves sideways, both options lose value daily.
> You do not choose a side. You place one "leg" on the bullish side and one "leg" on the bearish side.

- **Basic definition:** Buy one `CE` and one `PE` at the same strike and same expiry.
- **Market view:** Expect a large move, but direction is uncertain. Usually used before events only if premiums are not too expensive.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Buy `22,000 CE` at `150` and 
  - Buy `22,000 PE` at `140`. Total premium = `290`. 
  - Upper break-even = `22,290`. Lower break-even = `21,710`.
- **Risk and reward:** Maximum loss is total premium paid. Profit needs a large move beyond either break-even before expiry.
- **Indian market note:** Event-day IV crush can hurt long straddles even if direction is right but move is smaller than priced-in premium.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Long Straddle, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6 for Indian payoff example.
- `https://web.sensibull.com/learn-options-strategies/long-straddle`

##### 3.2 Long Strangle (गला घोंटना) || (buy OTM CE & buy OTM PE) || net debit  || option buyer ||
> The targeted trader is a volatility trader who expects a massive, sharp price swing in the underlying asset before expiration, but does not know whether the market will break upward or downward
> **Why OTM over ITM:** Using In-the-Money (ITM) strikes would make the trade expensive (like a deep long combination or costly straddle). OTM options are cheaper, lowering the total risk, though they require a larger market breakout to turn a profit.
> By buying or selling these two separate lines, you are essentially `choking the current market price` between two tight walls.

- **Basic definition:** Buy an OTM `CE` and an OTM `PE` of the same underlying and same expiry.
- **Market view:** Expect a large move in either direction, but want cheaper entry than straddle.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Buy `22,200 CE` at `80` and
  - Buy `21,800 PE` at `70`. Total premium = `150`. 
  - Upper break-even = `22,350`. Lower break-even = `21,650`.
- **Risk and reward:** Maximum loss is total premium. Needs a bigger move than straddle because both options start OTM.
- **Indian market note:** Cheap options can still expire worthless. Check liquidity at far OTM strikes.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Long and Short Strangle, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6.
- `https://web.sensibull.com/learn-options-strategies/long-strangle`

##### 3.3 Short Straddle (पैर फैलाकर बैठना) || net credit || option seller || 

> ⛔ **Do not trade this version.** The naked short straddle below has **undefined maximum loss** and is an automatic blocker under [`option_chain_n_greeks.md` §7](../option_chain_n_greeks.md). Learn the payoff here; trade the **hedged, delta-neutral, time-boxed** replacement in [§8.6.1](#861-intraday-delta-neutral-hedged-short-straddle--the-920-structure).

> targeting neutral or `sideways markets`. The trader sells both an At-The-Money (ATM) call and an ATM put at the same strike price and expiry, collecting maximum upfront premium and profiting from time decay (Theta) and falling volatility
> **Target Trader:** Advanced/experienced option sellers with high risk tolerance.
> **Core Goal:** Expect the underlying index to stay flat or range-bound so both options expire worthless.
> **Risk/Reward:** Limited maximum profit (the total premium collected) and high/unlimited potential risk if NIFTY moves sharply

- **Basic definition:** Sell one `CE` and one `PE` at the same strike and same expiry.
- **Market view:** Expect the underlying to stay near the sold strike and implied volatility/time value to fall.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Sell `22,000 CE` at `150` 
  - Sell `22,000 PE` at `140`. Total credit = `290`. 
  - Upper break-even = `22,290`. Lower break-even = `21,710`. Maximum profit = `290` if expiry is exactly `22,000`.
- **Risk and reward:** Profit is limited to premium received. Loss can be very large on either side.
- **Indian market note:** This is a high-risk option selling strategy requiring margin. Sudden RBI policy, election, global market, gap-up/gap-down, or expiry volatility can create large losses.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Short Straddle, NSE Academy options strategies, SEBI derivatives risk material.
- **Best source:** Zerodha Varsity Module 6 for payoff; SEBI/NISM for risk awareness.
- `https://web.sensibull.com/learn-options-strategies/short-straddle`

##### 3.4 Short Strangle (गला घोंटना) || net credit || option seller || 

> ⛔ **Do not trade this version.** Naked = undefined loss = automatic blocker. The tradeable form is the **delta-banded hedged strangle** in [§8.6.2](#862-the-delta-banded-hedged-strangle--the-weekly-workhorse) — and note that selling *equidistant* strikes is not neutral: see [§8.6.8](#868-skew-aware-delta-matched-condor--stop-measuring-in-points).

> **Market Outlook:** Neutral or low volatility. The seller expects the index to stay inside a specific safe zone until expiration.
> **Profit Source:** Time decay (Theta) and drops in market volatility, which make both OTM contracts lose value so they can expire worthless.
> **Risk** If a sharp breakout pushes NIFTY past 24,600 or below 23,400, losses can grow rapidly and become theoretically unlimited.

- **Basic definition:** Sell an OTM `CE` and an OTM `PE` of the same underlying and same expiry.
- **Market view:** Expect range-bound movement between the sold strikes.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Sell `22,300 CE` at `60` and 
  - Sell `21,700 PE` at `55`. Total credit = `115`. Upper break-even = `22,415`. Lower break-even = `21,585`.
- **Risk and reward:** Profit is limited to premium received. Loss can be very large if market moves strongly beyond either break-even.
- **Indian market note:** Wider strikes feel safer but can fail in gap moves. Margin and stop-loss planning are essential.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Long and Short Strangle, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6 plus SEBI/NISM risk material.
- `https://web.sensibull.com/learn-options-strategies/short-strangle`

##### 3.5 Long Call Butterfly || option buyer || 
> It is executed by an option buyer because you pay a net debit upfront to set up the four legs. However, it embeds short options (the body) to cheapen the trade
> 

- **Basic definition:** A three-strike limited-risk strategy using calls: buy 1 lower strike `CE`, sell 2 middle strike `CE`, buy 1 higher strike `CE`, same expiry and equal strike spacing.
- **Market view:** Expect expiry near the middle strike with low movement.
- **Basic example:** 
  - Assume the NIFTY 50 index is trading at `24,000`. A trader expects NIFTY to stay near 24,000 and expire right there at the end of the month. 
  - They set up an equidistant 100-point Long Call Butterfly using 4 contracts:
  - **Buy 1 ITM Call (Lower Wing):** Strike 23,900 Call at a cost of ₹180.
  - **Sell 2 ATM Calls (The Body):** Strike 24,000 Call, collecting ₹100 each = ₹200 collected.
  - **Buy 1 OTM Call (Upper Wing):** Strike 24,100 Call at a cost of ₹45.
  - Net Debit Paid (Max Loss): ₹180 (ITM bought) + ₹45 (OTM bought) - ₹200 (2 ATM sold) = ₹25 net debit. This is your total risk.


  - `NIFTY = 22,000`. 
  - Buy `21,800 CE`, 
  - sell 2 lots `22,000 CE`, 
  - buy `22,200 CE`. If net debit is `60`, maximum loss = `60`. 
  - Maximum profit occurs near `22,000` and is approximately strike gap `200 - 60 = 140`.
- **Risk and reward:** Limited loss and limited profit. Best result if expiry is close to middle strike.
- **Indian market note:** Needs three strikes and four option legs; brokerage, slippage, and bid-ask spread matter a lot.
- **From where to learn:** NSE Academy options strategies, NISM Equity Derivatives, payoff calculators from Indian brokers.
- **Best source:** NSE Academy for strategy payoff; NSE/BSE option chain for tradability.
- `https://web.sensibull.com/learn-options-strategies/bull-butterfly`

##### 3.6 Long Put Butterfly || option buyer || 
> **Strategy Structure (1:2:1 Ratio)** Assume NIFTY 50 trades at 24,000. You choose a 200-point strike interval
  - **Buy 1 Higher-Strike Put (In-The-Money / ITM)** Buy 1 ITM Put at strike 24,200 (Higher strike)
  - **Sell 2 Middle-Strike Puts (At-The-Money / ATM)** Sell 2 ATM Puts at strike 24,000 (Middle strike)
  - **Buy 1 Lower-Strike Put (Out-of-The-Money / OTM)** Buy 1 OTM Put at strike 23,800 (Lower strike)

- **Basic definition:** A three-strike limited-risk strategy using puts: buy 1 higher strike `PE`, sell 2 middle strike `PE`, buy 1 lower strike `PE`, same expiry and equal strike spacing.
- **Market view:** Expect expiry near the middle strike with low movement.
- **Basic example:** 
  - `NIFTY = 22,000`. 
  - Buy `22,200 PE`, 
  - sell 2 lots `22,000 PE`, 
  - buy `21,800 PE`. 
  - If net debit is `55`, maximum loss = `55`. Maximum profit near `22,000` is approximately `200 - 55 = 145`.
- **Risk and reward:** Limited loss and limited profit. Time decay can help if price stays near the middle strike.
- **Indian market note:** Use only where all strikes have good liquidity; otherwise execution can be poor.
- **From where to learn:** NSE Academy options strategies, NISM Equity Derivatives.
- **Best source:** NSE Academy for payoff construction.

##### 3.7 Long Iron Butterfly || option seller || 
> designed for neutral, range-bound traders who profit from low volatility and time decay.
> **Target Trader:** Premium seller / neutral market trader.
> **Market Outlook:** Sideways, stable, or low-volatility.

- **Basic definition:** Buy ATM `CE` and ATM `PE`, then sell one OTM `CE` and one OTM `PE` as wings. It is the debit/long-volatility version of an iron butterfly.
- **Market view:** Expect a large move away from the middle strike, but want defined risk and capped profit.
- **Basic example:** 
  - Assume NIFTY is trading at 24,000 (At-The-Money / ATM). You set up an Iron Butterfly with 500-point wings:
  - **Sell (Short) 1 ATM Call:** Strike 24,000 CE (Earns premium)
  - **Sell (Short) 1 ATM Put:** Strike 24,000 PE (Earns premium)
    - You sell these options. They carry the highest time decay (theta) and highest initial value. Your goal is for NIFTY to stay right here so these expire at zero, letting you pocket the cash.
  - **Buy (Long) 1 OTM Call:** Strike 24,500 CE (Protection wing, costs less premium)
  - **Buy (Long) 1 OTM Put:** Strike 23,550/23,500 PE (Protection wing, costs less premium)
    - buy these options. They act as insurance ("wings"). If NIFTY crashes to 23,000 or surges to 25,000, your losses are strictly capped because your OTM bought options turn into ITM safety nets, preventing catastrophic loss.

---------------------------------------------------------------------------------
  - `NIFTY = 22,000`. 
  - Buy `22,000 CE`, 
  - buy `22,000 PE`, 
  - sell `22,200 CE`, 
  - sell `21,800 PE`. If net debit is `70`, maximum loss is `70` near `22,000`; 
  - maximum profit is wing width `200 - 70 = 130` if expiry is at or beyond either wing.
- **Risk and reward:** Limited loss and limited profit. It needs movement away from the ATM strike; time decay hurts if price stays near the middle.
- **Indian market note:** Many Indian traders use "iron butterfly" to mean the short/credit version, so confirm whether the payoff is debit long-volatility or credit short-volatility before placing orders.
- **From where to learn:** NSE Academy options strategies, NISM, Indian broker payoff tools.
- **Best source:** NSE Academy for structure; broker payoff tool for live margin/payoff.
- `https://web.sensibull.com/learn-options-strategies/iron-butterfly`

#### 4. Range-bound / neutral strategies

##### 4.1 Iron Condor (बड़ा गिद्ध) || option seller || Sideways || 

> ▶ **Live practice:** strikes must be **delta-matched, not point-matched** ([§8.6.8](#868-skew-aware-delta-matched-condor--stop-measuring-in-points)); the positional 25–40 DTE version with the 50%-target rule is in [§8.6.9](#869-positional-2540-dte-iron-condor--the-compounding-engine); directional leans without a naked leg are in [§8.6.7](#867-unbalanced-ratiod-iron-condor--lean-the-view-without-a-naked-leg).

> **Market Outlook:** Sideways or range-bound (expects the index to stay calm)
> **Primary Goal:** Collect upfront premium and let time decay erode option values so all legs expire worthless or can be bought back cheaper.

- **Basic definition:** Sell an OTM `PE` spread and sell an OTM `CE` spread together. It is a defined-risk range strategy.
- **Market view:** Expect underlying to stay between sold put and sold call strikes.
- **Basic example:** 
  - NIFTY 50 Index Example SetupAssume NIFTY 50 is trading at `24,500`. A trader expects NIFTY to stay between 24,000 and 25,000 until expiration. They construct an Iron Condor using 4 legs on the same expiry:
  - **Sell (Short) 1 OTM Put:** Strike `24,000 PE` (Seller collects premium)
  - **Buy (Long) 1 Farther OTM Put:** Strike `23,800 PE` (Buyer pays a smaller premium to cap downside risk)
  - **Sell (Short) 1 OTM Call:** Strike `25,000 CE` (Seller collects premium)
  - **Buy (Long) 1 Farther OTM Call:** Strike `25,200 CE` (Buyer pays a smaller premium to cap upside risk)

------------------------------------------------------------------------

  - `NIFTY = 22,000`. 
    - Buy `21,600 PE`, 
    - sell `21,800 PE`, 
    - sell `22,200 CE`, 
    - buy `22,400 CE`. 
  - If net credit is `80`, maximum profit = `80`. Maximum loss = wing width `200 - 80 = 120`.

- **Risk and reward:** Limited profit and limited loss. Profit comes from time decay if price stays in the range.
- **Indian market note:** Zerodha Varsity discusses iron condor under Indian margin framework context. Always verify live margin and liquidity.
- **From where to learn:** Zerodha Varsity Module 6 chapter on Iron Condor, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6 for Indian example and margin context.

##### 4.2 Iron Butterfly || option seller || Sideways || 

> ▶ **Live practice:** the Iron Fly is the *only* structure that still collects meaningful premium on expiry day, because 0-DTE premium is concentrated at the money. The expiry-day version — with the four-part entry filter and the CAS hard-exit rules — is [§8.6.10](#8610-0-dte-hedged-iron-fly-under-cas--expiry-day-done-properly). It is also the standard event-IV structure ([§8.6.11](#8611-iv-crush-event-harvest--rbi-policy-budget-big-results)).

> **Sell** an At-The-Money (ATM) Call and an ATM Put (the short body).
> **Buy** an Out-Of-The-Money (OTM) Call and an OTM Put (the protective wings).

- **Basic definition:** Sell ATM `CE` and ATM `PE`, then buy protective OTM `CE` and OTM `PE`.
- **Market view:** Strong range-bound view around one central strike.
- **Basic example:** 
  - Assume NIFTY 50 is trading at `24,500`.
  - The Body (Sold ATM options):
    - **Sell** 1 NIFTY `24,500 CE` (ATM) 
    - **Sell** 1 NIFTY `24,500 PE` (ATM)
  - The Wings (Bought OTM options for risk cover):
    - **Buy** 1 NIFTY `24,800 CE` (OTM Call)
    - **Buy** 1 NIFTY `24,200 PE` (OTM Put)


`NIFTY = 22,000`. Sell `22,000 CE`, sell `22,000 PE`, buy `22,200 CE`, buy `21,800 PE`. If net credit is `130`, max profit = `130`, max loss = `200 - 130 = 70`.
- **Risk and reward:** Defined risk and defined reward. Narrower profit zone than iron condor.
- **Indian market note:** Requires four legs and margin. Exit plan matters because risk can expand quickly near either wing.
- **From where to learn:** NSE Academy options strategies, NISM, Indian broker payoff tools.
- **Best source:** NSE Academy for payoff; broker margin/payoff calculator for live numbers.

##### 4.3 Call Condor || option buyer || SKIPPED

- **Basic definition:** A four-leg call strategy using four increasing `CE` strikes: buy lowest strike, sell next strike, sell next higher strike, buy highest strike.
- **Market view:** Expect underlying to expire between the two short call strikes.
- **Basic example:** `NIFTY = 22,000`. Buy `21,700 CE`, sell `21,900 CE`, sell `22,100 CE`, buy `22,300 CE`. If net debit is `70`, maximum loss = `70`. Maximum profit is the lower spread width `200 - 70 = 130` when expiry is between `21,900` and `22,100`.
- **Risk and reward:** Limited loss and limited profit. Similar range payoff to iron condor but built only with calls.
- **Indian market note:** More legs mean more execution cost. Prefer liquid index strikes for learning.
- **From where to learn:** NSE Academy options strategies, NISM, payoff calculators.
- **Best source:** NSE Academy for strategy payoff structure.

##### 4.4 Put Condor

- **Long Put Condor** (For Option Buyers / Low Volatility)
  - A Long Put Condor is a net debit strategy used by a trader acting primarily as an option buyer who expects the index to stay calm and range-bound within specific middle strikes.
  - **Target Trader:** Neutral trader expecting low volatility (sideways market).
    - NIFTY 50 Example Setup (assuming NIFTY is trading at `24,000`):
      - **Buy** 1 ITM Put at 24,300 (Deep in-the-money / Higher strike)
      - **Sell** 1 ITM/ATM Put at 24,100 (Higher middle strike)
      - **Sell** 1 OTM Put at 23,900 (Lower middle strike)
      - **Buy** 1 OTM Put at 23,700 (Far out-of-the-money / Lowest strike)
    - **Goal:** You pay a net debit to enter. Maximum profit is achieved if NIFTY expires right between the two short middle strikes (23,900 and 24,100).

- **Short Put Condor** (For `Option Sellers` / High Volatility)
  - A Short Put Condor is a net credit strategy used by a trader acting primarily as an option seller who expects a sharp breakout or high volatility in either direction.
  - **Target Trader:** Directional/breakout trader expecting a large price swing up or down.
  - NIFTY 50 Example Setup (assuming NIFTY is trading at `24,000`):
    - **Sell** 1 OTM Put at 23,900 (Lower strike - premium collected)
    - **Buy** 1 OTM Put at 23,700 (Lower middle strike - protection)
    - **Buy** 1 ITM Put at 24,100 (Higher middle strike - protection)
    - **Sell** 1 ITM Put at 24,300 (Higher strike - premium collected)
  - **Goal:** You collect a net credit upfront. Maximum profit is achieved if NIFTY makes a strong move and breaks out past your outer short strikes (either dropping below 23,900 or rallying above 24,300).

- **Basic definition:** A four-leg put strategy using four decreasing `PE` strikes: buy highest strike, sell next strike, sell next lower strike, buy lowest strike.
- **Market view:** Expect underlying to expire between the two short put strikes.
- **Basic example:** `NIFTY = 22,000`. Buy `22,300 PE`, sell `22,100 PE`, sell `21,900 PE`, buy `21,700 PE`. If net debit is `75`, maximum loss = `75`. Maximum profit is approximately `200 - 75 = 125` if expiry is between `21,900` and `22,100`.
- **Risk and reward:** Limited loss and limited profit.
- **Indian market note:** Same payoff family as call condor/iron condor, but execution liquidity can differ between calls and puts.
- **From where to learn:** NSE Academy options strategies, NISM, broker payoff tools.
- **Best source:** NSE Academy for payoff structure.

##### 4.5 Short Straddle || [3.3 Short Straddle](#33-short-straddle) ||

- **Basic definition:** Sell ATM `CE` and ATM `PE` of same strike and expiry.
- **Market view:** Neutral and low-volatility view.
- **Basic example:** `NIFTY = 22,000`. Sell `22,000 CE` at `150` and `22,000 PE` at `140`; total credit `290`; break-evens `21,710` and `22,290`.
- **Risk and reward:** Limited profit and very large open-ended risk on both sides.
- **Indian market note:** Treat this as high-risk even if it appears in neutral/income sections. It is not suitable for beginners with small capital.
- **From where to learn:** Zerodha Varsity Module 6 Short Straddle, SEBI/NISM risk material.
- **Best source:** Zerodha Varsity for payoff and SEBI/NISM for risk warning.

##### 4.6 Short Strangle || [4.6 Short Strangle](#46-short-strangle) || 

- **Basic definition:** Sell OTM `CE` and OTM `PE` of same expiry.
- **Market view:** Neutral/range-bound view with wider range than short straddle.
- **Basic example:** `NIFTY = 22,000`. Sell `22,300 CE` at `60`, sell `21,700 PE` at `55`; total credit `115`; break-evens `21,585` and `22,415`.
- **Risk and reward:** Limited profit and very large risk if the market trends or gaps.
- **Indian market note:** Needs margin, discipline, and event-risk awareness.
- **From where to learn:** Zerodha Varsity Module 6 Long and Short Strangle, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6.

#### 5. Spread strategies advanced

##### 5.1 Vertical Spreads

- **Basic definition:** A two-option spread with same underlying and same expiry but different strikes. It can be debit or credit, bullish or bearish.
- **Market view:** Directional with defined risk.
- **Basic example:** Bull call spread, bear put spread, bull put spread, and bear call spread are all vertical spreads because strikes are different but expiry is same.
- **Risk and reward:** Risk and reward are usually defined by strike difference and net premium.
- **Indian market note:** Vertical spreads are useful in NSE/BSE because they reduce naked option risk, but execution and liquidity still matter.
- **From where to learn:** Zerodha Varsity Module 6 spread chapters, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6.

##### 5.1.1 Bull Call Spread || [1.3 Bull Call Spread](#13-bull-call-spread)

- **Basic definition:** Buy lower strike `CE`, sell higher strike `CE`, same expiry.
- **Basic example:** Buy `22,000 CE` at `150`, sell `22,300 CE` at `60`; net debit `90`; max profit `210`; max loss `90`.
- **From where to learn:** Zerodha Varsity Module 6 Bull Call Spread.
- **Best source:** Zerodha Varsity Module 6.

##### 5.1.2 Bear Put Spread || [1.4 Bear Put Spread](#14-bear-put-spread)

- **Basic definition:** Buy higher strike `PE`, sell lower strike `PE`, same expiry.
- **Basic example:** Buy `22,000 PE` at `140`, sell `21,700 PE` at `55`; net debit `85`; max profit `215`; max loss `85`.
- **From where to learn:** Zerodha Varsity Module 6 Bear Put Spread.
- **Best source:** Zerodha Varsity Module 6.

##### 5.1.3 Bull Put Spread || [1.5 Bull Put Spread](#15-bull-put-spread)

- **Basic definition:** Sell higher strike `PE`, buy lower strike `PE`, same expiry.
- **Basic example:** Sell `21,900 PE` at `90`, buy `21,700 PE` at `40`; net credit `50`; max profit `50`; max loss `150`.
- **From where to learn:** Zerodha Varsity Module 6 Bull Put Spread.
- **Best source:** Zerodha Varsity Module 6 plus broker margin calculator.

##### 5.1.4 Bear Call Spread || [1.6 Bear Call Spread](#16-bear-call-spread)

- **Basic definition:** Sell lower strike `CE`, buy higher strike `CE`, same expiry.
- **Basic example:** Sell `22,100 CE` at `100`, buy `22,300 CE` at `45`; net credit `55`; max profit `55`; max loss `145`.
- **From where to learn:** Zerodha Varsity Module 6 Bear Call Spread.
- **Best source:** Zerodha Varsity Module 6 plus broker margin calculator.

##### 5.2 Calendar Spread || not same expiry 

> ⚠️ **This entry pre-dates the 1-Feb-2025 rule change and is incomplete without it.** SEBI removed the calendar-spread margin benefit for contracts expiring the same day: on the near leg's **expiry morning** the offset vanishes and margin can jump 3–4×, triggering an RMS auto-square-off you did not choose. **Close or roll the near leg the session before its expiry.** Mechanics, worked numbers and the Double Calendar / "Batman" build: [§8.6.12](#8612-double-calendar--batman--and-the-february-2025-margin-trap).

- **Basic definition:** Buy and sell options of the same type and strike but different expiries. Usually sell near expiry and buy later expiry.
- **Market view:** Expect near-term time decay while maintaining longer-term optionality.
- **Basic example:** `NIFTY = 22,000`. Sell current-week `22,000 CE` and buy next-month `22,000 CE`. If near expiry decays faster and price stays near strike, the spread may gain.
- **Risk and reward:** Exposed to time decay, volatility changes, and calendar margin. Risk is not as simple as a same-expiry vertical spread.
- **Indian market note:** Expiry availability and liquidity vary. Weekly/monthly expiry rules can change by exchange circular, so check current NSE/BSE contract specs.
- **From where to learn:** NSE Academy options strategies, NISM, broker payoff/margin tools.
- **Best source:** NSE Academy/NISM for concept; NSE/BSE contract specs for actual expiries.

##### 5.3 Diagonal Spread || not same expiry 

- **Basic definition:** Buy and sell options with different strikes and different expiries.
- **Market view:** Directional plus time-decay/volatility view.
- **Basic example:** Buy next-month `22,000 CE`, sell current-week `22,300 CE`. This can express a mildly bullish view while collecting near-term premium.
- **Risk and reward:** More complex than vertical/calendar because both strike and expiry differ. Greeks change in a non-linear way.
- **Indian market note:** Use only after understanding expiry, IV, margin, and liquidity. Do not enter just because payoff graph looks attractive.
- **From where to learn:** NSE Academy options strategies, NISM Greeks/risk sections, broker payoff tools.
- **Best source:** NSE Academy for structure; NISM for Greeks/risk.

##### 5.4 Ratio Spread || option seller || Sideways or slightly bullish/bearish || 

> ▶ **Live practice:** a front ratio spread sells more than it buys, so it carries an unhedged leg — a blocker as an **entry**. The professionally useful form is the **ladder used as a repair** on an already-tested vertical: [§8.6.13](#8613-the-ladder--a-repair-never-an-entry). For a directional lean with every leg defined, use the unbalanced condor ([§8.6.7](#867-unbalanced-ratiod-iron-condor--lean-the-view-without-a-naked-leg)) or the Broken-Wing Butterfly ([§8.6.6](#866-broken-wing-butterfly-bwb--the-credit-structure-with-zero-risk-on-one-side)) instead.

> Who it is for: Primarily an option seller (front ratio spread) because you sell more contracts than you buy. However, variants like the backspread exist for buyers.
> **Market Outlook:** Range-bound, slightly bullish/bearish, expecting the index to stall at a specific resistance or support.
> **Core Mechanics:** You buy 1 option and sell 2 (or more) options at a further strike.

- **Basic definition:** Buy options at one strike and sell a larger number of options at another strike, usually same expiry. Example: buy 1 option and sell 2 options.
- **Market view:** Directional or range view depending on construction, but extra short option can create large risk.
- **Basic example:** 
  - Assume Nifty 50 is trading at `24,000`. You expect Nifty to rise moderately and stall near 24,300 by expiry. You execute a 1:2 Call Ratio Spread:
  - **Leg 1 (Long/Buy):** Buy 1 Nifty 24,000 Call (At-The-Money / Near-ITM) at a cost of ₹150.
  - **Leg 2 (Short/Sell):** Sell 2 Nifty 24,300 Calls (Out-of-The-Money / OTM) at ₹70 each (Total premium received = ₹140).Net Cash Flow: Net debit of ₹10 (₹140 received - ₹150 paid).
------------------------------------------------------------------------------------------------------------

Buy 1 `22,000 CE`, sell 2 `22,300 CE`. If NIFTY rises moderately toward `22,300`, it can profit; if it rises far above `22,300`, the extra short call can create large loss.
- **Risk and reward:** Risk can become large because of the uncovered extra short option.
- **Indian market note:** Margin requirement and gap risk are serious. Beginners should learn it on paper only.
- **From where to learn:** Zerodha Varsity Module 6 ratio/backspread chapters, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6 for ratio/backspread mechanics; SEBI/NISM for risk warning.

##### 5.5 Backspread Call / Put || option buyer || SKIPPED 

- **Basic definition:** A ratio strategy where you sell fewer options and buy more options, often designed to benefit from a large move.
- **Market view:** Call backspread is bullish with large upside move expectation. Put backspread is bearish with large downside move expectation.
- **Basic example call backspread:** Sell 1 `22,000 CE`, buy 2 `22,300 CE`. If NIFTY rises sharply above the higher strike, the extra long call can profit. If it stays near `22,300`, loss can occur.
- **Basic example put backspread:** Sell 1 `22,000 PE`, buy 2 `21,700 PE`. If NIFTY falls sharply below lower strike, extra long put can profit.
- **Risk and reward:** Can have limited or defined risk depending on premiums and strikes, but has a danger zone around the long strike.
- **Indian market note:** Zerodha Varsity covers call ratio back spread and put ratio back spread with Indian examples. Check margin and liquidity for all legs.
- **From where to learn:** Zerodha Varsity Module 6 chapters on Call Ratio Back Spread and Put Ratio Back Spread.
- **Best source:** Zerodha Varsity Module 6.

##### 5.6 Butterfly Spread || option buyers || SKIPPED 

- **Basic definition:** A three-strike strategy with limited risk and limited reward, built using calls or puts. Common form: buy 1 lower strike, sell 2 middle strike, buy 1 higher strike.
- **Market view:** Expect price to expire near the middle strike.
- **Basic example:** Buy `21,800 CE`, sell 2 `22,000 CE`, buy `22,200 CE`. If net debit is `60`, max profit near middle strike is about `140`, max loss `60`.
- **Risk and reward:** Limited loss and limited profit; maximum profit around middle strike.
- **Indian market note:** Best learned on liquid index options because it needs clean execution across multiple strikes.
- **From where to learn:** NSE Academy options strategies, NISM, broker payoff tools.
- **Best source:** NSE Academy for payoff framework.

##### 5.7 Box Spread / Conversion-Reversal Arbitrage || institutional portfolio managers

- **Basic definition:** A box spread combines a bull call spread and bear put spread with same strikes and expiry. Conversion/reversal uses options plus stock/futures to exploit put-call parity mispricing.
- **Market view:** Arbitrage or financing strategy, not a normal directional trade.
- **Basic example box:** Buy `22,000 CE`, sell `22,300 CE`, buy `22,300 PE`, sell `22,000 PE`. The expiry payoff is designed to be close to the strike difference `300`, so entry price decides theoretical return.
- **Basic example conversion:** Long stock/futures plus long put plus short call can create a synthetic fixed payoff when pricing is favorable.
- **Risk and reward:** Theoretical arbitrage can disappear after brokerage, STT, taxes, bid-ask spread, margin, execution delay, and settlement differences.
- **Indian market note:** In NSE/BSE retail trading, these are usually advanced/institutional concepts. Do not assume risk-free profit. Indian taxes, STT, physical settlement, and execution costs can change the result.
- **From where to learn:** Zerodha Varsity Module 6 synthetic long/arbitrage chapter, NSE Academy options strategies, NISM derivatives curriculum.
- **Best source:** NISM/NSE for Indian market mechanics; Zerodha Varsity for put-call parity intuition.

#### 6. Income / theta strategies

##### 6.1 Covered Call || (on shares holdings) || 1.7 Covered Call || 

- **Basic definition:** Own shares and sell a `CE` to collect premium.
- **Basic example:** Hold stock at `1,000`, sell `1,050 CE` at `20`; premium gives income, but upside is capped and stock downside remains.
- **Indian market note:** Use only with deliverable stock quantity matching option lots and with physical settlement understanding.
- **From where to learn:** NISM Equity Derivatives, NSE settlement mechanism, Zerodha Varsity call basics.
- **Best source:** NISM/NSE for physical settlement.

##### 6.2 Cash-Secured Put on physically settled stock options || Cash-Settled Vs stock-Settled  

- **Basic definition:** Sell a `PE` only when you keep enough cash to take delivery of the stock if assigned/settled.
- **Market view:** You are willing to buy the stock at an effective lower price.
- **Basic example:** Stock = `1,000`. Sell `950 PE` at `20`. If stock stays above `950`, you keep premium. If stock expires below `950`, you may need to take delivery effectively near `950 - 20 = 930` before charges.
- **Risk and reward:** Profit limited to premium. Downside is similar to owning stock from the effective purchase price if stock falls sharply.
- **Indian market note:** This is specifically important because Indian stock options are physically settled. Cash must be truly available for delivery, not just margin.
- **From where to learn:** NSE settlement mechanism, NSE contract specs, NISM Equity Derivatives, SEBI investor risk material.
- **Best source:** NSE/NISM for Indian physical settlement and risk.

##### 6.3 Credit Spreads || option seller || 1.5 Bull Put Spread

> ▶ **Live practice:** the credit spread is the workhorse of a moderate-risk book — it is what [§8.5.2](#852-step-2--the-grid) returns for most directional cells. Size it from the **stop**, not the margin ([§8.11](#811-position-sizing--two-caps-take-the-smaller)); stop at **2× the entry credit** on the *structure*, never leg-by-leg ([§8.10](#810-stop-loss-architecture--four-types-and-which-to-use)); and when a genuine trend runs through it, **convert to a ladder** rather than roll ([§8.6.13](#8613-the-ladder--a-repair-never-an-entry)).

> **Target Trader:** The net seller of options who wants the high statistical win rate of selling but needs protection against unlimited risk.
> **Core Action:** You sell one option (collecting a higher premium) and simultaneously buy another option (paying a lower premium). This results in a net cash inflow (credit) into your account.

- **Basic definition:** Defined-risk option spreads entered for net credit, such as bull put spread or bear call spread.
- **Market view:** Expect the underlying to stay away from the sold strike.
- **Basic example:** 
  - Assume the Nifty 50 index is trading flat at `24,000`. A trader using a **Bull Put Spread** (a bullish credit spread) utilizes both ITM/ATM and OTM strikes:
    - **Sell (Short) Leg (Higher/Near Strike):** Sell a `24,000` Put (At-The-Money / near-the-money) and collect a premium of ₹150.Buy (Long) Leg (Lower/Far Strike): 
    - **Buy** a `23,800` Put (Out-of-The-Money protection) by paying a premium of ₹60.
    - **Net Credit Received:** ₹150 (sold) - ₹60 (bought) = ₹90 per share ( Net credit inflow).

Sell `21,900 PE` at `90`, buy `21,700 PE` at `40`. Net credit `50`; max loss `150`; max profit `50`.
- **Risk and reward:** Profit limited to credit. Loss limited by hedge option but can be larger than profit.
- **Indian market note:** Requires margin. Credit received is not guaranteed profit.
- **From where to learn:** Zerodha Varsity Module 6 bull put/bear call spread chapters, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6 plus broker margin calculator.

##### 6.4 Short Straddle || [3.3 Short Straddle](#33-short-straddle)

- **Basic definition:** Sell ATM `CE` and ATM `PE`.
- **Basic example:** Sell `22,000 CE` at `150` and `22,000 PE` at `140`; total credit `290`.
- **Indian market note:** Income strategy label does not reduce risk. It can lose heavily in trending/gap markets.
- **From where to learn:** Zerodha Varsity Module 6 Short Straddle, SEBI/NISM risk material.
- **Best source:** Zerodha Varsity for payoff; SEBI/NISM for risk.

##### 6.5 Short Strangle || [3.4 Short Strangle](#34-short-strangle)

- **Basic definition:** Sell OTM `CE` and OTM `PE`.
- **Basic example:** Sell `22,300 CE` at `60` and `21,700 PE` at `55`; total credit `115`.
- **Indian market note:** Often used by experienced option sellers, but gap risk and margin expansion are real.
- **From where to learn:** Zerodha Varsity Module 6 Long and Short Strangle, NSE Academy.
- **Best source:** Zerodha Varsity Module 6.

##### 6.6 Iron Condor || [4.1 Iron Condor](#41-iron-condor)

- **Basic definition:** Sell OTM call spread and OTM put spread together to collect credit with defined risk.
- **Basic example:** Buy `21,600 PE`, sell `21,800 PE`, sell `22,200 CE`, buy `22,400 CE`; if credit `80`, max loss `120` for `200`-point wings.
- **Indian market note:** Defined risk does not mean no risk. Adjustments and exits can be costly in fast markets.
- **From where to learn:** Zerodha Varsity Module 6 Iron Condor, NSE Academy.
- **Best source:** Zerodha Varsity Module 6.

##### 6.7 Iron Butterfly || [4.2 Iron Butterfly](#42-iron-butterfly)

- **Basic definition:** Sell ATM straddle and buy OTM wings to cap risk.
- **Basic example:** Sell `22,000 CE`, sell `22,000 PE`, buy `22,200 CE`, buy `21,800 PE`; if credit `130`, max loss `70` for `200`-point wings.
- **Indian market note:** Narrow range strategy. Watch expiry-day movement, slippage, and margin.
- **From where to learn:** NSE Academy options strategies, NISM, broker payoff tools.
- **Best source:** NSE Academy plus live broker payoff/margin tool.

#### 7. High-risk strategies: learn, but avoid as beginner

##### 7.1 Naked Short Call || AVOID ||

- **Basic definition:** Sell a `CE` without owning the underlying or buying a protective higher strike `CE`.
- **Market view:** Bearish or neutral, but risk is very high if market rises.
- **Basic example:** Sell `22,000 CE` at `150`. If expiry is `22,800`, intrinsic value is `800`, net loss = `800 - 150 = 650` before charges.
- **Risk and reward:** Maximum profit is premium. Loss can be very large because upside can continue.
- **Indian market note:** Requires margin and can face large mark-to-market losses. For stock options, physical settlement can create delivery obligation.
- **From where to learn:** SEBI investor derivatives risk material, NISM Equity Derivatives, Zerodha Varsity call writing payoff basics.
- **Best source:** SEBI/NISM for risk awareness.

##### 7.2 Naked Short Put || AVOID ||

- **Basic definition:** Sell a `PE` without holding cash/hedge sufficient for the downside.
- **Market view:** Bullish or neutral, but risk is high if market falls sharply.
- **Basic example:** Sell `22,000 PE` at `140`. If expiry is `21,200`, intrinsic value is `800`, net loss = `800 - 140 = 660` before charges.
- **Risk and reward:** Maximum profit is premium. Loss can be large if underlying falls strongly.
- **Indian market note:** For stock options, this can lead to physical delivery/cash requirement at expiry. Cash-secured put is safer than naked short put but still risky.
- **From where to learn:** SEBI investor derivatives risk material, NISM Equity Derivatives, NSE settlement mechanism.
- **Best source:** SEBI/NISM plus NSE settlement rules.

##### 7.3 Short Straddle || [3.3 Short Straddle](#33-short-straddle)

- **Basic definition:** Sell ATM `CE` and ATM `PE` at same strike and expiry.
- **Market view:** Very strong view that market will stay near the strike and volatility will fall.
- **Basic example:** Sell `22,000 CE` at `150`, sell `22,000 PE` at `140`; credit `290`; losses start beyond `22,290` or below `21,710`.
- **Risk and reward:** Premium is limited. Loss is very large on both sides.
- **Indian market note:** Avoid as beginner. One large gap move can erase many small premium gains.
- **From where to learn:** Zerodha Varsity Module 6, SEBI/NISM risk material.
- **Best source:** Zerodha Varsity for payoff; SEBI for risk awareness.

##### 7.4 Short Strangle || [3.4 Short Strangle](#34-short-strangle)

- **Basic definition:** Sell OTM `CE` and OTM `PE` of same expiry.
- **Market view:** Market stays inside a wide range.
- **Basic example:** Sell `22,300 CE` at `60`, sell `21,700 PE` at `55`; credit `115`; losses expand beyond outer break-evens.
- **Risk and reward:** Limited profit and very large loss potential.
- **Indian market note:** Avoid as beginner unless converted into defined-risk iron condor with proper hedges.
- **From where to learn:** Zerodha Varsity Module 6, NSE Academy, SEBI/NISM.
- **Best source:** Zerodha Varsity for payoff; NISM for risk.

##### 7.5 Ratio Spread with extra short option || 5.4 Ratio Spread

- **Basic definition:** A ratio spread where the number of sold options is greater than bought options, leaving uncovered short exposure.
- **Market view:** Moderate move or range view, but dangerous if the underlying moves too far.
- **Basic example:** Buy 1 `22,000 CE`, sell 2 `22,300 CE`. If NIFTY rallies sharply to `23,000`, the extra short `CE` causes increasing loss.
- **Risk and reward:** Can have attractive entry credit/debit but tail risk can be large.
- **Indian market note:** Margin can rise sharply during volatile moves. Avoid live trading until fully comfortable with payoff and stress scenarios.
- **From where to learn:** Zerodha Varsity Module 6 ratio/backspread chapters, NSE Academy options strategies.
- **Best source:** Zerodha Varsity Module 6 plus SEBI/NISM risk material.

##### 7.6 Stock option positions held to expiry without delivery planning || Stocks only (not index NIFTY50, BANKNIFTY)

- **Basic definition:** Holding ITM stock options or short stock option positions into expiry without understanding physical settlement and delivery obligation.
- **Market view:** This is not a strategy; it is an operational and risk-management mistake.
- **Basic example:** You are short an ITM stock `CE` at expiry and do not hold the shares. Physical settlement may require delivery obligation, and failure can create auction/penalty risk depending on clearing rules and broker process.
- **Risk and reward:** Risk can be larger than the visible option premium because delivery value, margin, auction, and settlement obligations matter.
- **Indian market note:** NSE states options on individual securities are European style and physically settled. Always square off or prepare delivery/cash before expiry according to broker deadlines.
- **From where to learn:** NSE Clearing settlement mechanism, NSE contract specifications, NISM Equity Derivatives.
- **Best source:** NSE Clearing settlement mechanism and broker physical settlement policy.


## 6. Best references to learn (Books/Blogs/Videos/Websites/Courses)

### ChatGPT Prompt and Answer

- **Question:** What are the best books one can read to learn options trading in the stock market, especially for the Indian stock market (NSE and BSE)?
- **Answer:**

#### Beginner Level

1. **Options Made Easy** by Guy Cohen
   - **Why read it:** Excellent for beginners, with clear explanations of options basics and strategies.
   - **Focus:** Simplifies complex concepts like Greeks and volatility.
2. **The Options Playbook** by Brian Overby
   - **Why read it:** Ideal for beginners looking to understand strategies visually.
   - **Focus:** Includes over 40 option strategies explained in plain language.
3. **Options Trading: The Basics Explained in Simple Terms** by ClydeBank Finance
   - **Why read it:** A concise guide for those starting out.
   - **Focus:** Basics of calls, puts, and basic strategies.
4. **YouTube:** Best Book for Options Trading in India | Beginner to Advanced | Divyam Parashar | Upmarket Academy
   1. *Trading Options Greeks: How Time, Volatility, and Other Pricing Factors Drive Profits* (Bloomberg Financial)
   2. *Time Is Money* by Kerry W. Given

#### Intermediate Level

1. **Option Volatility and Pricing** by Sheldon Natenberg
   - **Why read it:** Industry-standard book to understand volatility and pricing.
   - **Focus:** Option pricing models and the role of volatility.
2. **Trading Options Greeks** by Dan Passarelli
   - **Why read it:** Provides a deeper dive into the Greeks and how they impact options pricing and strategy.
   - **Focus:** Advanced risk management and strategy adjustments.
3. **The Bible of Options Strategies** by Guy Cohen
   - **Why read it:** Comprehensive reference guide for strategies.
   - **Focus:** Detailed examples of both basic and advanced strategies.
4. **YouTube:** Best Book for Options Trading in India | Beginner to Advanced | Divyam Parashar | Upmarket Academy
   1. *The Option Trader's Hedge Fund* by Dennis A. Chen and Mark Sebastian
   2. *Option Volatility & Pricing* by Sheldon Natenberg
   3. *The Option Trader Handbook* by George M.
5. **YouTube:** Top 3 Option Trading Books #optionstrading #stockmarket
   1. *Options, Futures, and Other Derivatives*
   2. *Dynamic Hedging*

#### Advanced Level

1. **Options as a Strategic Investment** by Lawrence G. McMillan
   - **Why read it:** Comprehensive and detailed; a classic in the field.
   - **Focus:** In-depth strategies and portfolio management techniques.
2. **Volatility Trading** by Euan Sinclair
   - **Why read it:** Focused on using volatility as an asset for trading.
   - **Focus:** Advanced topics like volatility surfaces and skew.
3. **Dynamic Hedging** by Nassim Nicholas Taleb
   - **Why read it:** Essential for understanding risk management in derivatives.
   - **Focus:** Explains complex hedging and trading strategies.

#### India-Specific Options Trading

1. **Derivatives Market in India** by Prof. Rajesh Kumar
   - **Why read it:** Focuses on the Indian derivatives market, including options.
   - **Focus:** Regulatory environment, NSE and BSE, and local nuances.
2. **How to Make Money in Derivatives: An Insider's Guide** by Ashwani Gujral
   - **Why read it:** Practical guide by a seasoned Indian market expert.
   - **Focus:** Application of options in Indian markets with examples.
3. **Options Simplified** by Ankit Gala and Jitendra Gala
   - **Why read it:** Written with Indian markets in mind.
   - **Focus:** Simplifies the jargon for Indian traders.

#### Youtbe video 
1.  Option Trading DEADLY books! || `https://www.youtube.com/watch?v=xeL1zCnF074`

## 7. AI usage on treading.

### 7.1 Scope: only Indian markets

- Keep this setup restricted to **Indian BSE and NSE only**.
- Primary instruments for options:
  - `NSE` index options: `NIFTY`, `BANKNIFTY`, `FINNIFTY`, `MIDCPNIFTY`.
  - `NSE` stock options where liquidity is good.
  - `BSE` index options like `SENSEX` and `BANKEX`, if supported by the broker/platform.
- Avoid foreign exchanges, crypto, CFDs, forex and unregulated signal providers for this workflow.
- Treat AI as a **copilot / decision-support assistant**, not as a fully automated trader.
- Final decision must stay manual:
  - AI can read data, summarize chart/option-chain context, and prepare a trade plan.
  - Human must approve `BUY`, `SELL`, `MODIFY`, `CANCEL`, and `EXIT`.

### 7.2 Important regulation and safety notes

- Official SEBI circular: `Safer participation of retail investors in Algorithmic trading`, circular no. `SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/0000013`, dated `04-Feb-2025`.
  - Link: `https://www.sebi.gov.in/legal/circulars/feb-2025/safer-participation-of-retail-investors-in-algorithmic-trading_91614.html`
- NSE has a page for `Empanelled Algo Providers of the Exchange`.
  - Link: `https://www.nseindia.com/static/trade/empanelled-algo-providers-exchange`
- NSE trading protocol FAQ says exchange-level direct protocol/API connectivity is mainly for members/vendors/trading systems, not normal retail users directly.
  - Link: `https://www.nseindia.com/static/trade/trading-protocols-faqs`
- For a retail trader, the practical route is:
  - Use a **SEBI-registered broker**.
  - Use the broker's official API.
  - Follow broker-specific API, static IP, rate limit, authentication and algo/non-algo rules.
- ICICI Direct's API FAQ explains important retail API changes:
  - Static IP mandatory from `01-Apr-2026`.
  - Existing API keys may need regeneration.
  - Strategy sending `10 or fewer orders/sec` may be treated differently from higher-frequency algo use, subject to broker/exchange rules.
  - Link: `https://www.icicidirect.com/faqs/fno/what-are-the-changes-mentioned-in-the-sebi-circular-on-api-trading`
- Do not share broker login, API key, API secret, TOTP seed, access token or OTP with Claude/OpenAI/ChatGPT or any third-party chat window.
- Store secrets only in local environment variables, a `local secrets manager`, or broker-approved secure backend.
- Always use hard risk limits:
  - Daily max loss.
  - Per-trade max loss.
  - Max open positions.
  - Max option premium exposure.
  - No fresh trades after a defined time.
  - Mandatory stop-loss and exit plan before entry.

### 7.3 Best ready-made tools for option trading guidance

| Tool | Best use | Useful features | Broker/execution notes |
| --- | --- | --- | --- |
| **Sensibull** | Beginner to advanced option strategy planning | Strategy builder, option chain, open interest, FII/DII data, IV chart, live options charts, practice/draft portfolio, payoff analysis | Login available with brokers like Zerodha, Angel One, Upstox, ICICI Direct. Official site says it is `SEBI Registered RA INH200006895`. Link: `https://sensibull.com/` |
| **Dhan Options Trader** | Broker-native option execution and analysis | Custom strategy builder, option chain, strategy charts, straddle tools, real-time payoff graphs | Good if using Dhan as broker. Link: `https://dhan.co/options-trader-web/` |
| **DhanHQ** | API + algo + managed algo marketplace | Free trading APIs, live prices, historical data, option chain, 20-depth market data, sandbox, low-latency claims | Good for Python/API based copilot. Link: `https://dhanhq.co/` |
| **Quantsapp** | Data-heavy options analytics | Strategy builder, Greek charts, OI, IV, PCR, Max Pain, backtesting, optimizer, order/trade analytics | Good for option-chain and Greek-based decision support. Link: `https://www.quantsapp.com/` |
| **TradingView India** | Chart reading and technical analysis | Advanced charts, indicators, alerts, Pine Script, NSE/BSE charts, community scripts | Can be used for analysis. Direct Indian broker execution is especially known through Dhan integration. Link: `https://in.tradingview.com/` |
| **Streak** | No-code systematic strategy testing | Scanners, technical strategies, backtesting, paper trading, deployment through supported brokers | Useful before coding your own Python logic. Verify current broker support. Link: `https://www.streak.tech/` |
| **Opstra / Definedge** | Advanced option analytics | IV, OI, Greeks, strategy simulation, volatility tools | Useful for serious options study and strategy testing. Link: `https://opstra.definedge.com/` |

### 7.4 Brokers and APIs that can connect Python/live data/order placement

| Broker/API | Good for | Live data | Order placement | Python support | Notes |
| --- | --- | --- | --- | --- | --- |
| **Zerodha Kite Connect** | Mature Indian broker API ecosystem | WebSocket live market ticks in paid Connect plan | Yes | Official SDKs include Python | Free personal tier covers order/GTT/alerts/portfolio. Full API with real-time WebSocket and historical candle data is listed at `₹500/month`. Links: `https://zerodha.com/products/api/`, `https://kite.trade/docs/connect/v3/` |
| **Upstox API** | Free API access with high rate limits | WebSocket market data, OHLC/quotes; option-chain Greeks mentioned as coming/roadmap on API page | Yes | SDKs include Python | Official page mentions free trading + market data APIs, order APIs, portfolio APIs and low-latency claims. Link: `https://upstox.com/trading-api/` |
| **DhanHQ API** | Strong API-first setup for traders | Live prices, historical data, option chain, 20 market depth | Yes | API/SDK ecosystem | Official page mentions free trading APIs, sandbox and low-latency infrastructure. Link: `https://dhanhq.co/` |
| **Groww API** | Simple API + Python SDK for Groww users | LTP, quote, OHLC, historical data, WebSocket feed | Yes, including stocks and F&O | Official Python SDK `growwapi` | Official page says API supports stocks and F&O on both BSE and NSE. Pricing shown as `₹499/month + taxes` at time of writing. Links: `https://groww.in/trade-api`, `https://groww.in/trade-api/docs/python-sdk` |
| **Angel One SmartAPI** | Free API access for Angel One users | Real-time market data | Yes | Python, Node.js, Java, R, PHP, C#, Go | Official page says free APIs, live market feed and trade execution. Link: `https://smartapi.angelone.in/` |
| **Kotak Neo Trade API** | Kotak broker users, bank-linked ecosystem | Real-time market data | Yes, equity and F&O | Python SDK mentioned | Official guide mentions order placement, market data, margin validation and zero brokerage for API orders; verify pricing in account before use. Link: `https://www.kotakneo.com/investing-guide/trading-account/kotak-neo-trade-api-guide/` |
| **FYERS API** | Chart/trader friendly broker API | Real-time data API, historical data API | Yes | API docs and SDK support | Official page says API is free, up to `1 lakh` requests/day and order placement under `<75ms`. Link: `https://fyers.in/products/api/` |
| **ICICI Direct Breeze API** | ICICI Direct users | Live streaming prices, option chain, OHLC | Yes | SDK/API docs available | Useful if already using ICICI Direct. Important static IP/API regulation FAQs are available. Link: `https://www.icicidirect.com/faqs/fno/what-are-the-changes-mentioned-in-the-sebi-circular-on-api-trading` |

### 7.5 Can Claude/OpenAI be connected to broker account and live market feed?

- Yes, technically it is possible, but do it through a **controlled Python backend**, not by directly giving broker credentials to an AI chat app.
- Recommended safe architecture:

```text
Broker API/WebSocket
        |
        v
Python market-data collector
        |
        v
Indicators + option-chain analytics + risk engine
        |
        v
Claude/OpenAI summarizer
        |
        v
Local dashboard / Telegram / Slack / web app alert
        |
        v
Human approves or rejects trade
        |
        v
Broker order API executes only after manual approval
```

- The AI should receive only limited, sanitized market context:
  - Current index/stock price.
  - Trend, support, resistance.
  - Volume and VWAP context.
  - Option chain snapshot.
  - OI change, PCR, IV, IV percentile, Max Pain if available.
  - Greeks for candidate strikes.
  - Your existing position and predefined risk rules.
- The AI should not receive:
  - API secret.
  - Access token.
  - TOTP secret.
  - Password.
  - OTP.
  - Full account login session.
- The Python risk engine should be able to block bad suggestions before they reach execution:
  - No trade if daily loss limit is hit.
  - No naked option selling unless explicitly allowed and margin/risk is checked.
  - No illiquid strikes.
  - No market orders in fast markets unless explicitly approved.
  - No trade close to expiry unless strategy allows it.
  - No trade without stop-loss and exit condition.

### 7.6 What the AI copilot should guide live

- Market direction:
  - Is the underlying trending, ranging, or highly volatile?
  - Is price above/below VWAP?
  - Are higher-highs/higher-lows or lower-highs/lower-lows forming?
- Key levels:
  - Previous day high/low.
  - Opening range high/low.
  - Intraday support/resistance.
  - Round numbers like `NIFTY 24000`.
- Option-chain reading:
  - Highest Call OI and Put OI.
  - Change in OI.
  - PCR direction.
  - IV expansion/contraction.
  - ATM straddle premium movement.
  - Whether premium is expensive or cheap versus recent range.
- Strategy suggestion, not blind signal:
  - If bullish: compare long call, bull call spread, short put spread.
  - If bearish: compare long put, bear put spread, short call spread.
  - If range-bound: compare iron condor, short strangle, short straddle only if risk/margin is understood.
  - If event/high IV: prefer defined-risk spreads over naked option buying/selling.
- Trade plan format:
  - `Bias`: bullish / bearish / range-bound / no-trade.
  - `Reason`: chart + option-chain reason.
  - `Instrument`: exact symbol/expiry/strike.
  - `Entry zone`: price range, not a single random number.
  - `Stop-loss`: invalidation level.
  - `Target`: partial/full exit.
  - `Risk`: rupee risk and max premium/margin.
  - `Confidence`: low / medium / high.
  - `Do not trade if`: clear conditions.

### 7.7 Python implementation plan for personal copilot

1. Start with read-only mode.
   - Connect to broker market-data API.
   - Pull option chain, quotes and candles.
   - Do not enable order placement yet.
2. Build analytics.
   - Indicators: VWAP, EMA, RSI, ATR, volume, previous day levels.
   - Options: OI, OI change, IV, Greeks, PCR, ATM straddle premium.
3. Add AI explanation.
   - Send only calculated summaries to Claude/OpenAI.
   - Ask AI for structured output: `bias`, `reason`, `candidate trade`, `risk`, `avoid conditions`.
4. Add a manual approval screen.
   - Button 1: `Approve`.
   - Button 2: `Reject`.
   - Button 3: `Modify quantity/price`.
   - Button 4: `Paper trade only`.
5. Add broker execution only after manual approval.
   - Use limit orders by default.
   - Log every decision and order request.
   - Keep an emergency kill switch.
6. Run paper trading for at least a few weeks.
   - Compare AI suggestions with actual market outcomes.
   - Measure win rate, average profit/loss, max drawdown, slippage and missed exits.
7. Move to tiny live size.
   - Use 1 lot only.
   - Stop immediately if rules are violated.

### 7.8 Good first practical setup

- Best no-code / low-code start:
  - Use `Sensibull` or `Dhan Options Trader` for option-chain + payoff + strategy builder.
  - Use `TradingView` for charts and alerts.
  - Use broker app for final execution.
- Best Python/API start:
  - Pick one broker API: `Zerodha Kite Connect`, `DhanHQ`, `Upstox`, `Groww`, `Angel One SmartAPI`, `Kotak Neo`, `FYERS`, or `ICICI Breeze`.
  - Start with only market data and paper signals.
  - Add Claude/OpenAI only for explanation and scenario comparison.
  - Add order placement only after manual approval workflow is stable.
- Best safety rule:
  - AI should answer: **"Should I consider this trade?"**
  - AI should not decide: **"Place this trade now without me."**

### 7.9 Prompt template for live option copilot

```text
You are my NSE/BSE options trading copilot.
Do not place trades. Do not give guaranteed predictions.
Use only the data below.

Market:
- Underlying:
- Current price:
- Time:
- Trend:
- VWAP:
- Support:
- Resistance:
- ATR:
- Volume context:

Option chain:
- Expiry:
- ATM strike:
- Highest Call OI:
- Highest Put OI:
- PCR:
- IV:
- IV change:
- ATM straddle premium:
- Candidate strikes with Greeks:

My risk rules:
- Max loss per trade:
- Max loss per day:
- Max lots:
- Allowed strategies:
- Disallowed strategies:

Existing position:
- None / details:

Return:
1. Bias: bullish / bearish / range-bound / no-trade
2. Reason in 5 bullet points
3. Best candidate strategy
4. Entry zone
5. Stop-loss / invalidation
6. Target / exit plan
7. Main risk
8. Conditions where I should avoid this trade
9. Confidence: low / medium / high
```

### 7.10 Final recommendation

- For learning and manual trading: start with **Sensibull + TradingView + broker app**.
- For broker-integrated option workflow: consider **Dhan Options Trader** or **Sensibull with supported broker login**.
- For Python AI copilot: start with **Zerodha Kite Connect**, **DhanHQ**, **Upstox**, **Groww**, **Angel One SmartAPI**, **Kotak Neo**, **FYERS**, or **ICICI Breeze**, depending on which broker account you actually use.
- Build in this order:
  1. Live data dashboard.
  2. Paper trade signals.
  3. AI explanation.
  4. Manual approval.
  5. Small live order execution.
- Never start with full automation. First build trust through logs, paper trading and small-size validation.

---

# 8. The Real-World Option Seller's Book — NIFTY 50 / BANKNIFTY / SENSEX (2026 regime)

> **What this section is.** Sections 1–7 above are the *textbook*: payoff shapes, definitions, break-even formulas. This section is the *operating manual* — how premium selling is actually run for money on NSE/BSE after the 2024–2026 rule changes, what the edge really is, how big it is, and the specific structures, timings, adjustments and kill-switches that separate a seller who compounds from one who gives back a year in one afternoon.
>
> **What this section is not.** It is not a signal service, not a guaranteed-return system, and not a replacement for the Pre-Trade Go/No-Go checklist in [`option_chain_n_greeks.md` §7](../option_chain_n_greeks.md#7-pre-trade-gono-go-checklist--session-learnings). Every structure below still requires a five-view classification, a defined maximum loss, a mandatory stop-loss, a per-trade rupee cap and a daily rupee cap **before entry**.
>
> **Capital anchor.** ⚠️ **Superseded — see [`TRADING_CONSTANTS.md`](../../TRADING_CONSTANTS.md).** Worked examples below were sized to *~₹6,00,000 deployed per session, ~1% net session target*. **Both figures are now wrong.** The book is **₹7,02,275**, the margin cap is **40%** (~₹2.8L, and margin is not a sizing input), and the **1%-per-session target is deleted** — it annualises to ~250% and, under a ₹3,500 planned-stop cap, requires capturing 200% of the credit. The live target is **2–4% per month**. Treat every worked example here as illustrating *method*, not size. The `pro_option_seller_playbook.md` is sized to a ₹20L dedicated book. Where the two disagree on contract specs or charges, [§8.0.3](#803-reconciliation--which-numbers-in-this-repo-supersede-which) is authoritative.

---

## Index — Section 8

| # | Chapter | What it answers |
|---|---------|-----------------|
| [8.0](#80-scope-non-duplication-map-and-reconciliation) | Scope, non-duplication map, reconciliation | Where each topic lives; which numbers supersede |
| [8.1](#81-where-the-money-actually-comes-from--the-volatility-risk-premium) | Where the money actually comes from | VRP, how big the edge is, why 9 of 10 still lose |
| [8.2](#82-the-20242026-rule-changes-that-decided-which-strategies-still-work) | The 2024–2026 rule changes | What SEBI killed, what it created |
| [8.3](#83-the-real-cost-sheet--charges-slippage-and-the-friction-floor) | The real cost sheet | Charges vs slippage; the friction floor; ROM |
| [8.4](#84-instrument-selection--nifty-vs-banknifty-vs-sensex) | Instrument selection | Which index, which expiry, for which job |
| [8.5](#85-the-sellers-regime-grid--direction--volatility--dte) | **The seller's regime grid** | Direction × Volatility × DTE → which structure |
| [8.6](#86-the-structure-library--what-real-sellers-actually-put-on) | **The structure library** | 14 live structures, full mechanics + examples |
| [8.7](#87-strike-selection--the-four-methods-and-when-each-wins) | Strike selection | Delta band, expected move, straddle rule, OI zones |
| [8.8](#88-entry-timing--the-intraday-premium-and-iv-curve) | Entry timing | The intraday IV curve; the windows that pay |
| [8.9](#89-the-adjustment-playbook--decision-tree) | **The adjustment playbook** | Shift, roll, convert, hedge-up, cut — and when not to |
| [8.10](#810-stop-loss-architecture--four-types-and-which-to-use) | Stop-loss architecture | Leg SL vs combined-premium SL vs MTM vs level |
| [8.11](#811-position-sizing--two-caps-take-the-smaller) | **Position sizing** | The one formula that keeps you alive |
| [8.12](#812-the-pattern-library--recurring-setups-a-seller-trades) | The pattern library | 14 recurring weekly/intraday patterns |
| [8.13](#813-trend-day-detection--the-sellers-kill-switch) | Trend-day detection | The single most important survival skill |
| [8.14](#814-blow-up-autopsy--the-six-ways-sellers-die) | Blow-up autopsy | Six failure modes and the rule that stops each |
| [8.15](#815-metrics-that-actually-matter) | Metrics that matter | ROM, MAE, expectancy per ₹1L margin |
| [8.16](#816-quick-reference-cards) | Quick-reference cards | One card per market situation |
| [8.17](#817-sources-for-section-8) | Sources | Circulars, exchange pages, practitioner material |

---

## 8.0 Scope, non-duplication map, and reconciliation

### 8.0.1 Where each topic lives in this repository

| Topic | Canonical location | Do **not** re-derive elsewhere |
|-------|-------------------|-------------------------------|
| Payoff shapes, break-even formulas, textbook definitions | [§5.4](#54-point-wise-strategy-reference-for-nsebse-options) of this file | ✅ |
| Greeks maths, option-chain columns, Pre-Trade Go/No-Go | [`option_chain_n_greeks.md`](../option_chain_n_greeks.md) | ✅ |
| Five-view classification, FII/DII scenarios, 9 data points | [`Market_View.md`](../Market_View.md) | ✅ |
| CAS (Closing Auction Session) mechanics and expiry-day time stops | [`rules_n_regulations/rules_constrints.md`](../rules_n_regulations/rules_constrints.md) | ✅ |
| ₹20L capital plan, weekly two-index calendar, annual projections | [`pro_option_seller_playbook.md`](./pro_option_seller_playbook.md) | ✅ |
| **Live structures, adjustments, sizing, regime grid, patterns** | **§8 (here)** | ✅ |

### 8.0.2 What §8 deliberately adds that is nowhere else in the repo

1. The **regime grid** — a direction × volatility × DTE lookup that outputs a structure, not a strategy name.
2. Eight structures that appear in no other file: **Jade Lizard, Big Lizard, Reverse Jade Lizard, Broken-Wing Butterfly, Unbalanced Iron Condor, Double Calendar / Batman, Bear Call Ladder as a repair, Skew-Aware Condor.**
3. The **adjustment decision tree** — the part that decides whether a seller compounds or bleeds.
4. **Sizing from the stop, not the margin** — with the ₹6L worked numbers.
5. The **friction floor**: why slippage, not charges, is the real cost, and the minimum premium below which a leg is not worth selling.
6. The **2024–2026 regulatory regime** and exactly which strategies it invalidated.

### 8.0.3 Reconciliation — which numbers in this repo supersede which

Three files in this repo quote contract specs and charges. They disagree. Use this order:

| Item | Authoritative here | Superseded / stale | Action |
|------|-------------------|--------------------|--------|
| **Lot sizes** | `option_chain_n_greeks.md` §4 dated table — NIFTY `65`, BANKNIFTY `30`, SENSEX `20` (as of 4-Aug-2026) | `pro_option_seller_playbook.md` §3 — NIFTY `25`, SENSEX `10`, BANKNIFTY `15` | Playbook §3 table is stale. **Re-verify against the live NSE/BSE contract master before every trading week** — SEBI's ₹15L minimum contract-value rule means lot sizes are revised whenever the index re-rates. |
| **BANKNIFTY expiry** | `CLAUDE.md` + §8.2 — **monthly only** (weekly BANKNIFTY was withdrawn 20-Nov-2024) | `pro_option_seller_playbook.md` §3 — "Wednesday (weekly)" | Playbook row is stale. Do not plan a weekly BANKNIFTY income leg. |
| **Charges per round trip** | §8.3 of this file (itemised build-up) | `pro_option_seller_playbook.md` §4 — "~₹2,520 for 12 lots" | The playbook figure over-states charges by roughly **8×** (its STT line of ~₹900 should be ~₹70; STT is 0.1% of *sale premium*, not of notional). Conservative in direction, but it makes small-credit trades look unviable when they are not. **The real cost is slippage — see §8.3.2.** |
| **Per-lot margin figures** | None — compute live | `pro_option_seller_playbook.md` §3 margin table | Those rupee figures were derived at a different lot size and cannot be scaled linearly. Always price margin with a **basket margin call** before entry (`mcp__dhan__margin_agent_tool`, or the Zerodha SPAN calculator). See §8.3.3. |
| **Expiry-day time stops** | ⭐ [`TRADING_CONSTANTS.md` §7](../../TRADING_CONSTANTS.md) — nothing else | `rules_constrints.md` §1.10 · `pro_option_seller_playbook.md` §11 Rule 3 ("2:45 PM") · the two-tier scheme formerly quoted here | **HARD FLAT: NIFTY/BANKNIFTY 2:30 PM · SENSEX 2:15 PM. One time per index.** The two-tier "target / hard" scheme is **deleted** — a later fallback deadline is what a losing position reaches for (20-Jul-2026 exited ~3:16 PM). |

---

## 8.1 Where the money actually comes from — the Volatility Risk Premium

Everything below rests on one structural fact. If you cannot state it, you are not selling premium — you are selling lottery tickets and calling it income.

### 8.1.1 The edge in one equation

```text
Seller's structural edge  =  Implied Volatility (what you sold)
                           − Realised Volatility (what actually happened)
                           − Friction (charges + slippage)

This difference is the Volatility Risk Premium (VRP).
```

Buyers of index options systematically overpay because option premium contains an **insurance loading** — the market pays up for protection against gaps it cannot hedge. In Indian index options this loading is real and persistent, but it is **small in vol points and lumpy in time**:

| Measure | Typical NIFTY weekly range (verify with live IV/HV data) | What it means |
|---|---|---|
| Weekly ATM IV | ~10–14% annualised in a calm regime | What you are paid |
| Trailing 20-day realised (HV20) | ~9–11% annualised in the same regime | What you actually pay out |
| **VRP** | **~1.5–3 vol points** | Your gross edge before friction |
| Frequency IV > subsequent RV | Roughly 7 sessions in 10 in calm regimes | Why win rate looks high |
| Size of the 3-in-10 loss vs the 7-in-10 win | Loss can be 3–6× a typical win | Why win rate is a liar |

**The three consequences that decide everything else in §8:**

1. **The edge is thin.** A 2-vol-point edge on a weekly NIFTY straddle is worth roughly 8–15 index points of expected value. If your slippage across four legs is 4 points, you have just eaten a third of your edge on execution alone. → §8.3.
2. **The edge is negative when IV < RV.** Selling into a low-IV, high-realised-movement market (VIX 11 while NIFTY swings 0.9% a day) is selling insurance below cost. → §8.5.
3. **The payoff is asymmetric by construction.** Many small wins, occasional large losses. Survival is therefore an *engineering* problem (stop architecture + sizing), not a *forecasting* problem. → §8.10, §8.11.

### 8.1.2 The three P&L buckets — know which one is paying you

Every seller position resolves into three buckets. Attribute your P&L to them daily; if you cannot, you do not know whether you were right or lucky.

| Bucket | Sign for a seller | Pays you when | Kills you when |
|--------|------------------|---------------|----------------|
| **Theta** | + | Time passes and spot behaves | Never directly — but it seduces you into holding |
| **Vega** | − | IV falls (post-event crush, calm drift) | IV expands — gap, news, VIX spike |
| **Gamma** | − | Never. Gamma is pure cost | Spot moves fast, especially near your short strike near expiry |

> **The one-line truth:** *Theta is not income. Theta is the rent the market pays you for holding short Gamma and short Vega.* On a quiet day you collect the rent. On the day the tenant burns the house down, you find out what you were actually insuring.

### 8.1.3 Why 9 of 10 F&O traders lose even though the edge is real

SEBI's study found ~93% of individual equity F&O traders lost money over FY22–FY24. The edge above is real, so the losses are not caused by the edge being absent. They are caused by:

| Cause | Mechanism | Fixed by |
|-------|-----------|----------|
| Size | Position sized to available margin instead of to the stop | §8.11 |
| No hedge | Naked short legs → one gap erases a quarter | §8.6 (every structure here is hedged) |
| Averaging into a loser | "Rolling for credit" on a trending market = martingale | §8.9.6 |
| Holding through the tail | No mechanical exit; hoping theta rescues a Gamma problem | §8.10 |
| Friction | 6–10 legs a day at market price | §8.3.2 |
| Regime blindness | Selling a range structure into a trend day | §8.13 |

---

## 8.2 The 2024–2026 rule changes that decided which strategies still work

This is the single biggest reason old YouTube/blog strategies do not work any more. Six changes between Oct 2024 and Aug 2026 rewrote the seller's economics.

### 8.2.1 The change log

| # | Change | Effective (verify circular) | What it did to sellers |
|---|--------|------------------------|-------------------------|
| 1 | **STT on option *sale* raised 0.0625% → 0.1% of premium** (Finance (No.2) Act 2024) | 1-Oct-2024 | Raised the friction floor on high-turnover intraday selling by ~60% on the STT line. Matters for scalping straddles many times a day; negligible for one weekly structure. |
| 2 | **Weekly index expiries rationalised to one per exchange** (SEBI index-derivatives framework) | 20-Nov-2024 | **Killed the 5-day-a-week 0-DTE business.** FINNIFTY, MIDCPNIFTY and BANKNIFTY weeklies withdrawn. Only NIFTY (NSE) and SENSEX (BSE) have weeklies. BANKNIFTY is **monthly only**. |
| 3 | **Minimum index contract value raised to ₹15 lakh** | 20-Nov-2024 | Lot sizes jumped. Minimum viable risk per lot rose sharply — a small account can no longer diversify across four indices. Lot sizes are now revised whenever the index re-rates. |
| 4 | **Removal of calendar-spread margin benefit on expiry day** | 1-Feb-2025 | **Killed the expiry-day calendar / diagonal trade.** A near-expiry short leg + far-expiry long leg gets *no* offset on expiry day, so margin can multiply intraday. See §8.6.7. |
| 5 | **Upfront premium collection from option buyers** + **intraday position-limit monitoring** | 1-Feb-2025 / 1-Apr-2025 | Reduced intraday leverage across the market; slightly reduced the reflexive premium spikes that used to stop sellers out. |
| 6 | **Extra tail-risk margin (ELM add-on) on short index options on expiry day** | 20-Nov-2024 | **Margin on your short legs *increases* on expiry day.** A position that fits comfortably on Monday can trigger a margin shortfall on Tuesday morning without you doing anything. |
| 7 | **Expiry days standardised — NSE Tuesday, BSE Thursday** | 2025 | The weekly seller's calendar is now fixed: Tue = NIFTY, Thu = SENSEX. |
| 8 | **Closing Auction Session (CAS)** | 3-Aug-2026 | Adds an unhedgeable 3:15–3:30 PM window on expiry day. Inflates morning IV (good — more credit) but makes holding past 3:00 PM a coin flip. Full treatment: [`rules_constrints.md` §1](../rules_n_regulations/rules_constrints.md). |

### 8.2.2 What each change killed and created

```text
KILLED
├── Daily 0-DTE income across 5 indices        → only Tue (NIFTY) + Thu (SENSEX) remain
├── Weekly BANKNIFTY strangle income           → monthly only; treat as a positional instrument
├── Expiry-day calendar / diagonal spreads     → no margin offset; margin can blow out intraday
├── "Sell 2-rupee options, they always expire" → contract value ₹15L+ means the tail is now
│                                                 large enough to end an account in one move
└── Holding any expiring leg past 3:15 PM      → CAS: no tradable underlying, IEP-driven marks

CREATED
├── Higher morning IV on expiry day (CAS risk premium priced from 9:15 AM)
│     → more credit available early; exit before 2:30 PM and you never carry the auction risk
├── A cleaner two-event weekly calendar (Tue / Thu) — easier to plan, easier to journal
├── A real premium for the Wednesday/Friday "no near-expiry" gap
│     → the positional 25–40 DTE condor is now more attractive relative to weekly churn
└── Margin relief that strongly favours hedged structures over naked ones
      → a hedged fly/condor can produce a HIGHER return-on-margin than a naked strangle
```

> **Practical instruction:** re-read this table at the start of every quarter and check for new SEBI circulars. Every one of these changes invalidated a strategy that a large number of traders were still running six months later.

#### What the CAS exit actually costs — measured, 27-Aug-2026

The hard flats (NIFTY/BANKNIFTY 2:30 · SENSEX 2:15 — one time per index) are not free, and it is worth having a real
number for what they give up so the rule is not quietly relaxed on a bad day.

| SENSEX 30-min bar | Move |
|---|---|
| 11:00 → 14:30 (3½ hrs, post-entry) | net ≈ **−40 pts**, chopping in a ~230-pt band |
| **15:00 → 15:30** | **77,274 → 76,933.59 = −340 pts** |

**340 of the day's 539 points — 63% — arrived after 3:00 PM.** A seller obeying the 2:15 PM SENSEX
time stop captured roughly half of what a rule-breaker did.

> **The rule is still correct.** That 63% was a coin flip until it landed: the same window that paid
> a short-call position −340 points *down* would have destroyed it −340 points *up*, with no tradable
> underlying to hedge against and IEP-driven marks. **A favourable auction is not evidence the exit
> rule is too conservative.** Budget the give-up as a known cost of the CAS regime, and price
> structures so they pay at the time stop, not at settlement.

---

## 8.3 The real cost sheet — charges, slippage, and the friction floor

Most retail sellers budget for the wrong cost. Charges are small and predictable. **Slippage is large and is the thing that actually eats the VRP.**

### 8.3.1 Charges — itemised, with real arithmetic

Component rates (NSE index options; verify current rates with your broker — BSE differs slightly):

| Component | Rate | Charged on |
|-----------|------|-----------|
| STT | **0.10%** | **Sell-side premium turnover only** |
| Exchange transaction charge (NSE F&O options) | ~**0.03503%** | Premium turnover, both sides |
| SEBI turnover fee | ₹10 per crore (0.0001%) | Premium turnover |
| Stamp duty | 0.003% | Buy-side turnover only |
| Brokerage | ₹20 per executed order (discount broker) | Per leg, per direction |
| GST | 18% | On (brokerage + exchange charge + SEBI fee) |

**Worked example — NIFTY Iron Condor, 8 lots, round trip.** Lot `65` → quantity `520`.

```text
LEGS (entry)
  Sell 24,900 CE @ 45     Buy 25,200 CE @ 15
  Sell 24,100 PE @ 40     Buy 23,800 PE @ 13
  Net credit = (45+40) − (15+13) = 57 points  →  57 × 520 = ₹29,640

EXIT at 50% of credit (net structure value 28.5 pts)
  Cover shorts @ 45 total   Close longs @ 16.5 total

PREMIUM TURNOVER
  Entry  sell 85 × 520 = ₹44,200   |  Entry  buy 28   × 520 = ₹14,560
  Exit   buy  45 × 520 = ₹23,400   |  Exit   sell 16.5 × 520 = ₹8,580
  Total premium turnover = ₹90,740

CHARGES
  STT       0.10%    × (44,200 + 8,580) sell turnover      =  ₹52.78
  Exchange  0.03503% × 90,740                              =  ₹31.79
  SEBI      0.0001%  × 90,740                              =   ₹0.09
  Stamp     0.003%   × (14,560 + 23,400) buy turnover      =   ₹1.14
  Brokerage ₹20 × 8 executed orders                        = ₹160.00
  GST       18% × (160.00 + 31.79 + 0.09)                  =  ₹34.54
  ─────────────────────────────────────────────────────────────────
  TOTAL CHARGES                                            ≈ ₹280

GROSS at 50% exit = 28.5 × 520 = ₹14,820
NET of charges                  ≈ ₹14,540      →  charges = 1.9% of gross profit
```

**Read that number again: ₹280.** Brokerage (₹160) is the largest single line — *more than STT, exchange charges, SEBI fee and stamp duty combined.* This is why the ₹2,520 estimate in the playbook is misleading, and why leg-count discipline matters more than STT.

### 8.3.2 Slippage — the cost that is 5–10× larger than charges

Same trade, same 8 legs, but priced at market instead of at limit:

```text
Bid–ask on a liquid NIFTY weekly strike: 0.5 – 1.0 point
Realistic slippage crossing the spread: 0.5 point per leg

  8 legs × 0.5 point × 520 quantity = 4 points × 520 = ₹2,080

SLIPPAGE (₹2,080)  vs  CHARGES (₹280)   →  slippage is 7.4× the charges
Slippage as % of the ₹14,820 gross target: 14%
```

**The four rules that come out of this:**

| Rule | Why |
|------|-----|
| **1. Never use market orders on a multi-leg structure.** Use a basket / spread order, or limit orders at mid, legged in with the *buy* legs first. | Each market order pays half the spread. Eight of them is a fixed 14% tax on the trade. |
| **2. Minimise leg count for the same payoff.** A 4-leg condor costs twice the slippage of a 2-leg credit spread. | If a bear call spread expresses the view, do not put on a condor for the extra ₹800 of credit and ₹1,040 of extra slippage. |
| **3. Prefer strikes with a spread ≤ ~2% of premium.** | A strike quoting 3.0/3.6 has a 20% spread. You lose a fifth of the credit at entry and another fifth at exit. |
| **4. Adjustments are not free.** Each adjustment is 2–4 more legs. | Three adjustments on a NIFTY condor = ~₹3,000 of slippage — often more than the credit you were defending. See §8.9.7. |

### 8.3.3 The friction floor — the minimum premium worth selling

```text
FRICTION FLOOR RULE

Do not sell a leg unless:

  (a) Premium ≥ 8 × (bid–ask spread)                  ← execution viability
  (b) Premium ≥ 0.20% of spot for a weekly index leg  ← risk-compensation viability
      NIFTY @ 24,500  →  minimum leg premium ≈ 8–10 points
      SENSEX @ 81,000 →  minimum leg premium ≈ 20–25 points
  (c) The structure's total net credit ≥ 2 × expected round-trip slippage

WHY (b) EXISTS: a 2-point far-OTM option has almost no premium but the SAME
tail exposure as a 20-point option. You are selling the identical gap risk
for a tenth of the compensation. This is the single most common way small
accounts are destroyed — it feels safe because the strike is far away.
```

### 8.3.4 Return on Margin (ROM) — the only P&L denominator that matters

Rupee P&L is meaningless without the capital it locked up.

```text
ROM (per trade)   = Net P&L ÷ Peak margin blocked
ROM (annualised)  = ROM per trade × cycles per year

Realistic reference bands for hedged index premium selling in India:
  Weekly defined-risk structure, exited at 50%:  1.5% – 3.5% ROM per cycle
  Positional 25–40 DTE condor, exited at 50%:    3%   – 6%   ROM per cycle
  Anything advertising > 8% ROM per week          is either unhedged, mis-sized,
                                                  or being measured on winners only
```

> **Margin must be priced live, never assumed.** Margin = SPAN (scenario) + Exposure/ELM (charged on short notional, so it does *not* fall to max-loss even for a fully hedged structure) + expiry-day ELM add-on. Get it from `mcp__dhan__margin_agent_tool` (basket) or the Zerodha SPAN calculator **before** you place the first leg. Every rupee margin figure in this repository is illustrative.

---

## 8.4 Instrument selection — NIFTY vs BANKNIFTY vs SENSEX

Three tradable index option books, three different jobs. Choosing the wrong one for the job is a silent, permanent drag.

| | **NIFTY 50 (NSE)** | **SENSEX (BSE)** | **BANKNIFTY (NSE)** |
|---|---|---|---|
| Weekly expiry | ✅ Tuesday | ✅ Thursday | ❌ none |
| Monthly expiry | Last Tuesday | Last Thursday | Last Tuesday |
| Lot size (verify live) | 65 | 20 | 30 |
| Liquidity / depth | Deepest in India | Good near ATM, thins fast in the wings | Deep, but concentrated in the monthly |
| Typical weekly realised move | ~1.0–1.5% | ~1.0–1.6% | ~1.8–2.5% |
| Gap behaviour | Moderate | Moderate | **Violent** — bank-heavy, RBI/credit sensitive |
| Best used as | **Core weekly income engine** | **Second weekly income event** | **Positional / event instrument only** |
| Seller caution | — | Wing liquidity: check the *hedge* leg fills before selling the body. Higher CAS distortion (see `rules_constrints.md` §1.10) | Weekly income is gone. Do not force a monthly BANKNIFTY into a weekly cadence — you carry 4 weekends and 20+ sessions of gap risk for one credit |

### 8.4.1 The weekly calendar for a ₹6L book

```text
MONDAY      Form the view (Market_View.md 9 data points). No entry before 9:45 AM.
            Optional: enter the NIFTY weekly structure 10:15–10:45 AM (1 DTE).
TUESDAY     NIFTY EXPIRY.
            Exit at 50% of credit. HARD FLAT all NIFTY legs by 2:30 PM. No later tier exists.
            2:00–2:30 PM: nothing new that expires today.
WEDNESDAY   "Dead zone" — no near expiry on either exchange.
            Best day to place the POSITIONAL 25–40 DTE structure (§8.6.10).
            Optional: enter SENSEX weekly structure 10:15–10:45 AM (1 DTE).
THURSDAY    SENSEX EXPIRY.
            Exit at 50% of credit. HARD FLAT all SENSEX legs by 2:15 PM. No later tier exists.
FRIDAY      Manage the positional book only. No new weekly entries —
            you would carry a weekend gap for two sessions of theta.
            Journal: ROM, MAE, adjustment count, attribution to Theta/Vega/Gamma.
```

> **The weekend-theta myth.** Friday-to-Monday is three calendar days of Theta, and the pricing model already knows that — market makers mark down extrinsic value into Friday's close. What you actually buy by holding over a weekend is **two extra sessions of global gap risk for decay that has largely already been taken out of the price.** For a ₹6L moderate-risk book, do not open a new weekly credit structure on Friday.

---

## 8.5 The seller's regime grid — Direction × Volatility × DTE

This is the heart of §8. Most traders pick a strategy and then look for a market for it. Professionals read the market and then look up the structure. **Do not skip a cell — if your reading does not land in a cell, you do not have a trade.**

### 8.5.1 Step 1 — classify volatility, not just direction

`Market_View.md §5` gives you the direction (one of five views). You also need the **volatility state**, which is a separate axis. Use these three readings together:

| Reading | Source | Interpretation for a seller |
|---------|--------|------------------------------|
| **IVP / IV-Rank** (percentile of current ATM IV over the trailing 6–12 months) | Sensibull / broker chain | < 30 = premium is cheap → sell less, or sell nothing naked. > 60 = premium is rich → sell more, widen. |
| **VRP proxy = ATM IV − HV20** | Chain IV vs 20-day realised | **Positive and widening → the seller's best regime.** Negative → the market is moving more than it is paying you for. Stand down. |
| **India VIX slope** (today vs 5-day average) and level | NSE / `Market_View.md §6` | Rising VIX = your short Vega is bleeding. Falling VIX = Vega tailwind. |

⛔ **The IVP / `IV − HV20` decision rule that stood here is DELETED (02-Sep-2026).** It was the better
test on paper and it is unusable in practice: **both inputs need a trustworthy ATM IV series, and no
vendor available here has one.** Dhan returns CE IV 11.47 and PE IV 6.41 at the *same strike and same
expiry* — arithmetically impossible, so every IVP percentile and every `IV − HV20` computed from it is
noise wearing a decimal point. Recomputing IV locally is not permitted (see §8.17 / the Greeks rule).

**The live rule is VIX only** — the one volatility number that is measured and published rather than
derived from a broken chain:

```text
VOLATILITY STATE — live rule (TRADING_CONSTANTS.md §10)

  VIX < 12                →  CHEAP     (credit will be thin; expect the §8.11.7 noise floor to fail)
  VIX 12–16               →  NORMAL    (the working state — full formula size)
  VIX 16–20               →  RICH      (full formula size; better credit for the same width)
  VIX ≥ 20                →  HOSTILE   (⛔ nothing, not one lot)
  VIX up ≥ 8% intraday    →  HOSTILE regardless of level. No new entries. Manage existing only.
```

> **What was lost, honestly.** VRP (`IV − RV − friction`) is still the correct theory of why the edge
> exists — §8.1 stands. What is gone is the ability to *measure* it per-session. VIX is a cruder
> instrument: it is a 30-day NIFTY-wide number, so it says nothing about SENSEX specifically or about
> today's expiry specifically. It is used because a crude number that is real beats a precise number
> that is fabricated. If a trustworthy IV source ever appears, restore the two-input test and re-open
> [open item 1 in `docs/mcp-usage-log.md` §6](../../docs/mcp-usage-log.md).

### 8.5.2 Step 2 — the grid

> ⚠️ **Read this grid for the SIZE column and the STAND-DOWN cells. Ignore every structure name in
> it** — the cells below name iron flies, condors, Jade Lizards and BWBs, and **all of them are locked**
> (see the §8.6 banner). The IVP headers are also retired; map them to the VIX bands above.
>
> ⛔ **Two cells are outright dangerous and are overridden here:** "Slightly Bearish + NORMAL → bear
> call spread **+ far bull put spread**" and any other cell pairing both sides. A bull put leg under a
> bearish view is forbidden by Gate 5A with **no override**, and pairing it with a bear call does not
> launder it — it makes it a condor, which is separately locked. Under a bearish view you sell **the
> call side only**; under a bullish view, **the put side only**.
>
> For the structure, go to [Card 3](#card-3--structure-by-situation). It is two lines long, which is
> the correct length for a list with two items on it.

| | **RICH** (IVP > 60) | **NORMAL** (IVP 30–60) | **CHEAP** (IVP < 30) |
|---|---|---|---|
| **Strongly Bullish** | Short put spread wide + far short call spread → **Unbalanced Condor, put-heavy** [§8.6.7](#867-unbalanced-ratiod-iron-condor--lean-the-view-without-a-naked-leg) | **Put Broken-Wing Butterfly** [§8.6.6](#866-broken-wing-butterfly-bwb--the-credit-structure-with-zero-risk-on-one-side) — credit, zero upside risk | Small **bull put spread** only, 1–2 lots. Do not sell calls into a cheap-IV rally. |
| **Slightly Bullish** | **Jade Lizard (hedged)** [§8.6.3](#863-jade-lizard-hedged--the-put-skew-harvester) — sells the rich put, near-zero upside risk | **Jade Lizard** or **put-side-skewed condor** [§8.6.8](#868-skew-aware-delta-matched-condor--stop-measuring-in-points) | **Put BWB**, small. Defined risk only. |
| **Sideways** | **Hedged Short Straddle / Iron Fly**, wide wings [§8.6.1](#861-intraday-delta-neutral-hedged-short-straddle--the-920-structure) / [§8.6.10](#8610-0-dte-hedged-iron-fly-under-cas--expiry-day-done-properly) | **Delta-banded hedged strangle** [§8.6.2](#862-the-delta-banded-hedged-strangle--the-weekly-workhorse) or **positional 25–40 DTE condor** [§8.6.9](#869-positional-2540-dte-iron-condor--the-compounding-engine) | **Iron Fly** (ATM, tight) — the only structure that still collects enough when IV is low. Half size. |
| **Slightly Bearish** | **Reverse Jade Lizard** [§8.6.5](#865-reverse-jade-lizard-twisted-sister--and-why-it-is-harder-in-nifty) or call-heavy unbalanced condor | **Bear call spread** + far bull put spread (call-heavy condor) | Small **bear call spread** only. |
| **Strongly Bearish** | **Bear call spread, wide** — and *only* the call side. Do not sell puts into a falling market for "balance". | Bear call spread, reduced size. Consider sitting out — down-moves come with IV expansion that hurts short Vega on both sides. | **Stand down.** Cheap IV + bearish = the buyer's regime, not yours. |
| **Any view + VIX spiking / event pending** | **IV-Crush Event Harvest** [§8.6.11](#8611-iv-crush-event-harvest--rbi-policy-budget-big-results) — sell the event, exit on the crush, not on the direction | Reduce to half size; widen wings | **No new positions.** |

### 8.5.3 Step 3 — DTE decides the *shape*, not the direction

| DTE | Dominant Greek | Correct shape | What kills you here |
|-----|---------------|---------------|---------------------|
| **0 DTE** (expiry day) | Gamma dominates everything | **Iron Fly** or tight hedged straddle, small size, hard time-stop | Gamma. One 0.6% move at 1:00 PM can be 5× your credit. Plus CAS after 3:15. |
| **1–3 DTE** | Theta high, Gamma rising fast | Hedged straddle / narrow condor, exit at 40–50% | Holding into the last two hours of expiry day |
| **5–10 DTE** | Balanced Theta vs Gamma — **the sweet spot** | Delta-banded hedged strangle, iron condor | Complacency; over-sizing because "it's far away" |
| **25–45 DTE** | Vega dominates, Theta slow but steady | Wide iron condor, BWB, positional | A VIX regime shift. You are long duration on short Vega. |
| **> 45 DTE** | Almost pure Vega | Only justified if IVP > 70 and you want the Vega, not the Theta | Time. You tie up margin for a slow drip. |

> **Theta/Gamma ratio, said plainly:** Theta is roughly proportional to `1/√DTE`; Gamma is roughly proportional to `1/√DTE` too, but Gamma's *damage* scales with the square of the move while Theta's *benefit* is linear in time. That is why the seller's efficiency peaks around **5–10 DTE** and collapses inside 1 DTE, even though the raw Theta number looks best on expiry day.

### 8.5.4 Step 4 — The PE-first principle: sell the expensive side

> **Expert-sourced rule (31-Aug-2026):** "CE selling is risky...try PE selling better." Validated below as structurally correct for neutral/sideways sessions. The directional regime grid in §8.5.2 overrides it when the view is explicitly bearish.

Indian index options (NIFTY, SENSEX, BANKNIFTY) carry a persistent **negative volatility skew**: OTM puts have higher IV than equidistant OTM calls. This is not a mispricing — it is compensation for the asymmetric crash risk in Indian equities (markets grind up, crash down). The skew is a permanent structural feature of the chain.

**What this means for a credit seller:**

| Side | Skew effect | Consequence |
|------|-------------|-------------|
| **PE sell (short put / bull put spread)** | Puts carry HIGHER IV → **you receive more credit** per unit of delta risk | Better paid, better risk/reward ratio; put buyers systematically overpay for protection |
| **CE sell (short call / bear call spread)** | Calls carry LOWER IV → **you receive less credit** per unit of delta risk | Appropriate only when the directional view explicitly demands it |

**The PE-first rule:**

```text
□ Is the market view Sideways, Slightly Bullish, or Strongly Bullish?
  → DEFAULT to PE selling (Bull Put Spread, Jade Lizard, put-heavy condor).
  → Selling calls on a non-bearish day = selling cheap premium on the wrong side of the skew.

□ Is the market view Slightly Bearish or Strongly Bearish?
  → CE selling (Bear Call Spread) is appropriate — directional thesis justifies the skew disadvantage.
  → Confirm: is overhead resistance identified? Is the call wall visible on the OI chain?
  → If yes → Bear Call Spread is the §8.5.2 grid call. Proceed.
  → If no → reconsider. A flat market with a weak bearish lean is not enough justification.

□ Compression break (§8.12.6)?
  → The direction of the break decides the side:
  → Break DOWN → Bear Call Spread (CE selling) — §8.12.6a explicitly permits this
  → Break UP   → Bull Put Spread (PE selling) — you sell puts, collecting rich skew premium
```

**Why "CE selling is risky" in a non-bearish market:**

1. **You sell cheap premium** — calls have lower IV, so you collect less for the same strike distance.
2. **You are directionally wrong** — if the market is flat-to-bullish, the call spread can rally into your short strike.
3. **You miss the structural edge** — the entire skew premium (the excess IV that puts carry) accrues to the put seller, not the call seller.
4. **Put walls provide visible support** — OI walls on the put side (e.g., 24,000 PE on 31-Aug-2026) give the PE seller a defined floor that the call seller never has on the other side.

**When CE selling IS the correct trade (override of PE-first):**

| Condition | Why CE selling wins |
|---|---|
| §8.5.2 grid → Slightly/Strongly Bearish + CHEAP/NORMAL | Directional regime. The skew disadvantage is accepted for directional edge. |
| §8.12.6a → compression break DOWN | Market has broken the floor; selling the overhead is the §8.12.6a-sanctioned structure. |
| Overhead OI wall visible and unbroken (e.g., 181.8L at 24,200 CE on 31-Aug-2026) | The call wall acts as resistance; the short strike has structural support from sellers. |

**31-Aug-2026 context (the trade this rule was sourced from):**

The Bear Call Spread (24,200/24,400 CE) was the **right trade** on 31-Aug-2026 despite the PE-first principle, because:
- Market view: Slightly Bearish ✅ — §8.5.2 grid points to Bear Call Spread
- Compression break: DOWN ✅ — §8.12.6a permits one-sided CE selling
- Call wall: 181.8L at 24,200 CE visible and building ✅
- OI put wall (24,000 PE): already acting as floor, so PE selling below it had less directional backing

The expert's "PE sell is better" principle would have applied perfectly on a **flat/sideways day** — where selling calls without a bearish thesis means selling cheap premium on the wrong side. That day, a Bull Put Spread below the 24,000 wall would have been the structurally superior choice.

> **The one-line rule:** *Sell the expensive side. In NIFTY, puts are almost always the expensive side. Override only when you have a genuine directional reason to sell calls.*

---

## 8.6 The structure library — what real sellers actually put on

> ## ⛔ NOT EXECUTABLE. Reference only.
>
> **Every structure in §8.6 is LOCKED as of 02-Sep-2026.** Not one of the thirteen below may be
> traded. See [`TRADING_CONSTANTS.md` §5](../../TRADING_CONSTANTS.md) — the permitted list is
> **two items**: the bear call spread and the bull put spread, both two-legged and defined-risk.
>
> Each structure here fails at least one live constraint:
>
> | Failure | Structures |
> |---|---|
> | **4 legs** — four fills, four exits, four things to get wrong manually in a mobile app | iron fly (8.6.1), condors (8.6.7, 8.6.8, 8.6.9), 0-DTE fly (8.6.10), IV-crush fly (8.6.11), double calendar (8.6.12) |
> | **Exceeds the ₹10,500 structural cap at ONE lot** | hedged strangle (8.6.2), Jade Lizard (8.6.3), BWB (8.6.6) |
> | **Increases short exposure while losing** — banned outright at any hour, on any day | ladder (8.6.13) |
> | **A repair, never an entry** — and §8.9 is closed on expiry day, which is when this book trades | ladder (8.6.13), roll/convert throughout |
> | **Standing inventory, not a trade** — sound practice, but it presumes a multi-position book | wing bank (8.6.14) |
>
> **Why keep them?** The worked Indian numbers are the best part of this book and the payoff
> reasoning transfers. Read §8.6 to understand *why* a wing is non-negotiable or how skew prices a
> Jade Lizard. Do not read it to pick today's trade — for that, go to
> [Card 3](#card-3--structure-by-situation).
>
> **The key out:** the 4-leg family unlocks after **30 clean two-leg verticals** (constants §11).
> "Clean" means gates written before strikes, resting SL within 90 seconds, and exit by stop, target
> or time — not profitable. Profit is not the qualification; process is.

**How to read every entry.** Each structure follows the same 10 fields. All examples assume **NIFTY 24,500 / lot 65**, **SENSEX 81,000 / lot 20**, **BANKNIFTY 55,000 / lot 30** and are *illustrative pricing* — always re-price live off the Dhan option chain before acting.

**Hard rule applied throughout:** every structure below is presented in its **hedged** form. Any variant with an unhedged short leg has undefined maximum loss and is an **automatic blocker** under [`option_chain_n_greeks.md` §7](../option_chain_n_greeks.md#7-pre-trade-gono-go-checklist--session-learnings). Where the classic textbook version is unhedged, the entry says so explicitly and gives the hedged replacement.

---

### 8.6.1 Intraday Delta-Neutral Hedged Short Straddle — "the 9:20 structure"

> The most widely-run systematic seller trade in India. The textbook calls it a short straddle. What is actually traded is a **hedged, delta-neutral, time-boxed, intraday** structure with a mechanical stop — a completely different animal from the naked overnight straddle in [§3.3](#33-short-straddle).

| Field | Detail |
|-------|--------|
| **When** | Sideways / range view, NORMAL or RICH volatility, 0–2 DTE. Never on a day with a scheduled 11:00 AM–2:00 PM event. |
| **Why it works** | The first 5 minutes of the session carry an overnight-risk premium in ATM IV. By 9:20 the opening auction imbalance has cleared but the premium has not yet decayed. You sell that residue and the day's Theta together. |

**Construction (NIFTY, 1 DTE, spot 24,500 at 9:20 AM):**

```text
SELL  24,500 CE  @  68        SELL  24,500 PE  @  62      →  credit 130
BUY   24,800 CE  @  12        BUY   24,200 PE  @  10      →  debit   22
────────────────────────────────────────────────────────────────────────
NET CREDIT = 108 points  ×  65  =  ₹7,020 per lot
Wing width = 300 points
MAX LOSS   = (300 − 108) × 65   =  ₹12,480 per lot   ← defined, this is your blocker-clear number
```

**Greeks at entry:** Delta ≈ 0 (by construction) · Theta strongly positive · Vega negative · **Gamma negative and rising all day** — this is the risk you are being paid for.

**Management — the part that makes it work:**

> ⚠️ **Read the base before you read the number.** The rows below are computed off the **NET
> credit of 108**, not the 130 "credit" line in the construction block above. A trader who
> reads "rises to 140" against 130 hard-stops on a **+7.7%** adverse move instead of +30% —
> a live misfire on a 4-leg structure being managed by hand in a phone app. Every stop
> percentage must name its base in the same cell.

| Trigger | Action |
|---------|--------|
| **Structure NET value** (entry net = 108) falls to **70 pts** (−35%) | **Book. This is the target.** ₹2,470/lot. Do not get greedy for the last 20%. |
| **Structure NET value** (entry net = 108) rises to **140 pts** (+30%) | **Hard stop. Exit both sides.** −₹2,080/lot. |
| ⛔ ~~Net position Delta exceeds ±0.15 per lot~~ — **UNAVAILABLE, no trustworthy Greeks (§8.7.1a).** Substitute: **the tested short's mark reaches 3× the untested short's mark** | **Delta-repair**, do not exit: shift the untested short leg toward spot by one strike. See [§8.9.2](#892-adjustment-2--shift-the-untested-side-delta-repair). |
| Any single leg's premium **doubles** from entry | Exit that leg's spread only; run the winning side to the time stop. |
| **2:30 PM** (NIFTY) / **2:15 PM** (SENSEX) on expiry day | **Time stop — flatten regardless of P&L.** |
| **2:30 PM** (NIFTY/BANKNIFTY) / **2:15 PM** (SENSEX) | ⭐ **HARD FLAT — the only exit time.** Close at any P&L. Nothing survives into CAS. |

**Why the 9:20 entry and not 9:15:** the first five minutes have the widest spreads of the day. You would pay 2–4 points of slippage across four legs (₹650–₹1,300 per lot) for a marginally better price. Enter after the first 5-minute candle closes.

**Common mistake:** running it every single day mechanically. The 9:20 structure loses on **trend days**, and trend days cluster. Apply the [§8.13](#813-trend-day-detection--the-sellers-kill-switch) filter at 9:45 and again at 10:30 — if two of the three trend markers fire, take the small loss and stand down for the day.

---

### 8.6.2 The Delta-Banded Hedged Strangle — the weekly workhorse

> This is the bread-and-butter position of most consistently profitable Indian index sellers. Not "sell 200 points away" — **sell a delta band**, hedge it, and let the band define the strikes for you.

| Field | Detail |
|-------|--------|
| **When** | Sideways to mildly directional, NORMAL/RICH volatility, **5–8 DTE**. The peak Theta-to-Gamma efficiency zone. |
| **Delta band** | Sell the **12–20 delta** strike on each side. 16Δ is the default (≈ 1 standard deviation, ≈ 84% probability of expiring OTM). Below 10Δ you are in the friction-floor problem of [§8.3.3](#833-the-friction-floor--the-minimum-premium-worth-selling); above 25Δ you are effectively selling a straddle with extra steps. |

**Construction (NIFTY, 6 DTE, spot 24,500, ATM IV ~12%):**

```text
1 SD move over 6 days = 24,500 × 0.12 × √(6/365) ≈ 377 points

SELL  24,900 CE  (≈16Δ)  @  52        SELL  24,100 PE  (≈16Δ)  @  58   → credit 110
BUY   25,400 CE          @   9        BUY   23,600 PE          @  12   → debit   21
──────────────────────────────────────────────────────────────────────────────────
NET CREDIT = 89 points  ×  65  =  ₹5,785 per lot
Wing width = 500 points
MAX LOSS   = (500 − 89) × 65   =  ₹26,715 per lot
Break-evens ≈ 24,989 (up)  /  24,011 (down)   →  ~2.0% band, vs ~1.5% expected weekly move
```

**Note the put premium is higher than the call premium at the same distance (58 vs 52).** That is the persistent NIFTY put skew. It is not a mispricing you can arbitrage — it is compensation for the fact that Indian index down-moves are faster than up-moves. Respect it: see [§8.6.8](#868-skew-aware-delta-matched-condor--stop-measuring-in-points).

**The wing-distance trade-off — the decision most people make by accident:**

| Wing distance from short strike | Credit retained | Max loss | Margin | Use when |
|---|---|---|---|---|
| **200 pts (tight)** | ~50–60% of gross | Small (~₹9k/lot) | Lowest | Small account, high-conviction range, event risk pending |
| **300–500 pts (standard)** | ~75–85% of gross | Medium (~₹16–27k/lot) | Moderate | **Default.** Best credit-to-margin balance |
| **800+ pts (far / "disaster wing")** | ~92–96% of gross | Large (~₹46k/lot) | Highest | Only when the wing is genuinely just a margin-relief and blocker-clearing device and your *stop* — not the wing — is your real risk control |

> **The wing is not your stop-loss.** A 500-point wing on NIFTY means your "defined max loss" is ₹26,715/lot — that is 4.6× your credit. If you ever actually reach max loss, you have failed at management. The wing exists to (a) satisfy the defined-max-loss blocker, (b) cut margin by roughly 3–4× versus naked, and (c) cap a gap. **Your stop-loss, at 1.5–2× credit, should always trigger long before the wing does.**

**Management:**

| Trigger | Action |
|---|---|
| Structure value falls to **50% of credit** (44.5 pts) | Book. ₹2,893/lot. This is the target — do not hold for the last 50%, it takes 2× the time for 1× the money at 3× the Gamma. |
| Structure value reaches **2× credit** (178 pts) | Hard stop. −₹5,785/lot. |
| One short leg's delta reaches **30Δ** | Adjustment trigger — go to [§8.9](#89-the-adjustment-playbook--decision-tree). |
| **2 DTE reached and position is at < 25% profit** | Close it. Beyond this point the Gamma is no longer worth the remaining Theta. |
| **VIX up > 8% intraday** | HOSTILE (`TRADING_CONSTANTS.md` §10). Close the position. The old 10% figure is retired — one threshold, used everywhere. |

---

### 8.6.3 Jade Lizard (hedged) — the put-skew harvester

> **The structure Indian index sellers should know and mostly do not.** A Jade Lizard is a short put + a short call spread, sized so that **total credit ≥ the width of the call spread**. When that condition holds, there is *no risk at all on the upside* — the worst the call spread can do is exactly offset the credit.
>
> It is the natural NIFTY trade because it **sells the expensive (skewed) put outright and only sells the cheap call as a defined-risk spread.**

**The condition:**
> [YT](https://youtube.com/shorts/p2P-s-LlM6M?si=1-CVIrGYTciBUAsJ)

```text
ZERO-UPSIDE-RISK CONDITION

    Total net credit  ≥  (long call strike − short call strike)

If credit = 104 and the call spread is 100 wide, then above the long call:
    P&L = 104 − 100 = +4 points.  You still make money on an unlimited rally.
```

**Construction (NIFTY, 6 DTE, spot 24,500) — textbook version, then the tradable version:**

```text
── TEXTBOOK JADE LIZARD (do NOT trade this: naked put = undefined loss = BLOCKER) ──
SELL  24,300 PE  @  76
SELL  24,700 CE  @  78
BUY   24,800 CE  @  50
NET CREDIT = 104 pts     Call spread width = 100     104 > 100  →  zero upside risk ✅
Downside break-even = 24,300 − 104 = 24,196
Risk below 24,196 = UNLIMITED  ← automatic blocker

── TRADABLE HEDGED JADE LIZARD (add the put wing) ──
SELL  24,300 PE  @  76
BUY   23,900 PE  @  26      ← the wing that makes it legal for a ₹6L moderate-risk book
SELL  24,700 CE  @  78
BUY   24,800 CE  @  50
──────────────────────────────────────────────────────────────
NET CREDIT = 78 points × 65 = ₹5,070 per lot

PAYOFF AT EXPIRY (per lot)
  Spot ≥ 24,800   →  78 − 100 = −22 pts  =  −₹1,430    ← tiny, DEFINED upside loss
  24,300–24,700   →  +78 pts             =  +₹5,070    ← max profit zone (400 pts wide)
  Spot = 23,900   →  78 − 400 = −322 pts =  −₹20,930   ← max loss
  Spot < 23,900   →  loss capped at −₹20,930
```

**What you traded away and what you gained:** the put wing converts "small profit on any rally" into "small *defined* loss (₹1,430) on a big rally" — and in exchange it caps a catastrophic downside at ₹20,930 instead of infinity. For a ₹6L book that trade is not close: **always take the wing.**

**When to use it:** Slightly Bullish to Sideways, IVP > 50, and **specifically when the put skew is steep** (25Δ put IV minus 25Δ call IV is wide). You are being paid the most for the risk you are most willing to define.

**Management:** manage the put side only — the call side cannot hurt you beyond ₹1,430. Target 50% of credit. Stop: if the short put reaches 30Δ, roll it down and out, or close.

---

### 8.6.4 Big Lizard — the aggressive cousin

> A Jade Lizard with the short put moved all the way to **ATM** — i.e. a short ATM straddle plus a long call. Same zero-upside-risk condition, far more credit, far more Gamma. Hedged, it is effectively an **unbalanced iron fly**.

```text
NIFTY 24,500, 6 DTE

SELL  24,500 CE  @ 152        SELL  24,500 PE  @ 148      → credit 300
BUY   24,700 CE  @  78        BUY   24,000 PE  @  52      → debit  130
────────────────────────────────────────────────────────────────────────
NET CREDIT = 170 pts × 65 = ₹11,050 per lot

Call spread width 200; unhedged version's credit (222) > 200 → the classic Big Lizard
has zero upside risk. The put wing costs 52, so the hedged version has:

  Spot ≥ 24,700  →  170 − 200 = −30 pts  =  −₹1,950     (small defined upside loss)
  Spot = 24,500  →  +170 pts             =  +₹11,050    (max profit, single point)
  Spot ≤ 24,000  →  170 − 500 = −330 pts =  −₹21,450    (max loss)
```

**When:** high-conviction pin/sideways view with IVP > 60 and a clear max-pain magnet at 24,500. **Not** a beginner structure — max profit exists only at one point, and Gamma near the ATM short is brutal inside 2 DTE.

**Reality check:** the credit is 2× the strangle's, and so is the pain. Run it at **half the lot count** you would run a strangle at, and never inside 1 DTE without a hard time stop.

---

### 8.6.5 Reverse Jade Lizard (Twisted Sister) — and why it is harder in NIFTY

> The mirror image: **short call + short put spread**, sized so total credit ≥ the put spread width → **zero risk on the downside.**

```text
NIFTY 24,500, 6 DTE

SELL  24,650 CE  @  88        ← the outright short (naked in textbook form)
BUY   25,100 CE  @  22        ← the wing that makes it tradable
SELL  24,300 PE  @  76
BUY   24,200 PE  @  56
──────────────────────────────────────────────────────────────
Put spread credit = 20, width = 100
Unhedged total credit = 88 + 20 = 108 ≥ 100  →  zero downside risk ✅
Hedged NET CREDIT = 108 − 22 = 86 pts × 65 = ₹5,590 per lot

  Spot ≤ 24,200  →  86 − 100 = −14 pts   =  −₹910        (tiny defined downside loss)
  24,300–24,650  →  +86 pts              =  +₹5,590      (max profit)
  Spot ≥ 25,100  →  86 − 450 = −364 pts  =  −₹23,660     (max loss)
```

**The expert caveat nobody tells you:** because NIFTY has a persistent **put** skew, the Reverse Jade Lizard **sells the cheap side outright and defines risk on the rich side** — the exact opposite of what the skew rewards. Use it only when you have a genuine Slightly Bearish view *and* the skew has flattened or inverted (which happens after a sharp panic, when put IV has already been paid for). In a normal skewed market, prefer a plain **bear call spread + far bull put spread** ([§8.6.7](#867-unbalanced-ratiod-iron-condor--lean-the-view-without-a-naked-leg)).

---

### 8.6.6 Broken-Wing Butterfly (BWB) — the credit structure with zero risk on one side

> The best risk-adjusted directional-lean credit structure available to a retail Indian seller, and completely absent from the textbook section above. A butterfly with **unequal wings**, constructed so that it is entered **for a net credit** and carries **no risk whatsoever** on one side.

**Construction — Put BWB (bullish / neutral lean), NIFTY 20 DTE, spot 24,500:**

```text
BUY   1 ×  24,400 PE  @ 215      ← narrow wing (200 pts above the body)
SELL  2 ×  24,200 PE  @ 165      ← the body
BUY   1 ×  23,700 PE  @  62      ← wide wing (500 pts below the body)
─────────────────────────────────────────────────────────────────────
NET  = −215 + (2 × 165) − 62  =  +53 points CREDIT  ×  65  =  ₹3,445 per lot

PAYOFF AT EXPIRY (per lot)
  Spot ≥ 24,400   →  +53 pts   =  +₹3,445    ← ZERO UPSIDE RISK. Any rally = full credit.
  Spot = 24,200   →  +253 pts  =  +₹16,445   ← max profit (the body)
  Spot = 23,700   →  −247 pts  =  −₹16,055   ← max loss
  Spot < 23,700   →  loss capped at −₹16,055

MAX LOSS = (wide wing width − narrow wing width) − credit
         = (500 − 200) − 53  =  247 points
```

**Why professionals love it:**

| Property | Consequence |
|---|---|
| Entered for a **credit** | Even if you are completely wrong to the upside, you keep 100% of the credit. There is no "wrong direction" on one side. |
| Risk exists on **one side only** | You only have to manage one direction. Half the adjustment work of a condor. |
| **Positive skew on the payoff** | Max profit (₹16,445) ≈ max loss (₹16,055), but the max-profit zone is reachable and the max-loss zone requires a 3.3% adverse move. |
| **Low Vega** relative to a condor | Butterflies are much less exposed to a VIX spike than a wide strangle. Safer to hold through news. |

**Mirror version — Call BWB (bearish / neutral lean):** buy 1 narrow-wing call *below*, sell 2 body calls, buy 1 wide-wing call further above. Zero risk on the downside; risk only on a strong rally.

**Management:**

| Trigger | Action |
|---|---|
| 50% of max profit | Book. |
| Spot approaches the **body strike** with > 7 DTE left | This is *good* — you are approaching max profit. Hold. |
| Spot breaks **below the body** with < 5 DTE | Danger zone. Either close, or buy back the extra short (converting to a plain balanced fly with defined smaller risk). |
| Spot approaches the **wide wing** | Close. You are near max loss and the structure has no recovery mechanism. |

**Sizing note:** because max loss ≈ ₹16,055/lot, a ₹6L book with a 2.5% per-trade cap (₹15,000) can hold **1 lot** if you are willing to ride to max loss, or 2 lots with a stop at 50% of max loss. See [§8.11](#811-position-sizing--two-caps-take-the-smaller).

---

### 8.6.7 Unbalanced (Ratio'd) Iron Condor — lean the view without a naked leg

> A standard iron condor is 1 put spread + 1 call spread. An **unbalanced** condor uses a different number of spreads per side, or different widths per side, to express a directional lean while keeping every leg defined-risk. This is how a professional expresses "Slightly Bullish" — not by removing the call side, and definitely not by selling a naked put.

**Two ways to unbalance:**

```text
METHOD A — UNEQUAL COUNT (put-heavy = bullish lean), NIFTY 6 DTE, spot 24,500

  2 ×  [ SELL 24,100 PE @ 58 / BUY 23,600 PE @ 12 ]   →  credit 2 × 46 = 92
  1 ×  [ SELL 24,900 CE @ 52 / BUY 25,400 CE @  9 ]   →  credit 1 × 43 = 43
  ──────────────────────────────────────────────────────────────────────
  NET CREDIT = 135 pts × 65 = ₹8,775
  Max loss (down) = (2 × 500 − 135) × 65 = ₹56,225   ← BIG. This is the cost of the lean.
  Max loss (up)   = (1 × 500 − 135) × 65 = ₹23,725

METHOD B — UNEQUAL WIDTH (call-side tighter = bearish lean)

  SELL 24,100 PE @ 58 / BUY 23,300 PE @  6    → 800-wide put spread, credit 52
  SELL 24,900 CE @ 52 / BUY 25,100 CE @ 26    → 200-wide call spread, credit 26
  ──────────────────────────────────────────────────────────────────────
  NET CREDIT = 78 pts × 65 = ₹5,070
  Max loss (down) = (800 − 78) × 65 = ₹46,930
  Max loss (up)   = (200 − 78) × 65 =  ₹7,930    ← cheap protection where you expect the move
```

**Which method when:**

| | Method A (unequal count) | Method B (unequal width) |
|---|---|---|
| Expresses | "I expect drift in my direction" | "I expect a move *against* the lean to be sharp if it happens" |
| Credit | Higher | Lower |
| Tail risk | **Concentrated and large on the heavy side** | Balanced-ish; explicitly cheap on the tight side |
| Recommended for a ₹6L moderate-risk book | ⚠️ Only at 1× base size, never more | ✅ Preferred |

> **The trap in Method A:** doubling the put spreads doubles your downside max loss while the credit only rises by ~50%. Traders reach for it because the credit looks good and the "probability" looks unchanged. It is a leveraged bet on your directional view wearing a market-neutral costume. If you use it, count the heavy side's max loss against your per-trade cap — not the average.

---

### 8.6.8 Skew-Aware Delta-Matched Condor — stop measuring in points

> The single most common unforced error in Indian retail selling: building a "neutral" strangle or condor by counting **points** from spot. Because of put skew, an equidistant structure is never neutral. It is quietly short the market — and you find out on the day it matters.

**The problem, in one table.** NIFTY, spot 24,500, 6 DTE, equidistant ±400 points:

| Leg | Strike | Distance | IV | Delta | Premium |
|---|---|---|---|---|---|
| Short CE | 24,900 | +400 | 11.2% | **0.13** | 52 |
| Short PE | 24,100 | −400 | 13.8% | **−0.19** | 71 |

```text
POSITION DELTA of the "neutral" strangle
  Short call →  −0.13
  Short put  →  +0.19
  ─────────────────────
  NET        =  +0.06   ← you are NET LONG the market by ~0.06/lot
                          On 6 lots that is +0.36 delta ≈ 23 NIFTY points of
                          directional exposure you never chose to take.
```

**Why this is worse than it looks.** The put side is both *closer in delta terms* **and** the side where a move arrives with an IV expansion. A 1% fall gives you three simultaneous losses — delta, gamma and vega — while a 1% rally typically gives you a delta loss partly offset by an IV *contraction* gain. **The downside tail on an equidistant structure is roughly 1.5–2× the upside tail.**

**The fix — match delta, not points:**

| Leg | Strike | Distance | IV | Delta | Premium |
|---|---|---|---|---|---|
| Short CE | 24,900 | **+400** | 11.2% | 0.13 | 52 |
| Short PE | 23,950 | **−550** | 14.2% | **−0.13** | 46 |

```text
NET DELTA ≈ 0.00      ← genuinely neutral
Credit    = 98 points (vs 123 for the equidistant version)

You gave up 25 points of credit and moved the put 150 points further from harm.
That is the trade. The 25 points was never "free" premium — it was payment for
carrying an unhedged directional view.
```

> **Read this line twice.** The put is **150 points further out** and still fetches **46**, while the call at 400 points fetches **52**. That gap *is* the skew — and it is why put-side selling at matched delta is the better-paid side of the Indian index chain. It is also the entire economic engine behind the Jade Lizard ([§8.6.3](#863-jade-lizard-hedged--the-put-skew-harvester)).

**The wings must be skew-matched too.** If you buy 500-wide wings on both sides, the put wing is materially more expensive and materially more useful. Match wings by *cost* or by *delta*, not by width — a 500-wide call wing and a 700-wide put wing often cost the same and leave you with a better-shaped risk graph.

**Doing this without a Greeks feed** *(directly relevant while `mcp__dhan__optionchain` is entitlement-blocked — see [`docs/mcp-usage-log.md`](../../docs/mcp-usage-log.md))*:

| Proxy | How | Accuracy |
|---|---|---|
| **Premium-matching** | Pick the put and call strikes with the **same premium**, not the same distance. Equal premium ≈ equal delta to within 1–2Δ. | ⭐⭐⭐⭐ Best no-Greeks proxy. Free from any chain. |
| **Straddle-multiple** | Compute the ATM straddle price `S`. Place shorts at `spot + 0.85S` (call) and `spot − 1.05S` (put). The asymmetry approximates NIFTY's typical skew. | ⭐⭐⭐ Good enough for a weekly. |
| **OI-symmetry** | Place shorts just beyond the nearest CE wall above and PE wall below with comparable OI. | ⭐⭐ Structural, not statistical. Use as a confirmation, not a primary. |

**Rule of thumb for NIFTY weeklies:** at equal delta, the put strike sits roughly **1.3–1.4×** as far from spot in points as the call strike. If your condor is symmetric in points, it is wrong.

---

### 8.6.9 Positional 25–40 DTE Iron Condor — the compounding engine

> Every retail seller wants the weekly. The traders who actually compound run a **monthly** book and use weeklies as a satellite. Fewer trades, less slippage, less screen time, and — decisively — a structure that survives a bad Tuesday.

| Field | Detail |
|-------|--------|
| **When** | Sideways to mildly directional, **NORMAL or RICH** volatility, entered at **25–40 DTE**. Practically: the first week after the previous monthly expiry. |
| **Instrument** | **NIFTY monthly only.** BANKNIFTY monthly is acceptable at half size (higher notional per lot). SENSEX monthly wings are too illiquid at this distance. |
| **Delta band** | **8–12Δ** shorts. Further out than the weekly workhorse, because you are holding through more calendar risk. |
| **Wings** | 400–600 points. Wider wings = more credit but the margin benefit collapses; 400 is the practical sweet spot on NIFTY. |

**Construction (NIFTY monthly, 32 DTE, spot 24,500, ATM IV ~12%):**

```text
1 SD over 32 days = 24,500 × 0.12 × √(32/365) ≈ 870 points
Shorts placed at ≈ 1.2 SD (≈ 10–11Δ)

SELL  25,500 CE @ 48   /  BUY  25,900 CE @ 20    →  call spread credit 28
SELL  23,500 PE @ 62   /  BUY  23,100 PE @ 32    →  put  spread credit 30
─────────────────────────────────────────────────────────────────────────
NET CREDIT = 58 points × 65  =  ₹3,770 per lot
Wing width = 400 points (both sides)
MAX LOSS   = (400 − 58) × 65 =  ₹22,230 per lot
Return on risk (if held to expiry) = 58 / 342 = 17.0%
Return on risk at the 50% target   = 8.5%, typically reached in 12–18 days
```

**The management rules that make it an engine rather than a lottery:**

| Rule | Value | Why |
|---|---|---|
| **Profit target** | **50% of net credit** | The last 50% of a condor's credit takes ~70% of the remaining time and carries ~100% of the remaining gamma risk. Taking half early and redeploying compounds faster than holding to expiry. This is the single highest-value rule in the section. |
| **Time exit** | **Close at 14 DTE regardless of P&L** (unless already at target) | Below ~14 DTE the gamma of a 10Δ condor starts to bite and the position stops behaving like a Vega/Theta trade. You did not enter a gamma trade. |
| **Loss stop** | Combined structure value = **2× net credit** | −58 pts = −₹3,770/lot. See [§8.10](#810-stop-loss-architecture--four-types-and-which-to-use). |
| **Delta stop** | Either short reaches **~25Δ** | The side is being tested. Adjust per [§8.9](#89-the-adjustment-playbook--decision-tree) or close that side. |
| **Adjustments allowed** | **One per side, per trade. Maximum two total.** | See [§8.9.7](#897-the-adjustment-budget--why-most-adjustments-lose-money). |

**Why 50%-and-out beats hold-to-expiry — the arithmetic that convinces people:**

```text
HOLD TO EXPIRY          :  58 pts over 32 days  =  1.81 pts/day
EXIT AT 50% ON DAY 15   :  29 pts over 15 days  =  1.93 pts/day   ← higher rate
                            ...AND the capital is free for 17 days
                            ...AND you were never exposed to the last-two-week gamma
```

**Indian-market liquidity check before you sell any 25–40 DTE strike** — this is where the theory breaks:

- Strike **OI > 50,000** and today's volume > 5,000 on the short legs.
- Bid-ask spread on the **wing** < 8% of its premium. Far monthly wings on NIFTY routinely quote 14 / 19 — a 26% spread. That wing costs you more to buy and is nearly unsellable in a hurry.
- Never sell a monthly strike whose wing you have not confirmed you can *buy back*. A hedge you cannot exit is not a hedge; it is a decoration that satisfies the margin engine.

> **Capital reality for a ₹6L book.** Margin on this structure is roughly max-loss-plus-a-little, so ≈ ₹23,000–28,000 per lot. At the ₹6,000 per-trade risk cap of [§8.11](#811-position-sizing--two-caps-take-the-smaller) with a 2×-credit stop (₹3,770/lot), you can carry **1 lot** comfortably. This is not a get-rich structure at ₹6L. It is the **base layer** — put 30–40% of the book here, run the weekly workhorse on top, and let the monthly do the compounding while the weekly does the earning.

---

### 8.6.10 0-DTE Hedged Iron Fly under CAS — expiry day done properly

> Expiry day is where Indian retail donates most of its money, and where a disciplined seller makes some of the cleanest returns of the week. The difference is entirely mechanical: **structure, size, and a clock.**

**Why an Iron Fly and not a strangle or condor at 0 DTE.** On expiry morning the OTM strikes have almost no extrinsic value left. A 200-point-OTM NIFTY call on expiry day trades at 6–9. After the friction floor in [§8.3.3](#833-the-friction-floor--the-minimum-premium-worth-selling) you are selling ~4 net points of real premium and carrying the full tail. **Virtually all of expiry-day premium is concentrated at the money.** If you are going to sell on expiry day, you must sell ATM — which means an Iron Fly, and which means accepting large gamma in exchange.

**Construction (NIFTY expiry Tuesday, entered 9:45 AM, spot 24,500):**

```text
SELL  24,500 CE @ 52     SELL  24,500 PE @ 48       →  credit 100
BUY   24,700 CE @  8     BUY   24,300 PE @  7       →  debit   15
──────────────────────────────────────────────────────────────────
NET CREDIT = 85 points × 65  =  ₹5,525 per lot
Wing width = 200 points
MAX LOSS   = (200 − 85) × 65 =  ₹7,475 per lot
BREAKEVENS = 24,415  /  24,585      ← a band of only ±0.35%
```

**The honest problem with this trade, stated plainly:**

```text
Breakeven band          =  ±0.35%
NIFTY average daily range ≈  0.60 – 0.80%

The 0-DTE Iron Fly is close to a coin flip UNLESS the day is genuinely pinned.
Its edge does not come from the structure. It comes from the FILTER.
```

**The filter — all four must be true before you put this on:**

1. **Trend-day markers clean** at 9:45 — zero of the three in [§8.13](#813-trend-day-detection--the-sellers-kill-switch) have fired.
2. **Today's opening range sits inside yesterday's range.** An inside day is the pin setup. A gap outside the prior range is not.
3. **Max Pain within ~0.3% of spot**, and the largest CE and PE OI walls straddle the current price rather than sitting on one side.
4. **No scheduled event** between 11:00 AM and 2:00 PM, and India VIX not up more than 5% on the day.

**Management — the clock does most of the work:**

| Time / Trigger | Action |
|---|---|
| **Structure NET value** (entry net = 85) falls to **51** (−40%) | **Book.** +34 pts = ₹2,210/lot. |
| **Structure NET value** (entry net = 85) reaches **127** (+50%) | **Hard stop.** −42 pts = −₹2,730/lot. |
| Spot touches either **breakeven** (24,415 / 24,585) | Reassess immediately. Either roll the tested short to ATM (converting to a wider fly) or cut. Do **not** hope. |
| **12:30 PM** | If P&L is flat or negative, close. The remaining theta is not worth the remaining gamma. |
| **2:30 PM (NIFTY) / 2:15 PM (SENSEX)** | **Time stop — flatten regardless of P&L.** |
| **2:30 PM (NIFTY/BANKNIFTY) / 2:15 PM (SENSEX)** | ⭐ **HARD FLAT — the only exit time.** Close at any P&L. |

#### The CAS rules that specifically govern this structure

Since **3-Aug-2026** the last 15 minutes are a Closing Auction Session. For a 0-DTE seller this changes three things, and none of them are theoretical:

| CAS consequence | What it means for the Iron Fly |
|---|---|
| **Continuous trading stops at 3:15 PM** | Your wings stop being hedges. A hedge you cannot trade is a payoff diagram, not a risk control. |
| **Settlement is the IEP, and the close is randomised between 3:28–3:30** | You cannot know your settlement price and you cannot manage into it. A short ATM straddle settling on an IEP you did not see is an **unhedgeable blind expiry**. |
| **Premium decay stalls inside CAS** | The one thing you were being paid for — decay — stops working precisely when your gamma is at its maximum. You are carrying the risk without the compensation. |

> **Non-negotiable:** no leg survives past the hard flat — **2:30 PM (NIFTY/BANKNIFTY) / 2:15 PM (SENSEX)**. Not the shorts, not the wings, not "just the far one, it's worthless anyway". A worthless-looking wing is exactly what stops being worthless in an auction. Full mechanics in [`rules_n_regulations/rules_constrints.md`](../rules_n_regulations/rules_constrints.md).

**Expiry-day margin surprise (Feb-2025 rule).** SEBI removed the calendar-spread margin benefit on expiry day, and exchanges levy **additional ELM on expiry-day positions**. Margin required on expiry morning for the same structure can be **20–40% higher** than the previous afternoon's number. Price the margin *on the day*, not from yesterday's basket call.

---

### 8.6.11 IV-Crush Event Harvest — RBI policy, Budget, big results

> The one seller trade where you are explicitly **not** trading direction, **not** trading theta, and **not** holding for days. You are trading a single variable — implied volatility — across a single known moment. Get the framing wrong and this becomes the fastest way to lose a month.

**The mechanic.** Ahead of a scheduled binary event, ATM IV rises because the market prices an unknown outcome. The instant the outcome is known, that uncertainty premium disappears — regardless of *what* the outcome was. That collapse is the "crush". You sell the elevated IV before, and buy it back after the crush, ideally within 15–45 minutes of the announcement.

**The Indian event calendar worth trading:**

| Event | Frequency | Typical ATM IV lift | Tradeable? |
|---|---|---|---|
| **RBI MPC decision** | 6× per year | +2 to +4 vol pts | ✅ **The best one.** Outcome range is narrow, crush is reliable. |
| **US Fed decision** (spillover into next-day NIFTY) | 8× per year | +1 to +2 | ✅ Small size. Second-hand event, weaker crush. |
| **Union Budget (1 Feb)** | Annual | +6 to +12 | ⚠️ Defined risk, **quarter size**. Realised moves of 2–3% are normal. |
| **Monthly F&O expiry week** | Monthly | +1 to +2 | ✅ Mild, blends into the normal weekly. |
| **Big-4 index-heavyweight results** (RIL, HDFC Bank, Infosys, TCS) | Quarterly | Index +1 to +2; the stock +8 to +20 | ✅ On the index. Stock options are physically settled — see the warning below. |
| **US CPI / NFP** | Monthly | +0.5 to +1.5 | ❌ Below the friction floor. Not worth the legs. |
| **General-election counting day** | Rare | +15 to +30 | ⛔ **Do not trade.** See below. |

**Construction (RBI MPC, decision at 10:00 AM tomorrow; entered today ~2:30 PM, NIFTY 3 DTE, spot 24,500, ATM IV elevated to 15.5%):**

```text
SELL  24,500 CE @ 118    SELL  24,500 PE @ 112      →  credit 230
BUY   24,900 CE @  32    BUY   24,100 PE @  28      →  debit   60
────────────────────────────────────────────────────────────────────
NET CREDIT = 170 points × 65  =  ₹11,050 per lot
Wing width = 400 points
MAX LOSS   = (400 − 170) × 65 =  ₹14,950 per lot

NEXT MORNING, 10:25 AM — decision out, spot 24,530, ATM IV collapses 15.5% → 11.5%
  Structure now worth ≈ 128 points
  GAIN = 42 points × 65  =  ₹2,730 per lot  in ~20 minutes of market exposure
  → CLOSE. The trade is over. There is nothing left to harvest.
```

**The four rules that separate this from gambling:**

| # | Rule | Why |
|---|---|---|
| 1 | **Exit on the crush, not on the direction.** | If IV has collapsed and you are up, you are done — even if you "think it goes lower from here". The moment the vol edge is gone you are running a naked directional bet you never analysed. |
| 2 | **Exit even if the direction went against you.** | If spot moved 0.6% against you but IV crushed 4 points, the vega gain has already offset much of the delta loss. That partial recovery is the *best exit you will get*. Waiting for a full recovery is how a −₹3,000 becomes a −₹12,000. |
| 3 | **Defined risk always. Half normal size. Quarter size on Budget day.** | The whole premise is that the event is *priced*. Occasionally it is not. |
| 4 | **Enter late, not early.** | IV lift is largest in the final session before the event. Entering three days early means paying theta and carrying direction for two days to capture the same crush. Enter in the **last 90 minutes** of the prior session. |

> ⛔ **The election-day lesson.** On **4 June 2024** (Lok Sabha counting day) NIFTY fell roughly **5.9% intraday** — the worst single-day fall in over four years — after opening higher on exit-poll optimism. India VIX had spiked above 26 the previous week. Every short-vol structure that was "collecting the crush" was destroyed, because the *realised* move was multiples of the *implied* move. **IV crush is real. It is not a substitute for the move being small.** Defined risk is the only thing that made survivors survivors.

> ⚠️ **Stock options are physically settled.** A short stock-option leg carried into expiry results in an obligation to deliver or take delivery of the shares, with a settlement value far exceeding your margin. Harvest results-season IV on the **index**, or close stock legs well before expiry. See [`CLAUDE.md`](../../CLAUDE.md) → Key Domain Concepts.

---

### 8.6.12 Double Calendar / "Batman" — and the February-2025 margin trap

> A structure with a genuinely different risk profile from everything above — **long** vega, **long** the term-structure — and one specific way to blow it up that did not exist before February 2025.

**The mechanic.** Sell near-expiry options and buy the same strikes in a later expiry, at two strikes straddling spot. You profit because the near leg decays faster than the far leg (theta is proportional to `1/√DTE`), and because you are long the vol term structure. The payoff has two humps — hence "Batman".

**Construction (NIFTY, spot 24,500; near expiry 3 DTE, far expiry 10 DTE):**

```text
SELL  24,700 CE (near) @ 28    BUY  24,700 CE (far) @ 62   →  debit 34
SELL  24,300 PE (near) @ 30    BUY  24,300 PE (far) @ 68   →  debit 38
──────────────────────────────────────────────────────────────────────
NET DEBIT = 72 points × 65  =  ₹4,680 per lot   ← this is your max loss
MAX PROFIT ≈ at 24,300 or 24,700 on the near expiry, roughly 1.6–2.0× the debit
```

| Property | Value |
|---|---|
| **Vega** | **Positive** — the only structure in §8 that *gains* if IV rises. |
| **Theta** | Positive, but modest. |
| **Best regime** | **CHEAP volatility** (IVP < 30) that you expect to normalise, with a range-bound price view. It is the natural complement to everything else here. |
| **Worst regime** | A sharp trending move — both humps are missed and the debit decays away. |
| **Max loss** | The net debit. Genuinely capped. No blocker issue. |

#### ⚠️ The February-2025 margin trap — read before you ever run one

Effective **1 February 2025**, SEBI **removed the calendar-spread margin benefit for contracts expiring on the same day**. Before this, the exchange margined a calendar as a spread (offsetting the near short against the far long), which was cheap. Now:

```text
DAY BEFORE NEAR EXPIRY   :  margined as a calendar spread   ≈ ₹40,000 / lot
MORNING OF NEAR EXPIRY   :  offset REMOVED — the near shorts
                            are margined as though standalone ≈ ₹1,50,000+ / lot
                            ...plus additional expiry-day ELM
```

**What actually happens to a retail account:** you wake up on the near leg's expiry day with a margin shortfall you did not create by trading. The broker's RMS system squares off your legs — usually the *hedges* first, because they are the liquid ones — leaving you momentarily naked, at market, at whatever price the auto-square-off engine finds. This is now one of the most common causes of unexplained expiry-day losses in Indian retail F&O.

> **The rule, and it is absolute:** **close or roll the near leg on the session *before* its expiry day.** Never carry a calendar, diagonal or double calendar into the near leg's expiry session. Set the reminder when you enter the trade, not when you remember.

**Related correction:** [§5.2 Calendar Spread](#52-calendar-spread-not-same-expiry) above describes the textbook structure without this rule, because the rule post-dates it. §8.6.12 supersedes it for anything traded after 1-Feb-2025.

---

### 8.6.13 The Ladder — a repair, never an entry

> Bear Call Ladder and Bull Put Ladder appear in [§5.4 / 7.5](#75-ratio-spread-with-extra-short-option-54-ratio-spread) as high-risk strategies, and as *entries* that is correct — a ladder entered for credit has an undefined-loss zone and is an automatic blocker. But as a **repair on an already-tested vertical**, the ladder is one of the most useful tools a seller has, and almost no retail trader uses it that way.

**The situation.** You are short a bear call spread. The market is running through it. Your options are: take the loss, roll (and risk turning it into a martingale — [§8.9.6](#896-adjustment-6--cut-and-when-rolling-for-credit-becomes-a-martingale)), or **convert**.

**The conversion — one extra long call:**

```text
EXISTING (tested) BEAR CALL SPREAD, NIFTY spot now 24,430
  SELL  24,400 CE   /   BUY  24,500 CE       entered for credit 11.75
  Max loss at expiry ≥ 24,500  =  −88.25 pts

ADD ONE LEG:  BUY 1 × 24,600 CE @ 5.00       →  now a BEAR CALL LADDER
  Net credit becomes  11.75 − 5.00  =  6.75 pts

PAYOFF AT EXPIRY (per lot of 65)
  Spot ≤ 24,400   →   +6.75 pts   =    +₹439      ← the move reverses: still a winner
  Spot = 24,500   →  −93.25 pts   =  −₹6,061      ← max loss
  Spot = 24,600   →  −93.25 pts   =  −₹6,061      ← max loss (flat across the zone)
  Spot = 24,693   →      0 pts    =        ₹0     ← upper breakeven
  Spot = 24,800   →  +106.75 pts  =   +₹6,939
  Spot = 25,000   →  +306.75 pts  =  +₹19,939     ← uncapped above
```

**What the conversion bought you, and what it cost:**

| | Before (plain spread) | After (ladder) |
|---|---|---|
| Max loss | −₹5,736 | **−₹6,061** (+₹325 worse) |
| Loss zone | Everything ≥ 24,500 | **Only 24,500 – 24,693** |
| A violent continuation | Full max loss | **Uncapped profit** |
| A reversal back below 24,400 | +₹764 | +₹439 |

> You paid **₹325 per lot** to convert "I lose the maximum if this keeps running" into "I lose the maximum only if it stalls in a 193-point pocket, and I profit if it really runs." On a genuine trend day — which is precisely when your spread is being tested — that is an excellent trade.

**The three conditions for using it:**

1. **The trend-day filter has fired** ([§8.13](#813-trend-day-detection--the-sellers-kill-switch)). If the move is real, the ladder pays. If it is a fake-out that stalls, the ladder is the *worst* outcome. Only convert when you now believe the move.
2. **Enough DTE left for the extra long to work** — at least 1 full session. On 0 DTE the third leg is a lottery ticket, not a repair.
3. **The extra long is genuinely cheap** — under ~40% of the original net credit. If the wing has already repriced, you are buying insurance after the fire started.

**Bull Put Ladder** is the exact mirror for a tested bull put spread: add one further-OTM long put, capping the loss zone and turning a hard breakdown back into a profit.

**What a ladder is *not*:** it is not a way to "avoid taking a loss". You still hold a losing position with a defined worst case. It changes the *shape* of the outcome, not the fact that you were wrong about the direction.

---

### 8.6.14 The Rolling Wing Bank — margin efficiency as a strategy

> Not a payoff structure — a **standing inventory practice**. It is the least glamorous item in §8 and probably the one with the largest effect on a ₹6L book's annual return.

**The economics.** After the October-2024 margin regime, an unhedged short NIFTY option consumes SPAN + Exposure of roughly **₹1.4–1.9 lakh per lot**. Add a single far-OTM long option costing ₹8–15 and the same position is margined as a spread — roughly **₹40,000–70,000 per lot**.

```text
COST OF THE WING      :  ~12 points × 65        =  ₹780
MARGIN RELEASED       :  ~₹1,00,000 per lot
EFFECTIVE "INTEREST"  :  you rented ₹1 lakh of buying power for ₹780

There is no other trade in the Indian market with this ratio.
This — not risk management — is why every professional Indian seller buys wings.
The risk cap is the bonus.
```

**The practice.** Instead of buying a wing at the moment you need it (when your short is under pressure and the wing has already repriced 3–5×), maintain a **standing bank of cheap far-OTM longs** bought when they are nearly free:

| Rule | Detail |
|---|---|
| **When to buy** | Early in the expiry cycle, in the **dead zone** (11:00 AM – 12:30 PM) when spreads are stable, and on **low-VIX days** — exactly when nobody wants them. |
| **What to buy** | 2–5Δ strikes, 600–1,000 points OTM on NIFTY weeklies. Target ₹5–15 per option. |
| **How many** | Enough to cover your **maximum planned short count for the week**, both sides. Typically 4–8 options for a ₹6L book. |
| **Cost budget** | Cap the wing bank at **0.15% of capital per week** — ₹900 on ₹6L. If it costs more than that, IV is too high to be buying tails cheaply; buy them next week. |
| **Rolling** | As spot drifts, the wings drift out of usefulness. Roll them **once** mid-cycle, not continuously — rolling is 2 legs of slippage each time. |

#### ⛔ The three ways the wing bank fails — all avoidable

| Failure | Mechanism | Rule |
|---|---|---|
| **Expiry mismatch** | Your hedge is in a different expiry from your short. Many margin engines give **reduced or zero** offset for cross-expiry hedges, and after 1-Feb-2025 the offset **vanishes entirely on the shared expiry day**. | **Hedge in the same expiry as the short. Always.** |
| **The hedge expires first** | Your wing expires Tuesday, your short is a monthly. Tuesday evening your margin jumps by ₹1 lakh per lot with no trade on your part → RMS auto-square-off Wednesday morning at market. | **Never let the hedge expire before the short.** Set a calendar alert on the hedge's expiry, not the short's. |
| **The illiquid wing** | You bought a 1,200-point-OTM strike at ₹3 with 400 OI. When you need to close the structure, the bid is ₹0.05 and there is no buyer. You cannot exit the spread; you can only exit the short, which un-hedges you and spikes your margin. | **OI > 25,000 and a live two-sided quote before you buy any wing.** A wing you cannot sell is not a hedge. |

> **Verify, do not assume.** Margin offsets change with exchange circulars and with your broker's own RMS policy. Price every structure with a **basket margin call** before entry — `mcp__dhan__margin_agent_tool`, the Zerodha SPAN calculator, or Kotak's `get_margin` — and confirm the *hedged* number, not the leg-by-leg sum. Never size a position off a remembered margin figure.

---

## 8.7 Strike selection — the four methods and when each wins

Everyone has a favourite method and defends it as if it were the only one. In practice each method answers a different question, and the professional habit is to run **two** and let the disagreement tell you something.

### 8.7.1 Method 1 — The delta band *(⛔ NOT USABLE — no trustworthy delta exists)*

> ## ⛔ Do not quote a vendor delta. Use `credit ÷ width`.
>
> This method needs a delta, and **there is no trustworthy delta available in this setup.** Dhan's are
> computed off spot rather than the forward (§8.7.1a below); Kite and Kotak publish none; and computing
> Black-Scholes locally is **not permitted**. Every Δ figure in the table below is therefore reference
> material describing what the bands *mean*, not an instruction to go and read one.
>
> **The live substitute — model-free, vendor-free, unbreakable:**
>
> ```text
>       credit ÷ width   ≈   the short strike's delta
> ```
>
> As width narrows, a vertical's price → Δ × W exactly, so the ratio *is* the delta, computed from two
> numbers you can see on any chain. It cannot go stale, cannot be computed off the wrong underlying,
> and cannot silently disagree between the CE and PE side.
>
> **Read the bands below through it:** `c/W` **≥ 15%, 20% preferred** (`TRADING_CONSTANTS.md` §6) — so
> the live band is roughly the **15–25Δ** row, which is where a directional credit vertical belongs.
> The floor is a tail-control rule, not a preference: at `c/W = 3.5%` max loss is 28× the credit and
> the breakeven win rate is 96.5%. **01-Sep-2026 sold exactly that and lost ₹15,564.**

Delta is a usable proxy for the probability of the strike being breached at expiry.

| Band | Approx. probability OTM | Use for |
|---|---|---|
| **8–12Δ** | 88–92% | Positional 25–40 DTE condors ([§8.6.9](#869-positional-2540-dte-iron-condor--the-compounding-engine)) |
| **12–20Δ** | 80–88% | The weekly workhorse strangle ([§8.6.2](#862-the-delta-banded-hedged-strangle--the-weekly-workhorse)) — **16Δ is the default** |
| **20–30Δ** | 70–80% | Directional credit spreads where you *want* the delta |
| **> 30Δ** | < 70% | You are running a directional trade. Call it one and size it as one. |
| **< 8Δ** | > 92% | Friction floor territory ([§8.3.3](#833-the-friction-floor--the-minimum-premium-worth-selling)). The premium no longer covers the slippage. |

> ⚠️ **Never use `POP = 1 − |Delta|` as a probability of profit.** Delta approximates the probability of finishing **in the money**, which is the probability of *breaching*, not the probability of *losing money* — your breakeven sits beyond the strike by the credit received. See [`option_chain_n_greeks.md` §5](../option_chain_n_greeks.md).

#### 8.7.1a The forward-basis check — **run this before you trust any delta** *(added 28-Aug-2026)*

Options are priced off the **forward**, not the spot. Every vendor that computes Greeks off spot silently shifts your entire strike ladder. On 28-Aug-2026 Dhan's chain put NIFTY's Δ=0.50 point near 24,190 when the true ATM-forward was **24,237** — a **~85-point bearish skew on every strike selected**, invisible unless you check.

**The 30-second test — model-free, uses only chain prices:**

```text
1.  FORWARD, via put-call parity:        F  =  K  +  C  −  P
      Compute at 3–4 strikes around ATM. They must agree to within ~1 point.
      (If they don't agree, the chain is stale — stop, refetch.)

2.  BASIS:                          basis  =  F − Spot
      NIFTY 01-Sep 2026:   24,237 − 24,155  =  +82 pts  (+0.34%)
      SENSEX 03-Sep:       77,523 − 77,240  =  +283 pts
      BANKNIFTY 29-Sep:    57,916 − 57,534  =  +382 pts

3.  VENDOR SANITY CHECK — one strike, one expiry, one underlying = ONE IV.
      If the vendor reports CE IV ≠ PE IV at the same strike, its Greeks are broken.
      Observed 28-Aug: NIFTY 24,200 → CE IV 11.47 vs PE IV 6.41.  Gap +5.06.
      Calls inflated, puts deflated → the classic signature of pricing off spot.

4.  DECISION:
      basis < 0.1% of spot  →  vendor deltas usable
      basis > 0.1%          →  DISCARD the delta band. Use §8.7.3 (straddle rule)
                                and centre it on F, not on spot.
```

| Vendor symptom | What it means |
|---|---|
| CE IV ≠ PE IV at the same strike | Greeks computed off spot. Arithmetically impossible otherwise. |
| Deep-ITM legs return `IV = 0, Δ = 0, Θ = 0` | Solver failed to converge. Not "zero risk" — **no data**. |
| Parity forward disagrees strike-to-strike by > 2 pts | Stale or mixed-timestamp snapshot. Refetch before acting. |

> **Parity is arithmetic, not a model.** Using `F = K + C − P` is *not* the locally-computed Black-Scholes the user has ruled out — it assumes nothing about volatility or distribution. Recomputing delta or theta yourself **is** ruled out. When the basis check fails, the sanctioned path is §8.7.3 (the straddle rule, centred on F), plus telling the user the vendor Greeks are unusable — never a silent local substitute.

**Why the basis is not a constant.** It scales with time to expiry (cost of carry). A +82 basis on a 4-day NIFTY forward is steep; on the 32-day BANKNIFTY it was +382. Recheck it each session — do not carry over yesterday's number.

> **Corollary — GIFT Nifty is a futures price.** Comparing GIFT to NIFTY *spot* manufactures a gap that does not exist. On 28-Aug, GIFT at 24,250 against spot 24,090 looked like a +160 gap-up; against the forward it was flat. Always compare GIFT to the **future or forward of matching tenor**. See [`option_chain_n_greeks.md` §7 Filter 1](../option_chain_n_greeks.md).

### 8.7.2 Method 2 — Expected move

```text
EXPECTED MOVE (1 SD, over the holding period)

  Formula A (from IV)        :  EM  =  Spot × IV × √(DTE / 365)
  Formula B (from the chain) :  EM  ≈  ATM straddle price × 0.85

  Worked: NIFTY 24,500, IV 12%, 6 DTE
    A →  24,500 × 0.12 × √(6/365)  =  24,500 × 0.12 × 0.1282  =  377 points
    B →  ATM straddle 440 × 0.85                              =  374 points   ✅ agree
```

Sell **at or beyond 1 SD**. Formula B is the one to use in practice — it needs no IV feed, it is read straight off the chain, and it already contains the market's own view of the move rather than a model's.

> **When A and B disagree by more than ~10%,** trust B and be suspicious: it usually means the ATM IV you were quoted is stale, or the straddle is carrying event premium the annualised IV number is smoothing away.

### 8.7.3 Method 3 — The straddle rule *(the fastest, works with no Greeks at all)*

> The single most useful shortcut in this section, and the one to fall back on whenever the Greeks feed is unavailable.

```text
1.  Read the ATM straddle price.        NIFTY 24,500 straddle = 440
2.  Call short   =  Spot + (0.85 × straddle)  =  24,500 + 374  =  24,874  →  24,900
3.  Put short    =  Spot − (1.05 × straddle)  =  24,500 − 462  =  24,038  →  24,050
4.  Wings        =  400–500 points beyond each short.
```

The **asymmetric multipliers (0.85 call / 1.05 put)** are not arbitrary — they bake in NIFTY's structural put skew, so the output is approximately delta-matched without ever touching a delta. This reproduces [§8.6.8](#868-skew-aware-delta-matched-condor--stop-measuring-in-points) from chain prices alone.

### 8.7.4 Method 4 — OI walls and structural zones

Not a probability method — a **structural** one. Sell beyond the strike where writers have already committed capital.

| Signal | Read |
|---|---|
| **Largest CE OI above spot** | The market's consensus ceiling. Sell your call *at or above* it, never below. |
| **Largest PE OI below spot** | The consensus floor. Sell your put at or below it. |
| **OI *change* today**, not absolute OI | Fresh writing is the live signal. Absolute OI includes stale positions from earlier in the cycle. |
| **Max Pain** | Where the most option value expires worthless. A weak magnet in the last 1–2 days; nearly meaningless earlier. |
| **A wall being *unwound*** | ⛔ The most important and least-watched signal. If the PE wall under you is shrinking while price falls, the floor is being removed — do not sell puts there. |

Full matrix in [`open_interest.md`](../open_interest.md).

### 8.7.5 Which method wins when

| Situation | Primary | Confirm with | Why |
|---|---|---|---|
| Normal weekly, Greeks available | Delta band | Straddle rule | Delta is precise; straddle catches stale IV |
| **No Greeks feed** | **Straddle rule** | OI walls | Needs only chain prices |
| 0–1 DTE | Expected move | OI walls | Delta is unstable and near-binary this close in |
| Positional 25–40 DTE | Delta band | Expected move | The long horizon makes structure less relevant than statistics |
| Event trade | Expected move (from the *elevated* straddle) | — | The straddle already prices the event; use it |
| Strong directional view | OI walls | Delta band | You want a structural level, not a statistical one |

### 8.7.6 The reconciliation rule

> **Run two methods. If they land within one strike of each other, take the trade. If they disagree by two strikes or more, take the *further* strike — or take no trade.**
>
> A disagreement means the statistical view and the structural view are telling different stories. That is information. Trading the nearer strike because it pays more is how a seller converts a warning into a loss.

---

## 8.8 Entry timing — the intraday premium and IV curve

Premium is not uniformly priced across the day. Indian index options follow a repeatable intraday shape, and knowing it is worth more than most strike-selection refinements.

### 8.8.1 The intraday curve

```text
ATM PREMIUM / IV THROUGH AN INDIAN TRADING DAY (typical range day)

 IV
  │██
  │███                                                        ▄▄
  │████▄                                                   ▄▄███
  │██████▄▄                                            ▄▄██████
  │█████████▄▄▄▄                                 ▄▄▄▄████████
  │██████████████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄███████████████
  └─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬────
      9:15  9:30 10:30 11:15 12:30  1:30  2:15  2:30  3:15 3:30
       ▲     ▲         └──── the dead zone ────┘         ▲   ▲
     avoid  SELL         lowest RV, best decay        EXIT  CAS
```

> ⚠️ **The clock below is the market's shape; the windows are `TRADING_CONSTANTS.md` §7's.** Where the
> two disagree, the constants win. Three retired items are corrected inline: the entry window is
> **9:30–11:15**, not 9:20–9:45; there is **no "last clean entry" at 10:30**; and the exit times are
> **one per index**, not a target/hard pair.

| Window | Character | Seller's action |
|---|---|---|
| **9:15 – 9:30** | Widest spreads of the day. Opening auction imbalance. Overnight premium still in the price. | ⛔ **Do not trade.** You will pay 2–4 points per leg in slippage for a marginally better mid. The opening bar is also **excluded from the §8.11.7 noise-floor measurement** — it is not representative of the day's range. |
| **9:30 – 11:15** | ✅ **THE ENTRY WINDOW.** Auction cleared, premium still substantially intact, the day has shown enough character to score Gates 3–5 honestly. | **The only entry window there is.** Widened from the old 9:20–9:45 because gates take time to run properly and a 25-minute window pressures you into scoring them fast. Nothing enters after 11:15 — not a "second look", not a re-rack at better strikes. |
| **11:15 – 12:30** | Realised volatility falls, decay steadies, spreads tighten. | **Manage only.** ⛔ Not an entry window, and ⛔ **not an "add" window either** — one structure per calendar day (`TRADING_CONSTANTS.md` §3), and no order may increase short exposure in a losing structure at any hour. The old "best window to add or roll" line is retired. |
| **12:30** | — | 🔍 **MIDDAY GATE.** A scheduled re-score, not a glance at P&L. |
| **12:30 – 1:30** | Lunch lull. Volumes thin, spreads widen relative to volume. | Manage. Fills are poor for no compensating edge. |
| **1:30 – 2:15** | European open, US futures wake up. **The second directional leg of the day starts here.** | Manage. Most afternoon trend legs begin in this window, and you are already past any entry. |
| **2:15** | — | 🚪 **SENSEX HARD FLAT.** Close at any P&L. |
| **2:30** | — | 🚪 **NIFTY / BANKNIFTY HARD FLAT.** Close at any P&L. |
| **3:15 – 3:30** | **CAS.** Continuous trading has stopped. | **Be flat long before this.** CAS is not the deadline — it is what the deadline exists to keep you away from. |

### 8.8.2 The weekly calendar for entries

| Day | NIFTY DTE | SENSEX DTE | What a seller does |
|---|---|---|---|
| **Monday** | 1 | 3 | Poor entry day for the workhorse — too little DTE on NIFTY, and weekend news is still being digested. Manage existing. |
| **Tuesday** | **0 (expiry)** | 2 | Morning: 0-DTE fly if and only if the filter is clean ([§8.6.10](#8610-0-dte-hedged-iron-fly-under-cas--expiry-day-done-properly)). **Afternoon: the best entry of the week** — the new NIFTY weekly opens at 7 DTE with a full premium and no event risk yet priced. |
| **Wednesday** | 6 | **1** | ✅ **Prime entry day.** NIFTY at 6 DTE sits exactly in the 5–10 DTE Theta/Gamma sweet spot. |
| **Thursday** | 5 | **0 (expiry)** | SENSEX expiry day — **hard flat 2:15 PM**. NIFTY at 5 DTE is ⛔ blocked by Gate 1 (≥3 sessions). |
| **Friday** | 4 | 6 | Acceptable. Weekend gap risk is *already in the price* — see below. |

> **The weekend-theta myth, restated because it costs people money.** Options do not decay over the weekend in the way retail folklore claims. Market makers mark down the Friday close in anticipation of two non-trading days, and mark up Monday's open for weekend gap risk. **You are not paid to hold theta over a weekend — you are paid to hold gap risk over a weekend.** Selling Friday afternoon specifically "for the weekend decay" is selling gap risk for a premium that has already been removed. Covered in [§8.4](#84-instrument-selection--nifty-vs-banknifty-vs-sensex).

### 8.8.3 The three timing prohibitions

1. **Never enter in the 15 minutes before or after a scheduled announcement.** Spreads triple, IV is unstable, and you have no idea what you are being paid.
2. **Never enter on a gap-open day before 9:45.** A gap of more than 0.4% invalidates every level in your pre-market view. Re-derive the view first.
3. **Never enter after 2:00 PM on any day you cannot hold overnight.** You are buying the day's worst decay with the day's worst gamma and no time to repair.

---

## 8.9 The adjustment playbook — decision tree

> This is the part that decides whether a seller compounds or bleeds. The structures in §8.6 are commodity knowledge. What you do at 1:40 PM when the market is 40 points through your short strike is not.

### 8.9.1 Adjustment 1 — Do nothing *(the most under-used)*

The default action is **no action**. A 16Δ short reaching 22Δ is the structure working normally, not a problem.

| Do nothing when | Because |
|---|---|
| The short's delta is still inside your band + 8Δ | Normal fluctuation. Adjusting here converts noise into realised cost. |
| The move is inside the day's expected move | You priced this. |
| DTE > 5 and the structure is down less than 1× credit | There is time for mean reversion, which is the thing you sold. |
| It is between 12:30 and 1:30 PM | The lunch lull produces the day's worst fills and its least informative price action. |

> **The 30-minute rule.** When a level is breached, start a 30-minute timer. If price is still through the level after 30 minutes, the break is real — adjust. If it has come back, you saved four legs of slippage. Most intraday breaches of a 16Δ strike fail within 30 minutes.

### 8.9.2 Adjustment 2 — Shift the untested side *(delta repair)*

The workhorse adjustment. Do **not** touch the losing side; bring the *winning* side closer to re-neutralise delta and collect additional credit.

```text
SITUATION — NIFTY strangle, spot has fallen 24,500 → 24,220
  Short 24,900 CE @ 52 → now worth 18   (winning, delta collapsed to 5Δ)
  Short 24,100 PE @ 58 → now worth 96   (losing, delta now −31Δ)
  Net position delta ≈ +0.26/lot        ← you are now materially long the market

ACTION — roll the CALL side DOWN, not the put side away
  BUY  BACK  24,900 CE @ 18      (book +34 pts on that leg)
  SELL       24,600 CE @ 41      (fresh 15Δ)
  Roll the call wing down correspondingly: 25,400 → 25,100

RESULT
  Additional credit  =  +23 points
  Net delta          ≈  +0.11/lot        ← materially re-neutralised
  Breakeven          →  improved on BOTH sides
  Legs traded        =  4 (two shorts, two wings)
```

| Rule | Value |
|---|---|
| **Trigger** | Net position delta exceeds **±0.15 per lot**, or the untested short falls below **7Δ** |
| **How far to shift** | Back to the **original delta band** (15–16Δ), never closer |
| **Frequency** | **Once per side, per trade.** A second shift on the same side means the market is trending — go to §8.9.6. |
| **Never** | Shift the untested side so close that a reversal puts *both* sides in trouble. If the shift would put the new short inside 1 SD of spot, do not do it — cut instead. |

### 8.9.3 Adjustment 3 — Roll the tested side out and away

Buy back the tested short and sell a further-out strike, either in the same expiry (**out**) or the next (**away**).

| | Roll same-expiry, further OTM | Roll to the next expiry |
|---|---|---|
| Credit | Usually a **debit** — you are paying to move | Usually a **credit** |
| Effect | Buys distance, costs money now | Buys time *and* distance |
| Risk added | None | **Duration.** You have extended your exposure by a week. |
| Verdict | ✅ Acceptable once | ⚠️ Only if the view is unchanged and the credit is genuine |

> ⛔ **The rule that prevents the classic death spiral:** **never roll for a credit that requires increasing size.** "Roll out and double up so it's still a credit" is a martingale. It has a wonderful win rate and one terminal loss. See §8.9.6.

### 8.9.4 Adjustment 4 — Hedge up

Add long options *without* touching the existing legs.

| Variant | When | Cost |
|---|---|---|
| **Buy the wing closer** (roll the existing wing in) | The tested side is running and you want to cap the loss tighter | Debit; reduces max loss immediately |
| **Buy an extra long at the tested strike** | Converting toward a ladder ([§8.6.13](#8613-the-ladder--a-repair-never-an-entry)) | Small debit; changes the payoff shape |
| **Buy a futures hedge** | Position delta is large and you want a clean, liquid, one-leg fix | Margin-heavy, but **one leg instead of four** — often the cheapest adjustment in slippage terms on a large book |

> **Underrated:** on a multi-lot position, hedging delta with **one NIFTY futures lot** costs one leg of slippage. Re-strikeing four option legs costs four. On a ₹6L book futures are usually too blunt (one lot of NIFTY futures ≈ 65 delta), but know the tool exists.

### 8.9.5 Adjustment 5 — Convert the structure

| Conversion | From → To | Effect |
|---|---|---|
| **Add the opposite side** | Naked-ish credit spread → Iron Condor | Adds credit, widens the profit zone, no new risk on the added side |
| **Add a third strike** | Vertical → **Ladder** ([§8.6.13](#8613-the-ladder--a-repair-never-an-entry)) | Turns "max loss if it keeps running" into "profit if it keeps running" |
| **Buy back the extra short** | Unbalanced condor → balanced condor | Removes the leveraged side; reduces credit and risk together |
| **Move a wing** | Condor → **Broken-Wing Butterfly** | Eliminates risk on one side entirely |
| **Close one side** | Condor → single vertical | Cleanest adjustment there is. Take the winning side off, run the loser to its stop. |

> **The most under-used conversion:** simply **closing the winning side and keeping the loser**. It sounds backwards. It is correct. The winning side has almost no premium left to collect and is still consuming margin and slippage-on-exit. Bank it, and you now hold a single defined-risk vertical with a clear stop instead of a four-legged structure you are managing on two fronts.

### 8.9.6 Adjustment 6 — Cut, and when "rolling for credit" becomes a martingale

**Cut immediately, no timer, no adjustment, when any of these is true:**

| Condition | Why it is terminal |
|---|---|
| Combined structure value hits your stop ([§8.10](#810-stop-loss-architecture--four-types-and-which-to-use)) | The stop is the plan. Adjusting at the stop is abandoning the plan. |
| **Two of three trend-day markers have fired** ([§8.13](#813-trend-day-detection--the-sellers-kill-switch)) | Mean reversion — the thing you sold — is not available today. |
| You have already used your **two adjustments** | §8.9.7. |
| India VIX up **> 8%** intraday | Regime break → HOSTILE (`TRADING_CONSTANTS.md` §10). Short vega in a vol expansion is not a position you adjust; it is one you exit. |
| You cannot state, in one sentence, why the *adjusted* position is a trade you would enter fresh right now | The only honest test there is. |

```text
THE MARTINGALE TEST — apply before every roll

  Q1. Does this roll require MORE lots than I currently hold?          → YES = martingale
  Q2. Is my max loss AFTER the roll larger than it was BEFORE?         → YES = martingale
  Q3. Have I already rolled this side once?                            → YES = martingale
  Q4. Am I rolling because of the market, or because I don't want
      to book the loss?                                                → the second = martingale

  ANY yes  →  DO NOT ROLL. CLOSE THE POSITION.
```

> **"Rolling for credit" is the most dangerous phrase in option selling.** It is genuinely correct in a mean-reverting market, which is most of the time — which is exactly why it feels reliable, builds confidence, and grows in size right up until the trending market that ends it. Every large retail option-selling blow-up in India follows this shape. The rule that stops it is a hard adjustment count, not judgement in the moment.

### 8.9.7 The adjustment budget — why most adjustments lose money

```text
COST OF ONE ADJUSTMENT ON A NIFTY CONDOR (4 legs, 3 lots, qty 195)

  Slippage :  4 legs × 0.5 pt × 195      =  ₹390
  Charges  :  4 orders + STT + txn + GST =  ₹110
  ────────────────────────────────────────────────
  TOTAL    ≈  ₹500 per adjustment, per 3 lots

  Three adjustments  =  ₹1,500
  Original net credit on that condor  =  ~₹4,000

  You have spent 37% OF YOUR ENTIRE CREDIT defending it.
  The trade must now be a 60%+ winner just to match a plain 50%-target exit
  that was never adjusted at all.
```

| Rule | Value |
|---|---|
| **Adjustment budget** | **Maximum 2 per trade. Maximum 1 per side.** |
| **Adjustment cost cap** | Total adjustment cost < **25% of the original net credit**. Exceeded → close instead. |
| **Track it** | Log adjustment count per trade. If your average is above 1.0, your **entries** are wrong, not your adjustments. That is the real diagnosis and almost nobody makes it. |

### 8.9.8 The decision tree

```text
                    SHORT STRIKE IS BEING TESTED
                               │
              ┌────────────────┴────────────────┐
       Combined value                    Combined value
       BELOW stop?                       AT or ABOVE stop?
              │                                 │
              ▼                                 ▼
    Has 30 min passed with                  ► CUT. No adjustment. ◄
    price still through the level?             (§8.9.6)
              │
      ┌───────┴────────┐
     NO               YES
      │                │
      ▼                ▼
  DO NOTHING     Have 2 of 3 trend-day
   (§8.9.1)      markers fired? (§8.13)
                       │
              ┌────────┴────────┐
             YES               NO
              │                 │
              ▼                 ▼
        ► CUT, or        Adjustments used
          CONVERT TO      on this trade?
          A LADDER ◄            │
          (§8.6.13)     ┌───────┴───────┐
                       2+              0 or 1
                        │                │
                        ▼                ▼
                    ► CUT ◄     Is the OTHER side
                                 below 7Δ / deep in profit?
                                        │
                               ┌────────┴────────┐
                              YES               NO
                               │                 │
                               ▼                 ▼
                    ► SHIFT THE UNTESTED  ► ROLL TESTED SIDE
                      SIDE (§8.9.2) ◄       OUT + AWAY (§8.9.3)
                                            — once only, no size increase
```

---

## 8.10 Stop-loss architecture — four types and which to use

A stop-loss on a multi-leg position is not one decision. It is four, and using the wrong type is how sellers manage to lose *more* than their theoretical max loss.

### 8.10.1 The four types

| # | Type | Rule | Verdict |
|---|---|---|---|
| **1** | **Per-leg SL** | Exit a leg when its premium doubles from entry | ⛔ **Dangerous on a hedged structure.** Exiting one leg **un-hedges you** — margin spikes instantly and your defined-risk position becomes undefined. Acceptable *only* on a naked position, which you should not have. |
| **2** | **Combined-premium SL** | Exit the **whole structure** when its net value reaches `k × entry credit` | ✅ **The professional default.** Measures the actual thing that is going wrong. |
| **3** | **MTM rupee SL** | Exit when the position's unrealised loss reaches a fixed rupee figure | ✅ Use **alongside** type 2, as the account-level backstop. Non-negotiable per `CLAUDE.md`. |
| **4** | **Level / underlying SL** | Exit if spot breaches a chart level, PDH/PDL, or the short strike | ✅ Excellent **secondary** trigger — it fires on the cause rather than the symptom, and often earlier. |

> **Use 2 + 3 always. Add 4 when you have a clear structural level. Never use 1 on a hedged position.**

### 8.10.2 Setting `k` for the combined-premium stop

### ★ `k = 1.6`. It is a constant, not a choice.

```text
  Defined-risk two-leg credit vertical  →  k = 1.6  →  loss at stop = 0.6 × credit
```

There is one permitted structure family, so there is one `k`. It is not an input to `size-it`, it is
not tuned per setup, and **`k = 2.0` is ⛔ permanently retired.**

> **The table that stood here listed 1.3 / 1.5 / 2.0 by structure — and had no row for the credit
> vertical**, which is the only thing now traded. So the vertical inherited `k = 2.0` from the nearest-
> looking row. That is how a stop got set at twice the credit on a structure where twice the credit
> can sit *beyond max loss* and never trigger at all.

**Stop reachability — check this before accepting any `k`:**

```text
  k × credit  <  width          ⟺        c/W  <  1/k        (at k = 1.6, c/W < 62.5%)

  Above that line the premium stop is unreachable: the structure hits its wing before it
  ever prints k × credit, and you sit holding a position you believe is stopped, all the
  way to max loss. §8.6.2's "your stop at 1.5–2× credit should always trigger long before
  the wing does" is true for a wide-wing strangle and FALSE for any near-ATM vertical.
```

With the c/W floor at 15–20%, reachability is comfortable in practice — but it is checked, not assumed.

> **Why not a wider stop?** Credit-structure losses are convex. A structure at 1.6× credit is not
> "halfway to max loss" — it is typically 25–30% of the way there and accelerating. Every point of
> further adverse move costs more than the last. **This is where the position stops being a theta
> trade and becomes a gamma trade.**

### 8.10.3 Execution — why SL-M orders on options are a trap

| Problem | Consequence |
|---|---|
| **Exchange execution-range / freeze limits** | An SL-M on an option can be rejected outright at the exact moment volatility spikes — precisely when you need it. |
| **Illiquid strikes** | An SL-M on a far wing can fill 20–40% away from the last traded price. |
| **Four legs, four separate stops** | They will not fire together. You end up part-hedged, at market, mid-move. |
| **NSE restricts SL-M on options** | Several brokers disable it for F&O entirely. |

**What to do instead:**

1. **Price alerts, not orders.** Set alerts on the *underlying* (level SL) and on combined premium. Execute the exit manually as a **basket / multi-leg order** with a limit a few points beyond the mid.
2. **Always exit the structure as a basket.** Buying back the short before selling the wing leaves you momentarily naked; the reverse leaves you long-only and over-margined. Most platforms support basket exit — use it.
3. **If exiting manually leg by leg is unavoidable: buy back the shorts FIRST, sell the wings second.** Never the other way around. The seconds you are un-hedged are the only seconds that can produce an unbounded loss.
4. **Dhan Super Orders** attach bracket legs at entry and are the closest thing to a reliable automated structure stop currently available across the three brokers in this repo.

### 8.10.4 The trailing rule — ⛔ SUSPENDED

```text
  THE LIVE RULE:   +50% of credit captured  →  CLOSE.  That is the whole rule.

  ⛔ Do NOT move the stop to breakeven at +50%.
  ⛔ Do NOT trail.
  ⛔ Do NOT scale out.
```

The retired version made +50% a *stop-move* and pushed the exit out to +70%. Two problems:

1. **It contradicted the exit target.** +50% is where the trade closes. A rule that turns the exit
   into a stop adjustment means the target is never actually taken.
2. **It adds a manual decision at the worst possible moment.** Moving a stop means cancelling a live
   order and placing a new one, in a mobile app, on a position that is currently winning and moving.
   The documented failure mode of this book is **freezing on exactly one such decision** — on
   01-Sep-2026 the exit trigger fired and what followed six minutes later was a *ninth lot sold*, not
   an exit. Every removed decision is a removed opportunity to freeze.

The reasoning behind the old rule was sound and still holds — the last 30% of a credit structure's
value carries ~70% of its remaining calendar risk and ~100% of its remaining gamma risk. **That is an
argument for closing at 50%, which is what the live rule does.** It was never an argument for staying
in until 70%.

> **Unlocks after 20 clean trades** (`TRADING_CONSTANTS.md` §11). Until then the position has exactly
> three ways out: **stop, target, or time.**

### 8.10.5 Abort conditions must match the structure's Greeks — *added 27-Aug-2026*

A stop (§8.10.1–8.10.4) fires on **loss**. An **abort condition** fires on a *thesis* breaking, before
the loss arrives. Aborts are worth having — but a wrong one is worse than none, because it exits
winners at the moment they start working.

**The failure mode: importing a neutral-structure abort onto a directional one.**

| Abort | Correct for | ⛔ Wrong for | Why |
|---|---|---|---|
| **"Exit if India VIX rises > X%"** | Straddle · iron fly · condor · strangle | **Any one-sided credit vertical** | A vertical's vega is one-sided and small. If price is moving **away** from the short strike, **delta gain dominates vega loss** — the position is *winning* while VIX rises. |
| "Exit if the range breaks" | Range/pin structures | Trend-aligned verticals | The break is the payoff (§8.12.6a). |
| "Exit if spot touches the short strike" | ✅ Everything | — | Fires on the actual cause. Keep this one. |

**The rule:**

> **Before attaching an abort, name the Greek it is protecting.** If the structure is not materially
> exposed to that Greek in that direction, the abort is noise and it will cost you the trade.
> A vol-based abort belongs on a **vega-dominant** position. A directional credit spread is
> **delta-dominant** — abort it on *price*, not on volatility.

**Preferred aborts for a one-sided credit vertical:**

1. **Spot reclaims a defined level** (the level that invalidated the directional read) — the primary.
2. **The OI wall you sold into starts *shrinking*** (§8.12.8) — writers are abandoning the defence.
3. Combined-premium stop per §8.10.2 — the backstop, not the trigger.

**Evidence — 27-Aug-2026.** A bear call spread was planned with the abort *"exit if India VIX
re-crosses 11.17."* VIX crossed it at ~11:23 and went on to close +4.73%. **The spread expired
worthless — a full winner.** Obeying that abort would have exited near flat at 11:23 and forfeited
the entire move. The plan, not the market, would have destroyed the trade.

---

## 8.11 Position sizing — two caps, take the smaller

> If you read one subsection of §8, read this one. Every other decision in this document can be wrong and survivable. This one cannot.

### 8.11.1 The formula

```text
                     PER-TRADE RUPEE RISK CAP
  NUMBER OF LOTS  =  ────────────────────────────
                     RUPEE LOSS PER LOT AT YOUR STOP


  ⛔ NOT:  Lots = Available margin ÷ Margin per lot
```

> ⚠️ **This single-cap formula is superseded. It caps the loss at your STOP but not the loss if the
> stop never executes** — which is exactly what happened on 01-Sep-2026. The live rule is **two caps,
> take the minimum** ([`TRADING_CONSTANTS.md` §4](../../TRADING_CONSTANTS.md)):
>
> ```text
> lots_A = floor( 10,500 ÷ ((width − credit) × lot_size) )    structural — if the stop never fires
> lots_B = floor(  3,500 ÷ (0.6 × credit × lot_size) )        planned stop, k = 1.6
> LOTS   = min(lots_A, lots_B)          ⛔ LOTS < 2 → narrow the width, or no trade
> ```
>
> **Width is chosen AFTER the cap, never before** — never widen the strikes to afford more lots.
> The rest of §8.11 below explains *why* sizing comes from the stop and not from margin; that
> reasoning is intact. Take the numbers from the constants file.

Margin tells you what the exchange will *permit*. It has no relationship to what you can *survive*. The margin engine is sizing for the exchange's risk, not yours.

### 8.11.2 The caps for a ₹7,02,275 book *(moderate-to-low risk profile)*

> ⛔ **Every row below except the two new ones caps the loss AT YOUR STOP. None of them caps
> the payoff.** §8.11.1's denominator is explicitly "rupee loss per lot *at your stop*". When
> the stop fails — a gap, an exchange freeze, a missed alert, or a 100-minute lag between
> "EXIT NOW" at 13:12 and the actual fill at 14:51 — the binding constraint is **max loss**,
> and until 02-Sep-2026 this table had no line for it.
>
> The gap was not theoretical. §8.11.3's own worked row — "Bear call spread (100 wide), 7 lots,
> ~₹6,000 at the stop" — carries `7 × (6,500 − 764) = ₹40,152` of max loss, **5.7% of capital
> and 3.8× the daily cap, in one structure the table calls compliant.** Three of them, all
> permitted, is 17% of the account.

| Cap | Value | Rationale |
|---|---|---|
| ★ **Per-structure MAX LOSS** *(payoff, not stop)* | **₹10,500 (1.5%)** | **New, 02-Sep-2026.** Set deliberately EQUAL to the daily cap, so that total failure of the stop still lands inside the day's limit. This is the only cap that does not depend on you pressing a button. |
| ★ **Aggregate MAX LOSS, all open structures** | **₹10,500 (1.5%)** | **New.** One structure per day (see below) makes this the same number. |
| **Per-trade loss at the stop** | **₹3,500 (0.5%)** | Three consecutive stops = the daily cap. |
| **Daily max loss** | **₹10,500 (1.5%)** | Hit it → **stop for the day**, and the next session is a mandatory no-trade day. Not "one more small one to recover". |
| **Weekly max loss** | **₹21,000 (3.0%)** | Hit it → stop for the week, and the following week is paper-only. Review entries, not adjustments. |
| ★ **Minimum credit ÷ width** *(defined-risk vertical)* | **≥ 15%, 20% preferred** | **New.** A tail-control rule: at c/W = 3.5% max loss is 28× the credit; at 20% it is 4×. **01-Sep-2026 sold a 200-wide spread for 6.99 points — c/W = 3.5%, breakeven win rate 96.5%, max loss ₹12,545/lot — and lost ₹15,564.** Nothing in §8.3.3, §8.6, §8.7, §8.10 or §8.11 forbade it. Note `c/W ≈ the short strike's delta` — this is a model-free Greek that no vendor can break. |
| ★ **Stop reachability** | `k × credit < width` | **New.** Above `c/W = 1/k` the premium stop sits *beyond* max loss: it can never trigger, and you hold a position you believe is stopped all the way to the wing. §8.6.2's claim that "your stop-loss at 1.5–2× credit should always trigger long before the wing does" is true for a wide-wing strangle and **false for any near-ATM vertical.** |
| **Maximum margin deployed** | **₹2,80,000 (40%)** | ⚠️ **Revised down from 60–70% on 02-Sep-2026.** And note what it is *for*: margin is a **backstop, not a sizing input.** It never appears in the lot formula. If margin is what is limiting your size, the two loss caps above have already been breached and you are reading the wrong constraint. |
| **Maximum concurrent structures** | **ONE per calendar day** | ⚠️ **Revised down from 3 on 02-Sep-2026.** Three structures is three stops to watch manually in a mobile app during a fast market — and the aggregate cap above is a single ₹10,500, so a second structure cannot be sized without shrinking the first. One trade, watched properly, beats three watched partially. |
| **Maximum correlated exposure** | n/a — one structure | NIFTY and SENSEX are ~0.95 correlated, so "diversifying" across them was always one position at double size. The one-per-day rule makes the question moot. |

### 8.11.3 Sizing table — the two permitted structures, at the two live caps

⛔ **The previous version of this table is DELETED (02-Sep-2026).** It sized eight §8.6 structures at
a retired ₹6,000 per-trade cap and returned 1–7 lots for structures that are now **locked outright**
(§5 of the constants). Worse, it sized every row from the loss *at the stop* only — the same
single-cap error that let 01-Sep's ₹12,546-per-lot structure through. It is not repaired here because
there is nothing in it to repair: seven of its eight rows are un-tradeable.

**Size from the two caps, take the smaller. Width is chosen AFTER the cap, never before.**

```text
  lots_A = floor( 10,500 ÷ ((width − credit) × lot_size) )    ← structural: if the stop never fires
  lots_B = floor(  3,500 ÷ (0.6 × credit × lot_size) )        ← planned stop, k = 1.6
  LOTS   = min(lots_A, lots_B)

  ⛔ LOTS < 2  →  narrow the width and recompute.  Still < 2  →  NO TRADE.
     Do NOT widen the strikes to "afford" more lots. Do NOT use margin as the input.
```

Pre-computed at a typical `c/W ≈ 20%` (from `TRADING_CONSTANTS.md` §4):

| Index | Lot size | Width | **LOTS** | Note |
|---|---|---|---|---|
| NIFTY | 65 | 50 | **4** | ✅ |
| NIFTY | 65 | 100 | **2** | ✅ |
| NIFTY | 65 | 200 | **0** | ⛔ **Banned.** One single lot breaches the ₹10,500 structural cap. This is the exact width sold on 01-Sep-2026. |
| SENSEX | 20 | 100 | **6** | ✅ |
| SENSEX | 20 | 200 | **3** | ✅ |
| BANKNIFTY | 30 | 200 | **2** | ⚠️ Monthly-only, and locked until 30 net-positive NIFTY/SENSEX trades. |

> **Why the 200-wide NIFTY row reads 0 and not 1.** `(200 − 40) × 65 = ₹10,400` — it *just* clears the
> cap arithmetically, and that is precisely the trap. At `c/W = 20%` it survives; at the 3.5% actually
> sold on 01-Sep it is ₹12,546 and does not. A width whose feasibility flips on the credit you happen
> to get filled at is not a width you can commit to before seeing the fill. **One lot is not a safe
> size. One lot is a size like any other, and it must clear the cap with room.**

### 8.11.4 The margin buffer — the rule that prevents forced liquidation

```text
WHY YOU NEVER DEPLOY MORE THAN 70%

  Capital                              ₹6,00,000
  Margin deployed (70%)                ₹4,20,000
  Free margin                          ₹1,80,000

  Adverse move → MTM loss              −₹15,000
  Volatility rises → SPAN re-computes  −₹45,000   ← THIS is the one people forget
  ────────────────────────────────────────────────
  Free margin now                       ₹1,20,000   ✅ still fine

  SAME DAY, at 95% deployment:
  Free margin                            ₹30,000
  Same two events                       −₹60,000
  ────────────────────────────────────────────────
  Free margin now                       −₹30,000   ⛔ SHORTFALL
  → RMS auto-square-off at market, hedges first, worst prices of the day.
    You did not choose this exit. You will not like the fill.
```

**SPAN margin is recomputed intraday and rises when volatility rises.** A position that needed ₹70,000 at 9:30 can need ₹1,05,000 at 1:00 PM on a VIX spike **without you trading at all**. The buffer exists for that, not for new trades.

### 8.11.5 Why the 1%-per-session target was DELETED

> ⛔ **The ~1%-net-per-session target no longer exists.** It has been removed from `CLAUDE.md` and
> replaced by **2–4% per month (₹14,000–28,000)**, measured as a rolling 3-month mean —
> [`TRADING_CONSTANTS.md` §2](../../TRADING_CONSTANTS.md). This section is kept because it is the
> arithmetic that killed it.

```text
1% per session × 21 sessions  =  21% per month  =  ~800% per year compounded.
That number does not exist. If it did, this document would not.
```

And the sizing arithmetic is worse than the compounding arithmetic. The per-trade **planned stop** is
₹3,500 (0.5%). Netting 1% of capital — ₹7,023 — against a ₹3,500 stop means `(k−1) × credit ≤ 3,500`
while `profit ≥ 7,023`, i.e. capturing **200% of the credit**. There is no such trade. The target was
not merely optimistic; it was unreachable by construction, and chasing it is what produced the size
creep on 01-Sep-2026.

**For the first three months the target is a violation count of zero.** P&L is not the metric yet.

**What a disciplined hedged seller on ₹6L actually looks like:**

| Metric | Realistic value |
|---|---|
| Sessions traded per month | 12–16 (you sit out the rest — that is the job) |
| Win rate | 60–70% |
| Average winning session | ₹3,000 – ₹5,000 (0.5 – 0.8%) |
| Average losing session | ₹4,000 – ₹6,000 (0.7 – 1.0%) |
| **Expectancy per traded session** | **≈ ₹1,274 (0.20%)** — the worked figure below |
| **Net monthly return on deployed capital** | **2 – 5%** |
| Worst month you should plan for | **−6 to −8%** |

```text
EXPECTANCY, WORKED
  0.65 × ₹4,200  −  0.35 × ₹4,160  =  ₹2,730 − ₹1,456  =  ₹1,274 per session
  × 14 sessions/month  =  ₹17,836  =  2.97% per month on ₹6L
```

> **Read the win/loss columns again.** The average loss is *larger* than the average win. That is normal and correct for a premium seller — the edge lives in the **frequency**, not the size. This is precisely why the per-trade cap and the daily cap are the load-bearing rules: a single unstopped loss of ₹25,000 erases fourteen good sessions. Your entire year is decided by the losses you refuse to let run, not by the wins you manage to catch.

> See [§8.11.6](#8116-the-feasibility-gate--can-todays-target-be-reached-at-all-added-28-aug-2026) for the arithmetic that decides, **before any analysis**, whether the day's target is reachable at all.

### 8.11.6 The feasibility gate — can today's target be reached *at all*? *(added 28-Aug-2026)*

Run this **at 9:15, before pricing a single structure.** It takes two minutes and on most days it ends the session's work honestly. Three consecutive no-trades (24, 27, 28-Aug-2026) were each diagnosed only after 2+ hours of chain analysis; all three were decidable at the open by the arithmetic below.

#### The credit-ceiling theorem

The per-trade risk cap does not just cap your loss — **it caps your maximum possible credit**, and therefore your maximum possible profit.

```text
With a combined-premium stop at k × credit (§8.10.2):
      loss at stop  =  (k − 1) × credit
Risk cap R therefore bounds the credit you may collect:
      MAX CREDIT     =  R / (k − 1)

To net a profit target T you must capture fraction f of that credit:
      f  =  T / credit  =  T × (k − 1) / R

★ SET T = R  (target 1% of capital, risk cap 1% of capital) :

      REQUIRED CAPTURE  =  (k − 1) × 100%
```

**The stop multiple alone decides whether the target is arithmetically possible.**

| Structure | k (§8.10.2) | Credit capture needed to net 1% | Verdict |
|---|---|---|---|
| Intraday straddle | 1.3 | **30%** | Reachable |
| 0-DTE hedged fly | 1.5 | **50%** | Reachable on expiry day |
| Weekly strangle / monthly condor | **2.0** | **100%** | ⛔ **Only arrives at expiry** |

> A wide stop is not free. Every widening of `k` raises the share of the credit you must harvest to hit the same rupee target. **At k = 2.0 the 1% intraday target is not difficult — it is impossible**, because 100% of the credit only exists at settlement.

#### The DTE overlay — how much can you actually capture in one session?

Theta is not linear in the session; what you can harvest between 9:20 and 2:30 depends almost entirely on **sessions remaining**, not calendar days.

| Trading sessions to expiry | Realistic intraday capture (9:20 → 2:30) | Nets 1% at k=1.5? | at k=2.0? |
|---|---|---|---|
| **0** (expiry day) | 60 – 100% | ✅ | ⚠️ marginal |
| **1** | 35 – 50% | ⚠️ marginal | ❌ |
| **2** | 20 – 30% | ❌ | ❌ |
| **4+** | 10 – 20% | ❌ | ❌ |

*Measured 28-Aug-2026, 2 sessions out: the NIFTY 24,200 straddle decayed 194.10 → 190.20 in two hours — **3.9 points, ~2% of the straddle** — and that already included a vega tailwind (VIX 11.07 → 10.80). Extrapolated to 2:30 it is ~20–25% of an OTM vertical's credit.*

> ⚠️ **Estimate the capture with the structure's DOMINANT Greek — the table above is a THETA table, and theta stops being dominant past ~10 DTE.** §8.10.5 already says an abort condition must match the dominant Greek; the same is true of the P&L estimate that decides whether to trade at all.
>
> **The 28-Aug-2026 self-inflicted error:** I wrote "at 32 DTE the position is vega-dominant" and then estimated the BANKNIFTY 57,900 straddle's intraday P&L **from theta alone** — ₹86/lot. Actual close-to-close: **₹915/lot**, ~7× the estimate, because VIX fell 11.07 → 10.68 and the vega term buried the theta term.
>
> The error is **symmetric and that is the whole point**: had VIX risen 0.39 instead, the straddle would have *expanded* ~30 pts and the position would have **lost ₹915/lot** on a day the index moved −13.65 points. A theta-only estimate on a vega-dominant structure does not merely understate the return — it hides the actual risk driver.
>
> | Sessions to expiry | Dominant Greek | Estimate the session's P&L from |
> |---|---|---|
> | 0 – 2 | **Theta / Gamma** | the DTE table above |
> | 3 – 10 | Theta, with vega material | the table, then **stress ±0.5 VIX** |
> | 10+ | **Vega** | **Δstraddle ≈ straddle × (Δσ / σ)**, theta is the rounding error |
>
> Rule of thumb at 30+ DTE: a **1 VIX point** move on a ~10.5 VIX is ~10% relative, and moves an ATM straddle ~10%. No amount of theta competes with that in one session.

#### ⛔ The uncomfortable conclusion, stated plainly

> **A 1%-of-capital intraday target and a 1%-of-capital per-trade risk cap are compatible on expiry day and almost nowhere else.**
>
> And expiry day is precisely when short gamma is least manageable by hand (§8.6.10, §8.14). **This tension is structural. Do not resolve it by raising size.**

The three ways the target *is* legitimately reached — none of which is "trade bigger":

1. **Trade the expiry-day structure** with a tight stop (k = 1.5), correctly filtered, exited by the §8.3 hard time.
2. **Accept multi-session holds** — a 4-session vertical reaching ~0.9% is a *weekly* return, not a session's. Measure it against the right denominator, and only if the calendar (§8.4.1) and IVP (§8.12.4) permit.
3. **Accept the real expectancy** — §8.11.5's ₹1,274/session. Roughly **0.20%, not 1%.** Sitting out is what makes that number positive.

#### The gate, as a checklist

Run in order. **Any ❌ ends the session — do not proceed to chain analysis.**

```text
□ 1. FETCH the expiry list for all three indexes. Never assume; never guess a date.
□ 2. SESSIONS to nearest expiry — per index, in trading sessions, not calendar days.
        ★ CONVENTION: expiry day = 1 ("0-DTE").  Expiry eve = 2 ("1-DTE").
□ 3. Per index:   sessions = 1  →  ✅ tradeable, full theta.
                  sessions = 2  →  ⚠️ tradeable ONLY on a Gate-5-clean directional view.
                                     Delta-driven, not theta-driven. State the required
                                     move in POINTS.
                  sessions ≥ 3  →  ❌ NO TRADE on this index. Hard stop.
        All three indexes ≥ 3  →  ❌ no trade today. Common (~75% of sessions) and correct.
□ 4. k = 1.6. It is a constant (§8.10.2), not a per-structure lookup.
□ 5. MAX CREDIT = ₹3,500 / (k − 1) = ₹3,500 / 0.6 = ₹5,833  per structure.
        ⚠️ The numerator is the PER-TRADE stop cap, never the ₹10,500 daily cap.
           Using the daily figure here silently authorises a 3× structure.
□ 6. REQUIRED CAPTURE = (k − 1) × 100% = 60% of the credit.
□ 7. If required > realistic
        →  ❌ no size fixes this. Report the ceiling, do not hunt for another structure.
□ 8. Only if all pass  →  price a bear call or bull put spread, side chosen by Gate 5.
```

> ⛔ **Two corrections to the version that stood here.** The old step 3 read `≥ 2 sessions → ❌`, which
> is **off by one** against the counting convention and would have blocked every expiry-eve trade this
> book actually takes. And step 5 read `R = ₹6,000` with `k = 1.5 / 2.0` — a retired cap and a retired
> `k`, producing a MAX CREDIT more than double the live ₹5,833.

#### The trap this closes

When the target is unreachable, the temptation is to solve for lots instead of admitting it. **Always invert the calculation and quote the capital at risk:**

```text
28-Aug-2026 — HISTORICAL. Reproduced at that day's retired ₹6,000 cap and 1% target,
because the arithmetic is the lesson, not the constants. The live caps are §3 of the
constants; the live target is 2–4% per month.

   NIFTY iron fly, 6-pt straddle decay by 2:30 → ₹234/lot net
   lots needed for ₹6,000    =  33
   max loss at 33 lots       =  ₹1,48,005  =  24.7% of capital
   loss at the 1.5× stop     =  ₹1,40,498  =  23.4% of capital      (cap: 1.0%)

Even at a generous 10-pt Friday markdown → 20 lots → 14.9% of capital at risk.
```

> **Reaching 1% that day required risking 14–23% of capital: 14× to 23× the cap.** Quote that number. "It doesn't reach the target" invites negotiation; **"it reaches the target at 23× the risk cap" ends the conversation.**

---

### 8.11.7 The noise-floor test — is your stop inside one candle? *(added 28-Aug-2026)*

§8.11.6 asks whether the target is reachable. This asks the mirror question, and it kills a different
class of trade: **a credit so thin that ordinary noise reaches the stop before the thesis has a chance
to be right or wrong.**

The stop distance on a combined-premium stop is fixed by the credit:

```text
      LOSS AT STOP  =  (k − 1) × credit          ← in POINTS, per lot
```

That number is not a risk parameter you chose. It is whatever the credit happened to be. On a thin
OTM vertical it can be **smaller than a single 30-minute candle in the short leg.**

```text
□ 1.  STOP DISTANCE (pts)  =  (k − 1) × credit
□ 2.  NOISE (pts)          =  the SHORT leg's typical 30-min high−low, today, at this DTE
                             (pull 30-min candles on the leg itself — not on the index)
□ 3.  RATIO = stop distance ÷ noise
         < 1.5×   →  ⛔ the stop is inside the noise. NO TRADE at any size.
         1.5–3×   →  ⚠️ marginal. Widen the spread or move closer to the money for more credit.
         > 3×     →  ✅ the stop can distinguish a thesis failing from a candle printing.
```

**Why widening `k` does not rescue it.** Raising `k` widens the stop *and* raises the required capture
(§8.11.6) one-for-one. You buy survival with the thing you were trying to earn. The only real fixes are
**more credit** (closer strikes, wider width) or **a different day**.

#### The 28-Aug-2026 case that produced this rule

```text
NIFTY 01-Sep bull put 24000/23900 · 2 DTE · entry 11:15 · credit 10.10 pts · k = 2.0
   stop distance = (2.0 − 1) × 10.10  =  10.10 pts     ( = 0.04% of a 24,100 spot )
   24000 PE 30-min range that morning  ≈  ±12 pts
   RATIO = 0.84×   →  ⛔
```

What actually happened: the spread printed **−9.60 at 11:45 — 95% of the stop distance, 30 minutes
after entry** — and then finished the day at **+1.25**. Full drawdown, a coin-flip's chance of being
stopped at the exact low, and no payoff for surviving it.

> **A near-stop-out that ends flat is the worst cell in the matrix.** It is invisible in a win/loss
> column and it is the single best argument for logging **MAE** (§8.15.3, §8.15.4). A trade can be
> "green" and still have been a mistake you got away with.

**Where this bites hardest:** far-OTM verticals at low IV. That is exactly the structure a compressed,
low-VIX tape tempts you into, because it looks safe — the short strike is 100 points away. The strike
being far away is *why* the credit is thin, and the thin credit is what puts the stop inside the noise.
**Distance from the money and distance to the stop move in opposite directions.**

---

## 8.12 The pattern library — recurring setups a seller trades

Fourteen setups that recur often enough to be worth naming. For each: how to recognise it, what to do, and — usually more valuable — what **not** to do.

### 8.12.1 The Monday Gap Fade

| | |
|---|---|
| **Recognise** | NIFTY gaps 0.3–0.8% on Monday on global cues, with **no domestic news**. GIFT Nifty led the gap overnight. First 30 minutes show no follow-through and the gap starts filling. |
| **Trade** | Wait for 9:45. If price has re-entered Friday's range, sell a strangle skewed **against** the gap direction (gap-up → sell calls closer). |
| **Do not** | Fade a gap larger than **1%**, or any gap caused by a domestic event. Those are trend-day openings, not fades. |
| **Kill** | Price makes a new post-open extreme after 10:15. |

### 8.12.2 The Expiry-Day Pin

| | |
|---|---|
| **Recognise** | Expiry morning. Spot within ~0.3% of Max Pain. Large CE and PE OI walls **straddling** price. Inside day relative to yesterday's range. |
| **Trade** | 0-DTE Iron Fly at the pin strike ([§8.6.10](#8610-0-dte-hedged-iron-fly-under-cas--expiry-day-done-properly)), small size, hard 2:30 PM stop. |
| **Do not** | Assume the pin. Max Pain is a weak magnet, and it **moves** as OI shifts intraday. Recompute it at 11:00 and 1:00. |
| **Kill** | Price closes a 15-min candle outside the wall on either side. |

### 8.12.3 The Post-Event IV Crush

| | |
|---|---|
| **Recognise** | Scheduled event tomorrow. ATM IV **2+ vol points above** its 10-day average. India VIX elevated but not spiking. |
| **Trade** | [§8.6.11](#8611-iv-crush-event-harvest--rbi-policy-budget-big-results). Enter in the last 90 minutes of the prior session, exit within 45 minutes of the announcement. |
| **Do not** | Hold past the crush "for the direction". Do not run it on election counting day at any size. |

### 8.12.4 The Friday Premium Bleed *(mostly a trap)*

| | |
|---|---|
| **Recognise** | Friday afternoon, no weekend event, NIFTY at 4 DTE. |
| **Trade** | Sell only if IVP > 50 **and** you would hold the position on a Monday gap of either sign. |
| **Do not** | Sell "for the weekend theta". It is not there — market makers already marked the Friday close down. You are being paid for **gap risk**, not decay. See [§8.8.2](#882-the-weekly-calendar-for-entries). |

### 8.12.5 The Opening-Range Fake-out

| | |
|---|---|
| **Recognise** | Price breaks the first 15-minute range, fails to extend more than ~0.15% beyond it, and re-enters within 15 minutes. |
| **Trade** | The most reliable intraday seller's setup there is. Sell the side that just failed — a failed upside break means sell calls just above the fake high. |
| **Do not** | Take it before the re-entry is complete. A break that holds is [§8.12.9](#8129-the-trend-day-the-anti-pattern), and it is the same picture 15 minutes earlier. |

### 8.12.6 The Range-Compression Squeeze ⛔ *(the anti-setup)*

| | |
|---|---|
| **Recognise** | Bollinger Bands at multi-week narrowest, ATR falling, India VIX at a 3-month low, 4+ sessions of overlapping ranges. |
| **Trade** | **Nothing.** Or a long-vega structure — Double Calendar ([§8.6.12](#8612-double-calendar--batman--and-the-february-2025-margin-trap)) — the only place in §8 where being long vol is the seller's play. |
| **Do not** | Sell **neutral** premium here. It feels like the safest possible market and it is where the expansion starts. Compression resolves into expansion; the only unknown is the direction. **This is the highest-frequency way a seller gets caught.** |

> *This is exactly the state flagged in the 17-Aug-2026 session — IVP ≈ 2%, VIX at a 6-month floor and rising. See `my-treads/August-2026/17-08-2026/17-08-2026-tread.md`.*

#### 8.12.6a The neutral/one-sided distinction — **amendment, 27-Aug-2026**

The "Trade Nothing" verdict above is **about neutral premium selling.** It was written against
straddles, iron flies and condors, and for those it stands unchanged. It is **too broad as stated**,
and applying it to every credit structure costs real trades.

| Structure into compression | What the break does to it | Verdict |
|---|---|---|
| **Neutral** — straddle, iron fly, condor, strangle | Loses **whichever way** the range breaks. Both wings are exposed; you are short the one thing that is about to happen. | ⛔ **Trade Nothing — the original rule holds** |
| **One-sided** — bear call spread, bull put spread, credit vertical | Loses on **one** side only. If it is positioned on the side the market is already leaning, **the break is what pays it.** | ✅ **Permitted**, defined-risk, at the size §8.13 allows |

**The test:** does the structure need the range to *hold*, or only to *not reverse*?
A fly needs a pin. A vertical only needs price not to travel 0.3% the wrong way. Those are different
bets and the compression veto only applies to the first.

> **Sequencing rule that follows from this:** when the §8.5.2 grid names a structure, **price that
> structure first.** Do not test a different one against the day's filters and then declare the day
> dead when it fails — a failed iron fly says nothing about a bear call spread.

**Evidence — 27-Aug-2026 (SENSEX expiry).** IVP 2.5%, VIX at a 6-month floor and rising: textbook
§8.12.6. The grid cell (Slightly Bearish × CHEAP) named *"small bear call spread only."* The §8.6.10
iron fly was tested instead, failed 2 of 4 filters, and the day was called a no-trade at 10:30.

The compression **did** break — exactly as §8.12.6 predicts — and it broke **downward**: SENSEX closed
76,933.59, −0.70%, at the day's low, 192 pts below the 6-session floor. The 77500/77700 bear call
spread **expired worthless.** The veto was right about the expansion and wrong about the harm,
because the structure was on the correct side of it.

*Full accounting: `my-treads/August-2026/27-08-2026/27-08-2026-tread.md` §16:12.*

### 8.12.7 The VIX Spike Fade

| | |
|---|---|
| **Recognise** | India VIX up **> 15% in one or two sessions** on a news shock, then **flattening** — not still rising. Price has stopped making new lows. *(This 15% is a **pattern signature over 1–2 sessions**, deliberately different from the +8% single-day HOSTILE abort in §10 — it describes a shock that has already happened and is decaying, not one arriving. Both can be true; they are measuring different windows.)* |
| **Trade** | The single best-paid seller setup in the book. Wide defined-risk condor or strangle at 5–8 DTE. IVP is high, so widen the strikes and still collect well. |
| **Do not** | Catch it while VIX is still climbing. Wait for **two consecutive sessions of a lower VIX close.** "VIX is high so I'll sell" during the spike is how people meet the 2020 and 2024 gap days. |

### 8.12.8 The OI Wall Bounce

| | |
|---|---|
| **Recognise** | Price approaches a strike with dominant OI **that is still growing**. Writers are defending. |
| **Trade** | Sell just beyond the wall. The wall is a structural, capital-backed level, not a chart line. |
| **Do not** | Trade a wall whose OI is **shrinking** as price approaches. That is writers covering — the wall is being dismantled and the level will not hold. **Watch OI *change*, not OI level.** |

### 8.12.9 The Trend Day (the anti-pattern)

| | |
|---|---|
| **Recognise** | See [§8.13](#813-trend-day-detection--the-sellers-kill-switch) in full. |
| **Trade** | Nothing short-premium. If already in: cut, or convert to a ladder ([§8.6.13](#8613-the-ladder--a-repair-never-an-entry)). |
| **Reality** | Roughly **1 session in 5** is a trend day, and trend days account for **the majority of a seller's annual losses.** Every other pattern here is worth less than reliably avoiding this one. |

### 8.12.10 The Gap-and-Go

| | |
|---|---|
| **Recognise** | Gap > 0.7%, price extends **away** from the gap in the first 30 minutes, no fill attempt, VWAP untouched. |
| **Trade** | Sell only the **far side** — gap-up and going → sell puts well below, leave calls entirely alone. |
| **Do not** | Sell the side the market is running toward, at any distance. |

### 8.12.11 The Afternoon Reversal

| | |
|---|---|
| **Recognise** | A one-directional morning, then a stall between 1:30 and 2:15, then a reversal back through VWAP. |
| **Trade** | If you are short the tested side and it reverses, **do not adjust** — let it come back. This is the situation the 30-minute rule ([§8.9.1](#891-adjustment-1--do-nothing-the-most-under-used)) exists to protect. |
| **Do not** | Enter fresh premium after 2:00 PM ([§8.8.3](#883-the-three-timing-prohibitions)). |

### 8.12.12 The Rollover-Week Drift

| | |
|---|---|
| **Recognise** | Final week of the monthly expiry. Rollover activity dominates; futures basis widens; index tends to drift rather than trend. |
| **Trade** | Favourable for the weekly workhorse strangle. Widen strikes slightly — rollover flow can produce sharp, brief moves with no follow-through. |
| **Do not** | Read the futures basis as a directional signal. During rollover it is mostly mechanics. |

### 8.12.13 The Results-Season Index Dampener

| | |
|---|---|
| **Recognise** | Peak quarterly results season. Individual stock IVs are high; **index IV is comparatively low** because single-stock moves are uncorrelated and partly cancel at the index level. |
| **Trade** | Sell index premium, not stock premium. The dispersion works in your favour: you collect index premium while the component chaos nets out. |
| **Do not** | Sell single-stock options — **physical settlement**, gap risk on results, and far worse liquidity. |

### 8.12.14 The Global-Cue Gap

| | |
|---|---|
| **Recognise** | GIFT Nifty is materially away from the previous NIFTY close at 8:45 AM; the driver is overnight US/Asia action, not domestic. |
| **Trade** | Wait for 9:45. Global-cue gaps fill more often than domestic-news gaps — but only *after* the opening auction imbalance clears. |
| **Do not** | Treat GIFT Nifty as a *prediction*. It is a **price**, not a forecast, and the correlation to the day's close is weak. Its only reliable use is sizing the opening gap. See `Market_View.md`. |

---

## 8.13 Trend-day detection — the seller's kill switch

> If you learn one operational skill from §8, learn this. Every profitable seller is, functionally, someone who is good at not being short premium on trend days.

### 8.13.1 The three primary markers

| # | Marker | Definition | Check at |
|---|---|---|---|
| **1** | **Opening range holds** | Price breaks the first **30-minute** high/low and does **not** re-enter that range within the following 15 minutes. | 9:45, then continuously |
| **2** | **VWAP one-sidedness** | Price has stayed entirely on one side of VWAP for **> 60 minutes**, with no touch. | 10:30, 11:30, 1:30 |
| **3** | **Confirming OI direction** | Price ↓ **and** CE OI ↑ **and** PE OI ↓ (short buildup), or price ↑ **and** PE OI ↑ **and** CE OI ↓ (long buildup). **All three legs of the pattern**, not two. | Every 30 minutes |

```text
                    THE KILL SWITCH

  0 of 3 fired  →  Normal seller's day. Trade the plan.
  1 of 3 fired  →  Caution. Half size on new entries. No fresh naked-side risk.
  2 of 3 fired  →  ⛔ NO NEW PREMIUM SELLING.
                     Existing positions: cut, or convert (§8.6.13).
  3 of 3 fired  →  ⛔ FLATTEN. Take the loss. Close the terminal.
                     This day is not yours. It costs a small loss to leave and
                     a very large one to stay.
```

### 8.13.2 Secondary confirmations

| Signal | Threshold | Meaning |
|---|---|---|
| **India VIX rising with price falling** | VIX **+8%** or more → HOSTILE, exit | Panic bid in options. Your short vega is bleeding while your short gamma is bleeding. *(Was +5%. Aligned to the single §10 threshold — a second, lower number here meant two different "VIX is spiking" rules fired at different moments.)* |
| **Consecutive same-colour 15-min candles** | 5 or more | Textbook trend structure. |
| **Non-overlapping 15-min candles** | 3 in a row with no overlap | Extremely strong trend. Rare and decisive. |
| **ADX on the 15-min chart** | > 25 and rising | Confirms trend strength. Lagging — use as confirmation, not a trigger. |
| **Cumulative advance/decline** | Strongly one-sided and widening | Breadth confirms; the move is the whole market, not two heavyweights. |
| **Price never touches VWAP after 10:00** | — | The cleanest single tell there is. |

### 8.13.3 The three rules around the kill switch

1. **Check at fixed times, not when you feel worried.** 9:45, 10:30, 11:30, 1:30. Set the alarms. A check you perform because you are already anxious is a check you will rationalise your way out of.

   **What to re-pull at every check — OI is not optional** *(added 28-Aug-2026)*

   | Pull | Why |
   |---|---|
   | Spot, day high/low, VWAP | The three kill-switch markers |
   | India VIX + day high | Vol regime drift |
   | ATM straddle | Actual decay vs modelled |
   | **OI *and* `oi_day_high` at your short strikes and the walls** | **The wall you are leaning on may already be dissolving** |

   > ⛔ **The failure this closes (28-Aug-2026).** At 11:00 the NIFTY 24,200 PE wall read 193.1L and was cited as evidence for a pin. By 13:09 it was **110.6L — a 43% unwind — and 193.1L had been the day's high.** The wall was at its peak in the exact minute it was read. Put support migrated from 24,200/24,250 down to 24,000 while the position thesis still described a floor at 24,200. The 11:27 recheck pulled spot, VIX and the straddle but **not OI**, so the one signal that would have flipped the read was in the field not requested.
   >
   > **Compare `oi` against `oi_day_high`, not just against the morning reading.** A number equal to its day high is a *peak*, not a *level*; the same figure means the opposite thing depending on which side of it you are on. This is [§8.7.4](#874-method-4--oi-walls-and-structural-zones)'s "wall being unwound" and [§8.12.8](#8128-the-oi-wall-bounce)'s "watch OI change, not OI level" — both already in this book, both missed in real time because the data was never re-fetched.

   > **A short observation window is not evidence of stability.** At 11:27, 27 minutes with no new high or low was written up as "compression continuing, not resolving." Within 100 minutes both NIFTY and SENSEX had made new lows, VIX a new day high, and the range had gone 0.34% → 0.46%. **Declaring stability ahead of the evidence is the same error as declaring a breakout ahead of the evidence** (27-Aug-2026), and it is the more dangerous one because it argues for inaction while a position bleeds.
2. **The switch is one-directional.** Once 2 of 3 have fired, the day is a trend day **for the rest of the session**, even if price calms down. Trend days often consolidate mid-day before the second leg. Do not re-enter.
3. **Log every trend day.** They cluster — around events, around global-risk episodes, at regime turns. Two trend days in a week means the volatility regime has changed and your entire sizing should drop until it settles.

> **The cost asymmetry, plainly.** Standing down on a day that turns out to be a range day costs you roughly ₹1,274 of expectancy (§8.11.5). Staying short premium on a genuine trend day costs ₹6,000–₹25,000. You need to be wrong about standing down **five to twenty times** before it costs as much as being wrong about staying in **once**. The switch does not need to be accurate. It needs to be *used*.

---

## 8.14 Blow-up autopsy — the six ways sellers die

Every large retail option-selling loss in India fits one of six shapes. Each has exactly one rule that prevents it.

### 8.14.1 Death 1 — The naked short into a gap

```text
The mechanism : Undefined max loss meets an overnight gap.
The history   : 24-Feb-2022 (Ukraine)    NIFTY  −4.8% in one session
                23-Mar-2020 (COVID)      NIFTY  −13.0% in one session
                04-Jun-2024 (election)   NIFTY  closed −5.9%; intraday −8.5%
                                         India VIX had roughly doubled in a week

A naked short strangle 2% OTM, 5 lots, on any of those mornings:
  the "safe" side was breached before you could reach a terminal.
  Loss is not 2× the credit. It is 15–40× the credit, and it is realised
  at whatever price the auto-square-off engine happens to find.
```
> **Rule:** every short leg has a long leg **in the same expiry**. No exceptions, no "just for today", no "it's so far away". This is an automatic blocker under [`option_chain_n_greeks.md` §7](../option_chain_n_greeks.md).

### 8.14.2 Death 2 — Over-sizing because the margin allowed it

The margin engine sizes for the **exchange's** risk. It has no view on your survival. A ₹6L account can be permitted 8 lots of a hedged strangle. Eight lots at the stop is a ₹46,000 loss — **7.7% of the account in one trade.**

> **Rule:** [§8.11.1](#8111-the-formula). Lots = risk cap ÷ loss per lot at your stop. Never margin ÷ margin-per-lot.

### 8.14.3 Death 3 — Averaging in, a.k.a. "rolling for credit"

Works beautifully in a mean-reverting market, which is most of the time. Confidence and size grow together. Then one trending week arrives and the accumulated position is many times the original.

> **Rule:** the martingale test in [§8.9.6](#896-adjustment-6--cut-and-when-rolling-for-credit-becomes-a-martingale). **Never roll if it requires more lots or increases max loss.** Hard cap of two adjustments per trade.

### 8.14.4 Death 4 — The auto-square-off spiral

You are 90% deployed. The market moves; SPAN recomputes upward on the vol spike; free margin goes negative. RMS liquidates — **and it usually liquidates the liquid legs, which are your hedges.** Now you are naked, in a fast market, at market prices, with the margin requirement climbing further. This is a *mechanical* spiral: it does not need the market to keep moving against you.

> **Rule:** deploy a maximum of **70%**. The 30% buffer is for the SPAN re-computation, not for new trades. [§8.11.4](#8114-the-margin-buffer--the-rule-that-prevents-forced-liquidation).

### 8.14.5 Death 5 — Holding into expiry and CAS

Gamma at 0 DTE inside the final hour is effectively unbounded, decay has already been collected, and since 3-Aug-2026 the last 15 minutes are an auction you cannot trade into. Your wings stop being hedges at 3:15 PM.

> **Rule:** one hard flat per index — **NIFTY/BANKNIFTY 2:30 PM · SENSEX 2:15 PM.** Close at any P&L. The old target/absolute pair is deleted: a later fallback deadline is what a losing position reaches for. [`rules_constrints.md`](../rules_n_regulations/rules_constrints.md).

### 8.14.6 Death 6 — Selling into a hostile regime

Selling because "VIX is low and premium decays" while the market is realising *more* than it is implying. Every trade is priced against you from entry; no amount of good management recovers a negative edge.

> **Rule:** the **IV − HV20** filter. Negative → do not sell, at any size, in any structure. [§8.5.1](#851-step-1--classify-volatility-not-just-direction).

### 8.14.7 Honourable mention — the wing you could not exit

You bought a 1,200-point-OTM wing at ₹3 with 400 OI. It satisfied the margin engine and the risk checklist. When you need to close, there is no bid. You cannot exit the structure as a basket; you can only exit the short, which un-hedges you and spikes margin — feeding straight back into Death 4.

> **Rule:** **OI > 25,000 and a live two-sided quote** before buying any wing. [§8.6.14](#8614-the-rolling-wing-bank--margin-efficiency-as-a-strategy).

### 8.14.8 The six rules on one card

```text
  1.  Every short has a long in the SAME EXPIRY.
  2.  Lots = risk cap ÷ loss-per-lot AT THE STOP.
  3.  Max 2 adjustments per trade. Never roll into more size.
  4.  Never deploy more than 70% of capital.
  5.  Flat by 2:30 PM on expiry (NIFTY) / 2:15 PM (SENSEX). Never in CAS.
  6.  IV − HV20 negative  →  do not sell.
```

---

## 8.15 Metrics that actually matter

Most sellers track the wrong three numbers and are surprised by their year.

### 8.15.1 The metrics that count

| Metric | Definition | Target | Why it matters |
|---|---|---|---|
| **ROM** (Return on Margin) | Net P&L ÷ margin blocked ÷ days held | **> 0.30% per day** | The only denominator that reflects what the trade actually cost you. Return-on-premium flatters everything. |
| **Expectancy per traded session** | `(Win% × avg win) − (Loss% × avg loss)` | **≈ ₹1,274 (0.20%)** — see §8.11.5 | ⭐ The one number that predicts your year. **Stated once, here and in §8.11.5, and nowhere else.** The retired "> ₹1,000", "₹1,200" and "₹1,300" variants are all the same estimate rounded differently, and four roundings of one number read as four numbers. |
| **Expectancy per ₹1L margin** | Expectancy ÷ (margin ÷ 100,000) | **> ₹1,500** | Makes structures with different margins comparable. A BWB and a strangle cannot be compared any other way. |
| **MAE** (Max Adverse Excursion) | Worst unrealised loss on trades that finished **profitable** | Stop should sit **1.5× beyond typical MAE** | If your winners routinely dipped to 1.9× credit and your stop is at 2.0×, you are running a stop-hunting machine against yourself. |
| **Slippage as % of credit** | Actual fills vs mid at entry + exit | **< 10%** | Above 15% your strikes are too illiquid or your orders too aggressive. |
| **Adjustments per trade** | Count | **< 1.0** | Above 1.0 diagnoses your **entries**, not your management. |
| **Days in trade** | Calendar days held | 40–50% of DTE at entry | Matches the 50%-target discipline. Longer means you are holding for the worst-paid part of the curve. |
| **Max drawdown / recovery days** | Peak-to-trough and time to new high | **< 8% / < 30 days** | Above this, sizing is wrong regardless of what the P&L says. |

### 8.15.2 Why win rate is a vanity metric

```text
Seller A :  92% win rate.  Avg win ₹1,000.  Avg loss ₹14,000.
            (0.92 × 1,000) − (0.08 × 14,000)  =  920 − 1,120  =  −₹200   ✗ LOSING

Seller B :  61% win rate.  Avg win ₹4,200.  Avg loss ₹4,100.
            (0.61 × 4,200) − (0.39 × 4,100)  =  2,562 − 1,599  =  +₹963  ✓ WINNING
```

Seller A has the better-looking statement, the better-looking screenshot, and a negative edge. **A high win rate is the natural by-product of selling premium; it says nothing about profitability.** Track expectancy.

### 8.15.3 The journal columns

Log these for every trade. Anything less and the metrics above cannot be computed.

```text
Date │ Index │ DTE │ Structure │ Strikes │ Lots │ IVP │ IV−HV20 │ Five-view
     │ Credit │ Margin blocked │ Max loss │ Planned stop │ Planned target
     │ Entry time │ Exit time │ Exit reason (target/stop/time/adjustment/discretion)
     │ Gross P&L │ Charges │ Slippage │ Net P&L │ ROM
     │ MAE │ Adjustments (count + what) │ Trend-day markers at entry
     │ ONE LINE: what I would do differently
```

> **The single most valuable column is `Exit reason`.** Sort a quarter of trades by it. If "discretion" is your most frequent exit, you do not have a system — you have a habit with a spreadsheet. If "stop" trades cluster on days where the trend-day markers had already fired at entry, your problem is entry discipline and no amount of adjustment skill will fix it.

---

### 8.15.4 Scoring the day — mark at the mandated exit, and always report MAE and MFE *(added 28-Aug-2026)*

Applies to trades taken **and** to trades declined. Scoring a no-trade day is how a stand-down rule
earns or loses its keep — but only if the scoring is honest about *when* it marks the book.

#### The rule

> **A mid-session mark is not an outcome. It is one sample from a path.**
>
> Score at the structure's **mandated exit time** (§8.3: NIFTY 2:30 PM · SENSEX 2:15 PM), and report
> **three** numbers, never one:
>
> | | What it answers |
> |---|---|
> | **MAE** — max adverse excursion over the holding window | *Would the stop have fired?* This decides whether the outcome was even reachable. |
> | **Mark at the mandated exit** | *What the trade actually pays under the discipline you trade by.* This is **the** outcome. |
> | **MFE** — max favourable excursion | *How much was left on the table, and was the target ever touchable?* |
>
> Marking at the close is also wrong for an intraday mandate — it credits you with hours you were
> never allowed to hold.

Price both sides honestly: **buy shorts at the ask, sell longs at the bid.** Then subtract the §8.3
cost sheet. A gross point-count is not a score.

#### Why this is a rule and not a preference — 28-Aug-2026

I validated the day's declined structures at **13:09**, which happened to sit inside the worst
90-minute window of the session. Two of three conclusions reversed by the mandated exit:

| Structure (entry 11:15) | MAE | **14:30 — §8.3 exit** | 15:30 close | What I claimed at 13:09 |
|---|---|---|---|---|
| Iron fly 24250 | −7.20 | **−1.45** (scratch) | +5.70 | "losing, −₹675" ❌ |
| Bull put 24000/23900 | **−9.60 = 95% of stop** | −5.00 | +1.25 | "76% to its stop" — understated, and mistimed ❌ |
| Bear call 24250/24450 | — (MFE **+25.90**) | **+19.80** | +4.60 | "+₹1,407/lot" — a peak, not an outcome ❌ |

The bear call, held to the close as the snapshot implied, would have finished a **loss after costs.**
The bull put's decisive fact — 95% of the stop, 30 minutes in — was invisible at 13:09 and only MAE
surfaces it. → §8.11.7.

#### The failure mode this prevents

Marking once, mid-session, at a moment you did not choose in advance, and then reasoning from it.
The mark will confirm whatever the tape is doing at that instant, and you will write the lesson the
noise dictated. **Pick the mark time from the rulebook before you look at the price.**

#### For a no-trade day specifically

```text
□ Re-price EVERY declined candidate at its mandated exit time — including any you rejected in analysis
     and never wrote up. (28-Aug: the best structure of the day was one I never proposed.)
□ Report MAE / exit-mark / MFE for each.
□ Size each at the MAXIMUM the risk cap permits — not one lot, not the lots you imagined.
     The question is "what was the best this book could have done", not "what would one lot have done".
□ State which of the three stand-down reasons the outcome supports: too dangerous · too small ·
     stop inside the noise (§8.11.7). They generalise differently and only one of them was right.
□ If the outcome contradicts the decision, say so plainly. A stand-down that was WRONG is the most
     valuable entry the journal can hold.
```

---

## 8.16 Quick-reference cards

> ⚠️ **These cards were rewritten on 02-Sep-2026.** The previous six quoted a ₹6,000 per-trade cap,
> a ₹9,000 daily cap, a ₹4.2L deploy limit, an `IV − HV20` volatility test, eleven locked structures
> and a two-tier exit clock — **all retired.** Cards are the section most likely to be read at 9:20
> with a chain already open, so a stale card is worse than no card. Every number below is quoted from
> [`TRADING_CONSTANTS.md`](../../TRADING_CONSTANTS.md); if they disagree, that file wins.

### Card 1 — Every morning, before 9:15

```text
□  Five-view classification + HH:MM timestamp  .....................  ______
     ⛔ Older than 60 minutes = stale. Re-pull. Do not derive it inline.
□  Sessions to expiry, all 3 indexes (fetched, never guessed)  .....  __ __ __
     expiry day = 1 · expiry eve = 2 · ⛔ ≥ 3 = NO TRADE on that index
□  India VIX level + change vs previous close  .....................  ______
□  Volatility state (§10 of the constants — VIX only, no IVP, no IV−HV):
     CHEAP < 12  ·  NORMAL 12–16  ·  RICH 16–20  ·  ⛔ HOSTILE ≥ 20 or +8%
□  Forward basis F = K + C − P at 3–4 strikes; agree within 1 pt?  ..  ______
□  GATE 5 INPUTS — all six, written out, FII read first:
     FII  net short CE ____  net short PE ____  net futures ____
     Pro  net short CE ____  net short PE ____  net futures ____
□  Scheduled events today, 9:15–3:30  ..............................  ______
□  Caps: see TRADING_CONSTANTS.md §3. Do not write them here from memory.
□  Structure permitted today: bear call spread OR bull put spread. Nothing else.
```

### Card 2 — The regime cheat sheet

```text
  VIX < 12    CHEAP    →  Credit will be thin. Expect the §8.11.7 noise floor to fail.
  VIX 12–16   NORMAL   →  The working state. Full formula size.
  VIX 16–20   RICH     →  Full formula size. Credit is better; width can stay tight.
  VIX ≥ 20    HOSTILE  →  ⛔ NOTHING. Not one lot.
  VIX +8% intraday     →  ⛔ HOSTILE regardless of level. No new entries. Manage only.

  ⛔ IVP and IV − HV20 are NOT used. Both need an IV series, and no vendor here has
     a trustworthy one (Dhan's CE IV ≠ PE IV at the same strike). VIX is the only
     volatility input that is actually measured rather than derived.
```

### Card 3 — Structure by situation

```text
  There are TWO permitted structures, and the view picks between them:

    Slightly / Strongly BEARISH  →  BEAR CALL SPREAD   (sell CE above, buy CE above that)
    Slightly / Strongly BULLISH  →  BULL PUT SPREAD    (sell PE below, buy PE below that)
    SIDEWAYS                     →  either side, chosen by the Gate 5 participant numbers
                                     — not both, and never as a condor.

  ⛔ Bull Put under ANY bearish view and ⛔ Bear Call under ANY bullish view are
     forbidden with no override — not vol state, not skew, not §8.5.4, not participants.
```

**Everything in §8.6 is LOCKED.** All thirteen worked structures there — iron fly, hedged strangle,
Jade Lizard, BWB, unbalanced condor, 0-DTE fly, IV-crush harvest, double calendar, ladder, wing bank —
are **not executable** under `TRADING_CONSTANTS.md` §5. Each is either 4-legged, undefined-risk, or
exceeds the ₹10,500 structural cap at one lot. They stay in the book as reference. The 4-leg family
unlocks after **30 clean two-leg verticals**; see §11 of the constants for the key.

### Card 4 — The intraday clock

```text
  9:15–9:30   ⛔ Widest spreads, and the opening bar is excluded from the noise floor.
  9:30–11:15  ✅ THE ENTRY WINDOW. The only one. Outside it, there is no entry.
  fill+90s    🔒 RESTING SL-LIMIT on the SHORT LEG must be live. Record the order ID.
  fill+30min  🔍 FIRST CHECK — off the FILL time, not off a clock hour.
  every 30min 🔍 …and every 30 minutes after that, without exception.
 12:30        🔍 MIDDAY GATE.
  2:15        🚪 SENSEX HARD FLAT.        ← one time per index, no "target/hard" tier
  2:30        🚪 NIFTY / BANKNIFTY HARD FLAT.
  3:15–3:30   ☠️  CAS. Be flat well before this — it is not the deadline, it is the disaster.
```

### Card 5 — In-trade decision card

```text
  EXIT — any one of these, immediately:
    → Spread at k × credit (k = 1.6)      →  the resting SL should already have done this.
                                             If it has not, exit at market and audit why.
    → +50% of credit captured             →  CLOSE. Take it.
    → Hard flat time reached              →  CLOSE, at any P&L.
    → 3 of 3 kill-switch markers          →  CLOSE at market.
    → Short strike touched by spot        →  CLOSE.

  ⛔ Do NOT move the stop to breakeven at +50%. Do NOT trail. Do NOT scale out.
     Each is one more manual decision under P&L pressure in a mobile app, and the
     documented failure mode here is freezing on exactly one such decision.
     Trailing and scale-out unlock after 20 clean trades. Until then: stop, or target, or time.

  ⛔ NO order may ever increase short exposure in a losing structure — any hour, any day.
  ⛔ On expiry day §8.9 is CLOSED. The only two actions are HOLD and EXIT.
```

### Card 6 — Exit-in-a-hurry card

```text
  1.  CANCEL THE RESTING SL-LIMIT FIRST.  Otherwise it fires against the flat
      position later and re-opens a naked short you are no longer watching.
  2.  BUY BACK THE SHORT LEG.  Always first.
  3.  SELL THE LONG LEG.  Always second. Never the other way round.
  4.  Limit orders a few points through the mid — never market, never SL-M.
  5.  Budget 2.0 pts/leg of slippage on a stop exit (01-Sep-2026 observed 23.85 pts
      total). If the fill is worse than that, say so in the log; do not round it away.
```

---

## 8.17 Sources for Section 8

**Regulatory (primary — always verify against the live circular, not a summary):**

| Source | What to check |
|---|---|
| **SEBI circulars** — [sebi.gov.in](https://www.sebi.gov.in) → Legal → Circulars | The 1-Oct-2024 derivatives framework (single weekly expiry, ₹15L contract value, upfront premium, STT change, expiry-day ELM); the 1-Feb-2025 removal of same-day calendar-spread margin benefit. |
| **NSE circulars & contract master** — [nseindia.com](https://www.nseindia.com) | **Current lot sizes** (revised whenever the index re-rates against the ₹15L rule), expiry calendar, holiday-shifted expiries, freeze quantities, execution ranges. |
| **BSE circulars** — [bseindia.com](https://www.bseindia.com) | SENSEX contract specs, Thursday expiry calendar, BFO lot size. |
| **Exchange CAS documentation** | Closing Auction Session mechanics, IEP determination, the randomised 3:28–3:30 close. Cross-referenced in [`rules_constrints.md`](../rules_n_regulations/rules_constrints.md). |

> ⚠️ **Lot sizes and margin rules in this document will go stale.** Re-verify the contract master **before every trading week**. The figures used throughout §8 (NIFTY 65, BANKNIFTY 30, SENSEX 20) are dated **4-Aug-2026** — see [§8.0.3](#803-reconciliation--which-numbers-in-this-repo-supersede-which).

**Data and tooling:**

| Source | Use |
|---|---|
| **NSE participant-wise OI** (daily, ~7:30 PM) | FII/DII/Pro/Client positioning. Tracked in `my-treads/fii_dii_data_2026.md`. |
| **NSE India VIX historical** | IVP / IV-Rank computation. Kite `get_historical_data` on token `264969` works for this. |
| **Sensibull** | Strategy payoff visualisation, IV/IVP, pre-built structures. |
| **Broker SPAN / basket margin calculators** | The **only** acceptable source for a margin figure. Never scale a remembered number. |
| **Dhan option chain** | Pre-calculated IV and Greeks per strike — the intended source for every delta reference in §8. *(Currently entitlement-blocked; see [`docs/mcp-usage-log.md`](../../docs/mcp-usage-log.md).)* |

**Practitioner material — read critically:**

| Source | Value | Caveat |
|---|---|---|
| **Zerodha Varsity**, Modules 5 & 6 | The best free options education in India. Greeks and strategy mechanics. | Pre-dates the 2024–2026 regime. Lot sizes, margins and expiry structure in it are stale. |
| **tastytrade research** (Sosnoff / Battista) | The empirical backbone of 45-DTE entry, the 50%-profit target and managing at 21 DTE. The 50% rule in [§8.6.9](#869-positional-2540-dte-iron-condor--the-compounding-engine) comes from here. | US market: SPX/SPY, different tax, no STT, far cheaper commissions, no CAS, no physical settlement on equities. **Adapt the principle; never the numbers.** |
| **Option Alpha / Project Option** backtests | Delta-band and management-rule studies. | US indices. Directionally useful, numerically not transferable. |
| **Indian systematic-selling communities** (Twitter/X — see [§2](#2-twitter-profiles-to-follow)) | Live regime commentary, real fills, real slippage. Genuinely the best source for what is currently *tradeable*. | Survivorship bias is severe. Nobody posts the blow-up. Assume every published return is the best account of many. |

**Internal cross-references:**

- [`option_chain_n_greeks.md`](../option_chain_n_greeks.md) — Greeks, chain columns, safe-trade filter (§5), Pre-Trade Go/No-Go (§7)
- [`Market_View.md`](../Market_View.md) — nine data points, five-view classification, FII/DII scenarios
- [`open_interest.md`](../open_interest.md) — Price vs OI matrix
- [`rules_n_regulations/rules_constrints.md`](../rules_n_regulations/rules_constrints.md) — CAS, SEBI constraints, time stops
- [`pro_option_seller_playbook.md`](./pro_option_seller_playbook.md) — the ₹20L capital plan (specs superseded per §8.0.3)
- [`docs/mcp-usage-log.md`](../../docs/mcp-usage-log.md) — which broker feed actually serves which data point

---

> **Closing note for §8.** Nothing above is an edge on its own. The structures are public, the Greeks are public, and the regime grid is just organised common sense. The edge is entirely in the parts nobody enjoys: standing down on trend days, sizing from the stop, taking 50% instead of 90%, capping adjustments at two, and being flat before CAS. A mediocre structure run with these disciplines compounds. The best structure in this document, run without them, is a slow way to fund somebody else's account.

---