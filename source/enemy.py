import pygame
import game
from random import randint  # I think that we should have a couple different
from sprite import Sprite  # costumes that are randomized with each play!



class Enemy:

    def __init__(self, costume="art_team/bee.png", starting_pos=(0,0)):
    	super(Tile, self)
        self.alive = True
        # not exact syntax, just basic idea
        self.sprite = Sprite(costume, starting_pos)
    def update():
        pass

    def die():
        pass

    def draw(self):
        self.sprite.draw()



