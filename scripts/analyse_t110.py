"""T110 read by its registered words (PREREGISTRATION.md). Usage:

    python scripts/analyse_t110.py [results/t110_growth_scaled_window] [results/t110_growth_scaled_window_heldout]

T110, growth at a time that scales with the length (T109's replacement, her words of 7 November 2026): per length,
the share of replicas in which the outside foot's gain over the scaled window (from the second-largest to the largest
recorded time after the escape, both scaled with L) is positive; the verdict HOLDS if the share is above one half at
every fitting length; the held-out number is the mean of the fitting shares plus or minus 0.15. Read beside it, not
scored: the inside foot's gain over the same window, and its size against the band's. Pure reading; writes nothing.
"""
import sys

import numpy as np
import pandas as pd


def read(stem):
    f = pd.read_csv(stem + "_feet.csv")
    f = f[f["escape"].notna()]
    out = {}
    for L, g in f.groupby("L"):
        dts = sorted(g["dt"].unique())
        lo, hi = dts[-2], dts[-1]
        p = g[g["dt"].isin([lo, hi])].pivot_table(index="replica", columns="dt", values=["inside", "outside", "band_points"])
        gain_out = p["outside"][hi] - p["outside"][lo]
        gain_in = p["inside"][hi] - p["inside"][lo]
        out[int(L)] = dict(window=(int(lo), int(hi)), n=int(len(gain_out)), share=float((gain_out > 0).mean()),
                           gain_out_median=float(gain_out.median()), gain_in_median=float(gain_in.median()),
                           inside_over_band=float((p["inside"][hi] / p["band_points"][hi]).median()),
                           escaped=int(g["replica"].nunique()))
    return out


def report(stem, label):
    out = read(stem)
    print(f"== {label}: {stem}")
    for L, r in sorted(out.items()):
        print(f"L {L:4d}: window {r['window'][0]} to {r['window'][1]} sweeps after the escape; outside gain positive in "
              f"{r['share']:.2f} of {r['n']} replicas (median gain out {r['gain_out_median']:+.0f}, in "
              f"{r['gain_in_median']:+.0f}); inside foot over band {r['inside_over_band']:.2f}")
    shares = [r["share"] for _, r in sorted(out.items())]
    print("  verdict on these lengths:", "HOLDS" if all(s > 0.5 for s in shares) else "FAILS")
    print(f"  mean share {np.mean(shares):.2f}; held-out range if these are the fitting lengths: "
          f"{np.mean(shares) - 0.15:.2f} to {np.mean(shares) + 0.15:.2f}")
    return out


if __name__ == "__main__":
    fit = sys.argv[1] if len(sys.argv) > 1 else "results/t110_growth_scaled_window"
    held = sys.argv[2] if len(sys.argv) > 2 else "results/t110_growth_scaled_window_heldout"
    report(fit, "fitting lengths")
    try:
        report(held, "held out")
    except FileNotFoundError:
        print("(held-out not run yet)")
