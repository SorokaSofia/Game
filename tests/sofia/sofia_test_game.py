import pytest
import pygame

# Assuming the move_player function is in the game_logic module
from game_logic import move_player

# A pytest fixture to set up the player environment
@pytest.fixture
def player_setup():
    x, y = 100, 100  # Initial player position
    player_speed = 5  # Player speed
    return x, y, player_speed

def test_move_player_right(player_setup):
    x, y, player_speed = player_setup
    direction = 0  # Direction right
    turns_allowed = [True, False, False, False]  # Only right movement allowed

    # Call the function under test
    new_x, new_y = move_player(x, y, direction, turns_allowed, player_speed)

    # Assert the expected results
    assert new_x == x + player_speed
    assert new_y == y