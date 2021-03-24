import pygame
from pygame import Surface
from settings import *
from colors import *

class Tower:

    def __init__(self, x: int, index: int):

        self.x = x
        self.y = TOWER_Y
        self.width = TOWER_WIDTH
        self.height = TOWER_HEIGHT
        self.color = CHOCOLATE
        self.index = index
        self.disks = list()
        self.baseWidth = TOWER_WIDTH
        self.baseHeight = TOWER_HEIGHT

        rect = self.x - DELTA * 3 // 8, \
             self.y - int(self.height * 1.5), \
                  DELTA * 3 // 4, \
                      int(self.height * 2)
        self.towerRect = pygame.Rect(rect)

    def draw(self, win: Surface):
        x = self.x - self.width // 2
        y = self.y - self.height
        rect = x, y, self.width, self.height
        
        pygame.draw.rect(win, self.color, rect)

        cX, cY = self.x, y
        radius = self.width // 2

        pygame.draw.circle(win, self.color, (cX, cY), radius)
        # pygame.draw.rect(win, self.color, self.towerRect, 2)

    def get_stack_height(self):
        return BASE_Y - len(self.disks) * DISK_HEIGHT

    def is_proper_disk(self, disk):
        return disk.get_index() < self.get_min_disk_index()

    def add_disk(self, disk) -> bool:
        if self.get_min_disk_index() > disk.get_index():
            disk.set_tower(self)
            self.disks.append(disk)
            return True
        
        return False

    def remove_disk(self, disk) -> bool:
        if disk in self.disks:
            self.disks.remove(disk)
            return True
        return False

    def get_min_disk_index(self):
        if len(self.disks) == 0:
            return 20
        return min(self.disks, key=lambda d: d.get_index()).get_index()

    def get_x(self) -> int:
        return self.x

    def sort_disks(self):
        self.disks.sort(key=lambda d: d.get_index(), reverse=True)

    def clear_tower(self):
        self.disks.clear()

    def get_top_disk(self):
        if len(self.disks) == 0:
            return None
        self.sort_disks()
        return self.disks[-1]

    def in_tower(self, x: int, y: int) -> bool:
        return self.towerRect.collidepoint(x, y)

    def get_index(self) -> int:
        return self.index