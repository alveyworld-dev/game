import pygame
import game


class Sprite(pygame.sprite.Sprite):

    def __init__(self, texture, position):
        self.image = pygame.image.load(game.rpath + texture).convert()
        self.image.set_colorkey(0)  # I don't know if we really need this
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def draw(self):
        game.screen.blit(self.image, self.rect)
