import copy
from board import boards
import pygame
import sys
import math


pygame.init()
pygame.mixer.init()  # Ініціалізація для звуку


WIDTH, HEIGHT = 900, 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PacMan")

# Завантаження ресурсів
font = pygame.font.Font(None, 48)
menu_sound = pygame.mixer.Sound('Paramind_cotton_eye_joe_mashup.mp3') 
menu_sound.set_volume(0.013)

# Завантаження фонового зображення
background_image = pygame.image.load('assets/background_image/Background.jpg') 
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Масштабування зображення до розміру екрану

colors = [pygame.Color('Red'), pygame.Color('Green'), pygame.Color('Blue'), pygame.Color('Yellow')]

def render_multi_color_text(text, font, colors):
    """Відображає текст, розділений на чотири кольори."""
    words = text.split()
    space = font.size(' ')[0]  # Ширина пробілу
    x_offset = 0
    images = []  # Зображення слів різного кольору
    for index, word in enumerate(words):
        color = colors[index % len(colors)]  # Циклічне використання кольорів
        word_surface = font.render(word, True, color)
        images.append((word_surface, x_offset))
        x_offset += word_surface.get_width() + space  # Збільшуємо зміщення на ширину слова та пробілу
    return images

# Глобальні змінні
running_game = False  # Змінна для керування станом гри

def start_menu():
    menu_sound.set_volume(0.013)
    menu_sound.stop() 
    menu_sound.play(-1)
    global running_game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Старт гри
                    running = False
                    running_game = True
                elif event.key == pygame.K_ESCAPE:  # Вихід з гри
                    pygame.quit()
                    sys.exit()

         # Відображення фонового зображення
        screen.blit(background_image, (0, 0))
             # Відображення тексту з різнокольоровими словами
        enter_text_surfaces = render_multi_color_text('Press Enter to Start', font, colors)
        escape_text_surfaces = render_multi_color_text('Press Escape to Exit', font, colors)
        
        # Розрахунок позиції для відображення тексту
        enter_text_width = sum(image.get_width() for image, _ in enter_text_surfaces) + (len(enter_text_surfaces) - 1) * font.size(' ')[0]
        escape_text_width = sum(image.get_width() for image, _ in escape_text_surfaces) + (len(escape_text_surfaces) - 1) * font.size(' ')[0]

        for image, offset in enter_text_surfaces:
            screen.blit(image, (WIDTH / 2 - enter_text_width / 2 + offset, HEIGHT / 2 + 100))
        for image, offset in escape_text_surfaces:
            screen.blit(image, (WIDTH / 2 - escape_text_width / 2 + offset, HEIGHT / 2 + 150))
        pygame.display.flip()

def game_loop():
    global running_game
    while running_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Використання ESC для повернення до меню
                    running_game = False
                    start_menu()  # Повторний виклик start_menu

start_menu()

def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

      # Відображення фонового зображення
        screen.blit(background_image, (0, 0))

        title = font.render('Pac-Man', True, 'white')
        start_text = font.render('Press Enter to start', True, 'white')
        quit_text = font.render('Press Esc to quit', True, 'white')

        title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/3))
        start_rect = start_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        quit_rect = quit_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))

        screen.blit(title, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
