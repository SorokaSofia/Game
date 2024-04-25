import pytest
from game_module import Ghost

def test_ghost_movement():
    player_position = (5, 5)
    ghost = Ghost("Blinky", "normal", (3, 3))

    # Move towards player
    assert ghost.move(player_position) == (4, 4), "Ghost should move towards the player"

    # Change mode to frightened
    ghost.mode = "frightened"
    assert ghost.move(player_position) == (3, 3), "Ghost should move away from the player"
