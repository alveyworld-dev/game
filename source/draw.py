import pygame
import graphics
import game
import random
from sprite import Sprite
for i in range(100):
    random.seed(random.randint(1,1000000000))

colorList=[
    13, #random.randint(0,255),
    13, #random.randint(0,255),
    random.randint(0,255)
]

colorChangeList=[0,0,0]

def solveColor(listPosition):
    # Add to the color value using the current color change rate
    colorList[listPosition]+=colorChangeList[listPosition]

    # Make sure it is in range
    if colorList[listPosition]>255:
        colorList[listPosition]=255
    elif colorList[listPosition]<0:
        colorList[listPosition]=0

    # Add to the color change rate
    colorChangeList[listPosition]+=random.randint(-1,1)

    # Make sure it is in range
    if colorChangeList[listPosition]>5:
        colorChangeList[listPosition]=5
    elif colorChangeList[listPosition]<-5:
        colorChangeList[listPosition]=-5

    # return the color
    return colorList[listPosition]

def solveColors():
    #r=solveColor(0)
    r=13
    #g=solveColor(1)
    g=13
    b=solveColor(2)
    return (r,g,b)


def draw():
    """
    Drawing logic
    """

    # Draw background
    color_overlay = solveColors()
    game.screen.fill(color_overlay)
    
    # Drawing a sprite called my_sprite
    # my_sprite.draw()

    # Draw some text
    # graphics.draw_text("Hello World", (255, 255, 255), (50, 50))

    game.world.draw()

    if game.alvey.direction == 1:
        game.alvey.draw()
    else:
        game.screen.blit(game.alvey.left_sprite, game.alvey.left_sprite_rect)

    return