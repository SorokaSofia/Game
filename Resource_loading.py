import copy
from board import boards
import pygame
import sys
import math

pygame.init()
pygame.mixer.init()  # Sound initialization

WIDTH, HEIGHT = 900, 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PacMan")

# Resource loading
font = pygame.font.Font(None, 48)
menu_sound = pygame.mixer.Sound('Paramind_cotton_eye_joe_mashup.mp3') 
menu_sound.set_volume(0.012)

# Background image loading
background_image = pygame.image.load('assets/background_image/Background.jpg')  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scaling image to fit screen size