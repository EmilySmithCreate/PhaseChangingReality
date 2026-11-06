"""Sandbox look (6 November 2026, night; T106's question before it is registered): her moves with her clock on the
opened tube six around (graphity.tubes.twisted_tube, the exact end state of the tube's opening, O116) against the
flat torus of the same point count. Stores per pair at the freeze as lambda rises, under the one-number rule (T105's)
and the second-number rule (6 November). A look, not a test; her prediction for T106 is owed before any registration."""
import sys

import numpy as np

from graphity.cqg import NO_CAP, torus
from graphity.curl_pair_moves import PairMoves
from graphity.curl_pairs import CurlState
from graphity.tubes import twisted_tube


def cell(adj, part, lam, seed, rule):
    pm = PairMoves(CurlState(adj, part), lam=lam, barrier=12.0, seed=seed, price_from="gravity", clock="simultaneous",
                   twist_rule=rule)
    c = pm.run()
    return c["stores"] / max(c["pairs_made"], 1), c["stores"], c["pairs_made"], c["gluons_plus"] + c["gluons_minus"]


if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 36        # 4 x 36 = 144 points; the torus 12 x 12
    reps = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    side = int(round((4 * L) ** 0.5))
    for rule in ("one_number", "second_number"):
        for lam in (1.25, 1.5, 2.0):
            rows = {"twisted tube six around": [], "flat torus, same N": []}
            for rep in range(reps):
                seed = 20261106 + 97 * rep + int(lam * 100)
                adj, part = twisted_tube(L, 2)
                rows["twisted tube six around"].append(cell(adj, part, lam, seed, rule))
                adj, part = torus(side, side, NO_CAP)
                rows["flat torus, same N"].append(cell(adj, part, lam, seed, rule))
            for name, r in rows.items():
                spp = np.array([x[0] for x in r]); st = np.array([x[1] for x in r]); pm = np.array([x[2] for x in r]); gl = np.array([x[3] for x in r])
                print(f"{rule:14s} lam {lam:.2f} {name:24s} (N {4 * L if 'tube' in name else side * side}): stores per pair "
                      f"{spp.mean():.3f} +- {spp.std():.3f}; stores {st.mean():.1f}; pairs {pm.mean():.1f}; gluons {gl.mean():.1f}", flush=True)
