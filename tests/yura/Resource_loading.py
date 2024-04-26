import copy
import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 900, 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PacMan")

# Resource loading
font = pygame.font.Font(None, 48)

# Background image loading
background_image = pygame.image.load('assets/background_image/Background.jpg')  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scaling image to fit screen size
