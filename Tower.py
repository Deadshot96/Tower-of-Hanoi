import pygame
from pygame import Surface
from settings import *
from colors import *
from Disk import Disk

class Tower:

    def __init__(self, x: int, id: int):

        self.x = x
        self.y = TOWER_Y
        self.width = TOWER_WIDTH
        self.height = TOWER_HEIGHT
        self.color = CHOCOLATE
        self.id = id
        self.disks = list()
        self.baseWidth = TOWER_WIDTH
        self.baseHeight = TOWER_HEIGHT

    def draw(self, win: Surface):
        x = self.x - self.width // 2
        y = self.y - self.height
        rect = x, y, self.width, self.height
        
        pygame.draw.rect(win, self.color, rect)

        cX, cY = self.x, y
        radius = self.width // 2

        pygame.draw.circle(win, self.color, (cX, cY), radius)

    def get_stack_height(self):
        return len(self.disks) * DISK_HEIGHT + BASE_Y

    def is_proper_disk(self, disk: Disk):
        return disk.get_index() < self.get_min_disk_index()

    def add_disk(self, disk: Disk) -> bool:
        if self.get_min_disk_index() < disk.get_index():
            self.disks.append(disk)
            return True
        
        return False

    def get_min_disk_index(self):
        return min(self.disks, key=lambda d: d.get_index())

    def get_x(self) -> int:
        return self.x

    def sort_disks(self):
        self.disks.sort(key=lambda d: d.get_index())
