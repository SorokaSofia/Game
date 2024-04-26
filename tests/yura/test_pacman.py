import pytest
import Resource_loading as Resource_loading
import pygame
import os

# Function to initialize Pygame, which can be used in tests
def init_pygame():
    pygame.init()

@pytest.fixture
def resource_setup():
    init_pygame()
    font = pygame.font.Font(None, 48)
    return font


def test_background_image_loading():
    init_pygame()
    assert os.path.exists('assets/background_image/Background.jpg'), "Background image file does not exist"
    background_image = pygame.image.load('assets/background_image/Background.jpg')
    WIDTH, HEIGHT = 900, 950
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    assert background_image.get_size() == (WIDTH, HEIGHT), "Background image not scaled correctly"

