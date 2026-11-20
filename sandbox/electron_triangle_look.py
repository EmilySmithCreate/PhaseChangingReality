"""SANDBOX LOOK (20 November 2026, later; rule 16: a look, nothing registered). Her words of the same day (verbatim
in sandbox/NOTEBOOK.md): the loop that closes only the third time round "could be another way to think about the
loop of an electron, where each root 6 diagonal holds 1/3 twist and 3 together make a full twist on one closed
loop"; "every point on the surface of the doughnut is 2 curled directions"; "a klein bottle from the 2 mobius
strips".

Three exact looks, integers only. The loop test is the one of sandbox/wilson_line_look.py (its functions are
imported): a loop is "filled in after k times round" when k times its signed link vector is a whole-number
combination of the wiring's squares (the toy's squares are all its four-link loops, graphity.u1). NOT HER LIGHT and
not her twist rules: this reads the wiring only.

WRITTEN BEFORE COMPUTING (ours):
  F1. Arithmetic. Every closed loop of three box diagonals (steps of the kind (1, 1, 2), length root 6) is a flat
      triangle with three equal sides, lying across one of the cube's four body diagonals, and a third of a turn
      about that body diagonal carries each side to the next. Its three steps have one sign turned, as
      (1, 1, -2), (1, -2, 1), (-2, 1, 1); the three named in the first look, (1, 1, 2), (1, 2, 1), (2, 1, 1), do
      not close (they add to (4, 4, 4)). Count: 8 triangles per lattice point, 16 with a direction of travel (the
      record's count, twist_curl_relations_2026-10-30.md, E3). The triangle's middle is a lattice point of the
      corners' color, one face diagonal (root 2) from each corner.
  F2. The third-turn space glued so that its loops across the axis run along the box diagonals (translations
      m (1, 1, -2) and m (1, -2, 1); the turn (x, y, z) -> (y, z, x) + (2, 2, 2) as before). With m = 2 and m = 3
      the loop along one box-diagonal direction is filled in only when taken THREE times, and the triangle of the
      three sides, walked in open space, is that one loop three times (the triangle minus three times the loop is
      filled in). With m = 1, where the loop is one single box diagonal, the loop is four links long, so it is
      itself a square of the wiring and is filled in at once (k = 1).
  F3. Which family reads in thirds is set by the gluing. In the box-diagonal gluing the loop along a face-diagonal
      direction, m (0, 3, -3), is filled at once; in the first look's gluing (translations (4, -4, 0), (0, 4, -4))
      it is the other way round: the face-diagonal loop is filled after three (already run) and the box-diagonal
      loop (4, 4, -8) at once.
  F4. Doughnuts. A sheet with BOTH directions four round (4 x 4, 16 points): both loops filled in, three squares on
      every link. One direction four round (the tube 4 x 12): one filled, the other never. Neither (6 x 12): none.
      Six links, two directions four round and one open (4 x 4 x 6): both curled loops filled, the open one never.
  F5. The flat one-sided sheet (6 around, 12 along), cut along the two lines halfway between its two mirror rows,
      falls into exactly two bands, and each band has ONE edge, a single ring of 12 points: each is a Moebius
      strip. The same cut on the two-sided 6 x 12 doughnut gives two bands with TWO edges each (rings of 6).

Usage: python sandbox/electron_triangle_look.py    (writes sandbox/out/electron_triangle_look_2026-11-20.txt)
"""
import itertools
import sys
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphity.cqg_d import torus                                              # noqa: E402
from graphity.u1 import Field                                                 # noqa: E402
from read_flat_kind import klein_bottle                                       # noqa: E402
from wilson_line_look import echelon, fill_order, in_lattice, link_vector    # noqa: E402

EX, EY, EZ = (1, 0, 0), (0, 1, 0), (0, 0, 1)
MX, MY, MZ = (-1, 0, 0), (0, -1, 0), (0, 0, -1)


# ---------------------------------------------------------------- F1: the triangles, by arithmetic
def box_diagonals():
    out = set()
    for perm in set(itertools.permutations((1, 1, 2))):
        for signs in itertools.product((1, -1), repeat=3):
            out.add(tuple(s * v for s, v in zip(signs, perm)))
    return sorted(out)


def turn_about(axis, v):
    """A third of a turn about the body diagonal `axis` (entries +-1), exact: conjugate (x, y, z) -> (y, z, x)."""
    u = tuple(a * x for a, x in zip(axis, v))
    u = (u[1], u[2], u[0])
    return tuple(a * x for a, x in zip(axis, u))


def triangles():
    steps = box_diagonals()
    closed = [(a, b, c) for a in steps for b in steps for c in steps
              if all(a[i] + b[i] + c[i] == 0 for i in range(3))]
    rows = []
    for a, b, c in closed:
        normal = tuple(int(x) for x in np.cross(a, b))
        g = np.gcd.reduce(np.abs(normal))
        axis = tuple(x // g for x in normal)
        corners = [(0, 0, 0), a, tuple(a[i] + b[i] for i in range(3))]
        middle = tuple(Fraction(sum(p[i] for p in corners), 3) for i in range(3))
        rows.append({
            "steps": (a, b, c), "axis": axis,
            "axis_is_body_diagonal": sorted(abs(x) for x in axis) == [1, 1, 1],
            "sides_equal": len({sum(x * x for x in s) for s in (a, b, c)}) == 1,
            "turn_carries": turn_about(axis, a) in (b, c) and turn_about(axis, b) in (a, c),
            "middle_is_point": all(m.denominator == 1 for m in middle),
            "middle_same_colour": sum(middle) % 2 == 0,
            "middle_to_corner_sq": {int(sum((Fraction(p[i]) - middle[i]) ** 2 for i in range(3))) for p in corners},
        })
    # a triangle as a set of points, up to sliding it: slide its smallest corner to the origin
    shapes, directed = set(), set()
    for a, b, c in closed:
        corners = [(0, 0, 0), a, tuple(a[i] + b[i] for i in range(3))]
        low = min(corners)
        shapes.add(frozenset(tuple(p[i] - low[i] for i in range(3)) for p in corners))
        cyc = [(a, b, c), (b, c, a), (c, a, b)]
        directed.add(min(cyc))
    return closed, rows, shapes, directed


# ---------------------------------------------------------------- F2, F3: third-turn spaces
def third_turn(across_a, across_b, slide=2):
    """Six-link wiring of the cubic lattice glued by g: (x, y, z) -> (y, z, x) + (slide, slide, slide) and by the
    translations across_a, across_b (which the turn must carry into the lattice they span) and (3 slide) (1, 1, 1).
    Returns (adj, part, canon, closest), closest the fewest steps between two glued points."""
    basis = np.array([across_a, across_b, (3 * slide,) * 3], dtype=np.int64)
    det = int(round(np.linalg.det(basis)))
    if det < 0:
        basis = basis[[1, 0, 2]]
        det = -det
    adjugate = np.round(det * np.linalg.inv(basis)).astype(np.int64)
    assert np.array_equal(adjugate @ basis, det * np.eye(3, dtype=np.int64))

    def reduce(p):
        c = (np.asarray(p, dtype=np.int64) @ adjugate) // det
        return tuple(int(v) for v in np.asarray(p, dtype=np.int64) - c @ basis)

    def turn(p):
        return (p[1] + slide, p[2] + slide, p[0] + slide)

    for v in (across_a, across_b):                                  # the turn keeps the lattice
        assert reduce((v[1], v[2], v[0])) == (0, 0, 0), v

    def rep(p):
        a = reduce(p)
        b = reduce(turn(a))
        c = reduce(turn(b))
        return min(a, b, c)

    start = rep((0, 0, 0))
    reps, queue = {start}, deque([start])
    while queue:
        p = queue.popleft()
        for step in (EX, MX, EY, MY, EZ, MZ):
            q = rep(tuple(p[i] + step[i] for i in range(3)))
            if q not in reps:
                reps.add(q)
                queue.append(q)
    reps = sorted(reps)
    assert 3 * len(reps) == det, (len(reps), det)
    index = {p: i for i, p in enumerate(reps)}
    adj = np.empty((len(reps), 6), dtype=np.int64)
    for i, p in enumerate(reps):
        for k, step in enumerate((EX, MX, EY, MY, EZ, MZ)):
            adj[i, k] = index[rep(tuple(p[j] + step[j] for j in range(3)))]
        assert len(set(adj[i].tolist())) == 6 and i not in adj[i], "not a simple six-link wiring"
    part = np.array([sum(p) % 2 for p in reps], dtype=np.int64)
    # the fewest steps between two points that the gluing makes one: over the lattice and the two turned copies
    closest = None
    span = range(-3, 4)
    for ca in span:
        for cb in span:
            for cc in (-1, 0, 1):
                t = ca * basis[0] + cb * basis[1] + cc * basis[2]
                d = int(np.abs(t).sum())
                if d and (closest is None or d < closest):
                    closest = d
    return adj, part, (lambda p: index[rep(p)]), closest


def walk(canon, start, moves):
    """The points of the closed path from `start` along `moves` (the last move returns to the start)."""
    path, p = [], tuple(start)
    for m in moves:
        path.append(canon(p))
        p = tuple(p[i] + m[i] for i in range(3))
    assert canon(p) == path[0], "the path does not close"
    return path


def along(v):
    """Unit moves that add up to v, one direction after another."""
    moves = []
    for axis, (plus, minus) in enumerate(((EX, MX), (EY, MY), (EZ, MZ))):
        moves += [plus if v[axis] > 0 else minus] * abs(v[axis])
    return moves


def squares_on_links(field):
    return dict(sorted(Counter(int(x) for x in np.asarray(abs(field.B).sum(axis=0)).ravel()).items()))


# ---------------------------------------------------------------- F5: cutting a sheet into bands
def bands(adj, row_of, cuts):
    """Remove every link that joins the two rows of a pair in `cuts`; return, for each piece, its number of
    points, links and squares, and the rings its edge points form."""
    n = adj.shape[0]
    nbr = [set() for _ in range(n)]
    for a in range(n):
        for b in adj[a]:
            b = int(b)
            if (row_of(a), row_of(b)) in cuts or (row_of(b), row_of(a)) in cuts:
                continue
            nbr[a].add(b)
    seen, out = set(), []
    for s in range(n):
        if s in seen:
            continue
        piece, queue = {s}, deque([s])
        while queue:
            p = queue.popleft()
            for q in nbr[p]:
                if q not in piece:
                    piece.add(q)
                    queue.append(q)
        seen |= piece
        links = sum(len(nbr[p]) for p in piece) // 2
        fours = 0
        for u in piece:
            for a, c in itertools.combinations(sorted(nbr[u]), 2):
                fours += len(nbr[a] & nbr[c]) - 1
        edge = {p for p in piece if len(nbr[p]) < 4}
        rings, left = [], set(edge)
        while left:
            r, queue = set(), deque([next(iter(left))])
            r.add(queue[0])
            while queue:
                p = queue.popleft()
                for q in nbr[p] & edge:
                    if q not in r:
                        r.add(q)
                        queue.append(q)
            assert all(len(nbr[p] & r) == 2 for p in r), "an edge that is not a ring"
            rings.append(len(r))
            left -= r
        out.append({"points": len(piece), "links": links, "squares": fours // 4, "rows": sorted({row_of(p) for p in piece}),
                    "edge_rings": sorted(rings)})
    return out


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "electron_triangle_look_2026-11-20.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    # ---- F1
    closed, rows, shapes, directed = triangles()
    say("PART 1, exact arithmetic: every closed loop of three box diagonals")
    say(f"box-diagonal steps: {len(box_diagonals())}; closed walks of three from one point: {len(closed)}; "
        f"triangles per lattice point (as shapes): {len(shapes)}; with a direction of travel: {len(directed)}")
    say(f"each lies across a body diagonal: {all(r['axis_is_body_diagonal'] for r in rows)}; "
        f"three equal sides (length squared 6): {all(r['sides_equal'] for r in rows)}; "
        f"a third of a turn about that body diagonal carries each side to another side: {all(r['turn_carries'] for r in rows)}")
    say(f"the middle is a lattice point: {all(r['middle_is_point'] for r in rows)}; of the corners' color: "
        f"{all(r['middle_same_colour'] for r in rows)}; squared distance middle to corner: "
        f"{sorted(set().union(*[r['middle_to_corner_sq'] for r in rows]))} (2 is a face diagonal)")
    say(f"triangles per body diagonal: {dict(sorted(Counter(tuple(abs(x) for x in r['axis']) for r in rows).items()))} walks; "
        f"axes found: {sorted({tuple(x * (1 if r['axis'][0] > 0 else -1) for x in r['axis']) for r in rows})}")
    say(f"example: {closed[0][0]} + {closed[0][1]} + {closed[0][2]} = (0, 0, 0)")
    say(f"the first look's three, (1, 1, 2) + (1, 2, 1) + (2, 1, 1) = {tuple(int(x) for x in np.add(np.add((1, 1, 2), (1, 2, 1)), (2, 1, 1)))}: not closed")
    say()

    # ---- F2, F3
    say("PART 2, exact (integer row reduction): third-turn spaces; is a loop filled in, and after how many times round?")
    say(f"{'gluing':<46} {'points':<7} {'squares':<8} {'per point':<10} {'closest glued points':<21}")
    gluings = [(f"box-diagonal gluing, m = {m}", (m, m, -2 * m), (m, -2 * m, m), m) for m in (1, 2, 3)]
    gluings.append(("the first look's gluing (4, -4, 0), (0, 4, -4)", (4, -4, 0), (0, 4, -4), None))
    for name, a, b, m in gluings:
        adj, part, canon, closest = third_turn(a, b)
        field = Field(adj, part)
        ech = echelon(field.B.toarray().astype(np.int64).tolist())
        say(f"{name:<46} {field.n:<7} {field.n_squares:<8} {field.n_squares / field.n:<10.3f} {closest:<21}")

        def k_of(moves, kmax=6):
            k = fill_order(ech, link_vector(field, walk(canon, (0, 0, 0), moves)), kmax=kmax)
            return f"never (to k = {kmax})" if k is None else f"k = {k}"

        if m is not None:
            v1, v2, v3 = (m, m, -2 * m), (m, -2 * m, m), (-2 * m, m, m)
            say(f"    along one box-diagonal direction, {v1} ({4 * m} links): {k_of(along(v1))}")
            w1 = link_vector(field, walk(canon, (0, 0, 0), along(v1)))
            tri = link_vector(field, walk(canon, (0, 0, 0), along(v1) + along(v2) + along(v3)))
            say(f"    the triangle of the three sides, walked in open space ({12 * m} links): filled in "
                f"{in_lattice(ech, tri)}; the triangle minus three times the loop is filled in "
                f"{in_lattice(ech, [t - 3 * w for t, w in zip(tri, w1)])}")
            face = (0, 3 * m, -3 * m)
            say(f"    along a face-diagonal direction, {face} ({6 * m} links): {k_of(along(face))}")
        else:
            say(f"    along a face-diagonal direction, (4, -4, 0) (8 links): {k_of(along((4, -4, 0)))}")
            say(f"    along a box-diagonal direction, (4, 4, -8) (16 links): {k_of(along((4, 4, -8)))}")
        say(f"    along the axis, the turn and slide once (6 links): {k_of([EX, EX, EY, EY, EZ, EZ])}")
    say()

    # ---- F4
    say("PART 3, exact: doughnuts with both directions closed; which loops are filled in?")
    say(f"{'wiring':<34} {'points':<7} {'squares':<8} {'per point':<10} {'squares on a link: links':<28} loops")
    a44, p44 = torus([4, 4])                                      # index a * 4 + b
    at, pt = torus([12, 4])                                       # index y * 4 + x
    af, pf = torus([12, 6])                                       # index y * 6 + x
    a3, p3 = torus([6, 4, 4])                                     # index (a * 4 + b) * 4 + c
    sheets = [
        ("4 x 4: both directions four round", Field(a44, p44),
         [("one way round (4 links)", list(range(4))), ("the other way round (4 links)", [a * 4 for a in range(4)])]),
        ("the tube 4 x 12: one four round", Field(at, pt),
         [("round the curl (4 links)", list(range(4))), ("along (12 links)", [y * 4 for y in range(12)])]),
        ("6 x 12: neither four round", Field(af, pf),
         [("round (6 links)", list(range(6))), ("along (12 links)", [y * 6 for y in range(12)])]),
        ("six links, 4 x 4 x 6: two four round", Field(a3, p3),
         [("round one curl (4 links)", list(range(4))), ("round the other curl (4 links)", [b * 4 for b in range(4)]),
          ("along the open direction (6 links)", [a * 16 for a in range(6)])]),
    ]
    for name, field, loops in sheets:
        ech = echelon(field.B.toarray().astype(np.int64).tolist())
        say(f"{name:<34} {field.n:<7} {field.n_squares:<8} {field.n_squares / field.n:<10.3f} {str(squares_on_links(field)):<28}")
        for label, path in loops:
            k = fill_order(ech, link_vector(field, path), kmax=4)
            say(f"    {label:<40} {'never (to k = 4)' if k is None else 'k = ' + str(k)}")
    say()

    # ---- F5
    say("PART 4, exact: cut a sheet along two lines (between rows 3|4 and 8|9 of its 12); the pieces and their edges")
    cuts = {(3, 4), (8, 9)}
    say(f"{'sheet':<34} {'piece rows':<26} {'points':<7} {'links':<6} {'squares':<8} {'P - L + S':<10} edge rings (points in each)")
    for name, adj, row_of in (("the flat one-sided sheet 6 x 12", klein_bottle(6, 12), lambda i: i % 12),
                              ("the two-sided doughnut 6 x 12", af, lambda i: i // 6)):
        for piece in bands(adj, row_of, cuts):
            say(f"{name:<34} {str(piece['rows']):<26} {piece['points']:<7} {piece['links']:<6} {piece['squares']:<8} "
                f"{piece['points'] - piece['links'] + piece['squares']:<10} {piece['edge_rings']}")

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
