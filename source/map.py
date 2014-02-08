import game
import pygame
import sys
import os
from sprite import Sprite


class TileType:

    """
    This is different from Tile!  This class only has tile types.
    """

    def __init__(self):
        self.tiles = {
            'f': ("filename", "floor"),
            'b': ("sample-tile.png", "block"),
            'x': ("filename", "death"),
            'f': ("finished-tile.png", "finished")
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
        self.tiles = []
        self.camera_offset = 0
        self.finished = False

    def draw(self):
        for tile in self.tiles:
            tile.draw

    def update(self):
        for tile in self.tiles:
            tile.sprite.rect.x -= 1

    def collides_player(self):
        for tile in self.tiles:
            if tile.sprite.rect.colliderect(game.alvey.rect):
                if tile.tile_type == 'f':
                    if not self.finished:
                        self.finished = True
                    print("Level complete")
                return True

    def add(self, tile):
        self.tiles.append(tile)


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
        lines = []
        retmap = Map()

        with open(filename) as f:
            for tile_y, line in enumerate(f):
                for tile_x, tile in enumerate(line):
                    print(tile_x, tile_y, tile)

            # lines = [line.split() for line in f]

        return retmap
