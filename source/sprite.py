import pygame
import game

class Sprite():
    def __init__(self, texture, position):
        self.image 	= pygame.image.load(game.rpath + texture)
        self.rect 	= self.image.get_rect()
     	self.rect.x = position[0]
     	self.rect.y = position[1]
        self.pos 	= position
        return

    def draw(self):
        game.screen.blit(self.image, self.rect)