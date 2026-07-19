# Kite MCP (Zerodha) — Usage Guide

**Source:** [zerodha.com/z-connect/featured/connect-your-zerodha-account-to-ai-assistants-with-kite-mcp](https://zerodha.com/z-connect/featured/connect-your-zerodha-account-to-ai-assistants-with-kite-mcp)

Kite MCP connects your Zerodha account to Claude. Unlike Kotak Neo MCP, **Kite MCP supports order placement** — use with caution and always confirm before executing.

> ⚠️ **Safety rule:** Never let AI place an order without your explicit approval. Treat every order suggestion as a draft — you are the final executor.

---

## Capability Map (22 Tools)

```
Kite MCP
│
├── 📡 Market Data
│   ├── get_quotes        — real-time quotes (multiple instruments)
│   ├── get_ltp           — last traded price
│   ├── get_ohlc          — OHLC for any instrument
│   ├── get_historical_data — historical OHLC candles
│   └── search_instruments — find instrument tokens by name
│
├── 💰 Account
│   ├── get_profile       — user profile info
│   └── get_margins       — available margin, used margin
│
├── 📊 Portfolio
│   ├── get_holdings      — long-term equity holdings with P&L
│   ├── get_positions     — intraday + F&O open positions
│   └── get_mf_holdings   — mutual fund holdings
│
├── 📋 Orders & Trades
│   ├── get_orders        — today's full order book
│   ├── get_trades        — today's executed trades
│   ├── get_order_history — execution history for one order
│   └── get_order_trades  — trades under a specific order
│
├── ⚡ Order Execution (USE WITH CAUTION)
│   ├── place_order       — place new equity/F&O order
│   ├── modify_order      — change price/qty of pending order
│   └── cancel_order      — cancel a pending order
│
└── 🔔 GTT (Good Till Triggered)
    ├── get_gtts          — list all GTT orders
    ├── place_gtt_order   — create a GTT trigger
    ├── modify_gtt_order  — edit existing GTT
    └── delete_gtt_order  — remove a GTT
```

---

## Example Queries

### Market Data
```
"Get live quote for NIFTY 24500 CE expiring this Thursday"
"What is RELIANCE trading at right now?"
"Show me historical daily candles for BANKNIFTY last 5 days"
"Search instrument token for INFY"
```

### Account & Portfolio
```
"Show my Zerodha available margin"
"What are my holdings and their P&L?"
"Show my open F&O positions"
"What mutual funds do I hold?"
```

### Orders & Trades
```
"Show today's order book on Zerodha"
"Were any orders rejected today?"
"Show me today's executed trades"
"Get history for order ID 12345"
```

### GTT Orders
```
"Show all my GTT orders"
"Place a GTT on HDFC Bank — buy 10 shares if it falls to 1600"
"Delete my GTT on RELIANCE"
```

### Order Placement (confirm before executing)
```
"Place a MARKET BUY for 1 lot NIFTY 24500 CE" ← AI drafts, YOU confirm
"Modify my pending order 123 to price 85"      ← AI drafts, YOU confirm
"Cancel order 456"                             ← AI drafts, YOU confirm
```

---

## Power User Workflows

### Pre-Market Setup
```
1. "Show my Zerodha margin"
2. "Show open positions from yesterday"
3. "Get OHLC for NIFTY and BANKNIFTY"
4. "Search instrument for [target strike]"
```

### Live Trade Assist
```
1. "Get live quote for [strike] CE and PE"
2. "How much margin to buy 1 lot of [instrument]?"
3. "Draft a LIMIT BUY order for [instrument] at [price]" → review → confirm
```

### GTT-Based Risk Management
```
1. "Show all my GTT orders"
2. "Place a GTT stop-loss on [holding] at [price]"
```

---

## Kite MCP vs Kotak Neo MCP

| Feature | Kite MCP (Zerodha) | Kotak Neo MCP |
|---------|-------------------|---------------|
| Holdings | ✅ | ✅ |
| Positions | ✅ | ✅ |
| Funds/Margin | ✅ | ✅ |
| Live Quotes | ✅ | ✅ |
| Historical Data | ✅ | ❌ |
| Mutual Funds | ✅ | ❌ |
| Research Reports | ❌ | ✅ |
| Order Placement | ✅ ⚠️ | ❌ |
| GTT Orders | ✅ | ❌ |
| Margin Calculator | ✅ | ✅ |

---

## Login Flow

Kite MCP uses Zerodha's standard Kite Connect auth (2FA). No credentials pass through Claude.

```
1. Ask Claude: "Login to Zerodha" or "Show my holdings"
2. Claude generates an auth link → click it
3. Login with Zerodha credentials + TOTP on Zerodha's site
4. Redirected back → session active for the day
```

Session is valid for the trading day. Re-login required next session.

---

## Config (.mcp.json)

Already added to project `.mcp.json`:

```json
"kite": {
  "command": "npx",
  "args": ["-y", "mcp-remote", "https://mcp.kite.trade/mcp"],
  "env": {
    "npm_config_registry": "https://registry.npmjs.org"
  }
}
```

Restart Claude Code to pick up the new server.

---

*Disclaimer: AI suggestions are decision-support only. Always confirm orders before execution. [Zerodha T&C](https://zerodha.com/terms-conditions/) apply.*
