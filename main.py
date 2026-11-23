"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes the excuse (one line, at most 200 characters) to /output/entry.txt.
"""

from pathlib import Path

EXCUSE = "Error 404: victory not found. Root cause: me. Remediation: pending, like my last three fixes."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
