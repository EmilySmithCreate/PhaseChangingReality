"""Tube shapes of the four-link toy that are not the plain torus.

THE TWISTED TUBE (exact, O116 in the archive, 11 October 2026): what the 4 x L tube opens into is the same tube with
its seam shifted by two, six steps around where the tube was four, in 9,208 of 9,215 exactly flat end states. The
constructor is the archive's `scripts/read_endpoint_width.twisted_tube`, copied here unchanged on 6 November 2026 so
that T106 (her moves on the opened tube six around) has its wiring in the working copy. Point (x, y): x in 0..3 round
the tube, y in 0..length-1 along it; stepping round past x = 3 arrives at (0, y - shift). With shift 0 it is the tube;
with shift 2 no four steps round it close, the shortest way round is six, every link carries exactly two squares (flat,
S = N), and the wiring stays bipartite (the shift is even). The index is x * length + y, the opposite convention to
`cqg.torus` (which puts the short cycle last); `part` is (x + y) mod 2 with the shift even.
"""
import numpy as np


def twisted_tube(length, shift=2):
    """The 4 x `length` tube with its seam shifted by `shift` steps along the tube. Returns (adj, part)."""
    if length < 6 or shift % 2:
        raise ValueError("length at least 6 (the hard-core rule) and an even shift (bipartite)")

    def index(x, y):
        return x * length + (y % length)

    adj = np.empty((4 * length, 4), dtype=np.int64)
    for x in range(4):
        for y in range(length):
            ahead = index(0, y - shift) if x == 3 else index(x + 1, y)
            back = index(3, y + shift) if x == 0 else index(x - 1, y)
            adj[index(x, y)] = (ahead, back, index(x, y + 1), index(x, y - 1))
    part = np.array([(i // length + i % length) % 2 for i in range(4 * length)], dtype=np.int64)
    return adj, part


def width(adj, start=0):
    """The length of the shortest closed path through `start` that cannot be shrunk to a point, read from the balls:
    the first radius r at which the ball's growth falls short of the plane's 4r new points gives width 2r (exact for a
    flat torus; the archive's `read_endpoint_width.width`, rewritten here for the tests)."""
    seen = {start}
    frontier = [start]
    r = 0
    while frontier:
        r += 1
        new = []
        for p in frontier:
            for q in adj[p]:
                q = int(q)
                if q not in seen:
                    seen.add(q)
                    new.append(q)
        if len(new) < 4 * r:
            return 2 * r
        frontier = new
    return 2 * r
