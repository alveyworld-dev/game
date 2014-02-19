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
        
    if (len(keys)==0 or not pygame.K_SPACE in keys) and game.alvey.speed >= game.alvey.minspeed:
            game.alvey.speed -= (game.alvey.speed_power/100. * game.alvey.speed)*.7
            print (game.alvey.speed_power/100. * game.alvey.speed)*.7, game.alvey.speed
        
    for key in keys:
        # Perform jump
        if key == pygame.K_SPACE and game.alvey.jumping == False:
            if not game.alvey.is_down:
                game.alvey.change_costume(game.standing)
            game.alvey.jumping = True
            game.alvey.velocity -= game.alvey.jump_power
            game.alvey.rect.y += game.alvey.velocity
        
        if key == pygame.K_DOWN and game.alvey.jumping == True:
            if not game.test_map.collides_player():
                game.alvey.velocity += .5
            game.alvey.rect.y += game.alvey.velocity
        elif key == pygame.K_DOWN:
            game.alvey.change_costume(game.crouching)
            if not game.test_map.collides_player():
                game.alvey.velocity += .5
            game.alvey.rect.y += game.alvey.velocity

        # Move left/right/down
        if key == pygame.K_LEFT:
            
            if not game.alvey.is_down:
                game.alvey.change_costume(game.standingl)
            if not game.alvey.jumping:
                game.alvey.speed += game.alvey.speed_power/100. * (game.alvey.speed + 1)
            else:
                game.alvey.speed = max(game.alvey.maxspeed/2, game.alvey.speed)
            game.alvey.rect.x -= min(game.alvey.speed,game.alvey.maxspeed)
            game.alvey.direction = -1
        elif key == pygame.K_RIGHT:
            
            if not game.alvey.is_down:
                game.alvey.change_costume(game.standing)
            if not game.alvey.jumping:
                game.alvey.speed += game.alvey.speed_power/100. * (game.alvey.speed + 1)
            else:
                game.alvey.speed = max(game.alvey.maxspeed/2, game.alvey.speed)
            game.alvey.rect.x += min(game.alvey.speed,game.alvey.maxspeed)
            game.alvey.direction = 1
        
    
        #Degrad speed 
        

    # Handle gravity

    if game.test_map.collides_player():
        game.alvey.jumping = False
        game.alvey.velocity = 0
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
