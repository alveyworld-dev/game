import pygame
import game

def update(keys):
    """
    Update game world here
    """

    # Here's how you would go about getting keyboard input
    # for key in keys:
    #     if key == pygame.K_LEFT: sprite.rect.x -= 1
    #     else: ...
    
    # And how to move a sprite named my_sprite
    # my_sprite.rect.x -= 1
    # my_sprite.rect.y -= 1

    game.world.update()

    # Gravity
    if game.alvey.rect.bottom <= 677:
        game.alvey.rect.y += game.world.gravity

    if game.alvey.rect.bottom < 677:
        game.alvey.rect.bottom = 677
        print game.alvey.rect.bottom

    # Handle input
    for key in keys:
        if key == pygame.K_LEFT: 
            game.alvey.rect.x -= 15
        if key == pygame.K_RIGHT: 
            game.alvey.rect.x += 15
        if key == pygame.K_UP: 
            game.alvey.rect.y -= 25
            game.alvey.jump.play()

    if game.alvey.rect.right <= 0:
        print("boom. dead")

    if game.alvey.rect.right >= 0:
        game.alvey.rect.x -= 2

    return
