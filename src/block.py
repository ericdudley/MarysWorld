from vector import Vector
import pygame


class Block:
    def __init__(self):
        self.pos = Vector.New()
        self.size = Vector.New()
        self.size.x = 50
        self.size.y = 50

    def GetSurface(self):
        surf = pygame.Surface((self.size.x, self.size.y))
        surf.fill((255, 0, 0))
        return surf

    def GetRect(self):
        rect = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
        return rect
