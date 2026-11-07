"""Ashley's look, 7 November 2026 (his crystal model, not the hypothesis; rule 16: a look, nothing registered).

His idea: the black hole's size sets the crystal's size or snap, and "perhaps that leads to parts of the
universe expanding faster than others". Nearby galaxy-cluster studies report a slower side near the
afterglow's lopsided direction. If that is the snap and not a local drift, it should persist far away.

Data: Pantheon+ (Scolnic et al. 2022; Brout et al. 2022), public, downloaded to sandbox/out/ if missing.
One row per supernova (first per CID), calibrators out, diagonal errors only (the full covariance is not
used: a convention of this look). Residuals from flat LCDM (H0 73, Om 0.334; the offset is fitted away).
Per redshift band, a weighted monopole + dipole fit; the dipole in distance modulus mu is turned into a
fractional H0 dipole by dH/H = -dmu / 2.171. Reported: the slowdown toward (224, -22) and its spread from
20,000 shuffles of the residuals within the band (which keeps the sky coverage).
Needs pandas and astropy. Output: sandbox/out/sn_tilt_by_distance_look_2026-11-07.txt
"""
import json
import urllib.request
from pathlib import Path

import astropy.units as u
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy.cosmology import FlatLambdaCDM

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)
DATA = OUT / "PantheonPlusSH0ES.dat"
URL = ("https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/"
       "Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat")
if not DATA.exists():
    urllib.request.urlretrieve(URL, DATA)

df = pd.read_csv(DATA, sep=r"\s+")
df = df[df.IS_CALIBRATOR == 0].drop_duplicates("CID")
cosmo = FlatLambdaCDM(H0=73.0, Om0=0.334)
g = SkyCoord(ra=df.RA.values * u.deg, dec=df.DEC.values * u.deg).galactic
n = np.stack([np.cos(g.b.rad) * np.cos(g.l.rad), np.cos(g.b.rad) * np.sin(g.l.rad), np.sin(g.b.rad)], 1)
LOP = np.array([np.cos(np.radians(-22)) * np.cos(np.radians(224)),
                np.cos(np.radians(-22)) * np.sin(np.radians(224)), np.sin(np.radians(-22))])
rng = np.random.default_rng(5)
BANDS = [("nearby", 0.02, 0.07), ("middle", 0.07, 0.2), ("far", 0.2, 0.4), ("farthest", 0.4, 2.3)]


def fit(res, w, nn):
    X = np.column_stack([np.ones(len(res)), nn])
    return np.linalg.solve(X.T @ (X * w[:, None]), X.T @ (w * res))


out = {}
for zkey in ["zCMB", "zHD"]:   # zHD has the nearby galaxies' motions corrected; zCMB does not
    z = df[zkey].values
    res = df.MU_SH0ES.values - cosmo.distmod(z).value
    w = 1 / df.MU_SH0ES_ERR_DIAG.values ** 2
    rows = []
    for name, lo, hi in BANDS:
        m = (z >= lo) & (z < hi)
        r, ww, nn = res[m], w[m], n[m]
        dH = -fit(r, ww, nn)[1:] / 2.171
        amp = np.linalg.norm(dH)
        slow = -dH / amp
        along = float(-(dH @ LOP))
        amps, alongs = np.empty(20000), np.empty(20000)
        for i in range(20000):
            p = rng.permutation(m.sum())
            d = -fit(r[p], ww[p], nn)[1:] / 2.171
            amps[i], alongs[i] = np.linalg.norm(d), -(d @ LOP)
        rows.append({"band": name, "n": int(m.sum()), "z_median": round(float(np.median(z[m])), 3),
                     "tilt_pct": round(100 * amp, 2),
                     "slow_side_l_b": [round(float(np.degrees(np.arctan2(slow[1], slow[0])) % 360)),
                                       round(float(np.degrees(np.arcsin(slow[2]))))],
                     "p_tilt": float((amps >= amp).mean()),
                     "slower_toward_224_-22_pct": round(100 * along, 2),
                     "shuffle_sd_pct": round(100 * float(alongs.std()), 2)})
    out[zkey] = rows
text = json.dumps(out, indent=1)
(OUT / "sn_tilt_by_distance_look_2026-11-07.txt").write_text(text, newline="\n")
print(text)
