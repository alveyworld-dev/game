import pygame
import game
from math import randint  # I think that we should have a couple different
from sprite import Sprite  # costumes that are randomized with each play!


class Enemy():

    def __init__(self, health, texture):
        self.alive = True
        # not exact syntax, just basic idea
        self.texture = pygame.image.load(game.rpath + texture)

    def update():
        pass

    def die():
        pass

# Example: my_player = Player(3,"mysprite.png")



