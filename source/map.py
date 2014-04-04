import game
import pygame
import sys
import os
import math
import time
import string
from sprite import Sprite


class TileType:

    """
    This is different from Tile!  This class only has tile types.
    """

    def __init__(self):
        self.tiles = {
            'b': ("grass-tile.png", "block"),
            'd': ("dirt-tile.png", "block"),
            '-': ("uncollide-tile.png", "uncollideable"),
            'c': ("testclimb-tile.gif", "climb"),
            'e': ("testenemy-tile.gif", "enemy"),
            't': ("testtrap-tile.gif", "trap"),
            'x': ("sand-tile.png", "death"),
            'r': ("testride-tile.gif", "ride"),
            'p': ("testpowerup-tile.gif", "powerup"),
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


class Enemy(Tile):

    def __init__(self, tiletype, starting_pos=(0, 0), costume="art_team/bee.png"):
        Tile.__init__(self, tiletype, starting_pos)
        self.alive = True
        # not exact syntax, just basic idea
        self.sprite = Sprite(costume, starting_pos)

    def update():
        pass

    def die():
        pass

    def draw(self):
        if not game.test_map.collides_enemy(self):
            self.sprite.rect.y += 5
        else:
            self.sprite.rect.y += -1

        #self.sprite.rect.x -= 1
        self.sprite.draw()


class Map:

    """
    Defines a singular world map
    """

    def __init__(self):
        self.tiles = []
        self.camera_offset = 0
        self.finished = False
        self.scrolling = False

    def draw(self):
        for tile in self.tiles:
            tile[0].draw()

    def update(self, changed):
        for tile in self.tiles:
            if changed:
                tile[0].sprite.rect.x -= changed
            #tile[0].sprite.rect.y=tile[2]+int(math.sin((time.time()+tile[1]))*8)

    def block_tile(self, tile, enemy=None):  # its a block
        tiletop = tile[0].sprite.rect.copy()
        tileleft = tile[0].sprite.rect.copy()
        tileright = tile[0].sprite.rect.copy()
        tilebottom = tile[0].sprite.rect.copy()
        tiletop.height = 5
        tiletop.width = 22
        tiletop.left += 5
        tileleft.width = 5
        tileleft.height = 22
        tileleft.bottom += 5

        tilebottom.height = 5
        tilebottom.bottom += 27
        tilebottom.width = 20
        tilebottom.left += 6
        tileright.width = 5
        tileright.left += 27
        tileright.height = 22
        tileright.bottom += 5
        alveytile = game.alvey.rect.copy()
        alveytile.width = alveytile.width - 6
        alveytile.left += 3
        alveytile.height = game.alvey.rect.height - 7
        alveytile.bottom += 7

        if enemy:
            return enemy.sprite.rect.colliderect(tiletop)

        if alveytile.colliderect(tileleft):
            # print "LEFTHIT"
            game.alvey.rect.right = tile[0].sprite.rect.left - 1
        elif alveytile.colliderect(tileright):
            # print " RIGHTHIT"
            game.alvey.rect.left = tile[0].sprite.rect.right + 1
        elif game.alvey.rect.colliderect(tilebottom):
            # print "BOTTOMHIT"
            game.alvey.rect.top = tile[0].sprite.rect.bottom + 1
            game.alvey.velocity *= -1
        elif alveytile.colliderect(tiletop):
            # print "TOPHIT"
            game.alvey.velocity = 0
            game.alvey.rect.bottom = tile[0].sprite.rect.top + 1
            return True
        return False

    def climb_tile(self, tile):  # its a climb
        if game.alvey.rect.colliderect(tile[0].sprite.rect):
            return True
        return False

    def enemy_tile(self, tile):  # its a enemy
        alveyspos = (game.alvey.rect.x, game.alvey.rect.y)

        if game.alvey.rect.colliderect(tile[0].sprite.rect):
<<<<<<< HEAD
            print "Ima dumbhead"
=======
            game.alvey.dead = True
>>>>>>> 7f397b14cd66c5b68c4171f6e7ca566af733a271
        return False

    def trap_tile(self, tile):  # its a trap
        if game.alvey.rect.colliderect(tile[0].sprite.rect):
            game.alvey.velocity = .1
            return True

        return False

    def death_tile(self, tile):  # its a death
        alveyspos = (game.alvey.rect.x, game.alvey.rect.y)

        if game.alvey.rect.colliderect(tile[0].sprite.rect):
            game.alvey.dead = True
        return False

    def ride_tile(self, tile):  # its a ride
        return False

    def powerup_tile(self, tile):  # its a powerup
        return False

    def finish_tile(self, tile):  # its a finish
        if game.alvey.rect.colliderect(tile[0].sprite.rect):
                if not self.finished:
                    self.finished = True
                    print("Level complete")
                    game.alvey.velocity = 0

                    # change level
                    game.alvey.rect.x = 20
                    game.alvey.rect.y = 20
                    game.test_map = MapLoader.load("preston.map")

                return False

        return False

    def collides_player(self):
        # print "collides_player()"
        collide = False
        for tile in self.tiles:
            if tile[0].tile_type == 'b' or tile[0].tile_type == 'd':
                collide = self.block_tile(tile)  # its a block
            elif tile[0].tile_type == 'c':
                collide = self.climb_tile(tile)  # its a climb
            elif tile[0].tile_type == 'e':
                collide = self.enemy_tile(tile)  # its a enemy
            elif tile[0].tile_type == 't':
                collide = self.trap_tile(tile)  # its a trap
            elif tile[0].tile_type == 'x':
                collide = self.death_tile(tile)  # its a death
            elif tile[0].tile_type == 'r':
                collide = self.ride_tile(tile)  # its a ride
            elif tile[0].tile_type == 'p':
                collide = self.powerup_tile(tile)  # its a powerup
            elif tile[0].tile_type == 'f':
                collide = self.finish_tile(tile)  # its a finish
            if collide:
                    return True
        return collide

    def collides_enemy(self, enemy):
        # print "collides_player()"
        collide = False
        for tile in self.tiles:
            if tile[0].tile_type == 'b':
                collide = self.block_tile(tile, enemy=enemy)
            if collide:
                    return True
        return collide

    def add(self, tile):
        self.tiles.append([tile,tile.sprite.rect.x,tile.sprite.rect.y])


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
        experimental = []
        retmap = Map()

        with open(filename) as f:
            lines=open(filename).readlines()
            for tile_y, line in enumerate(f):
                experimental.append([])
                for tile_x, tile in enumerate(line):
                    experimental[tile_y].append(False)
                    if not tile == '\n':
                        if tile == 'e':
                            mT = Enemy(tile, starting_pos=(MapLoader.tile_offset(
                                tile_x), MapLoader.tile_offset(tile_y)), costume="art_team/bee.png")
                            retmap.add(mT)
                        else:
                            t = tile
                            try:
                                if tile == "b":
                                    stuff = lines[tile_y - 1]
                                    l = stuff[tile_x]
                                    if not l == "." or (tile_y >= 1 and not experimental[tile_y - 1][tile_x] is None and experimental[tile_y - 1][tile_x]):
                                        t = "d"
                                        experimental[tile_y][tile_x] = True
                                elif tile == '.':
                                    stuff = lines[tile_y]
                                    l = stuff[tile_x]
                                    if l == "d" or l == "b" or l == "-" or (tile_y >= 1 and not experimental[tile_y - 1][tile_x] is None and experimental[tile_y - 1][tile_x]):
                                        t = "-"
                                        experimental[tile_y][tile_x] = True
                            except:
                                pass
                            if not t == ".":
                                mT = Tile(t,
                                         (MapLoader.tile_offset(tile_x),
                                          MapLoader.tile_offset(tile_y)))
                                retmap.add(mT)

        return retmap
