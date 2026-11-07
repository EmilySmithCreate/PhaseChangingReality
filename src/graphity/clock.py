"""Option B: a clock on every point, tied to the lengths of its links (her decision of 7 November 2026; the brief
docs/design/clock_option_b_2026-11-07.md).

The rule, in its plainest form (ours, her "proceed"): a point's tick rate is the inverse of the mean length of its
links. With the lengths of graphity.lengths (a link's length is 1 + delta, delta relaxed from the curl with the one
constant alpha, negative, so links are longer near a knot) clocks run slow where links are long, near mass. The sign
is put in by hand through alpha's sign; what the rule then fixes without a further choice:

* exact: the mean of the mean link length over all points is 1 whenever the scale mode is fixed (sum of delta zero
  per family, her scale rule), so the slow clocks near a knot are balanced by clocks a shade fast far from it; on a
  torus there is no "infinity" to set the clock against, only the mean;
* exact: one link lengthened by d slows exactly its two endpoints, each by d / (2 D) in the mean length;
* the shape of the slowing with distance from a knot is the lattice Green's function of the stiffness, the same
  field that lengthens the links: logarithmic on the sheet, 1 / r in the cube (general knowledge for the continuum
  limit, to verify; measured in the toy by a look first, registered on her prediction).

A link of family a is placed at its lower point along a (graphity.lengths.curl_fields); point p's links of family a
are the one placed at p and the one placed at p - e_a.
"""
import numpy as np

from graphity import lengths


def mean_link_length(delta):
    """(dims): at each point the mean of 1 + delta over its 2 D links."""
    d = delta.shape[0]
    out = np.zeros(delta.shape[1:])
    for a in range(d):
        out += (1.0 + delta[a]) + (1.0 + np.roll(delta[a], 1, axis=a))
    return out / (2 * d)


def tick_rate(delta):
    """(dims): proper ticks per global tick at each point, 1 over the mean link length. One everywhere when flat."""
    return 1.0 / mean_link_length(delta)


def clock_field(adj, dims, alpha):
    """(rate, delta) from the wiring: the lengths relaxed from the curl, then the rate at every point."""
    delta, _ = lengths.relax(lengths.curl_fields(adj, dims), alpha)
    return tick_rate(delta), delta


def proper_ticks(rate, global_ticks):
    """Ticks a clock at each point has counted after global_ticks of the toy's sweep clock."""
    return rate * global_ticks
