"""The twisted tube (graphity.tubes): valid, bipartite, flat, six around, and the plain tube at shift 0."""
import networkx as nx
import numpy as np
import pytest

from graphity.cqg import NO_CAP, hamiltonian, is_valid, torus, total_squares
from graphity.dimension import local_dimension
from graphity.tubes import twisted_tube, width


def _graph(adj):
    return nx.Graph([(u, int(v)) for u in range(len(adj)) for v in adj[u] if v >= 0])


@pytest.mark.parametrize("L", [8, 12, 24])
def test_twisted_tube_is_valid_bipartite_four_regular_and_flat(L):
    adj, part = twisted_tube(L, 2)
    assert adj.shape == (4 * L, 4)
    assert is_valid(adj, NO_CAP)
    g = _graph(adj)
    assert nx.is_bipartite(g) and all(d == 4 for _, d in g.degree())
    col = nx.bipartite.color(g)
    same = [col[i] == part[i] for i in range(len(adj))]
    assert all(same) or not any(same)
    assert total_squares(adj) == 4 * L                       # flat: as many squares as points
    assert hamiltonian(adj, 1.25) == 0.0


@pytest.mark.parametrize("L", [8, 12, 24])
def test_twisted_tube_is_six_around_and_reads_sheet_everywhere(L):
    adj, part = twisted_tube(L, 2)
    assert width(adj, 0) == 6 and width(adj, 4 * L // 3) == 6
    assert np.all(local_dimension(adj) == 2)                 # no 4-cycle closes round it: every point reads sheet


def test_shift_zero_is_the_plain_tube_four_around():
    adj, part = twisted_tube(12, 0)
    assert width(adj, 0) == 4
    adj0, _ = torus(12, 4, NO_CAP)
    # the plain tube four around carries its wrap-around squares too (one per column: 60 at L = 12, exact), the same
    # count as cqg.torus(12, 4); the twisted tube has none, which is why it is flat
    assert total_squares(adj) == total_squares(adj0) == 60 and is_valid(adj, NO_CAP)
    assert nx.is_isomorphic(_graph(adj), _graph(adj0))


def test_bad_arguments_are_refused():
    with pytest.raises(ValueError):
        twisted_tube(12, 1)
    with pytest.raises(ValueError):
        twisted_tube(4, 2)
