# Kotak Neo MCP Setup

Connects Codex to Kotak Neo broker via MCP, enabling live fund/position/order queries from chat.

## `.codex/config.toml` (project-level)

Create `.codex/config.toml` in the project root:

```toml
[mcp_servers.kotak-neo]
command = "npx"
args = ["-y", "mcp-remote", "https://neo.kotaksecurities.com/mcp-server/mcp"]
env = { npm_config_registry = "https://registry.npmjs.org" }
```

> The `npm_config_registry` override is required if your npm is configured to use a private registry (e.g. JFrog Artifactory) — `mcp-remote` won't resolve from there.

## Login Flow (per session)

Each Codex session requires a fresh login:

1. Ask Codex to login with your **UCC** (5-char account code from Kotak Neo app → Profile)
2. Click the login link Codex returns
3. In Kotak Neo mobile app → **Profile → Web Login → Scan QR**
4. Type `DONE` in chat — Codex validates the session

Session tokens are ephemeral; repeat this on every new Codex session.

## What You Can Query

- Fund balance / available margin
- Holdings (with P&L)
- Open positions
- Order book & trade book (today only)
- Stock quotes
- Research recommendations
- Margin calculator

## Limitations

- Trade book only shows **today's** trades — for historical P&L use **Kotak Neo App → Reports → Contract Notes**
- No order placement via MCP (by design — human approval step required per AI copilot safety rules)
