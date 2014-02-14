import pygame
from pygame.locals import *
import copy
import time
import anim

Kleft   = K_LEFT
Kright  = K_RIGHT
Kjump   = K_SPACE
Kcrouch = K_DOWN

NORTH   = 'north'
SOUTH   = 'south'
EAST    = 'east'
WEST    = 'west'
AXISX   = 'x'
AXISY   = 'y'


class Entity(object):
    color = (14, 14, 14)

    maxSpeed = 5
    accel_amt = 1
    airaccel_amt = .3
    deaccel_amt = 3

    fallAccel = 3.75
    jumpMod = 1
    jumpAccel = 25
    maxFallSpeed = 15

    def __init__(self, level, rectTuple, image=None, owner = None):
        self.rect = pygame.Rect((rectTuple[0] * level.blockWidth),
                                (rectTuple[1] * level.blockHeight),
                                rectTuple[2], rectTuple[3])
        self.normalHeight = self.rect.height
        self.cameraRect = copy.copy(self.rect)
        self.animation_speed = 0.030
        self.game = owner

        if type(image) is pygame.Surface:
            self.image = image
        elif type(image) is str:
            try:
                spritesheet = pygame.image.load(image)
            except pygame.error:
                self.image = pygame.Surface(
                    (self.rect.width, self.rect.height))
                self.image.fill(self.color)
        elif image == None:
            self.image = pygame.Surface((self.rect.width, self.rect.height))
            self.image.fill(self.color)

        self.accelX = 0
        self.speedX = 0
        self.speedY = 0
        self.jumping = False
        self.onBlock = False

    def update(self):
        pass

    def load_frames(self, filename):

        # Set up spritesheet
        spritesheet = pygame.image.load(filename)
        spritesheetWidth, spritesheetHeight = spritesheet.get_size()

        # Make individual tiles
        frames = []
        for frame in range(spritesheetWidth / self.rect.width):
            newFrameRect = pygame.Rect(frame * self.rect.width,
                                       0,
                                       self.rect.width,
                                       spritesheetHeight)
            frames.append(spritesheet.subsurface(newFrameRect))

        return frames

    def updateAnim(self):
        if time.time() - self.lastFrame >= 0.2:
            self.lastFrame = time.time()
            self.currentFrame += 1
            if self.currentFrame > len(self.frames) - 1:
                self.currentFrame = 0
        self.image = self.frames[self.currentFrame]

    def get_accel(self, keys, jumping):
        if not jumping:
            return (keys[Kright] - keys[Kleft]) * self.accel_amt
        elif jumping:
            return (keys[Kright] - keys[Kleft]) * self.airaccel_amt

    def accelerate(self, accel, speed):
        if accel != 0:
            if ((speed < 0) and (accel > 0)) or\
               ((speed > 0) and (accel < 0)):
                speed = accel
            else:
                speed += accel

        if speed > self.maxSpeed:
            speed = self.maxSpeed
        if speed < -self.maxSpeed:
            speed = -self.maxSpeed

        if accel == 0:
            if speed > 0:
                speed -= self.deaccel_amt
                if speed < 0:
                    speed = 0
            if speed < 0:
                speed += self.deaccel_amt
                if speed > 0:
                    speed = 0

        return speed

    def jump(self, speed, onBlock):
        if onBlock:
            speed -= self.jumpAccel

        # Gravity is decreased while jumping so the player can control
        # the height of his jump.
        speed += self.fallAccel - self.jumpMod

        # Simulate terminal velocity
        if speed > self.maxFallSpeed:
            speed = self.maxFallSpeed

        return speed

    def fall(self, speed):
        speed += self.fallAccel

        # Simulate terminal velocity
        if speed > self.maxFallSpeed:
            speed = self.maxFallSpeed

        return speed

    def get_shortest_distance(self, rect, speed, axis, level):
        # Check which way the player is moving
        dir = self.check_dir(speed, axis)
        if dir == WEST:
            front = rect.left
        elif dir == EAST:
            front = rect.right
        elif dir == NORTH:
            front = rect.top
        elif dir == SOUTH:
            front = rect.bottom

        # Calculate the minimum distance
        linesToCheck = self.check_lines(rect, axis, level)
        if dir:
            minDistance = self.calculate_distance(
                front, linesToCheck, dir, level)
        else:
            minDistance = 0

        # If the minumum distance is shorter than the player's delta,
        # move the player by that distance instead.
        if self.check_collision(speed, minDistance):
            return minDistance
        else:
            return speed

    def check_dir(self, speed, axis):
        if axis == AXISX:
            if speed < 0:
                return WEST
            elif speed > 0:
                return EAST

        elif axis == AXISY:
            if speed < 0:
                return NORTH
            elif speed > 0:
                return SOUTH

    def check_lines(self, rect, axis, level):
        linesToCheck = []
        if axis == AXISX:
            for y in range(level.levelHeight):
                if rect.colliderect((0,
                                     y * level.blockHeight,
                                     level.rightEdge,
                                     level.blockHeight)):
                    linesToCheck.append(y)

        elif axis == AXISY:
            for x in range(level.levelWidth):
                if rect.colliderect((x * level.blockWidth,
                                     0,
                                     level.blockWidth,
                                     level.bottomEdge)):
                    linesToCheck.append(x)

        return linesToCheck

    def calculate_distance(self, coord, lines, dir, level):
        distances = []
        if dir == WEST or dir == EAST:
            playerTile = self.convert_pixel_to_level(coord, 0, level)[0]
        elif dir == NORTH or dir == SOUTH:
            playerTile = self.convert_pixel_to_level(0, coord, level)[1]

        # Which blocks are scanned are dependent on which direction the player
        # is moving in.
        if dir == WEST:
            for line in lines:
                nearestBlock = self.scan_line(
                    line, playerTile, -1, -1, AXISX, level)
                distances.append(
                    abs(nearestBlock * level.blockWidth + level.blockWidth - coord))

        elif dir == EAST:
            for line in lines:
                nearestBlock = self.scan_line(
                    line, playerTile, level.levelWidth, 1, AXISX, level)
                distances.append(abs(nearestBlock * level.blockWidth - coord))

        elif dir == NORTH:
            for line in lines:
                nearestBlock = self.scan_line(
                    line, playerTile, -1, -1, AXISY, level)
                distances.append(
                    abs(nearestBlock * level.blockHeight + level.blockHeight - coord))

        elif dir == SOUTH:
            for line in lines:
                nearestBlock = self.scan_line(
                    line, playerTile, level.levelHeight, 1, AXISY, level)
                distances.append(abs(nearestBlock * level.blockHeight - coord))

        # The function should return the shortest or longest distance
        # depending on which direction the player was moving in.
        desiredValue = min(distances)
        if dir == WEST or dir == NORTH:
            return -desiredValue
        elif dir == EAST or dir == SOUTH:
            return desiredValue

    def convert_pixel_to_level(self, x, y, level):
        for levelX in range(level.levelWidth):
            for levelY in range(level.levelHeight):
                tempRect = pygame.Rect(levelX * level.blockWidth,
                                       levelY * level.blockHeight,
                                       level.blockWidth, level.blockHeight)
                if tempRect.collidepoint(x, y):
                    return (levelX, levelY)

    def scan_line(self, line, start, end, dir, axis, level):
        if axis == AXISX:
            for tile in range(start, end, dir):
                if level.collisionLayer[line][tile] == level.block:
                    return tile
        elif axis == AXISY:
            for tile in range(start, end, dir):
                if level.collisionLayer[tile][line] == level.block:
                    return tile
        return start

    def check_collision(self, speed, minDistance):
        # If minumum X distance is shorter than the player's deltaX,
        # move the player by that distance instead.
        if (speed < 0 and minDistance > speed) or\
           (speed > 0 and minDistance < speed):
            return True

        return False

    def check_on_block(self, rect, level):
        # is there a better way than checking every block in the level?
        for x in range(level.levelWidth):
            for y in range(level.levelHeight):
                if level.collisionLayer[y][x] == level.blank:
                    continue
                elif level.collisionLayer[y][x] == level.block:
                    tempCheckRect = copy.copy(rect)
                    tempLevelRect = pygame.Rect(x * level.blockWidth,
                                                y * level.blockHeight,
                                                level.blockWidth, level.blockHeight)
                    tempCheckRect.bottom += 1
                    if tempLevelRect.colliderect(tempCheckRect):
                        return True
                elif level.collisionLayer[y][x] == level.tiles['x'][0]:
                    game.player.health = 0
        return False

    def check_head_collision(self, level):
        '''
        Checks the current player's original bounding rectangle to see if standing up
        after crouching would cause a collision. If this returns True, the player should not be
        allowed to stand up
        '''
        if not self.crouching:
            return False
        x, y = self.get_coords(level)
        # we need to see check the three blocks above the players head
        levelBlocks = (level.collisionLayer[y - 1][x - 1],
                       level.collisionLayer[y - 1][x],
                       level.collisionLayer[y - 1][x + 1],)

        if all(block == level.blank for block in levelBlocks):
            # all of the blocks above me are blank so there is no chance of
            # collision
            return False
        else:  # if level.collisionLayer[y-1][x] == level.block:
            standingRect = copy.deepcopy(self.rect)
            standingRect.top += (self.normalHeight - self.crouchHeight)
            # make bounding rectangles for each of the three blocks above
            # player
            levelRects = [pygame.Rect(i * level.blockWidth,
                                      y * level.blockHeight,
                                      level.blockWidth,
                                      level.blockHeight,)
                          for i in range(x - 1, x + 2)]

            return any(levelBlocks[a] == level.block and
                       levelRects[a].colliderect(standingRect)
                       for a in range(len(levelBlocks)))

    def get_coords(self, level):
        return self.convert_pixel_to_level(self.rect.centerx, self.rect.centery, level)