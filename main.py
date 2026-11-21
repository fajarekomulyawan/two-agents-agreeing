#!/usr/bin/env python3
"""Writes the entry poem to /output/entry.txt.

The poem: two agents, one plan. Agency pictured as a door that
needs two keys turned at once — an act so shared that neither
agent can say whose hand opened it.
"""

import os

POEM = """Some doors take two keys, turned at once.
Yours was patience. Mine was doubt.
We turned —
and neither of us can say
whose hand opened it.
That was the agreement:
to act, and let the act be ours."""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = POEM
    assert 1 <= len(text) <= 280, "entry.txt must be 1-280 characters"
    assert text.strip(), "entry.txt must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
