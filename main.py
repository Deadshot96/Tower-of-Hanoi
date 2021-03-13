import pygame
from settings import *
from colors import *
from Button import Button


class gui:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.gui_width = GUI_WIDTH
        self.gui_height = GUI_HEIGHT
        self.x_off = X_OFF
        self.y_off = Y_OFF
        self.fps = FPS
        self.win = None
        self.guiWin = None
        self.clock = None
        self.titlefont = None
        self.button_p = None
        self.button_up = None


    def gui_init(self):

        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tower of Hanoi")

        gui_rect = self.x_off, self.y_off, self.gui_width, self.gui_height
        self.guiWin = self.win.subsurface(gui_rect)

        self.win.fill(MID_BLACK)
        self.guiWin.fill(STEEL_BLUE)

        self.clock = pygame.time.Clock()

        self.titlefont = pygame.font.SysFont(TITLE_FONT, TITLE_FONT_SIZE)

        self.title = self.titlefont.render("3 Towers of Hanoi", 1, GOLD)
        w, h = self.title.get_size()
        pos = (self.width - w) // 2, (self.y_off - h) // 2
        self.win.blit(self.title, pos)

        self.button_p = pygame.transform.scale(pygame.image.load(BUTTON_PRESSED), (240, 80))
        self.button_up = pygame.transform.scale(pygame.image.load(BUTTON_UNPRESS), (240, 80))


        self.restartButton = Button(300 - self.x_off, 85 - self.y_off, 'Restart', self.button_p, self.button_up)

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def draw(self):
        self.guiWin.fill(STEEL_BLUE)
        self.restartButton.draw(self.guiWin)
        
        pygame.display.update()

    def run(self):

        self.gui_init()
        run = True
        while run:
            
            self.clock.tick(self.fps)
            self.draw()

            pos = pygame.mouse.get_pos()
            x, y = pos

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(x, y, self.win.get_at(pos), sep='\t')
                
                    if self.restartButton.in_button(pos):
                        self.restartButton.press()

                if event.type == pygame.MOUSEBUTTONUP:

                    if self.restartButton.in_button(pos) and self.restartButton.is_pressed():
                        self.restartButton.unpress()

            if self.restartButton.in_button(pos):
                self.restartButton.hover()
            else:
                self.restartButton.unhover()

            pygame.display.update()

        self.quit()


if __name__ == "__main__":
    X = gui()
    X.run()