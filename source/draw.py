import pygame
import graphics
import game
import math
from sprite import Sprite

# Seconds in an in-game day / night cycle
# The ten seconds situation is merely for testing, we can make it longer later.
daySeconds = 60

# Maximum R, G, B values for sky color
_R = 164.0
_G = 240.0
_B = 238.0

# Minimum R, G, B value for sky color
_M = 13.0

# Maximum darkness for ambient; 0-255, 255 is darkest
maxDark = 186.0

# Minimum darkness for ambient
minDark = 0.0

colorList = [
    (_R + _M) / 2,
    (_G + _M) / 2,
    (_B + _M) / 2,
    False,  # True if the colors are darkening
    (maxDark + minDark) / 2,
    127.5,
    127.5,
    0,
    360,
]


def rangec(num, minimum, maximum):
    n = num
    if n >= maximum:
        n = maximum
    elif n <= minimum:
        n = minimum
    return n


def solveColors(fr, delayed):
    notReallyGlobalVariableHi = (
        daySeconds) / ((1.0) * (delayed / fr)) / (fr / 1000)
    if not colorList[3]:
        colorList[0] += (_R - _M) / notReallyGlobalVariableHi  # Sky Red
        colorList[1] += (_G - _M) / notReallyGlobalVariableHi  # Sky Green
        colorList[2] += (_B - _M) / notReallyGlobalVariableHi  # Sky Blue
        # World Ambient Alpha
        colorList[4] -= (maxDark - minDark) / notReallyGlobalVariableHi
        colorList[5] -= 510 / notReallyGlobalVariableHi  # Stars Alpha
        colorList[6] -= 510 / notReallyGlobalVariableHi  # Sun Alpha
        colorList[7] += 720 / notReallyGlobalVariableHi  # Sun Angle
        colorList[8] += 720 / notReallyGlobalVariableHi  # Stars Angle
    else:
        colorList[0] -= (_R - _M) / notReallyGlobalVariableHi  # Sky Red
        colorList[1] -= (_G - _M) / notReallyGlobalVariableHi  # Sky Green
        colorList[2] -= (_B - _M) / notReallyGlobalVariableHi  # Sky Blue
        # World Ambient Alpha
        colorList[4] += (maxDark - minDark) / notReallyGlobalVariableHi
        colorList[5] += 510 / notReallyGlobalVariableHi  # Stars Alpha
        colorList[6] += 510 / notReallyGlobalVariableHi  # Sun Alpha
        colorList[7] += 720 / notReallyGlobalVariableHi  # Sun Angle
        colorList[8] += 720 / notReallyGlobalVariableHi  # Stars Angle

    if (colorList[0] >= _R and colorList[1] >= _G and colorList[2] >= _B and not colorList[3] and colorList[4] <= minDark) or (colorList[0] <= _M and colorList[1] <= _M and colorList[2] <= _M and colorList[3] and colorList[4] >= maxDark):
        if colorList[3]:
            colorList[3] = False
        else:
            colorList[3] = True

    colorList[0] = rangec(colorList[0], _M, _R)
    colorList[1] = rangec(colorList[1], _M, _G)
    colorList[2] = rangec(colorList[2], _M, _B)
    colorList[4] = rangec(colorList[4], minDark, maxDark)
    colorList[5] = rangec(colorList[5], 0, 255)
    colorList[6] = rangec(colorList[5], 0, 255)
    colorList[7] = colorList[7] % 720
    colorList[8] = colorList[8] % 720

    return (
        int((math.floor(colorList[0]), math.ceil(colorList[0]))[
            colorList[0] <= _R / 2]),
        int((math.floor(colorList[1]), math.ceil(colorList[1]))[
            colorList[1] <= _G / 2]),
        int((math.floor(colorList[2]), math.ceil(colorList[2]))[
            colorList[2] <= _B / 2])
    )


def starsUpdate():
    for i in game.starsList:
        x = math.sin(math.radians((i[1] + colorList[8]) / 2)) * i[2] * 2 + 640
        y = math.cos(math.radians((i[1] + colorList[8]) / 2)) * i[2] + 360
        i[0].image.set_alpha(colorList[5])
        i[0].rect.x = x
        i[0].rect.y = y
        i[0].draw()


def draw(fr, delayed):
    """
    Drawing logic
    """
    # Draw background
    color_overlay = solveColors(float(fr), float(delayed))
    game.screen.fill(color_overlay)

    # Drawing a sprite called my_sprite
    # my_sprite.draw()

    # Draw some text
    # graphics.draw_text("Hello World", (255, 255, 255), (50, 50))

    starsUpdate()

    # Draw the sun
    # game.sun.image.set_alpha(int(colorList[6]))  # Not used currently
    sunx = math.sin(math.radians((colorList[7]) / 2))
    suny = math.cos(math.radians((colorList[7]) / 2))
    game.sun.rect.x = sunx * 640 + 640
    game.sun.rect.y = suny * 320 + 320
    game.sun.draw()
    game.world.draw()

    if game.alvey.direction == 1:
        game.alvey.draw()
    else:
        game.screen.blit(game.alvey.left_sprite, game.alvey.left_sprite_rect)

    game.darkOverlay.set_alpha(int(colorList[4]))
    game.darkOverlay.fill((0, 0, 0))
    game.screen.blit(game.darkOverlay, (0, 0))

    return
