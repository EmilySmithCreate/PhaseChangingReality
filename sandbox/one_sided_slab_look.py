"""SANDBOX LOOK (20 November 2026, evening; rule 16: a look, nothing registered). Her words of the same evening
(verbatim in sandbox/NOTEBOOK.md): "in our toy face diagonals should be dark matter, 1/2 twist, closing with one
side. only when 2 of same direction bond we get the high energy density 1 twist 1 curl store"; and of X: "it is a
plane. 2 open directions, 1 curled. all the mobius strips lined up in a tessalation where the one sidedness
orients together (on the inside of the doughnut skin?) preventing there from being any dimension in there."

The same exact loop test as sandbox/wilson_line_look.py and sandbox/electron_triangle_look.py (their functions are
imported): a loop is "filled in after k times round" when k times its signed link vector is a whole-number
combination of the wiring's squares. Added here: the number of INDEPENDENT loops that are never filled in however
many times they are taken (links - points + 1 - the squares' rank, for a connected wiring); call it the number of
directions left open to a loop. The wiring only: not her light, not her twist rules, and "links" here are the toy's
bookkeeping for where the squares are (her base has only curl and twist).

WRITTEN BEFORE COMPUTING (ours):
  G1. Halves on the face diagonal. A sheet glued to itself by a mirror along a face diagonal with a slide along it,
      (x, y) -> (y, x) + (3, 3), and by the translation (4, -4): 24 points, flat (24 squares, two on every link),
      one-sided. The loop along the face-diagonal direction (4, -4), the direction the mirror reverses, is filled
      in only when taken TWICE (k = 2): one loop is a half, two together are a whole. The one-sided trip itself is
      never filled in. One direction left open.
  G2. Her X as the curled slab, 4 x 6 x 6, the curl glued three ways.
      (a) straight (the standing stand-in): round the curl k = 1; both open directions never; 2 directions left
          open; 3.25 squares a point.
      (b) one-sided: going round the curl arrives with ONE open direction reversed (every row along the other open
          direction is then a Moebius strip, all lined up alike). Round the curl k = 1 (on the two mirror rows the
          trip is four links, a square); the reversed open direction is now filled in at once (k = 1); the other
          open direction never. 1 direction left open. Fewer surplus squares than (a): only the mirror rows carry
          them.
      (c) one-sided both ways (both open directions reversed, a half turn about the curl's axis): every loop is
          filled in (k = 1). NO direction left open. Surplus squares only on four lines.

Usage: python sandbox/one_sided_slab_look.py    (writes sandbox/out/one_sided_slab_look_2026-11-20.txt)
"""
import sys
from collections import Counter, deque
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphity.cqg_d import torus                                              # noqa: E402
from graphity.u1 import Field                                                 # noqa: E402
from wilson_line_look import echelon, fill_order, link_vector, two_colour    # noqa: E402

L = 6


def diagonal_mirror_sheet(n=4, slide=3):
    """Four-link wiring of the square lattice glued by g: (x, y) -> (y, x) + (slide, slide) and by the translations
    (n, -n) and (2 slide, 2 slide). Returns (adj, canon)."""
    basis = np.array([[n, -n], [2 * slide, 2 * slide]], dtype=np.int64)
    det = int(round(np.linalg.det(basis)))
    assert det > 0
    adjugate = np.round(det * np.linalg.inv(basis)).astype(np.int64)
    assert np.array_equal(adjugate @ basis, det * np.eye(2, dtype=np.int64))

    def reduce(p):
        c = (np.asarray(p, dtype=np.int64) @ adjugate) // det
        return tuple(int(v) for v in np.asarray(p, dtype=np.int64) - c @ basis)

    def rep(p):
        a = reduce(p)
        return min(a, reduce((a[1] + slide, a[0] + slide)))

    steps = ((1, 0), (-1, 0), (0, 1), (0, -1))
    start = rep((0, 0))
    reps, queue = {start}, deque([start])
    while queue:
        p = queue.popleft()
        for s in steps:
            q = rep((p[0] + s[0], p[1] + s[1]))
            if q not in reps:
                reps.add(q)
                queue.append(q)
    reps = sorted(reps)
    assert 2 * len(reps) == det, (len(reps), det)
    index = {p: i for i, p in enumerate(reps)}
    adj = np.array([[index[rep((p[0] + s[0], p[1] + s[1]))] for s in steps] for p in reps], dtype=np.int64)
    assert all(len(set(row.tolist())) == 4 and i not in row for i, row in enumerate(adj))
    return adj, (lambda p: index[rep(p)])


def glued_slab(flip_y, flip_z, around=4, size=L):
    """Six-link slab, points (c, y, z); stepping past c = around - 1 arrives at (0, -y if flip_y, -z if flip_z)."""
    def index(c, y, z):
        return (c * size + y % size) * size + z % size

    adj = np.empty((around * size * size, 6), dtype=np.int64)
    for c in range(around):
        for y in range(size):
            for z in range(size):
                fy, fz = (-y if flip_y else y), (-z if flip_z else z)
                ahead = index(0, fy, fz) if c == around - 1 else index(c + 1, y, z)
                back = index(around - 1, fy, fz) if c == 0 else index(c - 1, y, z)
                adj[index(c, y, z)] = (ahead, back, index(c, y + 1, z), index(c, y - 1, z),
                                       index(c, y, z + 1), index(c, y, z - 1))
    assert all(len(set(row.tolist())) == 6 and i not in row for i, row in enumerate(adj))
    return adj, index


def report(say, name, field, loops, kmax=4):
    ech = echelon(field.B.toarray().astype(np.int64).tolist())
    open_dirs = field.n_links - field.n + 1 - len(ech)
    on_links = dict(sorted(Counter(int(x) for x in np.asarray(abs(field.B).sum(axis=0)).ravel()).items()))
    say(f"{name:<44} {field.n:<7} {field.n_squares:<8} {field.n_squares / field.n:<10.3f} {str(on_links):<24} {open_dirs}")
    for label, path in loops:
        k = fill_order(ech, link_vector(field, path), kmax=kmax)
        say(f"    {label:<64} {'never (to k = ' + str(kmax) + ')' if k is None else 'k = ' + str(k)}")


def main():
    lines = []

    def say(s=""):
        print(s)
        lines.append(s)

    out = Path(__file__).resolve().parent / "out" / "one_sided_slab_look_2026-11-20.txt"
    if out.exists():
        raise SystemExit(f"{out} exists; results are append-only")

    head = (f"{'wiring':<44} {'points':<7} {'squares':<8} {'per point':<10} {'squares on a link: links':<24} "
            f"directions left open to a loop")

    say("PART 1, exact: a sheet glued by a mirror along a face diagonal (halves on the face diagonal)")
    say(head)
    adj, canon = diagonal_mirror_sheet(4, 3)
    sheet = Field(adj, two_colour(adj))

    def walk(start, moves):
        path, p = [], tuple(start)
        for m in moves:
            path.append(canon(p))
            p = (p[0] + m[0], p[1] + m[1])
        assert canon(p) == path[0], "the path does not close"
        return path

    report(say, "mirror along the diagonal, slide (3, 3)", sheet, [
        ("along the face-diagonal direction (4, -4) (8 links)", walk((0, 0), [(1, 0)] * 4 + [(0, -1)] * 4)),
        ("the one-sided trip, the mirror and slide once (6 links)", walk((0, 0), [(1, 0)] * 3 + [(0, 1)] * 3)),
        ("along the mirror line twice, (6, 6) (12 links)", walk((0, 0), [(1, 0)] * 6 + [(0, 1)] * 6)),
    ])
    say()

    say("PART 2, exact: the curled slab 4 x 6 x 6 with the curl glued three ways")
    say(head)
    a_s, p_s = torus([L, L, 4])                                   # index (a * 6 + b) * 4 + c
    report(say, "(a) straight", Field(a_s, p_s), [
        ("round the curl (4 links)", list(range(4))),
        ("along one open direction (6 links)", [b * 4 for b in range(L)]),
        ("along the other open direction (6 links)", [a * 4 * L for a in range(L)]),
    ])
    for name, fy, fz in (("(b) one-sided: one open direction reversed", True, False),
                         ("(c) one-sided both ways: both reversed", True, True)):
        adj, index = glued_slab(fy, fz)
        field = Field(adj, two_colour(adj))
        trip = [index(c, 1, 0) for c in range(4)] + [index(0, -1, 0), index(0, 0, 0)]
        report(say, name, field, [
            ("round the curl on a mirror row (4 links, a square)", [index(c, 0, 0) for c in range(4)]),
            ("round the curl one row off the mirror row, and back (6 links)", trip),
            ("along the reversed open direction y (6 links)", [index(0, y, 0) for y in range(L)]),
            (f"along the other open direction z ({'reversed too' if fz else 'not reversed'}) (6 links)",
             [index(0, 0, z) for z in range(L)]),
        ])

    out.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
