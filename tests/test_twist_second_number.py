"""Twist as its own number (her reversal of 6 November 2026; docs/design/twist_second_number_2026-11-06.md):
the one-number rule is untouched, the second-number rule keeps the books, makes gluons and two-square stores."""
import numpy as np
import pytest

from graphity.cqg import NO_CAP, torus
from graphity.curl_pair_moves import PairMoves
from graphity.curl_pairs import CurlState


def _run(rule, seed=3, side=16, lam=1.5, barrier=4.0, clock="simultaneous", price="gravity", share=0.5, sweeps=10_000):
    pm = PairMoves(CurlState(*torus(side, side, NO_CAP)), lam=lam, barrier=barrier, seed=seed, price_from=price,
                   clock=clock, twist_rule=rule, twist_share=share)
    pm.run(max_sweeps=sweeps)
    return pm


def test_the_one_number_rule_is_the_default_and_never_touches_t():
    pm = _run("one_number")
    assert pm.twist_rule == "one_number" and not pm.second
    assert np.all(pm.state.t == 0.0)
    default = PairMoves(CurlState(*torus(8, 8, NO_CAP)), lam=1.25, barrier=0.0, seed=1)
    assert default.twist_rule == "one_number"


@pytest.mark.parametrize("clock,price", [("simultaneous", "gravity"), ("sequential", "ledger"), ("simultaneous", "ledger")])
def test_books_balance_through_a_run_under_the_second_number_rule(clock, price):
    pm = PairMoves(CurlState(*torus(16, 16, NO_CAP)), lam=1.5, barrier=4.0, seed=11, price_from=price, clock=clock,
                   twist_rule="second_number")
    for _ in range(40):
        pm.sweep()
        assert abs(pm.books() - pm.release) < 1e-9
    cen = pm.census()
    assert cen["net_twist"] == 0.0 and cen["net_curl"] == 0.0


def test_cancellation_leaves_gluons_and_releases_the_twist_share_only():
    pm = _run("second_number", share=0.5)
    cen = pm.census()
    gluons = cen["gluons_plus"] + cen["gluons_minus"]
    assert gluons == pm.photons                       # two gluons per cancellation, two photons per cancellation
    assert abs(pm.light - 0.5 * pm.photons * pm.unit) < 1e-9   # each photon carries s of a unit
    assert cen["gluons_plus"] == cen["gluons_minus"]  # one of each kind per cancellation
    c, t, s = pm.state.c, pm.state.t, pm.store
    assert np.all(np.abs(c[(t == 0) & (c != 0) & (s == 0)]) == 1.0)


def test_a_store_is_two_squares_with_both_curls_kept():
    pm = _run("second_number", lam=2.0)
    cen = pm.census()
    assert cen["stores"] > 0
    assert cen["store_squares"] == 2 * cen["stores"]
    s, c, t = pm.store, pm.state.c, pm.state.t
    assert np.all(c[s != 0] != 0.0)
    assert np.all(np.abs(t[s != 0]) == 0.5)
    # both squares of a store carry the store's sign, and the sign is the curl's
    assert np.all(np.sign(c[s != 0]) == s[s != 0])
    assert abs(pm.held - (2.0 * pm.unit * cen["stores"])) < 1e-9   # gravity form: two units per store held


def test_gluons_never_cancel_join_or_move():
    pm = PairMoves(CurlState(*torus(16, 16, NO_CAP)), lam=1.5, barrier=4.0, seed=5, price_from="gravity",
                   clock="simultaneous", twist_rule="second_number")
    last = 0
    for _ in range(30):
        pm.sweep()
        cen = pm.census()
        g = cen["gluons_plus"] + cen["gluons_minus"]
        assert g >= last
        last = g
    t, s, c = pm.state.t, pm.store, pm.state.c
    assert not np.any((t == 0) & (s != 0) & (c != 0))   # no store square is a gluon


def test_share_one_sends_the_whole_unit_to_light():
    pm = _run("second_number", share=1.0)
    assert abs(pm.light - pm.photons * pm.unit) < 1e-9
    assert abs(pm.books() - pm.release) < 1e-9


def test_same_seed_reproduces_and_rules_differ():
    a = _run("second_number", seed=21).census()
    b = _run("second_number", seed=21).census()
    o = _run("one_number", seed=21).census()
    assert a == b
    assert a["twist_rule"] != o["twist_rule"]


def test_bad_arguments_are_refused():
    with pytest.raises(ValueError):
        PairMoves(CurlState(*torus(8, 8, NO_CAP)), lam=1.25, barrier=0.0, seed=1, twist_rule="three")
    with pytest.raises(ValueError):
        PairMoves(CurlState(*torus(8, 8, NO_CAP)), lam=1.25, barrier=0.0, seed=1, twist_rule="second_number",
                  twist_share=1.5)
