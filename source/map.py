import game, pygame, sys
from sprite import Sprite

class Tile:
    """
    Tiles will be represented thusly, I think you get the gist.
    You can reference these by Tile.air, etc.
    """

    air     = 0
    floor   = 1

class Map:
    """
    Defines a singular world map
    """

    def __init__(self):
        self.tile_entities = set()

    def draw(self):
        pass

    def update(self):
        pass

class MapLoader:
    @staticmethod
    def load(filename):
        pass


