"""SANDBOX LOOK (10 November 2026; rule 16: a look, nothing registered). The published combining rules of the
two-dimensional layered liquid crystal (Chen, Alexander and Kamien 2009; the reading note
docs/reading/notes/2026-11-10_defects_in_ordered_media.md) set against the pair moves of graphity.curl_pair_moves.

THE PUBLISHED RULE. Two generators, S (a shift by one row) and F (a flip, a half turn), one relation F S F^-1 S = e:
carrying a shift through a flip reverses it. Every element is S^a F^n, written (a, n), and
(a, n)(b, m) = (a + (-1)^n b, n + m).

THE DICTIONARY (ours, unverified; the pairing argued in the notebook, 10 November): curl with shift, twist with
turning. A square holding curl c (a whole number here) and twist t (in halves) is the element (c, 2t). So her matter
half (+1 curl, +1/2 twist) is (1, 1), her antimatter half is (-1, -1), a dark gluon is (+-1, 0).

WHAT "ALLOWED" MEANS. Flaws combine along paths, and a different path conjugates an element. So a set of objects may
turn into another set exactly when some ordering and some choice of paths gives the same product. The part of that
which no path can change is the tally (net curl mod 2, net twist): the group made commutative is Z2 x Z.

PART 1, exact: for each move of the build, the products its objects can have before, and after.
PART 2, exact: the build run on a sheet under both twist rules; net curl and net twist after every sweep.

Usage: python sandbox/klein_rules_look.py     (writes sandbox/out/klein_rules_look_2026-11-10.txt)
"""
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.cqg import NO_CAP, torus                      # noqa: E402
from graphity.curl_pair_moves import PairMoves              # noqa: E402
from graphity.curl_pairs import CurlState                   # noqa: E402

E = (0, 0)


def mul(g, h):
    return (g[0] + (-1) ** (g[1] % 2) * h[0], g[1] + h[1])


def inv(g):
    return (-((-1) ** (g[1] % 2)) * g[0], -g[1])


def conj(g, x):
    return mul(mul(x, g), inv(x))


CONJUGATORS = [(a, n) for a in range(-3, 4) for n in (0, 1)]


def products(objects):
    """Every product the objects can have: all orders, each object carried along any path (conjugated)."""
    out = set()
    for order in itertools.permutations(objects):
        for xs in itertools.product(CONJUGATORS, repeat=len(order)):
            p = E
            for g, x in zip(order, xs):
                p = mul(p, conj(g, x))
            out.add(p)
    return out


def tally(objects):
    return (sum(g[0] for g in objects) % 2, sum(g[1] for g in objects))


def show(p):
    return "{" + ", ".join(f"S^{a} F^{n}" for a, n in sorted(p) if abs(a) <= 4) + "}"


def part_one(say):
    assert mul(mul(mul((0, 1), (1, 0)), inv((0, 1))), (1, 0)) == E          # the relation F S F^-1 S = e
    assert all(mul(g, inv(g)) == E for g in CONJUGATORS)
    matter, anti = (1, 1), (-1, -1)
    gluon_p, gluon_m = (1, 0), (-1, 0)
    say("PART 1. Each move of the build under the published rule. An element S^a F^n: a = curl, n = twist in halves.")
    say("")
    say(f"matter half is conjugate to S^-1 F: {conj(matter, (0, 1)) == (-1, 1)}  (the sign of the curl riding on a")
    say("  half is not defined in the published rule; only whether it is odd or even)")
    say(f"gluon S^1 is conjugate to S^-1: {conj(gluon_p, (0, 1)) == gluon_m}  (carried once round a half, a curl reverses)")
    say("")
    rows = [
        ("a pair made from nothing", [], [matter, anti]),
        ("a pair cancels, one-number rule (both squares empty)", [matter, anti], []),
        ("a pair cancels, second-number rule (two gluons stay)", [matter, anti], [gluon_p, gluon_m]),
        ("two matter halves join into a store (build: both curls kept)", [matter, matter], [(2, 2)]),
        ("two matter halves join, store with no net curl", [matter, matter], [(0, 2)]),
        ("two matter halves join, 'one twist and one curl' read as one unit", [matter, matter], [(1, 2)]),
        ("two matter halves become nothing", [matter, matter], []),
    ]
    for name, before, after in rows:
        pb, pa = products(before) if before else {E}, products(after) if after else {E}
        ok = bool(pb & pa)
        say(f"{name}")
        say(f"    before: tally {tally(before)}, products {show(pb)}")
        say(f"    after:  tally {tally(after)}, products {show(pa)}")
        say(f"    allowed by the published rule: {'YES' if ok else 'NO'}")
    say("")


def part_two(say):
    say("PART 2. The build on a sheet (lam 1.25 and 2.0, barrier 4, gravity price, her clock), every sweep read.")
    say("L  lam   rule            seed  sweeps pairs stores gluons  net curl always 0  net twist always 0")
    for L in (12, 16):
        for lam in (1.25, 2.0):
            for rule in ("one_number", "second_number"):
                for seed in (1, 2, 3):
                    adj, part = torus(L, L, NO_CAP)
                    m = PairMoves(CurlState(adj, part), lam=lam, barrier=4.0, seed=seed, price_from="gravity",
                                  clock="simultaneous", twist_rule=rule)
                    curl_ok = twist_ok = True
                    while m.sweeps < 10_000:
                        changed = m.sweep()
                        c = m.census()
                        curl_ok &= c["net_curl"] == 0.0
                        twist_ok &= c["net_twist"] == 0.0
                        if not changed:
                            break
                    c = m.census()
                    say(f"{L:<2} {lam:<5} {rule:<15} {seed:<5} {c['sweeps']:<6} {c['pairs_made']:<5} {c['stores']:<6} "
                        f"{c['gluons_plus'] + c['gluons_minus']:<7} {str(curl_ok):<18} {twist_ok}")


def main():
    lines = []

    def say(s):
        print(s)
        lines.append(s)

    part_one(say)
    part_two(say)
    out = Path(__file__).resolve().parent / "out" / "klein_rules_look_2026-11-10.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")
    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
