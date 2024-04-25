import pytest
from game_module import Ghost

def test_ghost_movement():
    player_position = (5, 5)
    ghost = Ghost("Blinky", "normal", (3, 3))