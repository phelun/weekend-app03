#!/usr/bin/env python3
"""Update exactly one GitOps deployment image to an immutable commit SHA."""

import re
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("usage: promote.py MANIFEST IMAGE_REPOSITORY COMMIT_SHA")

    manifest = Path(sys.argv[1])
    repository = sys.argv[2]
    commit_sha = sys.argv[3]
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha):
        raise SystemExit(f"invalid commit SHA: {commit_sha}")

    original = manifest.read_text()
    pattern = rf"(?m)^(\s*image:\s*{re.escape(repository)}:)[0-9a-f]{{40}}\s*$"
    updated, replacements = re.subn(pattern, rf"\g<1>{commit_sha}", original)
    if replacements != 1:
        raise SystemExit(
            f"expected one image reference for {repository} in {manifest}; "
            f"found {replacements}"
        )
    manifest.write_text(updated)


if __name__ == "__main__":
    main()
