"""Sandbox look, exact arithmetic (6 November 2026, night; her decision of the same night that gravity acts in two
and three dimensions, so the lengths need a four-link form): the published curvature of the four-link toy written
over link lengths, and how the flat sheet's energy changes when lengths are perturbed link by link. The archive's
`sandbox/regge_step1_stiffness.py` did this for six links and found H = (1/2) delta^T K delta with K = 4 (6 I - A)
per axis family. This is the same arithmetic on the square lattice (D = 2).

Definitions ([T25] Sec. II.2): m_x the uniform measure on the k = 4 neighbours of x; W(m_x, m_y) the transport
cost with shortest-path distances over the lengths; kappa(x, y) = 1 - W / d(x, y); H_curv = -4 D sum over links of
kappa, D = 2. The flat sheet has kappa = 0 on every link.

WRITTEN BEFORE COMPUTING (ours, by the six-link result's form): one link lengthened by delta changes H by
8 delta^2 / (1 + delta) (the six-link value 12 delta^2 / (1 + delta) with 2D - 2 = 2 squares per link in place of
4); two parallel neighbours give a mixed term of -4 delta^2 / (1 + delta) each; a perpendicular neighbour gives
zero; uniform scaling gives zero. If so K = 4 (4 I - A) per family: 4 times the square-lattice Laplacian, gapless.
What would refute it: a different diagonal, a non-zero perpendicular term, or a term that does not decay.
"""
import heapq
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from graphity.cqg import NO_CAP, torus  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 8
D = 2
adj, part = torus(L, L, NO_CAP)          # index i = x * L + y
N = adj.shape[0]
EDGES = sorted({(min(u, int(v)), max(u, int(v))) for u in range(N) for v in adj[u]})
assert len(EDGES) == 2 * N
length = {e: 1.0 for e in EDGES}
NB = {u: [int(v) for v in adj[u]] for u in range(N)}


def dijkstra(src, radius):
    dist = {src: 0.0}
    heap = [(0.0, src)]
    while heap:
        d, p = heapq.heappop(heap)
        if d > dist[p] or d > radius:
            continue
        for q in NB[p]:
            nd = d + length[(min(p, q), max(p, q))]
            if nd < dist.get(q, np.inf):
                dist[q] = nd
                heapq.heappush(heap, (nd, q))
    return dist


def kappa(x, y):
    A, B = NB[x], NB[y]
    k = len(A)
    cost = np.empty((k, k))
    for i, a in enumerate(A):
        da = dijkstra(a, 6.0)
        for j, b in enumerate(B):
            cost[i, j] = da[b]
    c = cost.ravel()
    Aeq = np.zeros((2 * k, k * k))
    for i in range(k):
        Aeq[i, i * k:(i + 1) * k] = 1
        Aeq[k + i, i::k] = 1
    res = linprog(c, A_eq=Aeq, b_eq=np.full(2 * k, 1.0 / k), bounds=(0, None), method="highs")
    assert res.success
    return 1.0 - res.fun / length[(min(x, y), max(x, y))]


def hops(src, r):
    seen = {src}
    frontier = [src]
    for _ in range(r):
        frontier = [q for p in frontier for q in NB[p] if q not in seen]
        seen.update(frontier)
    return seen


KAP = {}


def energy_full():
    for e in EDGES:
        KAP[e] = kappa(*e)
    return -4 * D * sum(KAP.values())


def energy_after(changed):
    near = set()
    for e in changed:
        near |= hops(e[0], 4) | hops(e[1], 4)
    for e in EDGES:
        if e[0] in near or e[1] in near:
            KAP[e] = kappa(*e)
    return -4 * D * sum(KAP.values())


H0 = energy_full()
print("four-link sheet L = %d, N = %d, links %d; flat energy %.6f; max |kappa| on the flat sheet %.2e" % (
    L, N, len(EDGES), H0, max(abs(v) for v in KAP.values())), flush=True)
K0 = dict(KAP)

coords = np.array(np.unravel_index(np.arange(N), (L, L))).T
idx = {tuple(c): i for i, c in enumerate(coords)}


def link(c, axis):
    a = idx[tuple(c)]
    cc = list(c); cc[axis] = (cc[axis] + 1) % L
    b = idx[tuple(cc)]
    return (min(a, b), max(a, b))


e0 = link((0, 0), 0)     # the x-link at the origin

print("\n(2) one link, length 1 + delta: change in H_curv (prediction 8 delta^2 / (1 + delta))")
for delta in (-0.2, -0.1, -0.05, -0.02, 0.02, 0.05, 0.1, 0.2):
    length[e0] = 1.0 + delta
    H = energy_after([e0])
    length[e0] = 1.0
    KAP.update(K0)
    print("   delta = %+.2f   dH = %+.6f   predicted %+.6f   dH/delta^2 = %+.4f" % (
        delta, H - H0, 8 * delta ** 2 / (1 + delta), (H - H0) / delta ** 2), flush=True)

length[e0] = 1.05
Hloc = energy_after([e0]); KAP.update(K0)
Hfull = energy_full()
length[e0] = 1.0; KAP.update(K0)
print("   locality check at delta = 0.05: local %.6f full %.6f" % (Hloc - H0, Hfull - H0), flush=True)

print("\n(3) two links at delta = 0.05 each: mixed term M = H(e,f) - H(e) - H(f) + H0 (prediction: parallel neighbours -4 delta^2/(1+delta) = %.6f, else 0)" % (-4 * 0.05 ** 2 / 1.05))
delta = 0.05
length[e0] = 1 + delta
He = energy_after([e0]); KAP.update(K0); length[e0] = 1.0
cases = [("same axis, +1 along", (1, 0), 0), ("same axis, +2 along", (2, 0), 0), ("same axis, +3 along", (3, 0), 0),
         ("parallel, 1 across", (0, 1), 0), ("parallel, 2 across", (0, 2), 0), ("parallel, 3 across", (0, 3), 0),
         ("perpendicular at origin", (0, 0), 1), ("perpendicular at far end", (1, 0), 1), ("perpendicular, 2 away", (0, 2), 1)]
for name, c, axis in cases:
    f = link(c, axis)
    length[f] = 1 + delta
    Hf = energy_after([f]); KAP.update(K0)
    length[e0] = 1 + delta
    Hef = energy_after([e0, f]); KAP.update(K0)
    length[e0] = 1.0; length[f] = 1.0
    print("   %-26s  dH(e) %+.5f  dH(f) %+.5f  mixed M %+.6f" % (name, He - H0, Hf - H0, Hef - He - Hf + H0), flush=True)

print("\n(4) uniform scaling, every link 1 + delta (prediction: zero)")
for delta in (0.05, 0.2):
    for e in EDGES:
        length[e] = 1 + delta
    H = energy_full()
    for e in EDGES:
        length[e] = 1.0
    KAP.update(K0)
    print("   delta = %+.2f   dH = %+.6f" % (delta, H - H0), flush=True)
