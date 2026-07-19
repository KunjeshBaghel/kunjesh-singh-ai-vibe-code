# Kotak Neo MCP — Full Usage Guide

**Source:** [kotakneo.com/platform/kotak-neo-mcp](https://www.kotakneo.com/platform/kotak-neo-mcp/)

MCP is a **read-only** AI layer — no orders can be placed. It's a decision-support copilot, not an executor.

---

## Capability Map

```
Kotak Neo MCP
│
├── 💰 Funds & Margin
│   ├── Available margin
│   ├── Cash balance
│   ├── Margin used
│   └── Margin from shares / collateral
│
├── 📊 Holdings (Long-term)
│   ├── Stock-wise quantity, avg cost, LTP
│   ├── Day P&L and total P&L
│   ├── Sector/allocation breakdown
│   └── Research recommendations on your holdings
│
├── 📈 Positions (Intraday / F&O)
│   ├── Open positions with unrealised P&L
│   ├── Exposure and risk per position
│   └── Net buy/sell quantities
│
├── 📋 Orders
│   ├── Today's order book (pending, executed, rejected)
│   ├── Today's trade book (filled orders with price)
│   └── Order history by order number
│
├── 🔍 Research
│   ├── Kotak's stock recommendations (BUY/ADD/REDUCE/SELL)
│   ├── Target price and expected return
│   └── Contextual match against your holdings
│
├── 📡 Market Quotes
│   ├── Live LTP for any NSE/BSE instrument
│   ├── OHLC and day change %
│   └── Volume data
│
└── 🔧 Margin Calculator
    ├── Required margin for a trade before placing
    └── Supports CNC, MIS, NRML product types
```

---

## Example Queries

### Funds
```
"What is my available margin?"
"How much cash do I have free for trading?"
```

### Holdings & P&L
```
"Show my holdings with today's P&L"
"Which stock is giving me the highest loss?"
"What is my total portfolio value?"
"Show sector-wise allocation of my holdings"
```

### Positions (F&O / Intraday)
```
"Show my open positions"
"What is my unrealised P&L on options today?"
"Which position has the most risk exposure?"
```

### Orders & Trades
```
"Show today's order book"
"Were any of my orders rejected today?"
"Show me executed trades for today"
```

### Research
```
"What does Kotak research say about RELIANCE?"
"Which of my holdings have a BUY recommendation?"
"Show me all stocks with BUY rating from Kotak research"
```

### Market Data
```
"What is the current price of NIFTY 24500 CE?"
"Show me BANKNIFTY quote"
"What is HDFC Bank trading at?"
```

### Margin Check (before trading)
```
"How much margin do I need to buy 1 lot of NIFTY options at 150?"
"Check margin for selling BANKNIFTY 50000 PE CNC"
```

---

## Power User Workflow

### Morning Pre-Market Routine
```
1. "What is my available margin?"
2. "Show my open positions from yesterday"
3. "What does Kotak research say about [stock you're watching]?"
4. "Get quote for NIFTY [strike] CE/PE"
```

### Post-Trade Review
```
1. "Show today's trade book"
2. "What was my realised P&L today?"
3. "Were any orders rejected and why?"
```

### Portfolio Health Check
```
1. "Show holdings with total P&L"
2. "Which stocks have a SELL or REDUCE rating from Kotak?"
3. "What is my sector exposure?"
```

---

## What MCP Cannot Do

| Action | Available? |
|--------|-----------|
| View holdings | ✅ |
| View positions | ✅ |
| View funds/margin | ✅ |
| Live quotes | ✅ |
| Research recommendations | ✅ |
| Margin calculator | ✅ |
| **Place orders** | ❌ |
| **Modify/cancel orders** | ❌ |
| **Historical P&L (past days)** | ❌ (use App → Reports → Contract Notes) |
| **Option chain data** | ❌ |
| **FII/DII data** | ❌ (use NSE website) |

---

## Security Model

- Claude receives **only the data needed** to answer your query
- No credentials, MPIN, OTP, or passwords ever leave Kotak's systems
- Session token is ephemeral — expires when Claude Code session ends
- Every session requires a fresh QR scan login

---

## Session Login (Quick Ref)

```
1. "Login to Kotak Neo" → provide UCC (5-char code)
2. Click login link → scan QR in Kotak Neo app (Profile → Web Login)
3. Type "DONE" → session active
4. Repeat every new Claude Code session
```

---

*Disclaimer: All AI analysis is decision-support only. Verify before acting. [T&C apply](https://www.kotaksecurities.com/disclaimer/terms-and-condition/)*
