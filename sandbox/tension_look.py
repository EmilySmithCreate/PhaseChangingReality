"""SANDBOX LOOK (20 November 2026, late night; rule 16: a look, arithmetic only). Her question of the same night
(verbatim in sandbox/NOTEBOOK.md): does "a loop's length is its mass" work "as long as a string of much more tension
(like a full twist on a single length face diagonal) can have greater mass? or should we think about it like there
are other types of energy that are counted for some types of particles? does a particle with a twist have more mass
than one without? or do we just say that there are more smaller diagonal count particles in a same size area?"

INPUTS. Measured (Particle Data Group 2024, read from the PDFs on 20 November): the masses and the proton's charge
radius. Constants: hbar c = 197.327 MeV fm; the fine-structure constant 1/137.036. Her record: the unit 0.511/3 MeV
per looped box diagonal; the store's bond 331.6 MeV per link (twist_energies_2026-11-04.md, decided 6 November).
The candidate size of the electron's triangle is the look of earlier tonight (hadron_translation_look, Part 4 (i)).
Two published laws used as formulas (general knowledge, to verify): the electric energy of one whole charge spread
over a size r is about alpha hbar c / r; holding something inside a size r costs about hbar c / r of motion.

WRITTEN BEFORE COMPUTING (ours):
  T1. The electric energy of one whole charge at the proton's size is 1 to 2 MeV, the size of the measured
      differences between charged and neutral relatives (1.3 to 4.6 MeV), which do not all have the same sign.
  T2. The cost of holding three things inside the proton's radius is several hundred MeV, most of the proton.
  T3. At the candidate size of the electron's triangle (about 1e-18 m) both energies are far above 0.511 MeV: the
      electric one thousands of MeV, the holding one hundreds of GeV.

Usage: python sandbox/tension_look.py     (writes sandbox/out/tension_look_2026-11-20.txt)
"""
import math
from pathlib import Path

HBARC = 197.3269804          # MeV fm
ALPHA = 1 / 137.035999
M_E = 0.51099895
UNIT = M_E / 3
M_P = 938.27208816
R_P = 0.8409                 # fm


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "tension_look_2026-11-20.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    say("PART 1, her record's two energies per link (arithmetic)")
    loop = UNIT / math.sqrt(6)
    say(f"a looped box diagonal: {UNIT:.6f} MeV over root 6 links = {loop:.5f} MeV per link")
    say(f"the store's bond: 331.6 MeV per link; ratio to the loop's: {331.6 / loop:.0f}")
    say()

    say("PART 2, measured: charged against neutral relatives (MeV, and in diagonals)")
    for label, d, of in (("charged pion minus neutral pion (the charged is heavier)", 4.5936, 139.57039),
                         ("neutron minus proton (the neutral is heavier)", 1.2933324, 938.272),
                         ("Delta0 minus Delta++ (the less charged is heavier)", 2.86, 1232.0)):
        say(f"    {label:<58} {d:<9.4f} = {d / UNIT:5.1f} diagonals of {of / UNIT:.0f}")
    say(f"the electric energy of one whole charge at the proton's radius {R_P} fm: {ALPHA * HBARC / R_P:.2f} MeV "
        f"= {ALPHA * HBARC / R_P / UNIT:.0f} diagonals")
    say()

    say("PART 3, the cost of holding things in a small size, hbar c / r")
    hold = HBARC / R_P
    say(f"one thing inside the proton's radius: {hold:.0f} MeV; three: {3 * hold:.0f} MeV = {3 * hold / M_P:.2f} of the proton's mass")
    say()

    say("PART 4, the same two energies at the candidate size of the electron's triangle")
    a = 2 * math.pi * R_P / ((M_P / UNIT) * math.sqrt(6))          # fm, the least lattice step of the earlier look
    for label, r in (("corner to middle", math.sqrt(2) * a), ("one side", math.sqrt(6) * a)):
        e_el, e_hold = ALPHA * HBARC / r, HBARC / r
        say(f"    size = {label} = {r * 1e-15:.2e} m: electric {e_el:,.0f} MeV = {e_el / M_E:,.0f} electron masses; "
            f"holding {e_hold / 1000:,.0f} GeV = {e_hold / M_E:,.0f} electron masses")
    say(f"the size at which one whole charge's electric energy equals the electron's mass: {ALPHA * HBARC / M_E:.3f} fm "
        f"= {ALPHA * HBARC / M_E * 1e-15:.2e} m")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
