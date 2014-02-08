import pygame
import sys
import game
from sprite import Sprite
from sound import Sound, Music


class BackgroundLayer:

    """
    Encapsulates a scrolling layer of the background.  It will move left
    at a given speed, and loop once it exits the screen.  Multiple layers
    with multiple speeds can be used to create a parallax effect, or to
    allow many-layered backgrounds
    """

    def __init__(self, filename, scroll_speed, ypos):
        pos = (0, ypos)

        self.s1 = Sprite(filename, pos)
        self.s2 = Sprite(filename, (1280, pos[1]))

        self.filename = filename
        self.position = pos
        self.speed = scroll_speed

    def draw(self):
        self.s1.draw()
        self.s2.draw()

    def update(self):
        self.s1.rect.x -= self.speed

        if self.s1.rect.x <= 0:
            self.s2.rect.x -= self.speed

        if self.s2.rect.x <= 0:
            self.s1.rect.x = 0
            self.s2.rect.x = 1280


class World:

    """
    World: encapsulates everything related to the world: time, children,
    background, drawing, etc.
    """

    def __init__(self):
        # World gravity constant
        self.gravity = 5

    def load(self):
        """
        Load the required resources to display the world
        """

        # The order here matters! Back to front.
        self.layers = [
            # Background mountains
            BackgroundLayer("world/mountain.png", 1, 82),

            # Foreground trees
            BackgroundLayer("world/trees.png", 2, 0),

            # Clouds
            BackgroundLayer("world/clouds.png", 3, 0),

            # Ground
            BackgroundLayer("world/test_bg_4.png", 2, 0)
        ]

    def update(self):
        """
        Update critical world information, such as background position, etc.
        """

        for layer in self.layers:
            layer.update()

    def draw(self):
        """
        Draw the world and everything in it
        """

        for layer in self.layers:
            layer.draw()
