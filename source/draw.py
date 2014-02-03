import pygame
import graphics
import game
import random
from sprite import Sprite
for i in range(100):
    random.seed(random.randint(1,1000000000))

dayIncrement=200

_R=164 * 1000000
_G=240 * 1000000
_B=238 * 1000000
_M=13 * 1000000

colorList=[
    _R/2,
    _G/2,
    _B/2,
    False #True if the colors are darkening
]

def rangec(num,minimum,maximum):
    n=num
    if n>=maximum:
        n=maximum
    elif n<=minimum:
        n=minimum
    return n

def solveColors():
    if not colorList[3]:
        colorList[0]+=int((_R-_M)/dayIncrement)
        colorList[1]+=int((_G-_M)/dayIncrement)
        colorList[2]+=int((_B-_M)/dayIncrement)
    else:
        colorList[0]-=int((_R-_M)/dayIncrement)
        colorList[1]-=int((_G-_M)/dayIncrement)
        colorList[2]-=int((_B-_M)/dayIncrement)

    if (colorList[0]>=_R and colorList[1]>=_G and colorList[2]>=_B) or (colorList[0]<=_M and colorList[1]<=_M and colorList[2]<=_M):
        if colorList[3]:
            colorList[3]=False
        else:
            colorList[3]=True

    colorList[0]=int(rangec(colorList[0],_M,_R))
    colorList[1]=int(rangec(colorList[1],_M,_G))
    colorList[2]=int(rangec(colorList[2],_M,_B))
    return (colorList[0]/1000000,colorList[1]/1000000,colorList[2]/1000000)

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