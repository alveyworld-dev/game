import pygame
import game
from math import randint # I think that we should have a couple different 
from sprite import Sprite # costumes that are randomized with each play!

# Maybe we should inherit from the Character class in character.py
# -josh

class Player():
	def __init__(self, health, texture):
		self.alive = True
		self.health = health
		self.texture = pygame.image.load(game.rpath + texture)  # not exact syntax, just basic idea

	def update():
		if self.health <= 0:	
			self.alive = False	

	def attack():
		pass

# Example: my_player = Player(3,"mysprite.png")