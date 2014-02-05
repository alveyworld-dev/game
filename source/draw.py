import pygame
import graphics
import game
import math
from sprite import Sprite

# Seconds in an in-game day / night cycle
daySeconds = 10 # The ten seconds situation is merely for testing, we can make it longer later.

# Maximum R, G, B values for sky color
_R=164.0
_G=240.0
_B=238.0

# Minimum R, G, B value for sky color
_M=13.0

# Maximum darkness for ambient; 0-255, 255 is darkest
maxDark=186.0

# Minimum darkness for ambient
minDark=0.0

colorList=[
    (_R+_M)/2,
    (_G+_M)/2,
    (_B+_M)/2,
    False, #True if the colors are darkening
    (maxDark+minDark)/2
]
def rangec(num,minimum,maximum):
    n=num
    if n>=maximum:
        n=maximum
    elif n<=minimum:
        n=minimum
    return n

def solveColors(fr,delayed):
    notReallyGlobalVariableHi = (daySeconds)/((1.0)*(delayed/fr))/(fr/1000)
    if not colorList[3]:
        colorList[0]+=(_R-_M)/notReallyGlobalVariableHi
        colorList[1]+=(_G-_M)/notReallyGlobalVariableHi
        colorList[2]+=(_B-_M)/notReallyGlobalVariableHi
        colorList[4]-=(maxDark-minDark)/notReallyGlobalVariableHi
    else:
        colorList[0]-=(_R-_M)/notReallyGlobalVariableHi
        colorList[1]-=(_G-_M)/notReallyGlobalVariableHi
        colorList[2]-=(_B-_M)/notReallyGlobalVariableHi
        colorList[4]+=(maxDark-minDark)/notReallyGlobalVariableHi

    if (colorList[0]>=_R and colorList[1]>=_G and colorList[2]>=_B and not colorList[3] and colorList[4]<=minDark) or (colorList[0]<=_M and colorList[1]<=_M and colorList[2]<=_M and colorList[3] and colorList[4]>=maxDark):
        if colorList[3]:
            colorList[3]=False
        else:
            colorList[3]=True

    colorList[0]=rangec(colorList[0],_M,_R)
    colorList[1]=rangec(colorList[1],_M,_G)
    colorList[2]=rangec(colorList[2],_M,_B)
    colorList[4]=rangec(colorList[4],minDark,maxDark)

    return (
        int((math.floor(colorList[0]), math.ceil(colorList[0]))[colorList[0]<=_R/2]),
        int((math.floor(colorList[1]), math.ceil(colorList[1]))[colorList[1]<=_G/2]),
        int((math.floor(colorList[2]), math.ceil(colorList[2]))[colorList[2]<=_B/2])
    )

def draw(fr,delayed):
    """
    Drawing logic
    """

    # Draw background
    color_overlay = solveColors(float(fr),float(delayed))
    game.screen.fill(color_overlay)
    
    # Drawing a sprite called my_sprite
    # my_sprite.draw()

    # Draw some text
    # graphics.draw_text("Hello World", (255, 255, 255), (50, 50))

    # Draw the stars
    # stars=Sprite(" ", (0,0))

    # Draw the sun
    # Sun=Sprite(" ", (0,0))

    game.world.draw()

    if game.alvey.direction == 1:
        game.alvey.draw()
    else:
        game.screen.blit(game.alvey.left_sprite, game.alvey.left_sprite_rect)
    
    overlay = pygame.Surface(game.window_size).convert()
    overlay.set_alpha(colorList[4])
    overlay.fill((0,0,0))          
    game.screen.blit(overlay, (0,0))

    return
