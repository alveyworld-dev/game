import pygame
import game


class Sprite(pygame.sprite.Sprite):

    def __init__(self, texture, position, area=None):
        self.image = pygame.image.load(game.rpath + texture).convert()
        self.image.set_colorkey(0)  # I don't know if we really need this
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        if area:
            self.rect.width = area.width
            self.rect.height = area.height
        self.area = area

    def draw(self):
        game.screen.blit(self.image, self.rect, area=self.area)
        
    def change_costume(self, costume):
        self.rect.width = costume.width
        self.rect.height = costume.height
        self.area = costume