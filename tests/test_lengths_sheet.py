"""The four-link form of the lengths (graphity.lengths with dims of length 2; 6 November 2026): K = 4 (4 I - A) per
family, the numbers of sandbox/regge_four_link_stiffness.py, the six-link form untouched."""
import numpy as np

from graphity import lengths
from graphity.cqg import NO_CAP, torus
from graphity.loose_band import loose_band_tube

DIMS = (8, 8)


def test_flat_squares_is_two_on_the_sheet_and_four_in_the_cube():
    assert lengths.flat_squares((8, 8)) == 2 and lengths.flat_squares((6, 6, 6)) == 4
    assert lengths.FLAT_SQUARES == 4


def test_stiffness_on_the_sheet_is_the_exact_numbers():
    """K on a unit perturbation of one link: 16 on itself (8 d^2 for one link), -4 on its four parallel neighbours
    (-4 d^2 for a parallel pair), 0 elsewhere; row sums zero (scaling free)."""
    e = np.zeros(DIMS); e[2, 3] = 1.0
    k = lengths.apply_stiffness(e)
    assert k[2, 3] == 16.0
    assert all(k[p] == -4.0 for p in [(1, 3), (3, 3), (2, 2), (2, 4)])
    assert np.count_nonzero(k) == 5 and k.sum() == 0.0


def test_the_six_link_stiffness_is_unchanged():
    e = np.zeros((6, 6, 6)); e[1, 2, 3] = 1.0
    k = lengths.apply_stiffness(e)
    assert k[1, 2, 3] == 24.0 and np.count_nonzero(k) == 7 and k.sum() == 0.0


def test_flat_sheet_has_no_curl_and_no_relaxed_energy():
    adj, part = torus(*DIMS, NO_CAP)
    f = lengths.curl_fields(adj, DIMS)
    assert f.shape == (2,) + DIMS and not f.any()
    assert lengths.relaxed_energy(adj, DIMS, -0.5) == 0.0


def test_relax_inverts_the_sheet_stiffness_up_to_the_zero_mode():
    rng = np.random.default_rng(1)
    f = rng.random((2,) + DIMS)
    delta, energy = lengths.relax(f, -0.7)
    for a in range(2):
        kd = lengths.apply_stiffness(delta[a])
        assert np.allclose(kd, 0.7 * (f[a] - f[a].mean()))
        assert abs(delta[a].mean()) < 1e-12
    assert np.isclose(energy, sum(-0.7 / 2 * np.sum(f[a] * delta[a]) for a in range(2)))


def test_a_loosened_band_on_the_sheet_carries_curl_and_lowers_the_energy_for_either_sign():
    """On the 4 x 32 tube (dims (32, 4), index x * 4 + y) a loosened band gives links with squares missing, so a
    curl field, a relaxed energy below zero for alpha of either sign, and a halo that follows the lattice Green's
    function (two point sources attract)."""
    adj, part, in_band, made = loose_band_tube(32, 4, np.random.default_rng(3))
    dims = (32, 4)
    f = lengths.curl_fields(adj, dims)
    assert f.any()
    for alpha in (-0.5, 0.5):
        assert lengths.relaxed_energy(adj, dims, alpha) < 0.0
    big = (16, 16)
    one = np.zeros((2,) + big); one[0][2, 2] = 1.0
    e1 = lengths.relax(one, 0.5)[1]
    e_int = []
    for d in (1, 2):
        two = one.copy(); two[0][2 + d, 2] = 1.0
        e_int.append(lengths.relax(two, 0.5)[1] - 2 * e1)
    assert e_int[0] < 0.0 and e_int[1] < 0.0 and e_int[1] > e_int[0]     # attract, less so farther apart
