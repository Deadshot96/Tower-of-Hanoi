import pygame
from settings import *


class gui:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = fps
        self.win = None
        self.clock = None
        self.font = None


    def gui_init(self):

        pygame.init()
        pygame.font.quit()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tower of Hanoi")

        



    def run(self):
        pass

if __name__ == "__main__":
    X = gui()
    X.run()