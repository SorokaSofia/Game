import pygame
import sys
import copy
import math
from board import boards

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Sound initialization

# Constants
WIDTH, HEIGHT = 900, 950
FONT_SIZE = 48
GAME_TITLE = "PacMan"
BACKGROUND_IMAGE_PATH = 'assets/background_image/Background.jpg'
MENU_SOUND_PATH = 'Paramind_cotton_eye_joe_mashup.mp3'

# Colors
COLORS = [pygame.Color('Red'), pygame.Color('Green'), pygame.Color('Blue'), pygame.Color('Yellow')]

# Setup screen and font
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)
font = pygame.font.Font(None, FONT_SIZE)

# Load and setup sounds
menu_sound = pygame.mixer.Sound(MENU_SOUND_PATH)
menu_sound.set_volume(0.012)

# Load and setup background image
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

def render_multi_color_text(text, font, colors):
    words = text.split()
    space = font.size(' ')[0]  # Space width
    x_offset = 0
    images = []  # Images of words in different colors
    for index, word in enumerate(words):
        color = colors[index % len(colors)]  # Cyclical color usage
        word_surface = font.render(word, True, color)
        images.append((word_surface, x_offset))
        x_offset += word_surface.get_width() + space  # Increase offset by the width of the word and space
    return images

def start_menu():
    menu_sound.stop()
    menu_sound.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start game
                    return True
                elif event.key == pygame.K_ESCAPE:  # Exit game
                    pygame.quit()
                    sys.exit()

        # Displaying background and text
        screen.blit(background_image, (0, 0))
        enter_text_surfaces = render_multi_color_text('Press Enter to Start', font, COLORS)
        escape_text_surfaces = render_multi_color_text('Press Escape to Exit', font, COLORS)
        
        # Displaying text
        display_text(enter_text_surfaces, HEIGHT / 2 + 100)
        display_text(escape_text_surfaces, HEIGHT / 2 + 150)
        pygame.display.flip()

def display_text(text_surfaces, y):
    for image, offset in text_surfaces:
        total_width = sum(img.get_width() for img, _ in text_surfaces) + (len(text_surfaces) - 1) * font.size(' ')[0]
        screen.blit(image, (WIDTH / 2 - total_width / 2 + offset, y))

def game_loop():
    running_game = start_menu()
    while running_game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type is pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Use ESC to return to the menu
                    running_game = False  # Stop game loop
                    start_menu()  # Re-calling start_menu

if __name__ == "__main__":
    game_loop()
