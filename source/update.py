import pygame
import game


def update(keys):
    """
    Update game world here
    """

    game.world.update()

    # Handle input
    if pygame.K_DOWN in keys:
        game.alvey.is_down = True
    else:
        game.alvey.is_down = False

    #running man!
    if (pygame.K_LEFT in keys or pygame.K_RIGHT in keys):
        game.alvey.toggle += 1
        if game.alvey.toggle % 5:
            game.alvey.toggle += 1

    
    for key in keys:
        # Perform jump
        if key == pygame.K_SPACE and game.alvey.jumping == False:
            if not game.alvey.is_down:
                game.alvey.change_costume(game.standing)
            game.alvey.jumping = True
            game.alvey.jump.play()
            if pygame.K_b in keys and (pygame.K_LEFT in keys or pygame.K_RIGHT in keys):
                game.alvey.jump_power = game.alvey.jump_high
            else:
                game.alvey.jump_power = game.alvey.jump_low
           
            game.alvey.velocity -= game.alvey.jump_power
            game.alvey.rect.y += game.alvey.velocity
        
        if key == pygame.K_DOWN and game.alvey.jumping == True:
            if not game.test_map.collides_player():
                game.alvey.velocity += game.alvey.gravity
            game.alvey.rect.y += game.alvey.velocity
        elif key == pygame.K_DOWN:
            game.alvey.change_costume(game.crouching)
            if not game.test_map.collides_player():
                game.alvey.velocity += game.alvey.gravity
            game.alvey.rect.y += game.alvey.velocity

        # Move left/right/down
        if key == pygame.K_LEFT:
            
            if not game.alvey.is_down:
                costumes = len(game.walkingl)
                game.alvey.change_costume(game.walkingl[game.alvey.toggle%costumes])
            if pygame.K_b in keys:
                game.alvey.speed = game.alvey.speed_fast
            else:
                game.alvey.speed = game.alvey.speed_slow
            game.alvey.rect.x -= game.alvey.speed
            game.alvey.direction = -1
        elif key == pygame.K_RIGHT:
            
            if not game.alvey.is_down:
                costumes = len(game.walking)
                game.alvey.change_costume(game.walking[game.alvey.toggle%costumes])
            if pygame.K_b in keys:
                game.alvey.speed = game.alvey.speed_fast
            else:
                game.alvey.speed = game.alvey.speed_slow
            game.alvey.rect.x += game.alvey.speed
            game.alvey.direction = 1
        
    
        

    # Handle gravity

    if game.test_map.collides_player():
        game.alvey.jumping = False
        game.alvey.velocity = 0
    else:
        #print "Velocity: ", game.alvey.velocity
        if game.alvey.velocity > 0:
            game.alvey.velocity += game.alvey.gravity
            if not pygame.K_RIGHT in keys and not pygame.K_LEFT in keys:
                game.alvey.velocity += game.alvey.gravity
        else:
            game.alvey.velocity += game.alvey.gravity

        if game.alvey.velocity > 3:
            for i in range(int(game.alvey.velocity)):
                #print "y: ", game.alvey.rect.y
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