# tests/test_rules.py

import pytest
from amazons.state import GameState, EMPTY, BLOCK, PLAYER1, PLAYER2
from amazons.rules import Rules

@pytest.fixture
def state():
    # état initial prêt à tester
    return GameState()

def test_ray_from_stops_on_block(state):
    # Place a block at (4, 4), ray from (2, 2) should not include (5, 5)
    state.set_case_blocked((4, 4))
    rules = Rules()
    cells = rules.ray_from(state, (2, 2))
    # Ray in (1,1) direction should stop at (4,4), not include (5,5)
    assert (5, 5) not in cells
    assert (4, 4) not in cells  # Blocked cell is not included

def test_ray_from_includes_all_empty_until_block(state):
    # Place a block at (2, 5), ray from (2, 2) in (0,1) direction
    state.set_case_blocked((2, 5))
    rules = Rules()
    cells = rules.ray_from(state, (2, 2))
    # Should include (2,3), (2,4) but not (2,5) or (2,6)
    assert (2, 3) in cells
    assert (2, 4) in cells
    assert (2, 5) not in cells
    assert (2, 6) not in cells

def test_ray_from_stops_on_edge(state):
    # Ray from (0, 0) should not go out of bounds
    rules = Rules()
    cells = rules.ray_from(state, (0, 0))
    for cell in cells:
        assert 0 <= cell[0] < state.board_X
        assert 0 <= cell[1] < state.board_y

def test_ray_from_diagonal_block(state):
    # Block diagonal path
    state.set_case_blocked((3, 3))
    rules = Rules()
    cells = rules.ray_from(state, (1, 1))
    # Should include (2,2) but not (3,3) or (4,4)
    assert (2, 2) in cells
    assert (3, 3) not in cells
    assert (4, 4) not in cells