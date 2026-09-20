# Data Sources — Where to Get Each Data Point

Priority order: Broker MCPs → NSE official → Trusted financial sites. Never use Telegram groups, WhatsApp tips, anonymous X accounts, or paid tip services.

---

## Broker MCP Sources (Priority 1 — fastest, most reliable)

| Tool | What it provides |
|------|-----------------|
| **Kite MCP** | Live NIFTY quote, PDH/PDL/PDC via historical OHLC, positions, margin |
| **Kotak Neo MCP** | Research reports, holdings, some FII/DII data |
| **Dhan MCP** (when configured) | Full option chain: all strikes, pre-calculated Delta/Theta/Gamma/Vega, IV, OI, prev OI, bid/ask per strike |

---

## NSE Official Sources (Priority 2 — authoritative, free)

| URL | What it provides |
|-----|-----------------|
| `nseindia.com/option-chain` | NIFTY option chain, PCR, OI per strike |
| `nseindia.com/reports/fii-dii` | FII/DII cash market net buy/sell |
| `nseindia.com/all-reports-derivatives` | Participant-wise OI report (EOD) |
| `nseindia.com/products-services/indices-vix` | India VIX level and chart |
| `nseindia.com/market-data/live-equity-market` | Advance/Decline ratio, market breadth |

---

## Trusted Third-Party Sources (Priority 3)

| Source | URL | Data |
|--------|-----|------|
| NiftyTrader | `niftytrader.in/participant-wise-oi` | Participant OI — visual, color-coded |
| NiftyTrader | `niftytrader.in/fii-dii-data` | FII/DII daily |
| Sensibull | `web.sensibull.com/option-chain` | Option chain + Greeks + IVP |
| Sensibull | `web.sensibull.com/open-interest/oi-vs-strike` | OI walls chart |
| Sensibull | `web.sensibull.com/open-interest/fut-oi-vs-time` | Fut OI vs Time bar colors |
| Sensibull | `web.sensibull.com/fii-dii-data` | FII/DII F&O data |
| Opstra | `opstra.definedge.com` | PCR, Max Pain, IV charts |
| Moneycontrol | `moneycontrol.com/markets/premarket` | Pre-market, global cues |
| Moneycontrol | `moneycontrol.com/markets/fii-dii-data` | FII/DII cash + derivatives |
| Investing.com | `investing.com/indices/us-spx-500` | S&P 500, Nasdaq, Dow |
| Investing.com | `investing.com/currencies/usdx-futures` | Dollar Index (DXY) |
| Trading Economics | `tradingeconomics.com/commodity/crude-oil` | Brent Crude price |
| Trading Economics | `tradingeconomics.com/bonds` | US 10Y Treasury yield |
| Livemint | `livemint.com` | Indian market news, RBI, SEBI |
| Economic Times | `economictimes.indiatimes.com/markets` | Macro events, earnings |
| Reuters | `reuters.com/markets` | Global geopolitical risk |

---

## What NOT to Use

- Telegram market tips channels
- WhatsApp broadcast groups
- Anonymous X/Twitter accounts promising "sure shot" calls
- Paid tip services not registered with SEBI
- Community-built MCPs (security risk — may inject bad data)
