import pytest
import pygame
from pacman_for_test import render_multi_color_text
from unittest.mock import patch


# Assuming the font and COLORS are defined somewhere in your code, or provided here:
pygame.init()
font = pygame.font.Font(None, 48)  # Use a default font
COLORS = [pygame.Color(255, 0, 0), pygame.Color(0, 255, 0), pygame.Color(0, 0, 255), pygame.Color(255, 255, 0)]  # Basic colors

@pytest.fixture
def setup_pygame():
    # Minimal setup for font rendering
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()

def test_render_multi_color_text(setup_pygame):
    text = "Test this"
    expected_colors = [(255, 0, 0), (0, 255, 0)]  # RGB values only, ignoring alpha
    result = render_multi_color_text(text, font, COLORS)

    assert len(result) == 2  # Two words
    for i, (surf, offset) in enumerate(result):
        # Checking the color of the first pixel on each rendered word surface, ignoring alpha channel
        assert pygame.Surface.get_at(surf, (0, 0))[:3] == expected_colors[i], f"Failed at index {i}"


    
