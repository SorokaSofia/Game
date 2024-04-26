import pytest
import pygame
from Resource_loading import start_menu, display_text

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
    text_surfaces = [(pygame.Surface((100, 50)), 0), (pygame.Surface((120, 50)), 150)]
    with pytest.raises(TypeError):
        display_text(text_surfaces, 300, font)  # Passing font as additional argument

def test_game_loop_exit(setup_pygame, mocker):
    mocker.patch('Resource_loading.start_menu', return_value=False)
    mocker.patch('pygame.event.get', return_value=[pygame.event.Event(pygame.QUIT)])
    with pytest.raises(SystemExit):
        start_menu()
