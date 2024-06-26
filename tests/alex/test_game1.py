import pygame
import pytest
from pacman_for_test import render_multi_color_text

# Initialize Pygame and set up fonts and colors
pygame.init()
font = pygame.font.Font(None, 48)  # Use a default font
COLORS = [
    pygame.Color(255, 0, 0),  # Red
    pygame.Color(0, 255, 0),  # Green
    pygame.Color(0, 0, 255),  # Blue
    pygame.Color(255, 255, 0)  # Yellow
]


@pytest.fixture
def setup_pygame():
    # Minimal setup for font rendering
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()


@pytest.fixture
def test_render_multi_color_text(setup_pygame):
    # Define the test scenario
    text = "Test this"
    expected_colors = [(255, 0, 0), (0, 255, 0)]
    result = render_multi_color_text(text, font, COLORS)

    # Assertions to validate the outcome
    assert len(result) == 2, "Expected two words"
    for i, (surf, offset) in enumerate(result):
        assert pygame.Surface.get_at(surf, (0, 0))[:3]\
              == expected_colors[i], f"Color mismatch at index {i}"
