import os
import pygame
from enum import Enum
import time
from vector import Vector
from threading import Timer


class PlayerState(Enum):
    IDLE = 1
    MOVE = 2
    JUMP = 3
    FALL = 4


class Player:

    def __init__(self):
        self.sprites = dict()

        self.sprites[PlayerState.IDLE] = []
        for i in range(4):
            self.sprites[PlayerState.IDLE].append(pygame.image.load(
                os.path.join('img', 'player', 'sprites', 'adventurer-idle-2-0' + str(i) + '.png')).convert())

        self.sprites[PlayerState.MOVE] = []
        for i in range(6):
            self.sprites[PlayerState.MOVE].append(pygame.image.load(
                os.path.join('img', 'player', 'sprites', 'adventurer-run-0' + str(i) + '.png')).convert())

        self.sprites[PlayerState.JUMP] = []
        for i in range(4):
            self.sprites[PlayerState.JUMP].append(pygame.image.load(
                os.path.join('img', 'player', 'sprites', 'adventurer-jump-0' + str(i) + '.png')).convert())

        self.sprites[PlayerState.FALL] = []
        for i in range(2):
            self.sprites[PlayerState.FALL].append(pygame.image.load(
                os.path.join('img', 'player', 'sprites', 'adventurer-fall-0' + str(i) + '.png')).convert())

        self.sprite_index = 0
        self.last_sprite_index_change = 0
        self.state = PlayerState.IDLE

        self.pos = Vector.New()
        self.vel = Vector.New()
        self.acc = Vector.New()

    def SetState(self, state: PlayerState):
        if self.state != state:
            self.state = state
            self.sprite_index = 0
            self.last_sprite_index_change = 0

    def GetSurface(self):
        sprite = self.sprites[self.state][self.sprite_index]

        now = time.time()
        if now - self.last_sprite_index_change >= 0.25:
            self.last_sprite_index_change = now
            self.sprite_index += 1
            if self.sprite_index >= len(self.sprites[self.state]):
                self.sprite_index = 0

        if self.vel.x < 0:
            sprite = pygame.transform.flip(sprite, True, False)

        return sprite

    def GetRect(self):
        rect = pygame.Rect(self.pos.x, self.pos.y, 50, 100)
        return rect

    def Update(self):

        if self.state == PlayerState.FALL:
            self.acc.y = 0.01
        else:
            self.acc.y = 0

        self.vel.x += self.acc.x
        self.vel.y += self.acc.y

        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def DoJump(self):
        self.vel.y = -2

    def Jump(self):
        self.SetState(PlayerState.JUMP)
        Timer(0.2, self.DoJump, ()).start()
