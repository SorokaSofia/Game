import pytest
from game_module import Ghost

def test_ghost_movement():
    player_position = (5, 5)
    ghost = Ghost("Blinky", "normal", (3, 3))

    # Move towards player
    assert ghost.move(player_position) == (4, 4), "Ghost should move towards the player"
