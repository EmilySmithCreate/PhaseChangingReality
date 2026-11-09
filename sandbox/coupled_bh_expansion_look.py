"""Ashley's look, 7 November 2026 (his crystal model, not the hypothesis; rule 16: a look, nothing registered).

His question: "could the uneven expansion be effected by the next X being formed ... it pulls or pushes at the
current universe?" Nearest published model: cosmologically coupled black holes (Farrah et al. 2023; Croker et
al. 2024): a black hole's mass grows as a^k; at k = 3 a population's energy is constant once born, acting as
dark energy.

A flat background with matter, radiation and black holes only (no Lambda put in): black holes born with the
star formation history of Madau and Dickinson (2014, their eq. 15), each cohort scaling as a^(k-3) in physical
density; the amount made is whatever fills 1 - Om today. H(a) is iterated to self-consistency. Each k (and
LCDM) is fitted to Pantheon+ (zHD, diagonal errors, offset free) over Om alone.
Conventions of ours: Madau-Dickinson at every redshift (Croker et al. use a different high-z rate), H0 70 for
the time unit, diagonal errors. Needs pandas and scipy. Reads the data file sn_tilt_by_distance_look.py saves.
Output: sandbox/out/coupled_bh_expansion_look_2026-11-07.txt
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import minimize_scalar

OUT = Path(__file__).parent / "out"
df = pd.read_csv(OUT / "PantheonPlusSH0ES.dat", sep=r"\s+")
df = df[(df.IS_CALIBRATOR == 0) & (df.zHD > 0.01)].drop_duplicates("CID")
zs, mu = df.zHD.values, df.MU_SH0ES.values
w = 1 / df.MU_SH0ES_ERR_DIAG.values ** 2

H0yr = 70 / 3.0857e19 * 3.156e7
Or = 9e-5
lna = np.linspace(np.log(1e-3), 0, 6000)
a = np.exp(lna)
z = 1 / a - 1
psi = 0.015 * (1 + z) ** 2.7 / (1 + ((1 + z) / 2.9) ** 5.6)
rho_c0 = 2.775e11 * 0.7 ** 2


def lcdm_E(Om):
    return np.sqrt(Om * a ** -3 + Or * a ** -4 + (1 - Om - Or))


def ccbh(Om, k):
    E = lcdm_E(Om)
    for _ in range(40):
        birth = psi * a ** -3 / (H0yr * E)
        rho = a ** (k - 3) * cumulative_trapezoid(birth * a ** (3 - k), lna, initial=0)
        Xi = (1 - Om - Or) * rho_c0 / rho[-1]
        E_new = np.sqrt(Om * a ** -3 + Or * a ** -4 + Xi * rho / rho_c0)
        if np.max(abs(E_new / E - 1)) < 1e-10:
            break
        E = E_new
    return E, Xi * rho / rho_c0, Xi


def chi2(E):
    zz, inv = z[::-1], (1 / E)[::-1]
    D = np.interp(zs, zz, cumulative_trapezoid(inv, zz, initial=0)) * (1 + zs)
    r = mu - 5 * np.log10(D)
    return float(np.sum(w * (r - np.sum(w * r) / np.sum(w)) ** 2))


out = {"n_sne": int(len(zs))}
best = minimize_scalar(lambda Om: chi2(lcdm_E(Om)), bounds=(0.1, 0.6), method="bounded")
out["LCDM"] = {"Om": round(best.x, 3), "chi2": round(best.fun, 1)}
for k in [0, 1, 2, 3, 4]:
    r = minimize_scalar(lambda Om: chi2(ccbh(Om, k)[0]), bounds=(0.05, 0.95), method="bounded")
    E, rde, Xi = ccbh(r.x, k)
    wde = -1 - np.gradient(np.log(np.maximum(rde, 1e-300)), lna) / 3
    out[f"k={k}"] = {"Om": round(r.x, 3), "chi2": round(r.fun, 1), "dchi2_vs_LCDM": round(r.fun - best.fun, 1),
                     "BH_mass_per_star_mass": round(Xi, 2), "w_today": round(float(wde[-1]), 3),
                     "w_z1": round(float(np.interp(-np.log(2), lna, wde)), 3)}
E3, rde3, _ = ccbh(out["k=3"]["Om"], 3)
out["k=3_dark_energy_share_of_today"] = {f"z={x}": round(float(np.interp(-np.log(1 + x), lna, rde3 / rde3[-1])), 3)
                                         for x in [0.5, 1, 2, 3, 4, 6]}
text = json.dumps(out, indent=1)
(OUT / "coupled_bh_expansion_look_2026-11-07.txt").write_text(text, newline="\n")
print(text)
