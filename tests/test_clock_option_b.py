"""Option B, the clock on every point tied to its link lengths (graphity.clock; her decision of 7 November 2026)."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from graphity import clock, lengths
from graphity.cqg import NO_CAP, torus
from graphity.dimension import local_dimension
from run_clock_knot import distance_to, plant_knot

DIMS = (16, 16)
ALPHA = -0.5          # negative: links longer near a knot (HYPOTHESIS, Gravity)


def brute_mean_length(delta):
    """Every point, every link, by hand: family a at the point and at its lower neighbour along a."""
    d = delta.shape[0]
    dims = delta.shape[1:]
    out = np.zeros(dims)
    for p in np.ndindex(*dims):
        total = 0.0
        for a in range(d):
            q = list(p); q[a] = (q[a] - 1) % dims[a]
            total += (1 + delta[a][p]) + (1 + delta[a][tuple(q)])
        out[p] = total / (2 * d)
    return out


def test_flat_sheet_and_flat_cube_tick_at_one_everywhere():
    for dims in [(8, 8), (6, 6, 6)]:
        assert np.all(clock.tick_rate(np.zeros((len(dims),) + dims)) == 1.0)


def test_mean_link_length_matches_the_brute_force_on_sheet_and_cube():
    rng = np.random.default_rng(2)
    for dims in [(7, 5), (4, 5, 6)]:
        delta = rng.normal(0, 0.1, (len(dims),) + dims)
        assert np.allclose(clock.mean_link_length(delta), brute_mean_length(delta))


def test_one_long_link_slows_exactly_its_two_endpoints():
    delta = np.zeros((2,) + DIMS); delta[0][3, 4] = 0.2            # the link from (3, 4) to (4, 4)
    m = clock.mean_link_length(delta)
    assert m[3, 4] == m[4, 4] == 1.0 + 0.2 / 4 and np.count_nonzero(m != 1.0) == 2
    r = clock.tick_rate(delta)
    assert r[3, 4] < 1.0 and r[5, 4] == 1.0


def test_the_mean_clock_is_one_whenever_the_scale_mode_is_fixed():
    rng = np.random.default_rng(5)
    for dims in [(12, 12), (6, 6, 6)]:
        f = rng.random((len(dims),) + dims)
        delta, _ = lengths.relax(f, ALPHA)                           # relax removes the zero mode per family
        assert abs(clock.mean_link_length(delta).mean() - 1.0) < 1e-12


def test_clocks_run_slow_at_a_planted_knot_and_a_shade_fast_far_from_it():
    adj, part = torus(*DIMS, NO_CAP)
    quad = plant_knot(adj, part, np.random.default_rng(3))
    rate, delta = clock.clock_field(adj, DIMS, ALPHA)
    assert delta.shape == (2,) + DIMS and np.any(delta > 0)
    knot = np.flatnonzero(local_dimension(adj) != 2)
    dist = distance_to(adj, knot).reshape(DIMS)
    near, far = rate[dist <= 1], rate[dist >= 4]
    assert near.mean() < 1.0 < far.mean()                             # slow near mass; the balance far away
    assert rate.min() == near.min()                                   # the slowest clock sits at the knot
    assert np.isclose((1.0 / rate).mean(), 1.0)


def test_the_sign_is_alphas_sign():
    """Put in by hand: with alpha positive the links shorten near the knot and the clock there runs fast."""
    adj, part = torus(*DIMS, NO_CAP)
    plant_knot(adj, part, np.random.default_rng(3))
    knot = np.flatnonzero(local_dimension(adj) != 2)
    dist = distance_to(adj, knot).reshape(DIMS)
    rate_pos, _ = clock.clock_field(adj, DIMS, -ALPHA)
    assert rate_pos[dist <= 1].mean() > 1.0


def test_proper_ticks_scale_with_the_rate():
    rate = np.array([[0.5, 1.0], [2.0, 1.0]])
    assert np.array_equal(clock.proper_ticks(rate, 10), np.array([[5.0, 10.0], [20.0, 10.0]]))
