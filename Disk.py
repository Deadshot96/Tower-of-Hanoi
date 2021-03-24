import pygame
from pygame import Surface
from settings import *
from colors import *
from Tower import Tower
from typing import Tuple

class Disk:

    def __init__(self, index: int, tower: Tower):
        self.index = index
        self.tower = tower
        self.width = index * DISK_WIDTH_MULTIPLIER
        self.height = DISK_HEIGHT
        self.color = DISKS_COLORS [index]
        self.x = 0
        self.y = 0
        self.diskRect = None

        self.disk_init()

    def disk_init(self):
        self.y = self.tower.get_stack_height()
        self.x = self.tower.get_x()

        self.set_rect()
        
    def get_top_left(self):
        pass

    def get_tower(self):
        return self.tower

    def set_rect(self):
        rect = self.x - self.width // 2, self.y - self.height, self.width, self.height
        self.diskRect = pygame.Rect(rect)

    def set_tower(self, tower: Tower):
        self.tower = tower
        self.disk_init()

    def draw(self, win: Surface):

        radius = self.height // 2
        rect = self.x - self.width // 2 + radius, self.y - self.height, self.width -  2 * radius, self.height
        pygame.draw.rect(win, self.color, rect)

        cX1, cX2 = self.x - self.width // 2 + radius, self.x + self.width // 2 - radius
        cY1 = cY2 = self.y - self.height // 2

        pygame.draw.circle(win, self.color, (cX1, cY1), radius)
        pygame.draw.circle(win, self.color, (cX2, cY2), radius)
        # pygame.draw.rect(win, self.color, self.diskRect, 2)

    def get_index(self) -> int:
        return self.index

    def in_disk(self, pos: Tuple) -> bool:
        print("Disk Index: ", self.get_index())
        return self.diskRect.collidepoint(pos)

    def get_pos(self) -> Tuple[int]:
        return self.x, self.y

    def set_positions(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        