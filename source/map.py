import game, pygame, sys, os
from sprite import Sprite

class TileType:
    """
    This is different from Tile!  This class only has tile types.
    """

    def __init__(self):
        self.tiles = {     
            'f'   : ("filename", "floor"),
            'b'   : ("sample-tile.png", "block"),
            'x'   : ("filename", "death")
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

class Tile:
    """
    Represents a singular tile entity
    """

    def __init__(self, tiletype, position):
        self.tile_type = tiletype
        self.position = position
        self.sprite = Sprite(TileType()[tiletype][0], self.position)

    def draw(self):
        self.sprite.draw()

class Map:
    """
    Defines a singular world map
    """

    def __init__(self):
        self.tile_entities = []
        self.camera_offset = 0

    def draw(self):
        """
        Draw all tile entities included in this map
        """

        for tile in self.tile_entities:
            tile.draw()

    def update(self):
        for tile in self.tile_entities:
            tile.sprite.rect.x -= 1

    def collides_player(self):
        for tile in self.tile_entities:
            if tile.sprite.rect.colliderect(game.alvey.rect):
                return True

    def add(self, tile):
        self.tile_entities.append(tile)

class MapLoader:
    @staticmethod
    def tile_offset(axis):
        """
        Returns an offset from tile position to real position (eg: * 32)
        """

        return (axis * 32)

    @staticmethod
    def load(filename):
        """
        Loads a map from a given .map file and returns a Map object
        """

        filename = game.rpath + "map/" + filename
        content  = []

        with open(filename) as f:
            for i in range(os.stat(filename).st_size):
                fct = f.read(1)
                content.append(fct)
        
        retmap = Map()

        for idx, val in enumerate(content):
            if val != '.': retmap.add(
                                    Tile(val, ((32 * idx), 
                                    MapLoader.tile_offset(19))))

        return retmap



