import game, pygame, sys
from sprite import Sprite

class Tile:
    """
    You can access a tile likewise:

        test_tile = Tile()["air"]
            => ("filename", 0)
    """

    def __init__(self):
        self.tiles = {
            "air"   : ("filename", 0),       
            "floor" : ("filename", 1)
        }

    def __getitem__(self, key):
        """
        Don't mind this.  It is simply a way to easily access tiles
        """
        return self.tiles[key]

    def __setitem__(self, key, value):
        """
        Don't mind this.  It is simply a way to easily access tiles
        """
        self.tiles[key] = value

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


