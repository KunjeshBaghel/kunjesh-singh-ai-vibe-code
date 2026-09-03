#!/usr/bin/env python3
"""
FII/DII F&O Participant-wise data — NSE Archive Fetcher

Two feeds, two purposes. No login required; data lands after ~4 PM IST each trading day.

  fao_participant_vol_DDMMYYYY.csv  — Participant wise TRADING VOLUME (contracts traded).
      Drives the activity tables below. Reproduces @Fii_Dii_Data / BluechipAlgos X.com posts.
      *** RETIRED as a Gate 5 input *** — it is flow, not position. See TRADING_CONSTANTS.md s9.

  fao_participant_oi_DDMMYYYY.csv   — Participant wise OPEN INTEREST (positions held).
      Drives the GATE 5 block: the T-1 vs T-2 CHANGE in net CE/PE OI, and the forbid verdict.
      This is the only Gate 5 input.

Usage:
  python3 fii_dii.py                  # uses yesterday (T-1)
  python3 fii_dii.py 2026-09-01       # specific date
  python3 fii_dii.py 2026-09-01 5     # specific date + last N days for 5-day table
"""

import sys
import csv
import io
import urllib.request
from datetime import date, timedelta

BASE_URL = "https://archives.nseindia.com/content/nsccl/fao_participant_vol_{}.csv"
PARTICIPANTS = ["FII", "Client", "Pro", "DII"]

# Column indices in NSE CSV (0-indexed after header)
# Client Type | Fut Idx L | Fut Idx S | Fut Stk L | Fut Stk S |
# Opt Idx Call L | Opt Idx Put L | Opt Idx Call S | Opt Idx Put S |
# Opt Stk Call L | Opt Stk Put L | Opt Stk Call S | Opt Stk Put S |
# Total L | Total S
COL = {
    "fut_idx_l": 1, "fut_idx_s": 2,
    "call_l": 5, "put_l": 6, "call_s": 7, "put_s": 8,
}


def fetch_csv(trading_date: date) -> dict | None:
    url = BASE_URL.format(trading_date.strftime("%d%m%Y"))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            raw = r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

    rows = {}
    reader = csv.reader(io.StringIO(raw))
    for i, row in enumerate(reader):
        if i < 2 or not row or row[0].strip() in ("", "TOTAL"):
            continue
        name = row[0].strip().upper()
        if name == "CLIENT":
            name = "Client"
        elif name == "FII":
            name = "FII"
        elif name == "PRO":
            name = "Pro"
        elif name == "DII":
            name = "DII"
        else:
            continue
        try:
            vals = [int(v.replace(",", "").strip()) for v in row[1:]]
        except ValueError:
            continue
        rows[name] = vals
    return rows if rows else None


def net(row, col_l, col_s):
    return row[col_l - 1] - row[col_s - 1]


def trend(value: int) -> str:
    return "Bullish" if value >= 0 else "Bearish"


def fmt(n: int) -> str:
    sign = "+" if n >= 0 else "-"
    return f"{sign}{abs(n):,}"


def last_n_trading_days(anchor: date, n: int) -> list[date]:
    days = []
    d = anchor
    while len(days) < n:
        data = fetch_csv(d)
        if data:
            days.append(d)
        d -= timedelta(days=1)
        if (anchor - d).days > 30:
            break
    return days


# ---------------------------------------------------------------------------
# Gate 5 — the ONLY block that may drive a structure decision.
#
# Reads fao_participant_OI_*.csv (positions), NOT the _vol_ file above, and
# reports the day-over-day CHANGE. See TRADING_CONSTANTS.md section 9 for why
# the volume file was retired and how these thresholds were calibrated.
# ---------------------------------------------------------------------------

OI_URL = "https://archives.nseindia.com/content/nsccl/fao_participant_oi_{}.csv"
GATE5_THRESHOLD = {"FII": 65_000, "Pro": 100_000}   # TRADING_CONSTANTS.md section 9


def fetch_oi(trading_date: date) -> dict | None:
    """Net SHORT (positive = net short) index CE/PE per participant, from the OI file."""
    url = OI_URL.format(trading_date.strftime("%d%m%Y"))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None
    out = {}
    for i, row in enumerate(csv.reader(io.StringIO(raw))):
        if i < 2 or not row:
            continue
        name = row[0].strip().upper()
        if name not in ("FII", "PRO"):
            continue
        try:
            out["FII" if name == "FII" else "Pro"] = {
                "CE": int(row[COL["call_s"]]) - int(row[COL["call_l"]]),
                "PE": int(row[COL["put_s"]]) - int(row[COL["put_l"]]),
            }
        except (ValueError, IndexError):
            continue
    return out or None


def print_gate5(t1: date):
    """T-1 vs T-2 change in cumulative net OI, with the forbid verdict."""
    cur = fetch_oi(t1)
    t2, prev = t1, None
    for _ in range(10):
        t2 -= timedelta(days=1)
        prev = fetch_oi(t2)
        if prev:
            break
    print(f"\n{'=' * 72}")
    print(f"  GATE 5 — participant OI CHANGE   T-1 {t1:%d-%b} vs T-2 {t2:%d-%b}")
    print(f"  Source: fao_participant_oi_*.csv (POSITIONS). TRADING_CONSTANTS.md section 9.")
    print(f"{'=' * 72}")
    if not cur or not prev:
        print("  Could not fetch both days — Gate 5 CANNOT be scored. Do not guess it.")
        return

    forbidden = []
    print(f"  {'':5} {'leg':4} {'level(T-1)':>12} {'level(T-2)':>12} {'CHANGE':>11} {'limit':>9}  verdict")
    print("  " + "-" * 68)
    for p in ("FII", "Pro"):
        if p not in cur or p not in prev:
            continue
        lim = GATE5_THRESHOLD[p]
        for leg in ("CE", "PE"):
            d = cur[p][leg] - prev[p][leg]
            hit = d >= lim
            if hit:
                forbidden.append("Bull Put" if leg == "CE" else "Bear Call")
            v = ("FORBIDS " + ("Bull Put" if leg == "CE" else "Bear Call")) if hit else "silent"
            print(f"  {p:5} {leg:4} {cur[p][leg]:>12,} {prev[p][leg]:>12,} "
                  f"{fmt(d):>11} {lim:>9,}  {v}")

    print("  " + "-" * 68)
    if not forbidden:
        print("  Gate 5: SILENT — no structure forbidden. NOT permission for either side.")
    elif len(set(forbidden)) >= 2:
        print("  Gate 5: BOTH sides forbidden  ->  NO TRADE.")
    else:
        print(f"  Gate 5: FORBIDDEN -> {sorted(set(forbidden))[0]}. "
              f"The other side is NOT thereby authorised.")
    print("  Reminder: the LEVEL never triggers Gate 5 — only the CHANGE column does.")


def print_detailed_table(data: dict, trading_date: date):
    print(f"\n{'=' * 72}")
    print(f"  {trading_date.strftime('%d/%m/%Y')} — FII DII FNO ACTIVITY  (Source: NSE archives)")
    print(f"{'=' * 72}")
    header = f"{'':10} {'Instrument':12} {'Change':>12}  {'Activity':22} {'Trend'}"
    print(header)
    print("-" * 72)

    for pname in PARTICIPANTS:
        row = data.get(pname)
        if row is None:
            continue
        fut_net = net(row, COL["fut_idx_l"], COL["fut_idx_s"])
        call_net = net(row, COL["call_l"], COL["call_s"])
        put_net = net(row, COL["put_l"], COL["put_s"])

        call_activity = "Bought Calls" if call_net >= 0 else "Sold Calls"
        put_activity = "Sold Puts" if put_net <= 0 else "Bought Puts"
        fut_activity = "Bought Futures" if fut_net >= 0 else "Sold Futures"
        call_trend = "Bullish" if call_net >= 0 else "Bearish"
        put_trend = "Bullish" if put_net <= 0 else "Bearish"
        fut_trend = "Bullish" if fut_net >= 0 else "Bearish"

        print(f"{'':2}{pname:<10} {'Future':12} {fmt(fut_net):>12}  {fut_activity:<22} {fut_trend}")
        print(f"{'':12} {'CE':12} {fmt(call_net):>12}  {call_activity:<22} {call_trend}")
        print(f"{'':12} {'PE':12} {fmt(put_net):>12}  {put_activity:<22} {put_trend}")
        print("-" * 72)

    # Overall: based on FII
    row = data.get("FII")
    if row:
        score = (net(row, COL["call_l"], COL["call_s"])
                 - net(row, COL["put_l"], COL["put_s"])
                 + net(row, COL["fut_idx_l"], COL["fut_idx_s"]))
        overall = "BULLISH" if score >= 0 else "BEARISH"
        print(f"\n  OVERALL TREND: {overall}  (FII activity score: {fmt(score)})")
    print(f"{'=' * 72}\n")


def fii_score(row: list) -> int:
    call_net = net(row, COL["call_l"], COL["call_s"])
    put_net = net(row, COL["put_l"], COL["put_s"])
    fut_net = net(row, COL["fut_idx_l"], COL["fut_idx_s"])
    return call_net - put_net + fut_net


def print_5day_table(anchor_date: date, n: int = 5):
    print(f"\n{'=' * 55}")
    print(f"  {anchor_date.strftime('%d/%m/%Y')} — FII Activity Last {n} Days")
    print(f"{'=' * 55}")
    print(f"  {'Period':<12} {'Value':>12}  {'Trend'}")
    print(f"  {'-' * 50}")

    trading_days = last_n_trading_days(anchor_date, n)
    scores = []
    labels = ["Today (T)"] + [f"T-{i} Day" for i in range(1, n)]

    for i, d in enumerate(trading_days):
        data = fetch_csv(d)
        label = labels[i] if i < len(labels) else f"T-{i}"
        if data and "FII" in data:
            score = fii_score(data["FII"])
            scores.append(score)
            t = trend(score)
            print(f"  {label:<12} {fmt(score):>12}  {t}")
        else:
            print(f"  {label:<12} {'N/A':>12}  (no data)")

    if scores:
        bullish_count = sum(1 for s in scores if s >= 0)
        bearish_count = len(scores) - bullish_count
        by_count = "Bullish" if bullish_count >= bearish_count else "Bearish"
        by_sentiment = "Bullish" if sum(scores) >= 0 else "Bearish"
        print(f"  {'-' * 50}")
        print(f"  {'Overall':<12} {'By Count':>12}  {by_count}  ({bullish_count}B/{bearish_count}Be)")
        print(f"  {'':12} {'By Sentiment':>12}  {by_sentiment}  (net {fmt(sum(scores))})")
    print(f"{'=' * 55}\n")


def main():
    args = sys.argv[1:]
    if args and args[0] not in ("", "-"):
        try:
            target = date.fromisoformat(args[0])
        except ValueError:
            print(f"Bad date: {args[0]}. Use YYYY-MM-DD.")
            sys.exit(1)
    else:
        target = date.today() - timedelta(days=1)

    n_days = int(args[1]) if len(args) > 1 else 5

    print(f"\nFetching NSE data for {target.strftime('%d-%b-%Y')}...")
    data = fetch_csv(target)
    if not data:
        print(f"No data found for {target}. Market may have been closed or data not yet published (available after ~4 PM IST).")
        print("Trying previous trading day...")
        for delta in range(1, 5):
            target = target - timedelta(days=1)
            data = fetch_csv(target)
            if data:
                print(f"Using {target.strftime('%d-%b-%Y')} instead.")
                break
        if not data:
            print("Could not fetch data. Check internet connection.")
            sys.exit(1)

    print_detailed_table(data, target)
    print_5day_table(target, n_days)
    print_gate5(target)


if __name__ == "__main__":
    main()
