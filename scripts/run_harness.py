#!/usr/bin/env python3
"""Run lab harness on synthetic text fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from aida_lab.harness import run_and_scrub, run_root, write_json  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", type=Path, help="Directory of .txt/.md fixtures")
    ap.add_argument("--json", type=Path, default=None, help="Write JSON here")
    ap.add_argument(
        "--raw",
        action="store_true",
        help="Keep fixture filenames (still no content snippets)",
    )
    args = ap.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    payload = run_root(root) if args.raw else run_and_scrub(root)
    if args.json:
        write_json(payload, args.json)
        print(f"wrote {args.json}")
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
