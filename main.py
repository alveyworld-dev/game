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
from source.sound import Sound, Music

def init():
    """
    Perform game-wide initilization, such as setting variables and loading
    resources
    """

    # Don't touch this unless you want to break everything
    game.main_font   = pygame.font.Font("resources/main_font.ttf", 18)

    # Example:
    # game.my_sprite = Sprite("filename.png", (50, 50))
    
    # Play a sound!
    # game.coin = Sound("coin.wav")
    # game.coin.play()

    # Drop those jams!
    # game.music = Music("music.ogg")
    # game.music.play()

    return

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: keys.add(event.key)
            if event.type == pygame.KEYUP: keys.discard(event.key)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()

        update(keys)        # update.py
        draw()              # draw.py
        
        # Simply flips the display for drawing
        pygame.display.update()
        pygame.display.flip()

    return

# Ignore this, it simply calls the main() function
if __name__ == "__main__":
    main()