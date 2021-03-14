import pygame
from pygame import Surface
from settings import *
from colors import *
from Tower import Tower

class Disk:

    def __init__(self, index: int, tower: Tower):
        self.index = index
        self.tower = tower
        self.width = index * 30
        self.height = DISK_HEIGHT
        self.color = DISKS_COLORS [index]
        self.x = 0
        self.y = 0

        self.set_positions()

    def set_positions(self):
        y = self.tower.get_stack_height()
        x = self.tower.get_x()

        self.x = x - self.width // 2
        self.y = y - self.height

    def get_top_left(self):
        pass

    def get_tower(self):
        return self.tower

    def set_tower(self, tower: Tower):
        self.tower = tower
        self.set_positions()

    def draw(self, win: Surface):
        pass

    def get_index(self) -> int:
        return self.index