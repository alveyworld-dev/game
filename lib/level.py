import pygame


class Level(object):
    blank       = '.'
    block       = 'b'
    blockWidth  = 32
    blockHeight = 32

    def __init__(self, file):
        self.collisionLayer = [row.strip('\n') for row in
                               open(file, 'r').readlines()]
        self.levelWidth = len(self.collisionLayer[0])
        self.levelHeight = len(self.collisionLayer)

        self.leftEdge = 0
        self.topEdge = 0
        self.rightEdge = self.levelWidth * self.blockWidth
        self.bottomEdge = self.levelHeight * self.blockHeight

        self.blockSurf = pygame.image.load("lib/block.gif")
