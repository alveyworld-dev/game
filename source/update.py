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

    moved=0
    if pygame.K_SPACE not in keys and pygame.K_RIGHT not in keys and pygame.K_LEFT not in keys and pygame.K_DOWN not in keys and not game.alvey.jumping:
        if game.alvey.direction == -1:
            game.alvey.change_costume(game.standingl)
        else:
            game.alvey.change_costume(game.standing)
    for key in keys:
        # Perform jump
        if key == pygame.K_SPACE and game.alvey.jumping == False:
            if game.alvey.direction == -1:
                game.alvey.change_costume(game.jumpingl)
            else:
                game.alvey.change_costume(game.jumping)

            
            game.alvey.jumping = True

            game.alvey.jump.play()
            if pygame.K_b in keys and (pygame.K_LEFT in keys or pygame.K_RIGHT in keys):
                game.alvey.jump_power = game.alvey.jump_high
            else:
                game.alvey.jump_power = game.alvey.jump_low
           
            game.alvey.velocity -= game.alvey.jump_power
            game.alvey.rect.y += game.alvey.velocity
        
        if key == pygame.K_DOWN and game.alvey.jumping == True:
            #if not game.test_map.collides_player():
            #    game.alvey.velocity += game.alvey.gravity
            #game.alvey.rect.y += game.alvey.velocity
            if game.alvey.direction == -1:
                game.alvey.change_costume(game.crouchingl)
            else:
                game.alvey.change_costume(game.crouching)
        elif key == pygame.K_DOWN:
            if game.alvey.direction == -1:
                game.alvey.change_costume(game.crouchingl)
            else:
                game.alvey.change_costume(game.crouching)
            if not game.test_map.collides_player():
                game.alvey.velocity += game.alvey.gravity
            game.alvey.rect.y += game.alvey.velocity

        # Move left/right/down
        if key == pygame.K_LEFT:
            if not game.alvey.is_down and not game.alvey.jumping:
                costumes = len(game.walkingl)
                game.alvey.change_costume(game.walkingl[game.alvey.toggle%costumes])

            if not game.alvey.is_down and game.alvey.jumping:
                game.alvey.change_costume(game.jumpingl)

            if pygame.K_b in keys:
                game.alvey.speed = game.alvey.speed_fast
            else:
                game.alvey.speed = game.alvey.speed_slow
            
            
            #only shift screen if close to the edge
            if game.alvey.rect.x < 300:
                moved-=game.alvey.speed
                #game.alvey.rect.x -= game.alvey.speed
            else:
                game.alvey.rect.x -= game.alvey.speed
                
            game.alvey.direction = -1
        elif key == pygame.K_RIGHT:
            
            if not game.alvey.is_down and not game.alvey.jumping:
                costumes = len(game.walking)
                game.alvey.change_costume(game.walking[game.alvey.toggle%costumes])

            if not game.alvey.is_down and game.alvey.jumping:
                game.alvey.change_costume(game.jumping)

            if pygame.K_b in keys:
                game.alvey.speed = game.alvey.speed_fast
            else:
                game.alvey.speed = game.alvey.speed_slow
            
            #only shift screen if close to the edge
            if game.alvey.rect.x > game.window_size[0]-300:
                moved+=game.alvey.speed
                #game.alvey.rect.x += game.alvey.speed
            else:
                game.alvey.rect.x += game.alvey.speed
            game.alvey.direction = 1
    #game.alvey.rect.x=100-game.alvey.rect.width
    
    # Handle gravity

    if game.test_map.collides_player():
        game.alvey.jumping = False
        game.alvey.velocity = 0
        #moved=0
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
    #print "Moved: ", moved
    game.test_map.update(moved)

    if game.alvey.rect.right <= 0 and game.alvey.dead == False:
        print("boom. dead")
        game.alvey.dead = True

    if game.test_map.scrolling:
        if game.alvey.rect.right >= 0:
            game.alvey.rect.x -= 1

    return