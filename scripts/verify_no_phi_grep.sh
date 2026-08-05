#!/usr/bin/env bash
# Fail if known denylist tokens appear in the tree.
#
# Public-safe design:
# - Committed PUBLIC_DENY_REGEX only contains synthetic / structural tokens
#   that may never appear in fixtures or docs (canary patterns).
# - Optional private denylist: .phi_denylist.local (gitignored) — one regex
#   per line or a single | alternation line. Use that on operator machines
#   that handle real clinical packets; never commit real names/IDs here.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Synthetic canaries only — not real people, meds, or medical IDs.
# Plant these in a secret test if you want to prove the scanner works.
PUBLIC_DENY_REGEX='PHI_CANARY_NEVER_COMMIT|REAL_MRN_PLACEHOLDER_999|REAL_PATIENT_NAME_PLACEHOLDER'

EXTRA=""
if [[ -f .phi_denylist.local ]]; then
  # Join non-empty, non-comment lines with |
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" =~ ^[[:space:]]*# ]] && continue
    if [[ -n "$EXTRA" ]]; then
      EXTRA="${EXTRA}|${line}"
    else
      EXTRA="$line"
    fi
  done < .phi_denylist.local
fi

if [[ -n "$EXTRA" ]]; then
  DENY_REGEX="${PUBLIC_DENY_REGEX}|${EXTRA}"
else
  DENY_REGEX="$PUBLIC_DENY_REGEX"
fi

EXCLUDE_ARGS=(
  -g '!.git'
  -g '!scripts/verify_no_phi_grep.sh'
  -g '!.phi_denylist.local'
  -g '!.phi_denylist.local.example'
)

if command -v rg >/dev/null 2>&1; then
  if rg -n --hidden "${EXCLUDE_ARGS[@]}" -e "$DENY_REGEX" . ; then
    echo "FAIL: PHI denylist match" >&2
    exit 1
  fi
else
  hits="$(grep -RInE --exclude-dir=.git \
    --exclude='verify_no_phi_grep.sh' \
    --exclude='.phi_denylist.local' \
    --exclude='.phi_denylist.local.example' \
    "$DENY_REGEX" . || true)"
  if [[ -n "$hits" ]]; then
    echo "$hits"
    echo "FAIL: PHI denylist match" >&2
    exit 1
  fi
fi

echo "verify_no_phi_grep: clean"
