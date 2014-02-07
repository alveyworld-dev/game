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
            # game.alvey.jump.play() this crashes game
        
        if game.alvey.jumping:
            speed = game.alvey.speed/2
        else:
            speed = game.alvey.speed

        if key == pygame.K_LEFT:
            game.alvey.rect.x -= speed
            game.alvey.left_sprite_rect = game.alvey.rect
            game.alvey.direction = -1
        if key == pygame.K_RIGHT:
            game.alvey.rect.x += speed
            game.alvey.direction = 1
        if key == pygame.K_DOWN:
            game.alvey.duck_sprite_rect = game.alvey.rect
            game.alvey.image = pygame.image.load(game.rpath + "art_team/alveyduck.png").convert()
            game.alvey.ducking = True

    if game.alvey.rect.bottom >= game.window_size[1]*.95:
        game.alvey.rect.bottom = game.window_size[1]*.95
        game.alvey.jumping = False
        game.alvey.velocity = 0
    if not game.alvey.rect.bottom == game.window_size[1]*.95:
        game.alvey.velocity += game.alvey.gravity
        game.alvey.rect.y += game.alvey.velocity

    if game.alvey.rect.right <= 0 and game.alvey.dead == False:
        print("boom. dead")
        game.alvey.dead = True

    if game.alvey.rect.right >= 0:
        game.alvey.rect.x -= 2

    return
