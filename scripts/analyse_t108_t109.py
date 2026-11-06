"""T108 and T109 read by their registered words (PREREGISTRATION.md). Usage:

    python scripts/analyse_t108_t109.py [results/t108_t109_size_and_growth] [results/t108_t109_size_and_growth_heldout]

T108, the size of the surplus against length: per length the median of her ratio, |net twist outside| over (curl
left on squares + held in stores), under her kind rule among replicas with a straddling pair; the fit of the median
to a over L on the fitting lengths (a by least squares in log space, the exponent reported beside it); the verdict.
T109, growth: per length the share of replicas in which the outside foot's gain from 200 to 500 sweeps after the
escape exceeds the inside foot's gain; the verdict. Pure reading; writes nothing.
"""
import sys

import numpy as np
import pandas as pd


def read(stem):
    return pd.read_csv(f"{stem}_feet.csv"), pd.read_csv(f"{stem}_kind.csv")


def report(feet, kind):
    out = {}
    for L, f in feet.groupby("L"):
        n = f["replica"].nunique()
        p = f[f["dt"].isin([200, 500])].pivot_table(index="replica", columns="dt", values=["inside", "outside"])
        gain_in = p["inside"][500] - p["inside"][200]
        gain_out = p["outside"][500] - p["outside"][200]
        growth = float((gain_out > gain_in).sum()) / n
        k = kind[(kind["L"] == L) & (kind["rule"] == "boundary") & (kind["outward_kind"] != 0)]
        ratio = np.abs(k["twist_out"]) / (k["stored_on_squares"] + k["held_in_stores"])
        out[L] = dict(n=n, growth=growth, gain_in_median=float(gain_in.median()), gain_out_median=float(gain_out.median()),
                      ratio_median=float(ratio.median()), ratio_mean=float(ratio.mean()), straddling=int(len(k)),
                      escape_median=float(f.groupby("replica")["escape"].first().median()))
    return out


def fit_one_over_L(out):
    Ls = np.array(sorted(out)); r = np.array([out[L]["ratio_median"] for L in Ls])
    ok = r > 0
    slope, intercept = np.polyfit(np.log(Ls[ok]), np.log(r[ok]), 1)
    a = float(np.exp(np.mean(np.log(r[ok]) + np.log(Ls[ok]))))      # the a of a/L by least squares in log space
    return a, float(slope)


if __name__ == "__main__":
    stems = sys.argv[1:] or ["results/t108_t109_size_and_growth"]
    for stem in stems:
        out = report(*read(stem))
        print(f"== {stem}")
        for L, r in sorted(out.items()):
            print(f"L {L:4d}: escape median {r['escape_median']:.0f}; T108 ratio median {r['ratio_median']:.4f} (mean {r['ratio_mean']:.4f}, "
                  f"{r['straddling']} straddling); T109 outside gained more than inside in {r['growth']:.2f} "
                  f"(median gains in {r['gain_in_median']:+.0f}, out {r['gain_out_median']:+.0f})")
        if len(out) >= 3:
            a, slope = fit_one_over_L(out)
            print(f"  T108 fit on these lengths: ratio = {a:.3f} / L (log-log slope {slope:.2f}; 1/L would be -1.00)")
        print("  T109 verdict on these lengths:", "HOLDS" if all(r["growth"] > 0.5 for r in out.values()) else "FAILS")
        print("  T108 verdict on these lengths:", "FALLS" if all(out[a]["ratio_median"] > out[b]["ratio_median"] for a, b in zip(sorted(out), sorted(out)[1:])) else "NOT MONOTONE")
