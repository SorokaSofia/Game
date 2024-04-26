import pytest
import Resource_loading
import pygame
import os

# Function to initialize Pygame, which can be used in tests
def init_pygame():
    pygame.init()
    pygame.mixer.init()

@pytest.fixture
def resource_setup():
    init_pygame()
    font = pygame.font.Font(None, 48)
    menu_sound = pygame.mixer.Sound('Paramind_cotton_eye_joe_mashup.mp3')
    return font, menu_sound

def test_font_loaded(resource_setup):
    font, _ = resource_setup
    assert isinstance(font, pygame.font.Font), "Font is not loaded"

def test_sound_loaded(resource_setup):
    _, menu_sound = resource_setup
    assert isinstance(menu_sound, pygame.mixer.Sound), "Sound is not loaded"

def test_background_image_loading():
    init_pygame()
    assert os.path.exists('assets/background_image/Background.jpg'), "Background image file does not exist"
    background_image = pygame.image.load('assets/background_image/Background.jpg')
    WIDTH, HEIGHT = 900, 950
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    assert background_image.get_size() == (WIDTH, HEIGHT), "Background image not scaled correctly"
