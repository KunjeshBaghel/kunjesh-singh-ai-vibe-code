# Rules, Regulations & Market Structure Constraints
## NSE / BSE Indian Options Market

---

## Index

- [1. CAS — Closing Auction Session](#1-cas--closing-auction-session)
  - [1.1 What is CAS](#11-what-is-cas)
  - [1.2 Global Context — Singapore, London, and India](#12-global-context--singapore-london-and-india)
  - [1.3 How CAS Works — The Timeline](#13-how-cas-works--the-timeline)
  - [1.4 The Core Problem: A Blind Expiry](#14-the-core-problem-a-blind-expiry)
  - [1.5 What Actually Happened on 6 Aug 2026 — Real Example](#15-what-actually-happened-on-6-aug-2026--real-example)
  - [1.6 The 5 Specific Impacts on Option Sellers](#16-the-5-specific-impacts-on-option-sellers)
  - [1.7 Auction Risk — The New Premium That Kills Theta](#17-auction-risk--the-new-premium-that-kills-theta)
  - [1.8 The Manipulation Risk the Article Flags](#18-the-manipulation-risk-the-article-flags)
  - [1.9 How to Profit — Adapting Your Strategy to CAS](#19-how-to-profit--adapting-your-strategy-to-cas)
  - [1.10 Hard Rules for Option Sellers Under CAS](#110-hard-rules-for-option-sellers-under-cas)
  - [1.11 What SEBI / Exchanges Need to Change](#111-what-sebi--exchanges-need-to-change)
  - [1.12 Summary — One-Page Reference](#112-summary--one-page-reference)

---

## 1. CAS — Closing Auction Session

> **Sources used:**
> - @AshishGupta325 article (6 Aug 2026) — "A Transparent Close but a Blind Expiry"
> - Zerodha Z-Connect official blog — "Everything you need to know about Closing Auction Session (CAS)" (Jul 10, 2026)
> - Saurabh WD expert comment (6 Aug 2026, WhatsApp)
> - Zerodha community comments from retail traders on Day 1 of CAS (3 Aug 2026)

### 1.1 What is CAS

**CAS (Closing Auction Session)** is a mechanism introduced on Indian exchanges (NSE/BSE) that replaces the old closing price calculation method for equities.

**Old method (pre-CAS):**
The official closing price of a stock or index was the **Volume Weighted Average Price (VWAP) of the last 30 minutes** of continuous trading (2:45–3:15 PM). This meant a handful of large trades in the final seconds of the session could distort the official close.

**New method (CAS):**
After continuous trading ends at 3:15 PM, a dedicated **auction window runs from ~3:15 to 3:28–3:30 PM**. Buyers and sellers submit orders, and the exchange calculates an **Indicative Equilibrium Price (IEP)** — the price at which the maximum quantity can be traded. When the auction closes (randomly between 3:28–3:30 PM), the IEP at that moment becomes the official closing price.

**The intent:** Better price discovery. Concentrate end-of-day liquidity into a single event rather than letting isolated late trades set the close. Institutional investors and index funds can rebalance at the close without moving the market.

**The unintended consequence:** Index options continue trading during the auction. But the underlying index is no longer observable as a continuously traded instrument — only as an IEP that changes with every order placed or cancelled.

---

### 1.2 Global Context — Singapore, London, and India

| Market | Has Closing Auction | Has Weekly Options Expiry During Auction | Problem? |
|--------|--------------------|-----------------------------------------|---------|
| London Stock Exchange | ✅ Since decades | ❌ No weekly options expire during auction | None |
| Singapore Exchange (SGX) | ✅ | ❌ No weekly options expire during auction | None |
| NSE / BSE India | ✅ Adopted recently | ✅ Weekly NIFTY (Tue) + SENSEX (Thu) expire during auction | **YES — critical problem** |

**Saurabh's insight (6 Aug 2026):**
> "It's implemented in other developed world — that's true. But without option expiry. That's the whole truth."

This is the core structural problem. In London and Singapore, the closing auction is clean because **options do not expire during the auction window**. India copied the auction mechanism but did not move option expiry outside the auction. The two systems are colliding every single expiry day.

India runs **one of the world's most active weekly index options markets** with a derivatives-to-cash turnover ratio of approximately **355:1** (F&O ₹500.6 trillion/day vs cash ₹1.41 trillion/day in June 2026). A mechanism built for equity investors is directly affecting a market that dwarfs the equity market by 355 times.

---

### 1.3 How CAS Works — The Timeline

```
2:45 PM – 3:15 PM  : Continuous trading (normal)
                     Options traders have a live, continuously updated underlying.
                     Delta, gamma, and theta all behave as expected.

3:00 PM            : ⚠️ PRO SELLERS: TARGET EXIT BEFORE THIS TIME on expiry day

3:15 PM            : Continuous trading ENDS for CAS-eligible constituent stocks
                     Options keep trading.
                     Underlying: STALE (last continuous price, no new trades)

3:15 – 3:20 PM     : DEAD ZONE — "The 5-minute vacuum"
                     No orders accepted in constituent stocks.
                     Futures/options continue trading.
                     No hedgeable underlying exists.
                     Correct delta, stop-loss levels: UNKNOWN.

3:20 – 3:25 PM     : Auction order entry opens
                     Both MARKET and LIMIT orders accepted.
                     IEP begins calculating and updating.
                     Options reprice against the changing IEP.
                     IEP can swing hundreds of points as large orders enter.

3:25 – 3:28/3:30 PM : FINAL AUCTION PHASE
                     NO new market orders accepted.
                     Limit orders CAN STILL be entered, modified, or CANCELLED.
                     IEP keeps changing.
                     Options keep repricing against the IEP.
                     IEP is NOT an executed price — it is an estimate.

3:28 – 3:30 PM     : RANDOM CLOSURE (time is not fixed — this is intentional)
                     Auction closes at a randomly selected second.
                     IEP at that moment = official closing price = settlement price.

3:30 – 3:40 PM     : Non-expiring futures/options continue trading until 3:40 PM
```

**The critical flaw for option sellers:**
Between 3:15 and 3:30 PM, you have an option with 15 minutes left to expiry. But the price of the underlying it settles against is:
- Not observable as a continuous trade
- Not executable at the IEP shown
- Subject to change by orders that may be cancelled
- Published with variable latency across brokers

---

### 1.3A Official CAS Specs — From Zerodha / SEBI (Verified)

**Implementation date:** August 3, 2026 (per SEBI directive)

**Which stocks are included:**
- **Phase I, Category I (CAS-eligible):** All stocks with active F&O contracts on NSE and BSE
- **Category II:** All other stocks — trade normally until 3:30 PM (no change)
- **Excluded entirely:** ETFs, commodity segment

**New trading hours under CAS:**

| Segment | Continuous Trading Ends | Notes |
|---------|------------------------|-------|
| F&O-listed stocks | 3:15 PM | Then enter CAS |
| All other stocks | 3:30 PM | No change |
| Index & stock F&O contracts | 3:40 PM | No CAS for derivatives themselves |

**Official CAS timeline (confirmed by Zerodha):**

| Session | What Happens | Time |
|---------|-------------|------|
| Transition | Reference price calculated; CTS ends | 3:15–3:20 PM |
| Order entry open | Limit AND market orders accepted | 3:20–3:25 PM |
| Final auction | Limit orders only; random close | 3:25–3:28/3:30 PM |
| Order matching | Matched at equilibrium price | 3:30–3:35 PM |

**Reference price:** VWAP of trades between 3:00–3:15 PM. CAS price band: **±3% of this reference price.** Stop-loss orders and orders outside the band are NOT carried forward into CAS.

**Equilibrium price determination:** Price at which the highest volume of shares can be executed. All matched trades clear at a **single price** — this becomes the official closing price.

**How settlement changes:**
- Old method: Closing price = VWAP of last 30 minutes (2:45–3:15 PM)
- New method: Closing price = CAS equilibrium price (~3:30–3:35 PM)
- For F&O expiry: ITM/OTM status is determined by the CAS closing price, not the 3:15 PM price

**Broker-specific change (Zerodha):**
- Intraday (MIS) auto square-off for CAS stocks: moved to **3:10 PM** (earlier than before)
- Intraday for non-CAS stocks: 3:25 PM
- F&O intraday: 3:26 PM

**Real trader observations from Day 1 (August 3, 2026):**
- DIVISLAB: bid-ask at 3:15 PM was ~₹8,338–8,340 in continuous trading; CAS closing price printed at **₹8,585** — a gap of ₹245 from where continuous trading left off
- NIFTY closed significantly higher on Day 1 than where continuous trading had ended at 3:15 PM
- Zerodha confirmed: during CAS, "the stock's reference and indicative closing price will be shown in the Nudge in the order window" (full market depth integration still in development as of launch)

---

### 1.4 The Core Problem: A Blind Expiry

Options are derivatives — their value is entirely derived from the underlying. Under normal market conditions:

```
Underlying is continuously traded → Option price is continuously observable → Hedge is possible
```

Under CAS from 3:15 PM on expiry day:

```
Underlying is NOT continuously traded → Option price is based on an IEP → IEP can change or be wrong → Hedge is IMPOSSIBLE
```

The article's description is precise: **"A transparent close but a blind expiry."**

The equity investor gets a better, cleaner closing price. The options trader who is still holding positions is trading against an imaginary reference price that may be hundreds of points away from any real transaction.

**What a market maker cannot do during 3:15–3:30 PM:**
- Correctly calculate delta (delta is relative to a live underlying, not an estimate)
- Hedge a short gamma position (cannot buy/sell constituent stocks in continuous market)
- Place stop-losses with any confidence (what price triggers them?)
- Determine margin requirements accurately

---

### 1.5 What Actually Happened on 6 Aug 2026 — Real Example

**Date:** Thursday, 6 August 2026 (SENSEX weekly expiry day)

**Events:**

| Time | What Happened |
|------|--------------|
| 3:25:30 PM | SENSEX IEP showing ~79,365 |
| 3:25:41 PM | SENSEX IEP falls to ~78,941 — **400+ point drop in 11 seconds** |
| 3:20–3:30 PM | SENSEX IEP swings ~1,000 points total across the auction window |
| Final close | SENSEX settles at 78,954 — 170 points above 3:15 PM level |

**Impact on the 79,000 CE (expiring that day):**
- When IEP briefly crossed 79,300 → 79,000 CE repriced from ₹100 to ~₹350 (**3.5× spike**)
- When IEP fell back below 79,000 → 79,000 CE expired **worthless**
- A trader who held a short 79,000 CE saw their position swing from near-maximum profit → sudden large loss → back to maximum profit — all in under 10 minutes
- A trader who stopped out during the 3.5× spike would have bought back at ₹350 and then watched it expire at zero

**The straddle picture:**
- ATM SENSEX straddle opened at ~₹500 that Thursday morning
- Made a high of ~₹700 during the day
- Stayed above ₹500 for most of the session
- Under normal expiry-day theta decay, a range-bound SENSEX should push the straddle toward ₹100–200 by 3:00 PM
- The straddle was elevated because the market was pricing in the **auction uncertainty** (3:15–3:30 risk), not just remaining time to 3:15 PM

---

### 1.6 The 5 Specific Impacts on Option Sellers

#### Impact 1: Stop-loss triggered on a winning trade

A short 79,000 CE is winning at 3:15 PM (SENSEX below 79,000). IEP briefly spikes to 79,300 at 3:26 PM. Broker's risk system marks the option at ₹350 (3.5× the entry credit). Stop-loss triggers. Option expires worthless. The seller was right on direction but got stopped out by a non-executed IEP spike.

**This is the most common damage CAS causes to option sellers.**

#### Impact 2: Margin calls during the auction window

IEP swings can push options into deep ITM territory for minutes. Broker risk engines calculate MTM loss based on current option prices, which are based on the IEP. This can trigger margin calls in real time — forcing additional margin posting or forced position closure — even if the final settlement is well within the original profit zone.

#### Impact 3: Theta no longer decays cleanly on expiry day

Pre-CAS: By 2:30–3:00 PM on expiry day, ATM options were rapidly approaching zero if the market was range-bound. Pure theta extraction.

Post-CAS: The market adds an **auction risk premium** to the option price. Even if SENSEX doesn't move between 10 AM and 3:15 PM, the straddle stays elevated because traders are pricing the 15-minute auction window where anything can happen. This premium does not decay normally.

#### Impact 4: Market makers widen bid-ask spreads near close

Market makers cannot hedge constituent stocks during the auction. To compensate for this unhedgeable risk, they widen quotes drastically in the 3:15–3:30 PM window. Exit prices for option sellers in this window become very expensive (you buy back at a much worse price than the mid-point).

#### Impact 5: The settlement price is less predictable

Pre-CAS: Settlement = VWAP of last 30 minutes of continuous trading. Predictable range.

Post-CAS: Settlement = IEP at a random second between 3:28–3:30 PM, which may differ substantially from the 3:15 PM level. The SENSEX on 6 Aug settled 170 points above its 3:15 PM price. For an Iron Butterfly seller with wings at 500 points, 170 points is fine. But in a volatile session, this gap could easily be 300–400 points.

---

### 1.7 Auction Risk — The New Premium That Kills Theta

Pre-CAS model of expiry-day theta:

```
Option value at 3:00 PM (15 min to settlement):
  Intrinsic value + tiny time value (almost zero if OTM)
  ATM straddle: ~₹100–200 at 3:00 PM (for a normal sideways day)
```

Post-CAS model of expiry-day option value:

```
Option value at 3:00 PM:
  Intrinsic value + time value to 3:15 PM + AUCTION RISK PREMIUM

Auction risk premium = market's estimate of IEP variance × probability
                     = effectively a new, non-decaying volatility component
```

**What this means for option sellers:**

You are no longer selling time value alone on expiry day. You are also selling **auction risk** — the uncertainty of a 1,000-point swing in SENSEX IEP during a 10-minute window where you cannot hedge.

This is not a normal theta trade. This is an unhedgeable binary risk.

**The silver lining:** Because the auction risk premium inflates IV, the credit you collect at the start of the day (9:15–11:00 AM) is **higher than it was pre-CAS**. You can collect more premium early in the day. But you must exit before the auction window to capture that premium without taking the auction risk.

---

### 1.8 The Manipulation Risk the Article Flags

The article describes a legitimate concern (not an allegation about any specific participant):

```
Hypothetical:
  3:15 PM → Participant holds large short call position (profits if SENSEX stays below 79,000)
  3:25 PM → Participant (or related entity) places large buy orders in SENSEX heavyweights
  IEP rises → SENSEX indicative value crosses 79,000 → short calls spike in value
  Participant buys back calls at a loss OR a competitor holding long calls sells at a profit
  3:27 PM → Large buy orders are CANCELLED or modified downward
  IEP falls back → SENSEX settles below 79,000 → calls expire worthless
```

The economic incentive exists because:
- Option notional exposure is 355× the cash market
- Moving a few large stocks' IEP by placing (and cancelling) limit orders can temporarily move the index IEP by hundreds of points
- This temporary move reprices options with much larger notional exposure
- Current surveillance systems check stock-level manipulation, not cross-market (auction order → index IEP → derivative position) manipulation

**For retail option sellers:** You are not doing this. But someone else doing this can stop you out of winning positions during the auction window. This is a structural risk, not a trading risk.

---

### 1.9 How to Profit — Adapting Your Strategy to CAS

CAS creates two distinct effects that can be turned into opportunity if understood correctly:

#### Opportunity 1: Collect the elevated auction-risk premium early

The inflated IV means morning straddles are MORE expensive than they were pre-CAS. An ATM SENSEX straddle that was worth ₹350 in the morning pre-CAS might now be worth ₹450–550 because the market is pricing the entire auction risk for the day.

**Action:** Enter Iron Butterfly / short straddle positions **earlier in the session** (9:45–10:30 AM) and target 50% profit exit **before 2:30 PM** on expiry day.

You are selling the inflated IV early and letting theta + IV contraction do the work — without holding through the auction.

#### Opportunity 2: Adjust expiry-day time stop to 2:45 PM → 3:00 PM hard wall

The old "2:45 PM close on expiry day" rule in the playbook was conservative for pre-CAS markets. Under CAS it becomes a **hard non-negotiable**. Exit even earlier — target 2:30–2:45 PM on SENSEX Thursday and NIFTY Tuesday.

Do not be in any expiring option position after 3:00 PM. The period 3:00–3:15 PM already has reduced liquidity as other traders exit. After 3:15 PM it becomes a completely different market.

#### Opportunity 3: The 50% profit target is now easier to hit before noon

Pre-CAS: On a sideways expiry day, the straddle premium decayed slowly through the morning, reaching 50% of collected value by ~1:00–2:00 PM typically.

Post-CAS: Because the straddle opens inflated (auction risk priced in from 9:15 AM), and then the market figures out the session is quiet, the IV compression happens faster. 50% profit on the collected credit can be hit by 11:00–12:00 PM on calm expiry days.

**Action:** On expiry day, be alert for the 50% exit target arriving earlier than expected. Do not assume you need to hold until 2:00 PM. When 50% is hit, close — do not wait.

#### Opportunity 4: Do NOT run the expiry-day strangle trade after 9:45 AM if CAS is creating IEP volatility

The expiry-day strangle (Strategy 7 in the playbook) works on calm sessions. On days where the session is already volatile (IEP swings visible in SENSEX/NIFTY pre-3:15 PM behaviour), skip the expiry strangle entirely. The auction will amplify that volatility.

**Signal to skip expiry strangle:** If SENSEX or NIFTY moves more than ±0.7% from 9:15 to 10:00 AM, do not initiate the expiry strangle. The day is directional, not range-bound.

---

### 1.10 Hard Rules for Option Sellers Under CAS

**These rules directly update and override the earlier playbook time stops:**

```
PRE-CAS RULE (old):   Exit expiry-day positions by 2:45 PM
POST-CAS RULE (new):  Exit expiry-day positions by 2:30 PM (target) / 3:00 PM (hard deadline)

PRE-CAS RULE (old):   Hold position if IV drops but 50% target not yet hit
POST-CAS RULE (new):  On expiry day, if clock reaches 2:45 PM and 50% not hit → exit anyway

PRE-CAS RULE (old):   Expiry-day strangle can be entered 9:45 AM and run until 2:45 PM
POST-CAS RULE (new):  Expiry-day strangle → target exit by 12:00 PM noon. Hard close 2:30 PM.

PRE-CAS RULE (old):   Stop-loss at 1.5× credit
POST-CAS RULE (new):  On expiry day after 2:45 PM, treat ANY adverse move as stop-loss.
                       After 3:15 PM — DO NOT HAVE ANY EXPIRING OPTIONS POSITION.
```

**Additional new rules specifically for SENSEX Thursday expiry:**
- SENSEX is more vulnerable to CAS distortion than NIFTY (lower liquidity in auction → larger IEP swings per rupee of order)
- SENSEX Iron Butterfly: target exit by **2:15 PM** on Thursday (even more conservative)
- If SENSEX IEP diverges more than 300 points from NIFTY IEP × ratio in the pre-auction window — close all SENSEX positions immediately

**Summary exit times by index under CAS:**

| Index | Normal session exit target | Expiry day exit target | Hard deadline |
|-------|--------------------------|----------------------|---------------|
| NIFTY (Tue expiry) | Whenever 50% profit hit | 50% profit or 2:30 PM | 3:00 PM |
| SENSEX (Thu expiry) | Whenever 50% profit hit | 50% profit or 2:15 PM | 2:45 PM |

---

### 1.11 What SEBI / Exchanges Need to Change

The article proposes 5 solutions. Understanding them matters for traders because these changes, if implemented, would reverse some of the CAS-related rules above.

**Proposed changes (from the article):**

| Change | What it means for traders if implemented |
|--------|------------------------------------------|
| **a) Settle expiring derivatives at 3:15 PM using 3:00–3:15 VWAP** | Removes auction risk entirely. Expiry-day theta decay resumes as pre-CAS. Exit times revert to 2:45 PM rule. |
| **b) Better IEP transparency** | Reduces information asymmetry. Smaller bid-ask spreads in auction window. Less manipulation headroom. |
| **c) Restrict late order cancellations** | Reduces IEP spikes from cancelled orders. Auction becomes more honest price discovery. |
| **d) Auto-extend unstable auctions** | Prevents rapid 400-point swings from becoming final settlement. Fairer settlement. |
| **e) Cross-market surveillance** | Reduces manipulation incentive. Level playing field. |

**Watch for:** SEBI circulars or exchange notices about CAS modifications. If SEBI implements (a) — settling expiring derivatives at 3:15 PM — it reverses the single biggest CAS risk for option sellers. Until that circular arrives, trade as if CAS is permanent in its current form.

---

### 1.12 Summary — One-Page Reference

```
WHAT IS CAS?
  Closing Auction Session — a 3:15–3:30 PM window where equity closing prices
  are determined by auction (not continuous trading). Adopted from global markets
  (London, Singapore) but India added it ON TOP OF active weekly options expiry
  — which global markets don't have. This is the structural mismatch.

THE CORE PROBLEM FOR OPTION SELLERS:
  After 3:15 PM on expiry day, options keep trading.
  But the underlying (SENSEX/NIFTY) is no longer continuously traded.
  Reference price = IEP = an estimate that can swing ±1,000 points
  based on orders that may be cancelled seconds later.
  You CANNOT hedge. You CANNOT trust stop-loss prices. Delta is meaningless.

WHAT CHANGED ON THE GROUND:
  Old expiry day: Theta decays cleanly → straddle melts toward zero by 3 PM
  New expiry day: "Auction risk premium" added from 9:15 AM → straddle stays
                  elevated all day → more credit to collect in the morning
                  → but CANNOT hold through 3:15–3:30 PM

TWO THINGS THAT CHANGED IN YOUR FAVOUR:
  1. Morning premiums are higher (collect more credit at entry)
  2. 50% profit target hit earlier in the day (exit before noon on calm days)

THREE THINGS THAT CHANGED AGAINST YOU:
  1. Holding past 3:00 PM on expiry = gambling on IEP, not trading theta
  2. Stop-losses can trigger on IEP spikes that revert in seconds
  3. Margin calls possible mid-auction even on winning positions

THE UPDATED RULE (supersedes playbook):
  SENSEX (Thu): Hard close all expiring positions by 2:45 PM. Target by 2:15 PM.
  NIFTY (Tue):  Hard close all expiring positions by 3:00 PM. Target by 2:30 PM.
  Expiry strangle: Target exit by noon. Hard close 2:30 PM.
  After 3:15 PM on expiry day: ZERO expiring option positions. No exceptions.

OPPORTUNITY ANGLE:
  CAS inflates IV on expiry morning → enter Iron Butterfly earlier (9:30–10:00 AM)
  → collect the elevated premium → exit when 50% profit hit (often by 11–12 AM)
  → sit out the auction entirely → repeat next week
```

---

*Source: Article by @AshishGupta325 (6 Aug 2026) — "A Transparent Close but a Blind Expiry: When Options Trade Without a Tradable Underlying". Expert comment: Saurabh WD (6 Aug 2026). Research synthesis as of Aug 2026.*

*Update this file when SEBI issues any circular modifying CAS settlement for expiring derivatives.*
