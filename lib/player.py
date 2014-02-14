import pygame
from pygame.locals import *
import copy
import time
import anim
from entities import *

class Player(Entity):
    crouching = False
    crouchHeight = 32
    crouchMaxSpeed = 6

    def __init__(self, level, rectTuple, image=None, owner = None):
        super(Player, self).__init__(level, rectTuple, image, owner)

        try:
            self.runAnim = anim.Animation(
                "lib/player.png", self.rect.width, self.animation_speed)
            self.crouchAnim = anim.Animation(
                "lib/crouching.png", self.rect.width, 0.07)
            self.idle = anim.Animation(
                "lib\\idle.png", self.rect.width, 0)
            self.idleCrouching = anim.Animation(
                "lib/idle_crouching.png", self.rect.width, 0)
            self.hasAnim = True
        except pygame.error:
            self.hasAnim = False

        self.defMaxSpeed = self.maxSpeed
        self.health = 100

    def update(self, keys, level):
        # disable midair crouching by only allowing crouching while on the ground
        # similar to how the mario series handles this
        self.onBlock = self.check_on_block(self.rect, level)
        # Crouch the player if needed
        if keys[Kcrouch] and not self.crouching and self.onBlock:
            self.crouching = True
            self.maxSpeed = self.crouchMaxSpeed
            self.rect.height = self.crouchHeight
            self.rect.bottom += self.normalHeight - self.crouchHeight

        elif not keys[Kcrouch] and self.crouching and self.onBlock:
            # check to see if you can uncrouch here
            if not self.check_head_collision(level):
                self.crouching = False
                self.maxSpeed = self.defMaxSpeed
                self.rect.height = self.normalHeight
                self.rect.bottom -= self.normalHeight - self.crouchHeight

        # Update the player's image to the new rect size
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(self.color)

        # Calculate movement on X-axis
        self.accelX = self.get_accel(keys, self.jumping)
        self.speedX = self.accelerate(self.accelX, self.speedX)

        # Calculate movement on Y-axis
        self.jumping = keys[Kjump]
        if self.jumping:
            self.speedY = self.jump(self.speedY, self.onBlock)
            if self.onBlock:
                self.onBlock == True
        else:
            self.speedY = self.fall(self.speedY)

        # Check if player needs to be stopped at an obstacle:
        # For X-axis
        try:
            self.minXDistance = self.get_shortest_distance(
                self.rect, self.speedX, AXISX, level)
        except (TypeError, IndexError, ValueError):
            self.minXDistance = self.speedX
        if abs(self.minXDistance) < abs(self.speedX):
            self.speedX = 0

        self.rect.left += self.minXDistance

        # For Y-axis
        try:
            self.minYDistance = self.get_shortest_distance(
                self.rect, self.speedY, AXISY, level)
        except (TypeError, IndexError, ValueError):
            self.minYDistance = self.speedY
        if abs(self.minYDistance) < abs(self.speedY):
            self.speedY = 0

        self.rect.top += self.minYDistance

        # Update camera rect
        self.cameraRect.bottom = self.rect.bottom
        self.cameraRect.left = self.rect.left

        # Update frames of player if possible
        if self.hasAnim:
            if self.speedX > 0:
                if self.runAnim.reversed or self.crouchAnim.reversed:
                    self.runAnim.reverse()
                    self.crouchAnim.reverse()
                    self.idle.reverse()
                    self.idleCrouching.reverse()
                self.runAnim.update()
                self.image = self.runAnim.image
            elif self.speedX < 0:
                if not self.runAnim.reversed or not self.crouchAnim.reversed:
                    self.runAnim.reverse()
                    self.crouchAnim.reverse()
                    self.idle.reverse()
                    self.idleCrouching.reverse()

            if not self.crouching:
                self.runAnim.update()
                self.image = self.runAnim.image
            elif self.crouching:
                self.crouchAnim.update()
                self.image = self.crouchAnim.image

            if self.speedY != 0 or self.jumping:
                self.image = self.runAnim.frames[4]
            elif self.speedX == 0 and self.speedY == 0:
                if not self.crouching:
                    self.image = self.idle.frames[0]
                elif self.crouching:
                    self.image = self.idleCrouching.frames[0]
                self.runAnim.reset()
                self.crouchAnim.reset()
