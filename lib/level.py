import pygame


class Level(object):
    blank       = '.'
    block       = 'b'

    tiles = {
        'b': (pygame.image.load("resources/testblock-tile.gif"), "block"),
        'c': (pygame.image.load("resources/testclimb-tile.gif"), "climb"),
        'e': (pygame.image.load("resources/testenemy-tile.gif"), "enemy"),
        't': (pygame.image.load("resources/testtrap-tile.gif"), "trap"),
        'x': (pygame.image.load("resources/testdeath-tile.gif"), "death"),
        'r': (pygame.image.load("resources/testride-tile.gif"), "ride"),
        'p': (pygame.image.load("resources/testpowerup-tile.gif"), "powerup")
    }

    blockWidth  = 32
    blockHeight = 32

    def __init__(self, file):
        self.collisionLayer = [row.strip('\n') for row in open(file, 'r').readlines()]
        self.levelWidth = len(self.collisionLayer[0])
        self.levelHeight = len(self.collisionLayer)

        self.leftEdge = 0
        self.topEdge = 0
        self.rightEdge = self.levelWidth * self.blockWidth
        self.bottomEdge = self.levelHeight * self.blockHeight

        self.blockSurf = pygame.image.load("lib/block.gif")
