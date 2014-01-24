import pygame
import graphics
import game
from sprite import Sprite

def draw():
    """
    Drawing logic
    """

    # Fill the screen with black
    game.screen.fill((40, 40, 40))
    
    # insert logic here

    # Don't change these
    pygame.display.update()
    pygame.display.flip()

    return