"""SANDBOX LOOK (20 November 2026, night; rule 16: a look, arithmetic only, nothing registered). Her words of the
same night (verbatim in sandbox/NOTEBOOK.md): "twists of the same direction also repel, so there is repulsion
associated with the 2 full twists held that allows a bunch of diagonals"; "what is the charge of this particle
[the Delta-minus]? what do we know about it?"; and the request to translate her hypothesis to accepted science
"that get's us closer to a prediction that could match or not match an observation".

MEASURED INPUTS, all from the Particle Data Group's 2024 tables (S. Navas et al., Phys. Rev. D 110, 030001), read
from the PDFs' text on 20 November 2026 (baryon summary table, the Delta(1232) listing, the light-meson summary):
masses in MeV. The Delta's separate charge states are listed but "not used for averages"; the Delta-minus has no
separate value. The strong force's string tension is NOT from those tables: about 0.9 GeV per fermi, general
knowledge, to verify (the range 0.89 to 1.12 is the commonly quoted root-tension 420 to 470 MeV).

HER COUNT RULE (the unit, Update 139): one looped box diagonal is 0.511 MeV / 3. A count below is a measured mass
divided by that unit: a division, never a prediction.

WRITTEN BEFORE COMPUTING (ours; the masses had been read, nothing had been divided):
  K1. The Delta's charge states differ by a few MeV in 1,232: the net twist (+2, +1, 0, -1) moves the count by a
      few tens of diagonals in about 7,200. The all-one-direction Delta++ is not the longest of them.
  K2. The same thirds come at different lengths: the proton and the Delta+ (both 2/3, 2/3, -1/3) differ by about
      1,700 diagonals; the four particles Delta-, Sigma*-, Xi*-, Omega- all hold -1/3, -1/3, -1/3 with charge -1
      and spin 3/2, at four lengths in nearly equal steps of about 850 diagonals.
  K3. Exact, the triangle family of the electron look: a walk along the three sides v1, v2, v3 (forward or
      backward) closes exactly when it holds the same net number of each side. That is the published counting rule
      for which groups of quarks are free (equal net numbers of the three colors).
  K4. Spin against mass squared: the Delta family and the rho family lie on straight lines of nearly the same
      slope, near 0.9 per GeV squared.
  K5. One unknown, the lattice's step a. If the proton is one ring of 5,508 box diagonals no smaller than its
      measured charge radius, then a is at least about 4e-19 m and the electron's triangle is about 1e-18 m across.
      With the strong force's published tension as the energy per length, a is about 7e-20 m and the ring's radius
      is about 0.15 fm, several times smaller than the measured 0.84 fm.

SECOND RUN, the same night (output _r2). The first output is kept. Its Part 3 printed the string's slopes in the
wrong units (0.03 where 0.8 belongs): the tension was not converted from GeV per fermi to GeV squared, a slip of the
look and not a result. Only those three lines change.

Usage: python sandbox/hadron_translation_look.py   (writes sandbox/out/hadron_translation_look_2026-11-20_r2.txt)
"""
import itertools
import math
from pathlib import Path

import numpy as np

M_E = 0.51099895
UNIT = M_E / 3.0
HBARC = 197.3269804                                   # MeV fm

# (name, thirds, net charge, spin, mass MeV, +-, note)
BARYONS = [
    ("proton", "2/3, 2/3, -1/3", +1, "1/2", 938.27208816, 0.0, ""),
    ("neutron", "2/3, -1/3, -1/3", 0, "1/2", 939.5654205, 0.0, ""),
    ("Delta, mixed charges", "all four", None, "3/2", 1232.0, 2.0, "PDG estimate 1230 to 1234"),
    ("Delta++", "2/3, 2/3, 2/3", +2, "3/2", 1230.55, 0.20, "GRIDNEV 06, not used for averages"),
    ("Delta0", "2/3, -1/3, -1/3", 0, "3/2", 1233.40, 0.22, "GRIDNEV 06, not used for averages"),
    ("Sigma*-(1385)", "-1/3, -1/3, -1/3", -1, "3/2", 1387.2, 0.5, "d d s"),
    ("Xi*-(1530)", "-1/3, -1/3, -1/3", -1, "3/2", 1535.0, 0.6, "d s s"),
    ("Omega-", "-1/3, -1/3, -1/3", -1, "3/2", 1672.45, 0.29, "s s s"),
]
RHO_LINE = [(1, 775.26), (2, 1318.2), (3, 1688.8), (4, 1967.0)]          # rho, a2, rho3, a4(1970)
DELTA_LINE = [(1.5, 1232.0), (3.5, 1930.0), (5.5, 2450.0)]               # Delta(1232), (1950), (2420): PDG "about"
R_PROTON = 0.8409                                     # fm, PDG charge radius
SIGMAS = (890.0, 981.0, 1120.0)                       # MeV per fm: root-tension 420, 440, 470 MeV (to verify)


def slope(points):
    j = np.array([p[0] for p in points])
    m2 = np.array([(p[1] / 1000.0) ** 2 for p in points])
    return float(np.polyfit(m2, j, 1)[0])


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "hadron_translation_look_2026-11-20_r2.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    say(f"the unit: {UNIT:.6f} MeV per looped box diagonal (0.511 MeV / 3)")
    say()
    say("PART 1, divisions: measured masses in diagonals")
    say(f"{'particle':<22} {'thirds':<18} {'charge':<7} {'spin':<5} {'MeV':<14} {'diagonals':<10} note")
    for name, thirds, q, spin, m, dm, note in BARYONS:
        say(f"{name:<22} {thirds:<18} {'' if q is None else format(q, '+d'):<7} {spin:<5} {m:<14.5f} {m / UNIT:<10.1f} {note}")
    say()
    d = 2.86
    say(f"Delta0 minus Delta++ (PDG listing, GRIDNEV 06): {d} +- 0.30 MeV = {d / UNIT:.1f} +- {0.30 / UNIT:.1f} diagonals "
        f"of about {1232 / UNIT:.0f}: the all-one-direction Delta++ is the LIGHTER.")
    say(f"neutron minus proton: 1.2933324 MeV = {1.2933324 / UNIT:.2f} diagonals of about 5,512.")
    say(f"Delta (mixed) minus proton, the same thirds as the Delta+: {1232 - 938.272:.1f} +- 2 MeV = {(1232 - 938.272) / UNIT:.0f} diagonals.")
    ms = [1232.0, 1387.2, 1535.0, 1672.45]
    steps = [b - a for a, b in zip(ms, ms[1:])]
    say("four particles, each -1/3, -1/3, -1/3, charge -1, spin 3/2 (Delta- taken at the mixed 1232): steps "
        + ", ".join(f"{s:.1f} MeV = {s / UNIT:.0f} diagonals" for s in steps))
    say()

    say("PART 2, exact arithmetic: which walks along the triangle's sides close")
    v = [np.array(x) for x in ((1, 1, -2), (1, -2, 1), (-2, 1, 1))]
    ok, closed_kinds = True, {}
    for n in range(1, 7):
        for word in itertools.product(range(6), repeat=n):
            net = [0, 0, 0]
            for w in word:
                net[w % 3] += 1 if w < 3 else -1
            closes = not np.any(sum(net[i] * v[i] for i in range(3)))
            equal = net[0] == net[1] == net[2]
            ok = ok and (closes == equal)
            if closes:
                plus, minus = sum(1 for w in word if w < 3), sum(1 for w in word if w >= 3)
                closed_kinds.setdefault(n, set()).add((plus, minus))
    say(f"every walk of 1 to 6 steps (forward or backward along v1, v2, v3): closes exactly when the net numbers of "
        f"the three sides are equal: {ok}")
    for n in sorted(closed_kinds):
        say(f"    {n} steps: closed walks have (forward, backward) = {sorted(closed_kinds[n])}")
    say("    so forward minus backward is always a multiple of three; 2 steps is one side out and back; 3 is one of each.")
    say(f"the sides are 3 x (e_i - (1,1,1)/3) up to sign: v1 / 3 = {tuple(round(float(x), 4) for x in v[0] / 3)}; "
        f"a difference of two sides: v1 - v2 = {tuple(int(x) for x in v[0] - v[1])}, three face diagonals.")
    say()

    say("PART 3, measured: spin against mass squared (least-squares slope, per GeV squared)")
    say(f"the rho line (rho, a2, rho3, a4; spins 1 to 4): {slope(RHO_LINE):.3f}")
    say(f"the Delta line (Delta(1232), (1950), (2420); spins 3/2, 7/2, 11/2): {slope(DELTA_LINE):.3f}")
    for s in SIGMAS:
        nat = s / 1000 * HBARC / 1000                 # the tension in GeV squared
        say(f"    a spinning open string of tension {s / 1000:.2f} GeV/fm ({nat:.3f} GeV squared) gives 1 / (2 pi tension) = "
            f"{1 / (2 * math.pi * nat):.3f}; a closed one gives half, {1 / (4 * math.pi * nat):.3f}"
            f"   (formulas: general knowledge, to verify)")
    say()

    say("PART 4, arithmetic: one unknown, the lattice's step a (1 fm = 1e-15 m)")
    n_p = 938.27208816 / UNIT
    a_min = 2 * math.pi * R_PROTON / (n_p * math.sqrt(6))
    say(f"(i) if the proton is one ring of {n_p:.0f} box diagonals, round, of radius at least its charge radius {R_PROTON} fm:")
    say(f"    a >= {a_min:.3e} fm = {a_min * 1e-15:.2e} m; the electron's triangle then has side >= {math.sqrt(6) * a_min * 1e-15:.2e} m,")
    say(f"    perimeter >= {3 * math.sqrt(6) * a_min * 1e-15:.2e} m, corner-to-middle >= {math.sqrt(2) * a_min * 1e-15:.2e} m;")
    say(f"    the loop's energy per length is then at most {UNIT / (math.sqrt(6) * a_min) / 1000:.3f} GeV/fm.")
    say("(ii) if the loop's energy per length is the strong force's string tension:")
    for s in SIGMAS:
        a = UNIT / (math.sqrt(6) * s)
        ring = n_p * math.sqrt(6) * a / (2 * math.pi)
        say(f"    tension {s / 1000:.2f} GeV/fm: a = {a * 1e-15:.2e} m; the proton ring's length {n_p * math.sqrt(6) * a:.3f} fm, "
            f"its radius if round {ring:.3f} fm ({R_PROTON / ring:.1f} times smaller than measured); "
            f"the electron's side {math.sqrt(6) * a * 1e-15:.2e} m")
    say("    (the ring's length under (ii) is just the proton's mass over the tension; a round ring is the widest shape)")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
