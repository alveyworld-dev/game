import pygame
import graphics
import game
import random
from sprite import Sprite
for i in range(100):
    random.seed(random.randint(1,1000000000))

daySeconds=200

_R=164
_G=240
_B=238
_M=13

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
        colorList[0]+=int((_R-_M)/daySeconds)
        colorList[1]+=int((_G-_M)/daySeconds)
        colorList[2]+=int((_B-_M)/daySeconds)
    else:
        colorList[0]-=int((_R-_M)/daySeconds)
        colorList[1]-=int((_G-_M)/daySeconds)
        colorList[2]-=int((_B-_M)/daySeconds)

    if (colorList[0]>=_R and colorList[1]>=_G and colorList[2]>=_B and not colorList[3]) or (colorList[0]<=_M and colorList[1]<=_M and colorList[2]<=_M and colorList[3]):
        colorList[3] = not colorList[3]

    return (rangec(colorList[0],_M,255),rangec(colorList[1],_M,255),rangec(colorList[2],_M,255))

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