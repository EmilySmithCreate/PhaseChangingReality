"""SANDBOX LOOK (20 November 2026, last of the night; rule 16: a look, exact arithmetic and divisions). Her words
(verbatim in sandbox/NOTEBOOK.md): "what might the electron be in our toy then?"; "could a twist and spin cancel
out 3 diagonals of mass? or electrons could be a form of photons which have no mass and are cube diagonals? 4 cube
diagonals locked in as a particle?"; "I think proton is a closed ring. the hypothesis does not allow an open strand."

INPUTS. Measured (Particle Data Group 2024, read 20 November): proton and pion and rho masses, the proton's charge
radius. Her record: the unit 0.511/3 MeV; a photon's repeat is any whole n >= 4 steps (the rules sheet). From
memory, to verify: the strong force's tension 0.89 to 1.12 GeV/fm; the highest-energy photon measured, about 1.4
PeV; a photon's energy is 2 pi hbar c over its wavelength (the measured Planck relation).

WRITTEN BEFORE COMPUTING (ours):
  U1. Body diagonals join black to white, so a closed loop of them has an even number of steps: none with 3; the
      smallest that is not out-and-back has 4. Some four-loops are flat (rhombi) and some are not (the four
      directions of a tetrahedron, which add to zero).
  U2. Shadows. An edge's shadow on a face diagonal is exactly one half of it; on a body diagonal exactly one third.
      A face diagonal's shadow on a body diagonal is two thirds or nothing. The triangle's sides (1, 1, -2) have no
      shadow on their body diagonal. With charge read as minus the shadow on the body diagonal and color class as
      the coordinate sum modulo 3 (the published charge lattice of the group U(3): general knowledge, to verify),
      cube vectors give the down quark, up quark, electron, proton and neutron their measured charges.
  U3. A closed ring carrying three unit sources of a quantity that counts modulo 3 always has one arc carrying
      nothing: the ring is an open strand with a silent arc.
  U4. One wavelength of light locked round a loop weighs 0.511 MeV only if the loop is 2.4e-12 m long. Under her
      repeat-of-four rule the hardest photon measured caps the lattice step near 1e-22 m.
  U5. An open strand at the strong force's tension is about 1 fm long, half of it 0.4 to 0.5 fm: within a factor
      of 2 of the proton's measured radius, where the round ring was 5 to 6 times too small.
  U6. Spin arrangement removes thousands of diagonals: the rho and the charged pion hold the same thirds.

Usage: python sandbox/electron_candidates_look.py   (writes sandbox/out/electron_candidates_look_2026-11-20.txt)
"""
import itertools
import math
from fractions import Fraction
from pathlib import Path

import numpy as np

HBARC = 197.3269804
M_E = 0.51099895
UNIT = M_E / 3
M_P = 938.27208816
R_P = 0.8409
BODY = [v for v in itertools.product((1, -1), repeat=3)]


def shadow(v, on):
    return Fraction(sum(a * b for a, b in zip(v, on)), sum(b * b for b in on))


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "electron_candidates_look_2026-11-20.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    say("PART 1, exact: closed loops of body diagonals")
    for n in (2, 3, 4, 5, 6):
        closed = [w for w in itertools.product(BODY, repeat=n) if not any(np.sum(w, axis=0))]
        clean = [w for w in closed if all(tuple(-x for x in w[i]) != w[(i + 1) % n] for i in range(n))]
        say(f"    {n} steps: closed walks {len(closed)}; with no step straight back: {len(clean)}")
        if n == 4:
            flat = sum(1 for w in clean if abs(np.linalg.det(np.array([w[0], np.add(w[0], w[1]), np.add(np.add(w[0], w[1]), w[2])]))) < 1e-9)
            tetra = sum(1 for w in clean if len(set(w)) == 4)
            say(f"       of those {len(clean)}: flat (rhombi) {flat}; not flat {len(clean) - flat}; using four different directions "
                f"(a tetrahedron's) {tetra}")
    say("    each step changes the point's color (coordinate sum odd), so an odd number of steps cannot close.")
    say()

    say("PART 2, exact: shadows (the fraction of the target a step covers along it)")
    for label, v, on in (("an edge on a face diagonal", (1, 0, 0), (1, 1, 0)),
                         ("an edge on a body diagonal", (1, 0, 0), (1, 1, 1)),
                         ("a face diagonal (1, 1, 0) on a body diagonal", (1, 1, 0), (1, 1, 1)),
                         ("a face diagonal (1, -1, 0) on a body diagonal", (1, -1, 0), (1, 1, 1)),
                         ("a box diagonal (1, 1, 2) on a body diagonal", (1, 1, 2), (1, 1, 1)),
                         ("the triangle's side (1, 1, -2) on its body diagonal", (1, 1, -2), (1, 1, 1))):
        say(f"    {label:<52} {shadow(v, on)}")
    say("the published charge table read on cube vectors: charge = minus the shadow on (1, 1, 1); color class = sum mod 3")
    say(f"    {'particle':<10} {'vector(s)':<44} {'sum':<5} {'charge':<7} color class")
    table = [("down", [(1, 0, 0)]), ("up", [(0, -1, -1)]), ("electron", [(1, 1, 1)]),
             ("proton", [(0, -1, -1), (-1, 0, -1), (0, 0, 1)]), ("neutron", [(0, -1, -1), (0, 1, 0), (0, 0, 1)])]
    for name, vs in table:
        tot = tuple(int(x) for x in np.sum(vs, axis=0))
        say(f"    {name:<10} {str(vs):<44} {sum(tot):<5} {str(-shadow(tot, (1, 1, 1))):<7} {sum(tot) % 3}")
    say()

    say("PART 3, exact: a closed ring with three unit sources of a quantity counted modulo 3")
    for k in range(3):
        arcs = [(k + i) % 3 for i in range(3)]
        say(f"    first arc carries {k}: the three arcs carry {arcs}; arcs carrying nothing: {arcs.count(0)}")
    say()

    say("PART 4, arithmetic: light locked round a loop, one wavelength round (energy = 2 pi hbar c / length)")
    L_e = 2 * math.pi * HBARC / M_E
    say(f"    to weigh 0.511 MeV the loop is {L_e:.0f} fm = {L_e * 1e-15:.2e} m long; as four body diagonals the step is {L_e / (4 * math.sqrt(3)) * 1e-15:.2e} m")
    a_b = 2 * math.pi * R_P / ((M_P / UNIT) * math.sqrt(6))
    L4 = 4 * math.sqrt(3) * a_b
    say(f"    at the earlier candidate step {a_b * 1e-15:.2e} m, four body diagonals are {L4 * 1e-15:.2e} m and one wavelength there is {2 * math.pi * HBARC / L4 / 1000:.0f} GeV")
    for label, e_mev in (("1 TeV", 1e6), ("1.4 PeV (to verify)", 1.4e9)):
        lam = 2 * math.pi * HBARC / e_mev
        a_max = lam / (4 * math.sqrt(3))
        say(f"    a photon of {label}: wavelength {lam * 1e-15:.2e} m; with a repeat of at least four body diagonals the step is at most "
            f"{a_max * 1e-15:.2e} m; a ring of 5,508 box diagonals is then at most {M_P / UNIT * math.sqrt(6) * a_max:.2e} fm long "
            f"(the proton's rim is {2 * math.pi * R_P:.2f} fm)")
    say()

    say("PART 5, arithmetic: an open strand at the strong force's tension (length = the proton's mass / tension)")
    for s in (890.0, 981.0, 1120.0):
        L = M_P / s
        say(f"    tension {s / 1000:.2f} GeV/fm: length {L:.3f} fm; middle to end {L / 2:.3f} fm, {R_P / (L / 2):.1f} times under the measured "
            f"{R_P} fm; the same length as a round ring: radius {L / (2 * math.pi):.3f} fm, {R_P / (L / (2 * math.pi)):.1f} times under")
    say()

    say("PART 6, measured: the same thirds, spins aligned against opposed")
    rho, pi = 775.26, 139.57039
    say(f"    rho {rho} MeV = {rho / UNIT:.0f} diagonals; charged pion {pi} MeV = {pi / UNIT:.0f}; difference {rho - pi:.2f} MeV = {(rho - pi) / UNIT:.0f} diagonals")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
