import pygame
import game
from random import randint
from sprite import Sprite
from sound import *


class Character:

    """
    Represents an in-game character: player, npc, enemy, etc.  This class
    _should not_ be used directly!  It should rather be inherited by the classes
    that will use it.
    """

    def __init__(self, filename, spawnpoint):
        """
        The filename is simply used to generate a sprite
        Spawnpoint is used for the initial position
        """

        self.spawnpoint = spawnpoint
        self.sprite = Sprite(filename, spawnpoint)
        self.health = 100
        self.alive = True

    def draw(self):
        self.sprite.draw()

    def update(self):
        pass

    def kill(self):
        pass

    def hurt(self, dmg):
        if self.health - dmg <= 0:
            self.alive = 0
            self.health = 0
        else:
            self.health -= dmg
