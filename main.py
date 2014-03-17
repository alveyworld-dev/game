 #
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
#
# Version 0.2.4
#

import sys
import pygame
from source import game
from source.update import update
from source.draw import draw
from source.sprite import Sprite
from source.sound import *
from source.world import World
from source.jukebox import Jukebox
from source.map import *

clock = pygame.time.Clock()

# Set the framerate. This makes the game smoother, or at least Jarod's
# section of code
framerate = 60


def init():
    """
    Perform game-wide initilization, such as setting variables and loading
    resources
    """

    # Don't touch this unless you want to break everything
    game.main_font = pygame.font.Font("resources/main_font.otf", 14)

    # Set up the game world.  There should only be one of these
    game.world = World()
    game.world.load()
    jukebox = Jukebox()
    jukebox.play()

    # Player (Alvey)
    game.standing = pygame.Rect(2,0,23,64)
    game.standingl = pygame.Rect(2,64,20,64)
    game.jumping = pygame.Rect(269,0,40,64)
    game.jumpingl = pygame.Rect(185,64,39,64)
    game.walking = [pygame.Rect(27,0,40,64),pygame.Rect(75,0,40,64),pygame.Rect(116,0,27,64),pygame.Rect(157,0,27,64),pygame.Rect(183,0,37,64),pygame.Rect(223,0,40,64),pygame.Rect(269,0,40,64),pygame.Rect(318,0,40,64),pygame.Rect(362,0,37,64),pygame.Rect(402,0,29,64),pygame.Rect(430,0,37,64)]
    game.walkingl = [pygame.Rect(27,64,37,64),pygame.Rect(66,64,25,64),pygame.Rect(104,64,28,64),pygame.Rect(138,64,38,64),pygame.Rect(185,64,39,64),pygame.Rect(230,64,40,64),pygame.Rect(274,64,37,64),pygame.Rect(312,64,25,64),pygame.Rect(349,64,29,64),pygame.Rect(381,64,39,64),pygame.Rect(426,64,40,64)]
    game.crouching = pygame.Rect(466,27,24,33)
    game.crouchingl = pygame.Rect(466,91,24,33)
    game.alvey = Sprite("art_team/alveyspritesheet.png", (125, 192), game.standing)
    #game.alvey.rect = game.alvey.area
    game.alvey.dead = False
    game.alvey.direction = 1
    game.alvey.is_down = False
    game.alvey.toggle = 0
    game.alvey.jump = Sound("Sound/jump.wav")
    
    # Alveysprite physics
    game.alvey.jumping = False
    game.alvey.ducking = False
    game.alvey.gravity = .8
    game.alvey.velocity = 0
    game.alvey.jump_high = 15
    game.alvey.jump_low = game.alvey.jump_power = 8
    game.alvey.speed = game.alvey.speed_slow = 8
    game.alvey.speed_fast = 10
    

    game.test_map = MapLoader.load("test3.map")
    game.score = 0


def main():
    """
    Main game initilization code
    """

    # Set up pygame
    pygame.init()
    pygame.mixer.init()
    game.screen = pygame.display.set_mode(game.window_size, pygame.DOUBLEBUF)
    keys = set()

    # Set up game
    init()

    # Perform game loop
    while True:
        timeDelayed = clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys.add(event.key)
            if event.type == pygame.KEYUP:
                keys.discard(event.key)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
        #print 'velocity: ',game.alvey.velocity
        #if game.alvey.velocity > 5:
        #    game.alvey.velocity = 5

        update(keys)        # update.py
        draw(framerate, timeDelayed)              # draw.py

        # Simply flips the display for drawing
        pygame.display.update()
        pygame.display.flip()

    return

# Ignore this, it simply calls the main() function
if __name__ == "__main__":
    main()