#!/usr/bin/env python3
"""Report configured trading MCP transport status at the start of a Codex session."""

from __future__ import annotations

import subprocess


def main() -> None:
    try:
        result = subprocess.run(
            ["codex", "mcp", "list"],
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
        output = f"{result.stdout}\n{result.stderr}".lower()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        output = ""

    unavailable = []
    for name, label in (
        ("kite", "Kite (Zerodha)"),
        ("kotak-neo", "Kotak Neo"),
        ("dhan", "Dhan"),
    ):
        line = next(
            (line for line in output.splitlines() if line.split() and line.split()[0] == name),
            "",
        )
        if "enabled" not in line:
            unavailable.append(label)

    if unavailable:
        print(
            "TRADING MCP WARNING: "
            + ", ".join(unavailable)
            + " not configured or unavailable. Login before any trade analysis — "
            "see docs/broker-session-startup.md"
        )


if __name__ == "__main__":
    main()
