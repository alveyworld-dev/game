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

    # Handle input
    for key in keys:
    
        if key == pygame.K_UP and game.alvey.jumping == False:
            game.alvey.jumping = True
            game.alvey.velocity -= game.alvey.jump_power
            game.alvey.rect.y += game.alvey.velocity
            game.alvey.jump.play()
    
        
        if game.alvey.jumping:
            speed = game.alvey.speed/2
        else:
            speed = game.alvey.speed

        if key == pygame.K_LEFT:
            game.alvey.rect.x -= speed
        if key == pygame.K_RIGHT:
            game.alvey.rect.x += speed
        
            

    if game.alvey.rect.bottom >= game.window_size[1]*.95:
        game.alvey.rect.bottom = game.window_size[1]*.95
        game.alvey.jumping = False
        game.alvey.velocity = 0
    if not game.alvey.rect.bottom == game.window_size[1]*.95:
        game.alvey.velocity += game.alvey.gravity
        game.alvey.rect.y += game.alvey.velocity

    if game.alvey.rect.right <= 0:
        print("boom. dead")

    if game.alvey.rect.right >= 0:
        game.alvey.rect.x -= 2

    return
