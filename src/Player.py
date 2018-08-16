import os
import pygame
from enum import Enum
import time


class PlayerState(Enum):
    IDLE = 1
    MOVE = 2
    JUMP = 3


class Player:

    def __init__(self):
        self.sprites = dict()

        self.sprites[PlayerState.IDLE] = []
        for i in range(4):
            self.sprites[PlayerState.IDLE].append(pygame.image.load(
                os.path.join('img', 'player', 'sprites', 'adventurer-idle-2-0' + str(i) + '.png')))

        self.sprites[PlayerState.MOVE] = []
        for i in range(6):
            self.sprites[PlayerState.MOVE].append(pygame.image.load(
                os.path.join('img', 'player', 'sprites', 'adventurer-run-0' + str(i) + '.png')))

        self.sprites[PlayerState.JUMP] = []
        for i in range(3):
            self.sprites[PlayerState.JUMP].append(pygame.image.load(
                os.path.join('img', 'player', 'sprites', 'adventurer-crnr-jmp-0' + str(i) + '.png')))

        self.sprite_index = 0
        self.last_sprite_index_change = 0
        self.state = PlayerState.JUMP

    def getSprite(self):
        sprite = self.sprites[self.state][self.sprite_index]

        now = time.time()
        if now - self.last_sprite_index_change >= 0.25:
            self.last_sprite_index_change = now
            self.sprite_index += 1
            if self.sprite_index >= len(self.sprites[self.state]):
                self.sprite_index = 0

        return sprite
