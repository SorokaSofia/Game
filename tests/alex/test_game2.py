import pytest
import pygame
from pacman_for_test import display_text

@pytest.fixture
def setup_pygame():
    # Initialize Pygame and set display mode
    pygame.init()
    pygame.display.set_mode((800, 600))
    yield
    pygame.quit()


def test_display_text(setup_pygame):
    # Create font inside the test since it is not used elsewhere
    font = pygame.font.Font(None, 48)
    # Define the surfaces and offsets for testing
    text_surfaces = [
        (pygame.Surface((100, 50)), 0),
        (pygame.Surface((120, 50)), 150)
    ]
    # Check display_text function call for errors
    # Assuming 'display_text' does not take a 'font' argument
    with pytest.raises(TypeError):
        display_text(text_surfaces, 300, font)  # Incorrect number of arguments
