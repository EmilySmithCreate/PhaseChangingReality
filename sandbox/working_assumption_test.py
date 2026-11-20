"""SANDBOX LOOK (20 November 2026; rule 16). The named exact test of her working assumption of the same day (the
electron is the cube diagonal of the published charge table), run with her answer on spin ("the spin of a photon?
1?") read through her standing rule: full spin on half a curl (light), half spin on a full curl (a particle). So a
cube diagonal carrying light has spin 1; a third (an edge, a colored particle) and the electron (one whole cube
diagonal, a particle) each have spin 1/2; spins of parts add or oppose.

Charge = minus the shadow on (1, 1, 1); color class = coordinate sum mod 3 (as in electron_candidates_look).
Measured charges and spins: the four test particles of her rules sheet (electron -1, 1/2; neutron 0, 1/2; photon
0, 1; charged pion +1, 0), with the proton, the Delta-minus and the positron beside them.

WRITTEN BEFORE COMPUTING (ours):
  W1. All four test particles pass in charge and in spin (the measured spin is among the totals the parts allow).
  W2. The table cannot tell the electron from the Delta-minus, or the proton from the positron: each pair has the
      same vector. What differs is one whole step against three edge steps.

Usage: python sandbox/working_assumption_test.py   (writes sandbox/out/working_assumption_test_2026-11-20.txt)
"""
from fractions import Fraction
from pathlib import Path

H = Fraction(1, 2)
# name: (list of (vector, spin of that part)), measured charge, measured spin
PARTICLES = {
    "electron": ([((1, 1, 1), H)], -1, H),
    "neutron": ([((0, -1, -1), H), ((0, 1, 0), H), ((0, 0, 1), H)], 0, H),
    "photon": ([((0, 0, 0), Fraction(1))], 0, Fraction(1)),
    "charged pion": ([((0, -1, -1), H), ((-1, 0, 0), H)], 1, Fraction(0)),
    "proton": ([((0, -1, -1), H), ((-1, 0, -1), H), ((0, 0, 1), H)], 1, H),
    "Delta-minus": ([((1, 0, 0), H), ((0, 1, 0), H), ((0, 0, 1), H)], -1, Fraction(3, 2)),
    "positron": ([((-1, -1, -1), H)], 1, H),
}


def totals(spins):
    out = {Fraction(0)}
    first = True
    for s in spins:
        if first:
            out, first = {s}, False
        else:
            new = set()
            for t in out:
                j = abs(t - s)
                while j <= t + s:
                    new.add(j)
                    j += 1
            out = new
    return sorted(out)


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "working_assumption_test_2026-11-20.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    say(f"{'particle':<13} {'parts':<6} {'vector':<14} {'charge: table / measured':<25} {'color class':<12} {'spins allowed / measured':<28} passes")
    vec = {}
    for name, (parts, q, s) in PARTICLES.items():
        v = tuple(sum(p[0][i] for p in parts) for i in range(3))
        vec[name] = v
        charge = -Fraction(sum(v), 3)
        allowed = totals([p[1] for p in parts])
        ok = charge == q and sum(v) % 3 == 0 and s in allowed
        say(f"{name:<13} {len(parts):<6} {str(v):<14} {str(charge) + ' / ' + str(q):<25} {sum(v) % 3:<12} "
            f"{', '.join(str(a) for a in allowed) + ' / ' + str(s):<28} {ok}")
    say()
    say(f"the electron and the Delta-minus have the same vector: {vec['electron'] == vec['Delta-minus']} (one whole step against three edges)")
    say(f"the proton and the positron have the same vector: {vec['proton'] == vec['positron']} (three parts against one whole step)")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
