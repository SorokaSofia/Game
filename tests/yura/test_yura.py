import pytest
import pygame
from Resource_loading import display_text


@pytest.fixture
def setup_pygame():
    pygame.init()
    pygame.font.init()
    pygame.display.set_mode((800, 600))
    yield
    pygame.quit()


@pytest.fixture
def font():
    return pygame.font.Font(None, 48)


def test_display_text(setup_pygame, font):
    # Організація даних у масивах для зручності та читабельності
    surface_one = pygame.Surface((100, 50))
    surface_two = pygame.Surface((120, 50))
    text_surfaces = [
        (surface_one, 0),
        (surface_two, 150)
    ]
    # Виклик функції з перехопленням виключення TypeError
    with pytest.raises(TypeError):
        display_text(text_surfaces, 300, font)
