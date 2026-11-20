"""SANDBOX LOOK (20 November 2026; rule 16: exact arithmetic). Her words (verbatim in sandbox/NOTEBOOK.md): "I think
edge thirds are a measurement tool, only the box diagonals exist. three edge cubes would also be an alternate to
cube diagonal, not box diagonal?" and "the positron should look like the opposite of our working electron model,
not a proton one."

The question: can the published charge table (charge = minus the shadow on the cube diagonal (1, 1, 1); color class
= coordinate sum mod 3) be laid on her lattice with the box diagonals as the only carriers, or is it a ruler only?

WRITTEN BEFORE COMPUTING (ours):
  X1. Three edges, one of each direction, add to a cube diagonal and never to a box diagonal. A box diagonal is
      four edges: a cube diagonal and one more edge, or steps that cancel along the cube diagonal.
  X2. A single box diagonal's shadow on the cube diagonal is 4/3, 2/3 or 0 of it, never 1/3.
  X3. No set of box diagonals adds up to one cube diagonal: every box diagonal has an even coordinate sum and a
      cube diagonal an odd one (the two colors of point). So with box diagonals alone the table gives charges in
      even numbers of thirds only: 0, 2/3, 4/3, 2, ... and never 1.
  X4. Any closed loop adds to nothing, so read by its shadow a closed loop has charge 0.
  X5. The positron's vector is exactly minus the electron's.

Usage: python sandbox/table_as_ruler_look.py    (writes sandbox/out/table_as_ruler_look_2026-11-20.txt)
"""
import itertools
from collections import Counter
from fractions import Fraction
from pathlib import Path

EDGES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
BOX = sorted({tuple(s * v for s, v in zip(signs, perm)) for perm in set(itertools.permutations((1, 1, 2)))
              for signs in itertools.product((1, -1), repeat=3)})


def add(vs):
    return tuple(sum(v[i] for v in vs) for i in range(3))


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "table_as_ruler_look_2026-11-20.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    say(f"three edges, one of each direction: {add(EDGES)}; is it a box diagonal: {add(EDGES) in BOX}")
    signed = [tuple(s * x for x in e) for e in EDGES for s in (1, -1)]
    four = Counter()
    for combo in itertools.combinations_with_replacement(signed, 4):
        if add(combo) == (1, 1, 2):
            four[tuple(sorted(combo))] += 1
    say(f"ways to make the box diagonal (1, 1, 2) from four edge steps: {len(four)}: {list(four)[0]}  (= (1, 1, 1) + (0, 0, 1))")
    say()
    shadows = Counter(Fraction(sum(v), 3) for v in BOX)
    say(f"the 24 box diagonals, by shadow on (1, 1, 1): {dict(sorted(shadows.items()))}")
    say(f"    as charge and color class: " + ", ".join(f"charge {-s} class {(3 * s) % 3} x{n}" for s, n in sorted(shadows.items())))
    say()
    target = (1, 1, 1)
    found = {n: sum(1 for c in itertools.combinations_with_replacement(BOX, n) if add(c) == target) for n in (1, 2, 3, 4)}
    say(f"sets of 1 to 4 box diagonals adding to one cube diagonal (1, 1, 1): {found}")
    say(f"coordinate sums of the box diagonals: {sorted({sum(v) for v in BOX})} (all even); of the cube diagonal: {sum(target)} (odd)")
    reach = sorted({-Fraction(sum(add(c)), 3) for n in (1, 2, 3) for c in itertools.combinations_with_replacement(BOX, n)})
    say(f"charges reachable with up to three box diagonals: {', '.join(str(x) for x in reach)}")
    say()
    tri = [(1, 1, -2), (1, -2, 1), (-2, 1, 1)]
    say(f"the electron's triangle (a closed loop) adds to {add(tri)}: charge by its shadow {-Fraction(sum(add(tri)), 3)}")
    say(f"electron {(1, 1, 1)}, positron {(-1, -1, -1)}: the positron is minus the electron: {tuple(-x for x in (1, 1, 1)) == (-1, -1, -1)}")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
