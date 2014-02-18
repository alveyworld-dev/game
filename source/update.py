import pygame
import game


def update(keys):
    """
    Update game world here
    """

    game.world.update()

    # Handle input
    for key in keys:
        # Perform jump
        if key == pygame.K_UP and game.alvey.jumping == False:
            game.alvey.jumping = True
            game.alvey.velocity -= game.alvey.jump_power
            game.alvey.rect.y += game.alvey.velocity
            


        # Decay jump velocity
        

        # Move left/right/down
        if key == pygame.K_LEFT:
            if not game.alvey.jumping:
                game.alvey.speed += .5
            else:
                game.alvey.speed = max(game.alvey.maxspeed/2, game.alvey.speed)
            game.alvey.rect.x -= min(game.alvey.speed,game.alvey.maxspeed)
            game.alvey.left_sprite_rect = game.alvey.rect
            game.alvey.direction = -1
        if key == pygame.K_RIGHT:
            print game.alvey.speed
            if not game.alvey.jumping:
                game.alvey.speed += .5
            else:
                game.alvey.speed = max(game.alvey.maxspeed/2, game.alvey.speed)
            game.alvey.rect.x += min(game.alvey.speed,game.alvey.maxspeed)
            game.alvey.direction = 1

    # Handle gravity

    if game.test_map.collides_player():
        game.alvey.jumping = False
        game.alvey.velocity = 0
    else:
        game.alvey.velocity += game.alvey.gravity
        if game.alvey.velocity > 3:
            for i in range(int(game.alvey.velocity)):
                print "y: ", game.alvey.rect.y
                game.alvey.rect.y += 1
                if game.test_map.collides_player():
                    game.alvey.velocity = -5
        else:
            game.alvey.rect.y += game.alvey.velocity

    game.test_map.update()

    if game.alvey.rect.right <= 0 and game.alvey.dead == False:
        print("boom. dead")
        game.alvey.dead = True

    if game.test_map.scrolling:
        if game.alvey.rect.right >= 0:
            game.alvey.rect.x -= 1

    return
