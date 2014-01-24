import pygame
import game

def draw_rect(size, color, position):
    """
    Draws a rectangle with style

    eg:
        size (width, height)
        color (255, 255, 255) rgb
        positon (x, y)
    """

    pygame.draw.rect(game.screen, color, (position, size), 0)

    return