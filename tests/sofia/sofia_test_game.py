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