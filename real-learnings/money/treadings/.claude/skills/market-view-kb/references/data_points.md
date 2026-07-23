# Complete Data Collection Checklist — market-view-kb

Collect ALL dimensions below. Mark as `null` if unavailable from any source. Never estimate.

---

## DIMENSION 1 — Global Cues (collect pre-market, 7–9 AM IST)

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| GIFT Nifty level | Gap vs prev NIFTY close (in points + %) | NSE / Moneycontrol pre-market |
| GIFT Nifty gap magnitude vs signal | Is actual gap ≤ 50% of GIFT Nifty implied gap? (Filter 1 from option_chain.md) | Cross-check at 9:15 AM open |
| US Dow Jones | Previous close, direction | Investing.com / Moneycontrol |
| US S&P 500 | Previous close, direction | Investing.com / Moneycontrol |
| US Nasdaq | Previous close, direction | Investing.com / Moneycontrol |
| Nikkei 225 | Live Asian session | Investing.com |
| Hang Seng | Live Asian session | Investing.com |
| Shanghai Composite | Live Asian session | Investing.com |
| Brent Crude ($/barrel) | Direction and magnitude | Trading Economics |
| Dollar Index (DXY) | Rising DXY = FII outflow risk for India | Investing.com |
| USD/INR | Rupee strength/weakness | RBI / Investing.com |
| US 10Y Treasury Yield | Rising yield → EM outflows, bearish India | Investing.com |
| Gold price | Risk-off signal (Gold up = risk-off = bearish equity) | Investing.com |

**Interpretation rule:** DXY rising + US yields rising + Crude spiking = triple headwind for India, heavily bearish regardless of GIFT Nifty.

---

## DIMENSION 2 — Price Action & Market Structure

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| NIFTY previous close (PDC) | Absolute level | Kite MCP / NSE |
| NIFTY gain/loss % | Direction | Kite MCP |
| PDH (Previous Day High) | Hard resistance level | Kite historical OHLC |
| PDL (Previous Day Low) | Hard support level | Kite historical OHLC |
| Weekly High | Resistance context | TradingView / Kite |
| Weekly Low | Support context | TradingView / Kite |
| Monthly High / Low | Macro structure | TradingView |
| Nearest round number | 24000 / 24500 / 25000 etc. | Calculate from spot |
| Candle type (prev day) | Bullish / Bearish / Doji / Hammer / Shooting Star | Kite OHLC |
| Opening Range High (ORH) | First 15-min candle high after 9:15 AM | Kite / TradingView 5-min chart |
| Opening Range Low (ORL) | First 15-min candle low after 9:15 AM | Kite / TradingView 5-min chart |
| VWAP (current) | Above VWAP = intraday bullish bias; below = bearish | Kite / TradingView |
| NIFTY vs EMA 20 (daily) | Trending above or below | TradingView |
| NIFTY vs EMA 50 (daily) | Structural support/resistance | TradingView |
| ATR (14-period, daily) | Daily expected range in points | TradingView |

**Key rule (from option_chain.md Filter 2):** Treat PDH and PDL as HARD LINES, not zones. Dip buyers stepped in within 0.20 points of PDL on 21-Jul-2026. Buffer = 0.

---

## DIMENSION 3 — India VIX

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| VIX current level | Below 12 = calm, 12–16 = normal, 16–20 = fear, 20–25 = high fear, >25 = panic | NSE India |
| VIX change % (vs yesterday) | Rising = fear entering | NSE India |
| VIX direction intraday | Rising / Falling / Flat (more important than level) | NSE India live |
| VIX zone classification | Calm / Normal / Moderate Fear / High Fear / Panic | Derived from level |

**Key rule (option_chain.md Filter 3):** Rising VIX even at 13 = adverse for option sellers. Falling VIX even with falling market = Theta Trap.

---

## DIMENSION 4 — FII / DII Cash Market (previous day data)

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| FII net cash (₹ crore) | Buy (+) or Sell (−) | NSE reports / NiftyTrader FII-DII |
| DII net cash (₹ crore) | Buy (+) or Sell (−) | NSE reports / NiftyTrader FII-DII |
| DII absorption | Is DII buy > FII sell? = market may hold despite FII selling | Calculate from above |
| 5-day FII trend | Consistently buying or selling over 5 sessions | NSE historical |
| Delivery % (NIFTY heavyweights) | Breakout on <40% delivery = likely trap | NSE bhavcopy / Moneycontrol |

---

## DIMENSION 5 — FII / DII F&O Participant-wise OI (previous day EOD)

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| FII Index Futures Net Change | Today's new positions (+ = long, − = short) | NSE derivatives reports / NiftyTrader participant OI |
| FII Index Futures Net OI | Cumulative direction | Same |
| FII Index Calls Net Change | Buying calls = bullish; selling calls = bearish | Same |
| FII Index Puts Net Change | Buying puts = bearish; selling puts = bullish | Same |
| FII Stock Futures Net Change | Alignment with index futures? | Same |
| Client (Retail) Index Futures Net Change | Contrarian read | Same |
| Client Index Calls Net Change | Contrarian read | Same |
| Client Index Puts Net Change | Contrarian read | Same |
| Pro Desk Net Change (Calls + Puts) | Alignment with FII? | Same |
| 3-day FII F&O trend | Sustained regime change needs 3+ days | NSE historical |

**Scenario Classification (from kb/Market_View.md §4):**
- Scenario 1: FII long + Client short → Strongly Bullish
- Scenario 2: FII short + Client long → Strongly Bearish
- Scenario 3: FII + Pro aligned → Ultra Bull/Bear
- Scenario 4: Pro sell Calls + FII buy Calls → Potential short squeeze
- Scenario 5: FII quiet + Pro writing both sides → Sideways/Range

**FII Futures Divergence (option_chain.md Filter 5):** If FII Index Futures and BankNifty Futures point opposite directions → treat as mixed / no-signal day.

---

## DIMENSION 6 — Option Chain (PCR, Max Pain, OI Walls)

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| Total Call OI (all strikes) | In crore | NSE option chain / NiftyTrader |
| Total Put OI (all strikes) | In crore | NSE option chain / NiftyTrader |
| PCR (Put-Call Ratio) | Total Put OI ÷ Total Call OI | Calculate from above |
| PCR interpretation | >1.3 = Bullish, 0.9–1.3 = Neutral, <0.7 = Bearish | kb/Market_View.md §7 |
| PCR trend (3 checkpoints) | Pre-market → 11:30 AM → 2:30 PM — rising or falling? | Intraday tracking |
| Max Pain strike | Most relevant in expiry week (Tue/Thu) | NSE / Opstra |
| Days to expiry | <5 days = Max Pain gravitational pull active | Calculate from today's date |
| Highest Call OI strike | Working resistance level | NSE option chain |
| Highest Put OI strike | Working support level | NSE option chain |
| ATM strike | Closest to current spot | Calculate |
| ATM CE LTP | Current premium | NSE option chain / Kite |
| ATM PE LTP | Current premium | NSE option chain / Kite |
| ATM Straddle premium | ATM CE + ATM PE = market's expected daily range | Sum of above two |
| IV at ATM strike | Implied Volatility % | Sensibull / Dhan option chain |
| IVP (IV Percentile) | > 60 = elevated premiums, favorable for sellers | Sensibull |
| OTM Put IV (−1 strike) | Higher than OTM Call IV = downside fear premium | Sensibull |
| OTM Call IV (+1 strike) | Compare with OTM Put IV for skew | Sensibull |
| Volatility Skew | OTM Put IV − OTM Call IV (positive = bearish skew) | Derived |

---

## DIMENSION 7 — Price vs OI Matrix (Futures)

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| NIFTY Futures OI (today) | Absolute OI in contracts | NSE |
| NIFTY Futures OI change | +ve = new positions, −ve = closing | NSE |
| Futures price vs spot | Futures premium = bullish carry; discount = bearish | NSE |
| Price+OI quadrant | Long Buildup / Short Covering / Short Buildup / Long Unwinding | Derive from price change + OI change |
| Fut OI vs Time bar color | Dark Green = Long Buildup, Pink = Short Buildup, Teal = Short Covering, Yellow = Long Unwinding | Sensibull Fut OI vs Time |
| Last 3-day bar colors | Is it consistently one color = conviction trend? | Sensibull |

---

## DIMENSION 8 — Intraday OI Monitoring (Live session)

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| OI Change vs Strike chart | Panic bars (bars down below 0 line) | Sensibull OI Change chart |
| OI vs Strike chart | Tallest CE bar (resistance) and PE bar (support) | Sensibull |
| Squash Effect | Is the resistance tower shrinking live? | Sensibull OI vs Strike |
| Multi Strike OI crossover | Put OI line crossing above Call OI line = bullish momentum | Sensibull Multi Strike OI |
| Intraday PCR slope | Falling = aggressive call writing, structural weakness | Sensibull / NSE option chain |

---

## DIMENSION 9 — Market Breadth & Sector Context

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| NSE Advance/Decline ratio | >1.5 = broad bullish, <0.5 = broad bearish | NSE market stats |
| BANKNIFTY direction | Same as NIFTY = high conviction; opposite = divergence (caution) | Kite quote / NSE |
| HDFC Bank | Supporting or dragging (heaviest weight) | Kite quote |
| Reliance | Supporting or dragging | Kite quote |
| ICICI Bank | Supporting or dragging | Kite quote |
| Infosys | Supporting or dragging (IT sector check) | Kite quote |
| TCS | Supporting or dragging | Kite quote |
| Sector rotation | Which sector driving the move? (IT / Banking / FMCG / Auto) | NSE sector indices |

**Key rule (kb/Market_View.md §1):** If NIFTY looks bullish but BANKNIFTY or heavyweights are weak → treat move as LOW CONVICTION.

---

## DIMENSION 10 — News & Macros (Today-Specific Events)

| Data Point | What to look for | Source |
|-----------|-----------------|--------|
| RBI policy / statement | MPC meeting dates, rate decisions | RBI.org.in |
| SEBI circular | Any regulatory changes affecting F&O | SEBI.gov.in |
| Earnings calendar today | Which heavyweights reporting? | Moneycontrol earnings calendar |
| FOMC / US Fed events | Rate decision dates | Fed calendar |
| Union Budget / state events | Market-moving domestic policy | Economic Times |
| Geopolitical risk | Middle East, Russia-Ukraine, China-Taiwan | Reuters |
| FII F&O ban list | If NIFTY in F&O ban period | NSE |

---

## Expiry Week Special Rules

If today is within 3 trading days of Tuesday (NIFTY expiry) or Thursday (SENSEX expiry):

1. **Max Pain gravity** is stronger — market tends to close near Max Pain strike on expiry day
2. **Theta decay accelerates** — ATM option buyers face ~30% more daily decay
3. **Gamma risk** is highest — ATM options can move violently in last 1 hour
4. **PCR significance** changes — even PCR 1.0 can be neutral (writers balanced on both sides)
5. **Do not use monthly option strikes** to judge weekly sentiment if they differ

Mark whether today is: Pre-Expiry (>5 days) / Near-Expiry (2–4 days) / Expiry Day

---

## Data Completeness Score

Before finalizing the classification, count how many dimensions have real data (not `null`):

- 8–10 dimensions with data = High confidence classification
- 5–7 dimensions = Medium confidence
- < 5 dimensions = Low confidence — say so explicitly in the output

If confidence is Low, do NOT classify. Say: "Insufficient data for a reliable market view today."
