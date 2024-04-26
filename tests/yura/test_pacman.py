import pytest
import Resource_loading as Resource_loading
import pygame
import os

# Function to initialize Pygame, which can be used in tests

@pytest.fixture
def test_background_image_loading():
    assert os.path.exists('assets/background_image/Background.jpg'), "Background image file does not exist"
    background_image = pygame.image.load('assets/background_image/Background.jpg')
    WIDTH, HEIGHT = 900, 950
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    assert background_image.get_size() == (WIDTH, HEIGHT), "Background image not scaled correctly"

