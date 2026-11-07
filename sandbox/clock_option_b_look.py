"""Sandbox look (7 November 2026; option B built the same day): the clock field round one planted knot on the sheet
(the four-link lengths) and round one switch in the cube (the six-link lengths), by distance from the knot, at
alpha = -0.5 (the tests' value; T84 ran a landscape in alpha). Reports the mean tick rate per distance band and the
fall-off of the slowing, 1 - rate, between bands. A look, not a test: the form of the fall-off is hers to predict
before anything is registered (brief: docs/design/clock_option_b_2026-11-07.md). Writes sandbox/out/."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graphity import clock, lengths                                  # noqa: E402
from graphity.cqg import NO_CAP, torus                               # noqa: E402
from graphity.cqg_d import _switch as switch_d, is_valid as valid_d, torus as torus_d   # noqa: E402
from graphity.dimension import local_dimension                       # noqa: E402
from run_clock_knot import distance_to, plant_knot                   # noqa: E402

ALPHA = -0.5


def bands(rate, dist, lines, label):
    lines.append(f"  {label}: mean rate by distance from the knot (1 - rate in brackets)")
    prev = None
    for d in range(int(dist.max()) + 1):
        sel = dist == d
        if not sel.any():
            continue
        r = rate[sel].mean(); s = 1 - r
        ratio = f"  slowing ratio to previous band {s / prev:.3f}" if prev not in (None, 0) and s > 0 else ""
        lines.append(f"    d = {d:2d} ({sel.sum():4d} points): rate {r:.5f} ({s:+.5f}){ratio}")
        prev = s if s > 0 else None
    lines.append(f"    mean of 1/rate over all points: {(1 / rate).mean():.12f} (exact 1)")


def sheet(L, seed, lines):
    adj, part = torus(L, L, NO_CAP)
    plant_knot(adj, part, np.random.default_rng(seed))
    rate, delta = clock.clock_field(adj, (L, L), ALPHA)
    knot = np.flatnonzero(local_dimension(adj) != 2)
    dist = distance_to(adj, knot).reshape(L, L)
    lines.append(f"sheet {L} x {L}, one planted switch, {len(knot)} knot points, alpha {ALPHA}")
    bands(rate, dist, lines, "sheet")


def cube(L, seed, lines):
    rng = np.random.default_rng(seed)
    adj, part = torus_d((L, L, L))
    n = adj.shape[0]
    for _ in range(100000):                                            # one valid switch near point 0, as on the sheet
        u1 = 0; u2 = int(rng.integers(n))
        v1 = int(adj[u1, rng.integers(6)]); v2 = int(adj[u2, rng.integers(6)])
        if len({u1, v1, u2, v2}) < 4 or (adj[u2] == v1).any() or (adj[u1] == v2).any():
            continue
        switch_d(adj, u1, v1, u2, v2)
        if valid_d(adj):
            break
        switch_d(adj, u1, v2, u2, v1)
    dims = (L, L, L)
    rate, delta = clock.clock_field(adj, dims, ALPHA)
    f = lengths.curl_fields(adj, dims)
    knot_links = np.argwhere(f.sum(axis=0) > 0)
    knot = [int(np.ravel_multi_index(tuple(p), dims)) for p in knot_links]
    dist = distance_to(adj, knot).reshape(dims)
    lines.append(f"cube {L}^3, one switch, {len(knot)} points with curl on a link, alpha {ALPHA}")
    bands(rate, dist, lines, "cube")


if __name__ == "__main__":
    lines = []
    for L in (16, 32):
        sheet(L, 3, lines)
    cube(12, 3, lines)
    out = Path("sandbox/out"); out.mkdir(exist_ok=True)
    (out / "clock_option_b_look_2026-11-07.txt").write_bytes("\n".join(lines).encode("utf-8") + b"\n")
    print("\n".join(lines))
