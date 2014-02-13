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
        if game.alvey.jumping:
            speed = game.alvey.speed / 2
        else:
            speed = game.alvey.speed

        # Move left/right/down
        if key == pygame.K_LEFT:
            game.alvey.rect.x -= speed
            game.alvey.left_sprite_rect = game.alvey.rect
            game.alvey.direction = -1
        if key == pygame.K_RIGHT:
            game.alvey.rect.x += speed
            game.alvey.direction = 1

    # Handle gravity
    if game.alvey.rect.bottom >= game.window_size[1] * .95:
        game.alvey.rect.bottom = game.window_size[1] * .95
        game.alvey.jumping = False
        game.alvey.velocity = 0
    if not game.alvey.rect.bottom == game.window_size[1] * .95:
        # Check if they are on a block or not
        if game.test_map.collides_player():
            game.alvey.jumping = False
            game.alvey.velocity = 0
        else:
            game.alvey.velocity += game.alvey.gravity
            game.alvey.rect.y += game.alvey.velocity

    game.test_map.update()

    if game.alvey.rect.right <= 0 and game.alvey.dead == False:
        print("boom. dead")
        game.alvey.dead = True

    if game.test_map.scrolling:
        if game.alvey.rect.right >= 0:
            game.alvey.rect.x -= 1

    return
