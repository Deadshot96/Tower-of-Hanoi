import pygame
from settings import *
from colors import *


class gui:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS
        self.win = None
        self.clock = None
        self.font = None


    def gui_init(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tower of Hanoi")

        self.win.fill(MID_BLACK)

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(BUTTONFONT, 40)
        
        self.title = self.font.render("Tower of Hanoi", 1, GOLD)
        w, h = self.title.get_size()
        pos = (self.width - w) // 2, (self.height - h) // 2
        self.win.blit(self.title, pos)

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def run(self):

        self.gui_init()
        run = True
        while run:
            
            self.clock.tick(self.fps)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False


            pygame.display.update()

        self.quit()


if __name__ == "__main__":
    X = gui()
    X.run()