"""SANDBOX LOOK (20 November 2026; rule 16: a look, nothing registered). The published recipe for "a jump or
smooth?" (Aharony, Marsano, Minwalla, Papadodimas and Van Raamsdonk 2003, arXiv hep-th/0310285; read from its TeX
source, sections 1, 5.7, 6.3 and 7.3) asks one thing of a space with a direction curled into a circle: what does
the light field read going once round the circle? Their statement (section 7.3): the reading is zero when the circle
is not filled in, and can be non-zero only when it is filled in, which in their setting is a black hole.

THE TOY'S OBJECT. Term 10 of the toy (graphity.u1): a phase on every link, the squares as its loops, weight
exp(beta * sum over squares of cos(holonomy)). The reading round a closed path is W, the signed sum of the link
phases along it. NOT HER LIGHT: her light travels the body diagonals and exists only in three dimensions (her
decisions of 28 October and 6 November); term 10 is the published lattice photon on the links, built and kept for
looks. What this look can carry over to her picture is the criterion, not the photon.

EXACT METHOD (the character expansion of two-dimensional lattice gauge theory, the same one behind
graphity.u1.exact_mean_cos_2d): with B the squares-by-links matrix,
    <exp(i k W)> = sum over whole-number q with q B = k w of prod_p I_{q_p}(beta)
                   / sum over whole-number q with q B = 0 of prod_p I_{q_p}(beta),
w the path's signed link vector, I_n the modified Bessel functions (all positive). So the reading is non-zero
EXACTLY when k w is a whole-number combination of squares: when the loop, taken k times, is filled in by squares.
That is decided here by exact integer row reduction, no floating point.

WRITTEN BEFORE COMPUTING (ours):
  E1. The tube (4 x L): the loop round the curl is itself a square, so it is filled in and reads non-zero.
      The opened tube six around: the loop round is never filled in, and reads exactly zero at every k.
  E2. The flat one-sided sheet (Klein bottle): the loop along the direction that the one-sided trip reverses is
      filled in only when taken twice, so the light reads it in halves (W is 0 or a half turn for a flat field);
      the loop that makes the one-sided trip is never filled in.
  E3. Two round-loops a distance l apart along the tube. Opened tube: the reading of one against the other falls
      as (I_1/I_0)^(4 l), a cost growing in a straight line with l (a linear bond, 4 squares per step). Tube: it
      levels off at the square of one loop's reading (no bond).
  E4. Light adds to the curling cost at every stiffness, by less than stiffness/4 per point.
  E5. On the tube the loop's own potential V(W) = -ln P(W) is a single well at W = 0 at every stiffness; on the
      opened tube it is exactly flat. So with one-phase light nothing in V can decide a jump.

CHECK AGAINST THE BUILT SAMPLER (rule 2): the tube's average square from the transfer matrix against
graphity.u1's Metropolis chain; the opened tube's against exact_mean_cos_2d (the registered gate's formula).

SECOND RUN, the same day (output _r2). The first run's output, sandbox/out/wilson_line_look_2026-11-20.txt, is
kept; E1 to E5 all held in it. Its Part 5 printed "nan" at beta 4 and 8: the potential was summed from 11
harmonics, too few at those stiffnesses, a slip in the look and not a result. Part 5 now sums 60. Parts 1 to 4 are
unchanged and print the same numbers. Added, written before computing (ours):
  E6. In three directions (six links). The curled slab 4 x 6 x 6: the loop round the curl is filled in (k = 1),
      the loops along the open directions never. A cubic space glued to itself by a third of a turn about a body
      diagonal (the cube's threefold axis) with a slide of (2, 2, 2) along it, the "third-turn space" of the
      published list of flat three-dimensional spaces (general knowledge, to verify): a loop lying across the axis
      is filled in only when taken THREE times, so light reads it in thirds; the loop along the axis never.
      No closed sheet can do this: a closed surface's loops fill after once or twice or never (general knowledge,
      to verify), which Part 1 shows for the five sheets here.

Usage: python sandbox/wilson_line_look.py     (writes sandbox/out/wilson_line_look_2026-11-20_r2.txt)
"""
import sys
from collections import deque
from pathlib import Path

import numpy as np
from scipy.special import ive

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity.cqg_d import torus                             # noqa: E402
from graphity.tubes import twisted_tube                      # noqa: E402
from graphity.u1 import Field, exact_mean_cos_2d             # noqa: E402
from read_flat_kind import klein_bottle                      # noqa: E402

L = 12
BETAS = (0.5, 1.0, 2.0, 4.0, 8.0)
NMAX = 14


# ---------------------------------------------------------------- wirings and paths
def two_colour(adj):
    part = -np.ones(len(adj), dtype=np.int64)
    part[0] = 0
    queue = deque([0])
    while queue:
        p = queue.popleft()
        for q in adj[p]:
            q = int(q)
            if part[q] < 0:
                part[q] = 1 - part[p]
                queue.append(q)
            elif part[q] == part[p]:
                raise ValueError("not two-colourable")
    return part


def link_vector(field, path):
    """Signed link vector of the closed path (a list of points, the last joined back to the first)."""
    w = [0] * field.n_links
    for a, b in zip(path, path[1:] + path[:1]):
        if b not in set(int(x) for x in field.adj[a]):
            raise ValueError(f"{a} and {b} are not linked")
        if field.part[a] == 0:
            w[field.index[(a, b)]] += 1
        else:
            w[field.index[(b, a)]] -= 1
    return w


# ---------------------------------------------------------------- exact integer row lattice
def echelon(rows):
    """An echelon basis of the whole-number row lattice (exact, Python integers)."""
    rows = [list(map(int, r)) for r in rows]
    n_cols = len(rows[0])
    out, r = [], 0
    for c in range(n_cols):
        live = [i for i in range(r, len(rows)) if rows[i][c] != 0]
        if not live:
            continue
        while len(live) > 1:
            live.sort(key=lambda i: abs(rows[i][c]))
            p = live[0]
            for i in live[1:]:
                f = rows[i][c] // rows[p][c]
                if f:
                    rows[i] = [x - f * y for x, y in zip(rows[i], rows[p])]
            live = [i for i in live if rows[i][c] != 0]
        p = live[0]
        rows[r], rows[p] = rows[p], rows[r]
        out.append((c, rows[r]))
        r += 1
    return out


def in_lattice(ech, w):
    w = list(w)
    for c, row in ech:
        if w[c] % row[c]:
            return False
        f = w[c] // row[c]
        if f:
            w = [x - f * y for x, y in zip(w, row)]
    return not any(w)


def fill_order(ech, w, kmax=4):
    """The smallest k for which the loop taken k times is filled in by squares; None if none up to kmax."""
    for k in range(1, kmax + 1):
        if in_lattice(ech, [k * x for x in w]):
            return k
    return None


# ---------------------------------------------------------------- exact readings where the squares' null space is 0 or 1
def ratio(n, beta):
    return ive(np.abs(n), beta) / ive(0, beta)


def reading(field, w, beta):
    """<exp(i W)> for the link vector w, exact, for wirings whose squares have at most one closed combination."""
    B = field.B.toarray().astype(float)
    P = field.n_squares
    null = P - np.linalg.matrix_rank(B)
    q = np.linalg.lstsq(B.T, np.asarray(w, dtype=float), rcond=None)[0]
    if null == 0:
        e = np.zeros(P)
    elif null == 1:
        e = field.square_signs().astype(float)
        q = q - (q[0] - np.round(q[0])) * e / e[0]
    else:
        raise ValueError(f"{null} closed combinations of squares: use the transfer matrix")
    qi = np.round(q).astype(np.int64)
    if not np.array_equal(qi @ field.B.toarray().astype(np.int64), np.asarray(w, dtype=np.int64)):
        return 0.0                                              # no whole-number filling: the reading is exactly zero
    ei = e.astype(np.int64)
    ns = np.arange(-NMAX, NMAX + 1) if null else np.array([0])
    num = sum(np.exp(np.sum(np.log(ratio(qi + n * ei, beta)))) for n in ns)
    den = sum(np.exp(np.sum(np.log(ratio(n * ei, beta)))) for n in ns) if null else 1.0
    return float(num / den)


# ---------------------------------------------------------------- the tube by transfer matrix
class TubeLight:
    """Light on the 4 x L tube, exact. A closed combination of squares is a whole number n_y on the ring of four
    faces between columns y and y + 1 together with n_y - n_(y-1) on the wrap square at column y. So
        Z / I_0^(5 L) = sum over n of prod_y r(n_y)^4 r(n_y - n_(y-1)),   r(n) = I_n / I_0.
    The number of closed combinations is checked against the wiring (squares minus the rank of B)."""

    def __init__(self, length, beta, nmax=NMAX):
        self.length, self.beta = length, beta
        ns = np.arange(-nmax, nmax + 1)
        self.ns = ns
        self.a = ratio(ns, beta) ** 4
        self.diff = ns[:, None] - ns[None, :]
        self.T = self._matrix(0)
        self.lnz = self._lntrace([self.T] * length)

    def _matrix(self, k, face=False):
        s = np.sqrt(self.a)
        d = ratio(self.diff + k, self.beta)
        m = s[:, None] * d * s[None, :]
        if face:                                                # one face factor r(n) replaced by its cos-inserted form
            n = self.ns
            ins = 0.5 * (ratio(n - 1, self.beta) + ratio(n + 1, self.beta)) / ratio(n, self.beta)
            m = m * ins[:, None]
        return m

    @staticmethod
    def _lntrace(mats):
        m, ln = np.eye(mats[0].shape[0]), 0.0
        for x in mats:
            m = m @ x
            s = np.abs(m).max()
            m, ln = m / s, ln + np.log(s)
        return ln + np.log(np.trace(m))

    def wrap(self, k=1):
        """<exp(i k W)> for the loop round the curl."""
        return float(np.exp(self._lntrace([self._matrix(k)] + [self.T] * (self.length - 1)) - self.lnz))

    def face_cos(self):
        return float(np.exp(self._lntrace([self._matrix(0, face=True)] + [self.T] * (self.length - 1)) - self.lnz))

    def wrap_cos(self):
        both = 0.5 * (self._matrix(1) + self._matrix(-1))
        return float(np.exp(self._lntrace([both] + [self.T] * (self.length - 1)) - self.lnz))

    def pair(self, sep):
        """<exp(i (W_0 - W_sep))> for two loops round the curl, sep columns apart."""
        mats = [self._matrix(1)] + [self.T] * (sep - 1) + [self._matrix(-1)] + [self.T] * (self.length - sep - 1)
        return float(np.exp(self._lntrace(mats) - self.lnz))


# ---------------------------------------------------------------- the third-turn space on the cubic lattice
def third_turn_space(n=4):
    """Six-link wiring of the cubic lattice glued by g: (x, y, z) -> (y, z, x) + (2, 2, 2), a third of a turn about
    the body diagonal with a slide along it, and by the translations (n, -n, 0), (0, n, -n) across the axis; g three
    times is the translation (6, 6, 6). Every identification joins points at least six steps apart, so the wiring
    is the cubic lattice near every point. Returns (adj, part, canon) with canon the map from a lattice point to
    its index."""
    basis = np.array([[n, -n, 0], [0, n, -n], [6, 6, 6]], dtype=np.int64)
    det = int(round(np.linalg.det(basis)))
    adjugate = np.round(det * np.linalg.inv(basis)).astype(np.int64)
    assert np.array_equal(adjugate @ basis, det * np.eye(3, dtype=np.int64))

    def reduce(p):
        c = (np.asarray(p, dtype=np.int64) @ adjugate) // det      # floor of the coordinates in the basis
        return tuple(int(v) for v in np.asarray(p, dtype=np.int64) - c @ basis)

    def turn(p):
        return (p[1] + 2, p[2] + 2, p[0] + 2)

    def rep(p):
        a = reduce(p)
        b = reduce(turn(a))
        c = reduce(turn(b))
        return min(a, b, c)

    reps = sorted({rep((x, y, z)) for x in range(-n, 2 * n + 6) for y in range(-n, 2 * n + 6)
                   for z in range(-n, 2 * n + 6)})
    assert len(reps) == 6 * n * n, len(reps)
    index = {p: i for i, p in enumerate(reps)}
    adj = np.empty((len(reps), 6), dtype=np.int64)
    for i, p in enumerate(reps):
        k = 0
        for axis in range(3):
            for step in (1, -1):
                q = list(p)
                q[axis] += step
                adj[i, k] = index[rep(q)]
                k += 1
    part = np.array([sum(p) % 2 for p in reps], dtype=np.int64)
    return adj, part, lambda p: index[rep(p)]


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "wilson_line_look_2026-11-20_r2.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    # ---- the wirings
    adj_t, part_t = torus([L, 4])                               # the tube: index y * 4 + x
    adj_o, part_o = twisted_tube(L)                             # the opened tube six around: index x * L + y
    adj_f, part_f = torus([L, 6])                               # a flat torus six around: index y * 6 + x
    adj_k = klein_bottle(6, L)                                  # the flat one-sided sheet: index x * L + y
    adj_r = klein_bottle(4, L)                                  # the Klein relative of the tube (T102's wiring)
    tube, opened, flat = Field(adj_t, part_t), Field(adj_o, part_o), Field(adj_f, part_f)
    klein, rel = Field(adj_k, two_colour(adj_k)), Field(adj_r, two_colour(adj_r))

    def round_opened(y):
        return [0 * L + y % L, 1 * L + y % L, 2 * L + y % L, 3 * L + y % L, 0 * L + (y - 2) % L, 0 * L + (y - 1) % L]

    def trip_klein(around, y):                                  # the one-sided trip: round x, arriving at -y, back to y
        path = [x * L + y % L for x in range(around)]
        yy = (-y) % L
        while yy != y % L:
            path.append(0 * L + yy)
            yy = (yy + 1) % L
        return path

    cases = [
        ("the tube 4 x 12", tube, [("round the curl (4 links)", [0 * 4 + x for x in range(4)]),
                                    ("along the tube (12 links)", [y * 4 + 0 for y in range(L)])]),
        ("the opened tube six around", opened, [("round (6 links)", round_opened(0)),
                                                 ("along (12 links)", [0 * L + y for y in range(L)])]),
        ("a flat torus 6 x 12", flat, [("round (6 links)", [0 * 6 + x for x in range(6)]),
                                        ("along (12 links)", [y * 6 + 0 for y in range(L)])]),
        ("the flat one-sided sheet 6 x 12", klein, [("the one-sided trip, at y = 0 (6 links)", trip_klein(6, 0)),
                                                     ("the one-sided trip, at y = 3 (12 links)", trip_klein(6, 3)),
                                                     ("along the reversed direction (12 links)",
                                                      [0 * L + y for y in range(L)])]),
        ("the Klein relative of the tube 4 x 12", rel, [("the one-sided trip, at y = 0 (4 links, a square)",
                                                         trip_klein(4, 0)),
                                                        ("the one-sided trip, at y = 3 (10 links)", trip_klein(4, 3)),
                                                        ("along the reversed direction (12 links)",
                                                         [0 * L + y for y in range(L)])]),
    ]

    say("PART 1, exact (integer row reduction): is the loop filled in by squares, and how many times round?")
    say(f"{'wiring':<40} {'points':<7} {'squares':<8} {'closed combos':<14} loop: filled after k times round")
    for name, field, loops in cases:
        B = field.B.toarray().astype(np.int64)
        ech = echelon(B.tolist())
        null = field.n_squares - len(ech)
        say(f"{name:<40} {field.n:<7} {field.n_squares:<8} {null:<14}")
        for label, path in loops:
            k = fill_order(ech, link_vector(field, path))
            say(f"    {label:<52} {'never (to k = 4)' if k is None else 'k = ' + str(k)}")
    say()

    say("PART 2, exact: the reading <cos k W> of the loop round, at five stiffnesses")
    say(f"{'beta':<6} {'tube k=1':<10} {'tube k=2':<10} {'opened k=1':<11} {'opened k=2':<11} "
        f"{'one-sided, reversed loop k=1':<29} {'k=2':<8}")
    w_o = link_vector(opened, round_opened(0))
    w_k = link_vector(klein, [0 * L + y for y in range(L)])
    for beta in BETAS:
        t = TubeLight(L, beta)
        say(f"{beta:<6} {t.wrap(1):<10.6f} {t.wrap(2):<10.6f} {reading(opened, w_o, beta):<11.6f} "
            f"{reading(opened, [2 * x for x in w_o], beta):<11.6f} {reading(klein, w_k, beta):<29.6f} "
            f"{reading(klein, [2 * x for x in w_k], beta):<8.6f}")
    say()

    say("CHECK against the built sampler (graphity.u1 Metropolis, 2,000 + 20,000 sweeps, step 1.0, seed 20261120)")
    say(f"{'wiring':<28} {'beta':<6} {'exact mean cos':<16} {'sampled':<10} {'naive error':<12}")
    for beta in (1.0, 2.0):
        t = TubeLight(L, beta)
        exact = (4 * L * t.face_cos() + L * t.wrap_cos()) / (5 * L)
        _, series, _ = tube.metropolis(np.zeros(tube.n_links), beta, 1.0, 2000, 20000, 20261120)
        blocks = series.reshape(20, -1).mean(axis=1)
        say(f"{'the tube 4 x 12':<28} {beta:<6} {exact:<16.5f} {series.mean():<10.5f} {blocks.std(ddof=1) / 20 ** 0.5:<12.5f}")
        exact = exact_mean_cos_2d(beta, opened.n_squares)
        _, series, _ = opened.metropolis(np.zeros(opened.n_links), beta, 1.0, 2000, 20000, 20261120)
        blocks = series.reshape(20, -1).mean(axis=1)
        say(f"{'the opened tube':<28} {beta:<6} {exact:<16.5f} {series.mean():<10.5f} {blocks.std(ddof=1) / 20 ** 0.5:<12.5f}")
    say(f"closed combinations of squares on the tube, from the wiring: {tube.n_squares - np.linalg.matrix_rank(tube.B.toarray())}"
        f" (the transfer matrix assumes L = {L})")
    say()

    say("PART 3, exact: two round-loops l columns apart; cost F(l) = -ln <cos(W_0 - W_l)>")
    beta = 2.0
    sigma = -np.log(ratio(1, beta))
    t = TubeLight(L, beta)
    say(f"beta = {beta}; one square's bond cost sigma = -ln(I_1/I_0) = {sigma:.5f}; 4 sigma per column = {4 * sigma:.5f}; "
        f"tube: -2 ln <cos W> = {-2 * np.log(t.wrap(1)):.5f}")
    say(f"{'l':<4} {'opened tube F':<15} {'F / l':<10} {'tube F':<10}")
    for sep in range(1, L // 2 + 1):
        w = [a - b for a, b in zip(link_vector(opened, round_opened(0)), link_vector(opened, round_opened(sep)))]
        f_open = -np.log(reading(opened, w, beta))
        say(f"{sep:<4} {f_open:<15.5f} {f_open / sep:<10.5f} {-np.log(t.pair(sep)):<10.5f}")
    say()

    say("PART 4, exact: what light adds to the curled tube's free energy, per point, in units of the coupling g")
    say("(energy stiffness * (1 - cos) on every square; beta = stiffness / g; tube minus opened tube)")
    say(f"{'beta':<6} {'extra per point':<17} {'bound beta / 4':<15} {'extra / beta (units of stiffness)':<34}")
    for beta in BETAS:
        t = TubeLight(L, beta)
        ln_i0 = np.log(ive(0, beta))                            # ln(e^-beta I_0)
        ns = np.arange(-NMAX, NMAX + 1)
        ln_open = np.log(np.sum(ratio(ns, beta) ** opened.n_squares))
        extra = (-(5 * L) * ln_i0 - t.lnz + opened.n_squares * ln_i0 + ln_open) / (4 * L)
        say(f"{beta:<6} {extra:<17.6f} {beta / 4:<15.4f} {extra / beta:<34.6f}")
    say()

    say("PART 5, exact: the loop's own potential on the tube, V(W) - V(0) = -ln [P(W) / P(0)]")
    say(f"{'beta':<6} {'V(pi/2)':<10} {'V(pi)':<10} {'single well at 0':<17} opened tube")
    grid = np.linspace(0.0, np.pi, 181)
    for beta in BETAS:
        t = TubeLight(L, beta, nmax=70)
        c = [t.wrap(k) for k in range(1, 61)]
        p = 1.0 + 2.0 * sum(ck * np.cos((k + 1) * grid) for k, ck in enumerate(c))
        ok = bool(np.all(p > 0))
        v = -np.log(np.where(p > 0, p, np.nan) / p[0])
        well = bool(np.all(np.diff(p) < 0)) if ok else "beyond double precision"
        say(f"{beta:<6} {v[90]:<10.4f} {v[-1]:<10.4f} {str(well):<17} flat (every reading zero)")
    say()

    say("PART 6, exact (integer row reduction), three directions, six links: which loops are filled in, and after")
    say("how many times round?")
    adj_s, part_s = torus([6, 6, 4])                            # the curled slab: index (a * 6 + b) * 4 + c
    slab = Field(adj_s, part_s)
    adj_3, part_3, canon = third_turn_space(4)
    third = Field(adj_3, part_3)
    step_path = lambda start, moves: [canon(tuple(start[i] + sum(m[i] for m in moves[:j]) for i in range(3)))  # noqa: E731
                                      for j in range(len(moves))]
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    my = (0, -1, 0)
    cases3 = [
        ("the curled slab 4 x 6 x 6", slab, [("round the curl (4 links)", [c for c in range(4)]),
                                              ("along an open direction (6 links)", [b * 4 for b in range(6)]),
                                              ("along the other open direction (6 links)", [a * 24 for a in range(6)])]),
        ("the third-turn space (96 points)", third,
         [("along the axis: the turn and slide once (6 links)", step_path((0, 0, 0), [ex, ex, ey, ey, ez, ez])),
          ("across the axis: the translation (4, -4, 0) (8 links)", step_path((0, 0, 0), [ex] * 4 + [my] * 4))]),
    ]
    say(f"{'wiring':<40} {'points':<7} {'squares':<8} {'squares per point':<18} loop: filled after k times round")
    for name, field, loops in cases3:
        ech = echelon(field.B.toarray().astype(np.int64).tolist())
        say(f"{name:<40} {field.n:<7} {field.n_squares:<8} {field.n_squares / field.n:<18.3f}")
        for label, path in loops:
            k = fill_order(ech, link_vector(field, path), kmax=6)
            say(f"    {label:<56} {'never (to k = 6)' if k is None else 'k = ' + str(k)}")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
