"""SANDBOX LOOK (20 November 2026, after her "read and proceed" on the bag model; rule 16: a look, arithmetic).

SOURCE, read on 20 November 2026 from the scanned pages (pp. 865, 866, 882, 885, 888, 889, 890): K. Johnson, "The
M.I.T. bag model", Acta Physica Polonica B6 (1975) 865, lectures at the XV Cracow School. Its mass formula (p. 890;
Eq. 4.25 on p. 888 with massless quarks), in units where hbar c = 1:

    M(R) = n * 2.04 / R  +  (4 pi / 3) B R^3  -  Z0 / R  +  (alpha_c mu / R) (4/3) [ n(n-6) + S(S+1) + 3 I(I+1) ]

minimised over the radius R. Its Table I parameters: B^(1/4) = 0.145 GeV, Z0 = 1.84, alpha_c = 0.55. The value of
mu was not on a page read; it is backed out here from ONE entry of Table I (the proton's Delta E_M = -0.155 GeV at
R = 5.00 per GeV), and the Delta row is then a check. Table I rows used (GeV; R in 1/GeV):
    P      M 0.938  R 5.00  -Z0/R -0.367  BV 0.234  kinetic 1.226  Delta E_M -0.155
    Delta  M 1.233  R 5.48  -Z0/R -0.336  BV 0.308  kinetic 1.119  Delta E_M +0.141
    pi     M_exp 0.139, M_bag 0.280
The lecture's own comparison (p. 890): "The mean square charge radius for the proton comes out to be 0.73 fm, in
comparison with the experimental value, 0.88 +- 0.03 fm." Today's measured value: 0.8409 fm (PDG 2024).

WRITTEN BEFORE COMPUTING (ours; rule 2, reproduce before extending):
  V1. The formula with those parameters gives the proton's and the Delta's mass and radius to within 1 % of
      Table I, and each of their four terms to within 2 %.
  V2. At the minimum the volume term B V is exactly a quarter of the mass (every other term goes as 1/R).
  V3. In her unit (0.511/3 MeV per diagonal; the count is energy, her decision of 20 November) that is one constant
      for every light particle: about 1,350 diagonals per cubic fermi of bag.

Usage: python sandbox/bag_look.py     (writes sandbox/out/bag_look_2026-11-20.txt)
"""
import math
from pathlib import Path

HBARC = 0.1973269804          # GeV fm
UNIT = 0.51099895e-3 / 3      # GeV per diagonal
B = 0.145 ** 4                # GeV^4
Z0, ALPHA_C, X = 1.84, 0.55, 2.04
TABLE = {"proton": dict(n=3, S=0.5, I=0.5, M=0.938, R=5.00, zp=-0.367, bv=0.234, kin=1.226, em=-0.155),
         "Delta": dict(n=3, S=1.5, I=1.5, M=1.233, R=5.48, zp=-0.336, bv=0.308, kin=1.119, em=0.141)}


def bracket(n, S, I):
    return n * (n - 6) + S * (S + 1) + 3 * I * (I + 1)


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "bag_look_2026-11-20.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    p = TABLE["proton"]
    amu = p["em"] * p["R"] / ((4 / 3) * bracket(p["n"], p["S"], p["I"]))      # alpha_c * mu, from one table entry
    say(f"alpha_c mu backed out of the proton's Delta E_M: {amu:.4f} (mu = {amu / ALPHA_C:.3f} at alpha_c = {ALPHA_C})")
    say()
    say("PART 1, reproduction of Table I (GeV; R in 1/GeV): ours / the table's")
    say(f"{'particle':<9} {'spin term bracket':<18} {'R':<14} {'M':<15} {'kinetic':<15} {'-Z0/R':<17} {'B V':<15} {'Delta E_M':<16} B V / M")
    worst = 0.0
    for name, t in TABLE.items():
        br = bracket(t["n"], t["S"], t["I"])
        c = t["n"] * X - Z0 + (4 / 3) * amu * br                 # everything that goes as 1/R
        R = (c / (4 * math.pi * B)) ** 0.25
        bv = (4 * math.pi / 3) * B * R ** 3
        M = c / R + bv
        kin, zp, em = t["n"] * X / R, -Z0 / R, (4 / 3) * amu * br / R
        for ours, theirs in ((R, t["R"]), (M, t["M"]), (kin, t["kin"]), (zp, t["zp"]), (bv, t["bv"]), (em, t["em"])):
            worst = max(worst, abs(ours / theirs - 1))
        say(f"{name:<9} {br:<18.1f} {R:.3f} / {t['R']:<6} {M:.4f} / {t['M']:<6} {kin:.3f} / {t['kin']:<7} {zp:.3f} / {t['zp']:<8} "
            f"{bv:.3f} / {t['bv']:<7} {em:+.3f} / {t['em']:<+8} {bv / M:.4f}")
        t.update(R_=R, M_=M, bv_=bv, kin_=kin, zp_=zp, em_=em)
    say(f"largest difference from the table over the twelve entries: {100 * worst:.1f} %")
    say()

    say("PART 2, the same in her unit: a particle's count of diagonals, by kind (the count is energy)")
    say(f"{'particle':<9} {'total':<8} {'held-in motion':<15} {'zero-point':<11} {'volume':<8} {'spin':<8}")
    for name, t in TABLE.items():
        say(f"{name:<9} {t['M_'] / UNIT:<8.0f} {t['kin_'] / UNIT:<+15.0f} {t['zp_'] / UNIT:<+11.0f} {t['bv_'] / UNIT:<+8.0f} {t['em_'] / UNIT:<+8.0f}")
    say()

    say("PART 3, the one constant")
    b_fm = B / HBARC ** 3                                        # GeV per fm^3
    say(f"B = (0.145 GeV)^4 = {1000 * b_fm:.1f} MeV per cubic fermi; a particle at rest holds 4 B = {4000 * b_fm:.0f} MeV = "
        f"{4 * b_fm / UNIT:.0f} diagonals per cubic fermi of bag")
    for name, t in TABLE.items():
        r_fm = t["R_"] * HBARC
        say(f"    {name}: bag radius {r_fm:.3f} fm, volume {4 * math.pi / 3 * r_fm ** 3:.2f} cubic fermi")
    say("the lecture's proton charge radius 0.73 fm against 0.88 +- 0.03 fm then and 0.8409 fm now; its pion 0.280 GeV against 0.139 GeV measured")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
