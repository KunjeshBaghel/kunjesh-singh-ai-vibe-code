# Repo map

Where every file lives and what owns what. **Loaded on demand, never at session start** —
`CLAUDE.md` links here rather than carrying the tree.

There is no `README.md`. `CLAUDE.md` is the router; this file is the index.

---

## The six layers

Each layer holds exactly one kind of thing. If content is in the wrong layer, that is the bug.

| Layer | Files | Holds ONLY | Must NEVER hold |
|---|---|---|---|
| **1 · Router** | `CLAUDE.md` | role · precedence · routing table · session invariants true in every context | any number, any procedure, any directory listing, any war story |
| **2 · Constants** | `TRADING_CONSTANTS.md` | every live-decision number: caps, targets, `k`, floors, times, lot sizes, thresholds, locks and their unlock keys | procedure, theory, broker status |
| **3 · Procedure** | `.claude/skills/*/SKILL.md` + `references/*.md` | HOW to execute ONE task, step by step, with the actual tool calls. `SKILL.md` is a router only | numbers (link a TC row), theory |
| **4 · Knowledge** | `kb/**` | WHY — theory, catalogues, background | live limits, procedure, broker status |
| **5 · Environment** | `docs/**` | what works, what is broken, the repo map, session history | rules, numbers |
| **6 · Memory** | `~/.claude/projects/…/memory/` | only cross-session facts NOT derivable from the repo | anything the repo already records |

---

## Tree

```
CLAUDE.md                    Layer 1 — the router. Read every session. Keep it small.
TRADING_CONSTANTS.md         Layer 2 — ★ THE SINGLE SOURCE OF TRUTH for every number.
                             Outranks every other file, including CLAUDE.md.
everyday_prompt.md           Web-prompt templates for Gemini/Claude *web* sessions. Not used here.

.claude/
  settings.json              SessionStart hook: runs `claude mcp list`, warns if kite / kotak-neo /
                             dhan are not Connected. Transport-level only — it does NOT test the
                             data endpoints.
  skills/
    Index-Derivatives-tread/ ★ the trading lifecycle skill — 8 sub-commands, one job each
      SKILL.md               router only: sub-command → which files to load
      references/
        analyse-today.md       pre-session market view + the 5 gates
        find-trade.md          candidate search, pricing, verdict
        followup.md            in-trade monitoring and exit triggers
        session-close.md       post-session write-up and scoring
        size-it.md             the two-cap sizing procedure
        check-expiry.md        expiry lists + the sessions-to-expiry convention
        basis-check.md         Gate 2 forward/basis + the realised-vs-implied rider
        no-trade.md            journalling a stand-down, with the reason codes
        dhan-api.md            shared — Dhan MCP + REST, auth root causes, curl blocks
        brokers.md             shared — 3-broker login and verification
        kill-switch.md         shared — Gate 3 trend-day markers and escalation
        adjustments-are-closed.md  shared — the three permitted actions, A1–A5
    market-view-kb/          /market_view_kb — critical second-opinion reviewer for a day's
      SKILL.md               market_view.md. Never writes without explicit approval.
      references/data_points.md    dimensions the skill must gather
      references/sources.md        trusted sources for those dimensions

.mcp.json                    Kite + Kotak Neo MCP config (stdio via mcp-remote). Dhan is in ~/.claude.json
.broker_creds                ⛔ gitignored. Client IDs / UCC / tokens. NEVER read into chat.
.remember/                   hook-managed conversation history. Grep on request; do not curate.

kb/                          Layer 4 — knowledge
  Market_View.md               9-data-point system · the five views · six FII/DII scenarios
  open_interest.md             OI chart reading + the Price-vs-OI matrix
  option_chain_n_greeks.md     chain columns · Greeks · §7 Pre-Trade Go/No-Go checklist
                               ⚠️ §7 L472/L667/L701 still carry the RETIRED "3+ distinct warnings"
                                  wording. TRADING_CONSTANTS.md's point score overrides it.
  rules_n_regulations/rules_constrints.md   CAS (3:15 PM) + SEBI rules affecting positions
  kb0-market/                  absolute basics: what the market is, reading the order book
  kb1/
    strategy_ref_book.md       ★★ 4,398 lines. §1–§7 = textbook catalogue, stale, never governs a
                               live call. §8 (from L1754) = THE LIVE OPERATING MANUAL; §8.0 is its
                               own validated index — start there, not at the top of the file.
                               ⚠️ ~52 anchors in the §1–§7 index are broken (Devanagari + `|| ||`
                                  decorations change the GitHub slug). Fixing means restructuring
                                  ~50 headings — ask before doing it.
    data_points_connections.md Root Variables → Greeks → Chain → P&L hierarchy
    trading_jargon_acronyms.md every abbreviation: PDH, PDL, PDC, PCR, IV, IVP, CAS…
    treading_tools.md          TradingView, Sensibull, Zerodha Streak
    pro_option_seller_playbook.md  ⚠️ STALE — wrong lot sizes, claims a BANKNIFTY *weekly*
                               (Wednesday) expiry, charges ~8× overstated. TRADING_CONSTANTS.md §13
                               is correct. Do not quote this file for specs.
    qualiy_of_a_good_treader.md    mindset and discipline
  kb2-Candlestick/             candlestick_kb.md · chart_patterns_kb.md (+ images/)
  kb3-indicators/              indicators_kb.md — RSI, MACD, Bollinger, VWAP… (+ images/)
  kb4-Commodity-options-trading/  besics_of_commodity_treading.md — ⚠️ OUT OF MANDATE (SI-7),
                               reference reading only, never a trade source
  books/ · images/             raw source material

docs/                        Layer 5 — environment
  repo-map.md                  ★ this file
  broker-session-startup.md    ★ the per-session login checklist
  mcp-usage-log.md             ★★ OBSERVED reality: §1 verified capability matrix · §2 root causes ·
                               §3 effective architecture · §4 session log · §6 open items
  kite_mcp.md · kotak_neo_mcp.md · kotak_neo_mcp_setup.md · dhan_mcp.md   per-broker capability maps
  superpowers/plans/ · specs/  historical design docs. Background, not active work.

tools/
  fii-dii/fii_dii.py           ★ two NSE archive feeds, no auth. Tracked in git ✅
                               · fao_participant_VOL_DDMMYYYY.csv → the activity tables.
                                 Context only — RETIRED as a Gate 5 input (TC §9).
                               · fao_participant_OI_DDMMYYYY.csv  → the `GATE 5` block:
                                 T-1 vs T-2 change in net CE/PE OI + the forbid verdict.
                                 SOLE source of Gate 5's numbers.
  fii-dii/global_cues.py       overnight global cues. Tracked ✅
  market-snapshot/docs/requirements.md   ⚠️ SPEC ONLY — the fetcher was never built. There is no
                               `fetch.py` and no `src/`. Write `snapshot-HH-MM.json` by hand from
                               MCP output when useful; each run is a new file, never an overwrite.

my-treads/                   the journal — one folder per trading day
  fii_dii_data_2026.md         ★ persistent FII/DII tracker across all 2026 sessions
  July-2026/ · August-2026/ · September-2026/   `DD-MM-YYYY/` folders inside each
  DD-MM-YYYY/                  blank template folder — copy it for a new day
```

---

## Contract specs at a glance

Authoritative copy is `TRADING_CONSTANTS.md` §13 — this row exists only so you know where to look.

| Index | Exchange | Expiry |
|---|---|---|
| NIFTY 50 | NSE | every Tuesday |
| SENSEX | BSE | every Thursday |
| **BANKNIFTY** | NSE | ⚠️ **MONTHLY ONLY** — last Tuesday. No weekly, post-2024 SEBI. |

Monthly = last Tuesday (NSE) / last Thursday (BSE); a holiday shifts expiry to the previous trading day.
All index options are cash-settled. **Always fetch the expiry list — never assume one.**

---

## Keeping the map current

Update **one** place. If you find yourself updating two, one of them is the bug.

| What changed | Update, and only this |
|---|---|
| A number — cap, target, threshold, time, spec | `TRADING_CONSTANTS.md`. Nothing else. |
| An MCP endpoint starts or stops working | `docs/mcp-usage-log.md` §1 + §2 |
| A vendor's data is found **wrong** (not just missing) | `mcp-usage-log.md` §2 root cause + §1 matrix. **Downgrade the ✅ — a populated field is not a verified field.** |
| A trading session happens | append a row to `mcp-usage-log.md` §4 |
| A procedure step changes | the one `references/*.md` that owns that sub-command |
| A new §8 chapter or structure | `strategy_ref_book.md` §8.0's index |
| A file or folder is added, moved, or deleted | this file |
| A sub-command is added or its file list changes | `SKILL.md`'s routing table + this file's tree |
| Capital or execution venue moves | `TRADING_CONSTANTS.md` §1 |

⛔ **Do not mirror a fact into `CLAUDE.md`.** The old maintenance table instructed exactly that, and it
is what produced 56 duplications and 14 live contradictions across the repo.
