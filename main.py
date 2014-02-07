#
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
# 
# Version 0.2.4
# 

import sys, pygame
from source import game
from source.update import update
from source.draw import draw
from source.sprite import Sprite
from source.sound import *
from source.world import World
from source.jukebox import Jukebox
from source.map import *

clock=pygame.time.Clock()

# Set the framerate. This makes the game smoother, or at least Jarod's section of code
framerate = 60

def init():
    """
    Perform game-wide initilization, such as setting variables and loading
    resources
    """

    # Don't touch this unless you want to break everything
    game.main_font              = pygame.font.Font("resources/main_font.ttf", 18)
    
    # Set up the game world.  There should only be one of these
    game.world                  = World()
    game.world.load()
    jukebox = Jukebox()
    jukebox.play()
    
    # Player (Alvey)
    game.alvey                  = Sprite("art_team/alveysprite.png", (125, 500))
    game.alvey.left_sprite      = pygame.image.load(game.rpath + "art_team/alveysprite.png")
    game.alvey.left_sprite      = pygame.transform.flip(game.alvey.left_sprite, True, False)
    game.alvey.left_sprite_rect = game.alvey.left_sprite.get_rect()    
    game.alvey.jump             = Sound("jump.wav")
    game.alvey.dead             = False
    game.alvey.direction        = 1
    # Alveysprite physics
    game.alvey.jumping          = None
    game.alvey.gravity          = .9
    game.alvey.velocity         = 0
    game.alvey.jump_power       = 12
    game.alvey.speed            = 10

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
        timeDelayed=clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: keys.add(event.key)
            if event.type == pygame.KEYUP: keys.discard(event.key)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()

        update(keys)        # update.py
        draw(framerate,timeDelayed)              # draw.py
        
        # Simply flips the display for drawing
        pygame.display.update()
        pygame.display.flip()

    return

# Ignore this, it simply calls the main() function
if __name__ == "__main__":
    main()