import pytest
from unittest.mock import Mock
from pacman import Ghost

# Тестування конструктора класу Ghost
def test_ghost_initialization():
    # Створення мок-об'єктів для зображення та напрямку
    mock_img = Mock()
    mock_direct = Mock()
    
    # Створення екземпляру класу Ghost
    ghost = Ghost(100, 200, 'Pacman', 5, mock_img, mock_direct, False, True, 1)
    
    # Перевірка атрибутів об'єкта
    assert ghost.x_pos == 100
    assert ghost.y_pos == 200
    assert ghost.center_x == 122  # x_pos + 22
    assert ghost.center_y == 222  # y_pos + 22
    assert ghost.target == 'Pacman'
    assert ghost.speed == 5
    assert ghost.img is mock_img
    assert ghost.direction is mock_direct
    assert not ghost.dead
    assert ghost.in_box
    assert ghost.id == 1

    # Перевірка викликів методів
    ghost.check_collisions.assert_called_once()
    ghost.draw.assert_called_once()