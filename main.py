import pygame
from settings import *
from colors import *
from Button import Button
from Tower import Tower
from Disk import Disk


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
        self.up_button = None
        self.down_button = None
        self.buttons = list()
        self.diskText = "Disks: "
        self.numDisks = DISKS if DISKS in range(3, 9) else 8
        self.moveText = "Moves: "
        self.moves = 0
        self.minMoveText = "Minimum moves: "
        self.minMoves = 2 ** self.numDisks - 1
        self.towerS = None
        self.towerT = None
        self.towerD = None
        self.disks = list()

        self.dblClickEvent = pygame.event.Event(EVENT_DBLCLICK)
        self.dblClickLimit = FPS // 3
        self.dblClickVar = 0

        self.selectedDisk = None
        self.selectedDiskDelta = None
        self.selectedDiskTower = None



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
        self.panelfont = pygame.font.SysFont(BUTTON_FONT, int(BUTTON_FONT_SIZE * 1.2))


        self.title = self.titlefont.render("3 Towers of Hanoi", 1, GOLD)
        w, h = self.title.get_size()
        pos = (self.width - w) // 2, (self.y_off - h) // 2
        self.win.blit(self.title, pos)

        # self.button_p = pygame.transform.scale(pygame.image.load(BUTTON_PRESSED).convert_alpha(), (240, 80))
        # self.button_up = pygame.transform.scale(pygame.image.load(BUTTON_UNPRESS).convert_alpha(), (240, 80))

        self.button_p = pygame.image.load(BUTTON_PRESSED).convert_alpha()
        self.button_up = pygame.image.load(BUTTON_UNPRESS).convert_alpha()

        self.up_button = Button(180 - self.x_off, BUTTONS_Y - self.y_off, "Up", self.button_p, self.button_up)
        self.down_button = Button(240 - self.x_off, BUTTONS_Y - self.y_off, "Down", self.button_p, self.button_up)

        self.up_button.set_multipliers(2, 1.5)

        # self.up_button = pygame.transform.scale(self.up_button, (DELTA_BUTTON_WIDTH, DELTA_BUTTON_HEIGHT))
        # self.down_button = pygame.transform.scale(self.down_button, (DELTA_BUTTON_WIDTH, DELTA_BUTTON_HEIGHT))

        self.restartButton = Button(730 - self.x_off, BUTTONS_Y - self.y_off, "Restart", self.button_p, self.button_up)
        self.solveButton = Button(860 - self.x_off, BUTTONS_Y - self.y_off, "Solve!", self.button_p, self.button_up)
        
        self.buttons.append(self.restartButton)
        self.buttons.append(self.solveButton)
        self.buttons.append(self.up_button)
        self.buttons.append(self.down_button)

        self.towerS = Tower(TOWER_S_X, 1)
        self.towerT = Tower(TOWER_T_X, 2)
        self.towerD = Tower(TOWER_D_X, 3)

        self.towers = [self.towerS, self.towerT, self.towerD]

        self.reset_disks()

    def quit(self):
        pygame.font.quit()
        pygame.quit()

    def clear_towers(self):
        for tower in self.towers:
            tower.clear_tower()

    def reset_disks(self):
        self.disks.clear()
        self.clear_towers()
        self.moves = 0
        for index in range(self.numDisks, 0, -1):
            disk = Disk(index, self.towerS)
            # print(self.towerS.get_min_disk_index())
            self.towerS.add_disk(disk)

            self.disks.append(disk)


    def draw_panel(self, win: pygame.Surface):
        diskRender = self.panelfont.render(self.diskText + f"{self.numDisks}", 1, BUTTON_LABEL_COLOR)
        w, h = diskRender.get_size()
        win.blit(diskRender, (20, BUTTONS_Y - self.y_off + 5))

        movesRender = self.panelfont.render(self.moveText + f"{self.moves}", 1, BUTTON_LABEL_COLOR)
        x = (self.width - movesRender.get_width()) // 2 - self.x_off
        win.blit(movesRender, (x, BUTTONS_Y - self.y_off + 5))

        minMoveRender = self.panelfont.render(self.minMoveText + f"{self.minMoves}", 1, BUTTON_LABEL_COLOR)
        blitx = (self.width - minMoveRender.get_width()) // 2 - self.x_off
        blity = (self.gui_height - minMoveRender.get_height())
        win.blit(minMoveRender, (blitx, blity))

        for button in self.buttons:
            button.draw(win)
 
    def draw(self):
        self.guiWin.fill(STEEL_BLUE)
        self.draw_panel(self.guiWin)

        # Draw Tower Base
        cX1, cX2 = BASE_X, BASE_X + BASE_WIDTH
        cY1 = cY2 = BASE_Y + BASE_HEIGHT // 2
        radius = BASE_HEIGHT // 2
        pygame.draw.rect(self.guiWin, CHOCOLATE, (BASE_X, BASE_Y, BASE_WIDTH, BASE_HEIGHT))
        pygame.draw.circle(self.guiWin, CHOCOLATE, (cX1, cY1), radius)
        pygame.draw.circle(self.guiWin, CHOCOLATE, (cX2, cY2), radius)

        for tower in self.towers:
            tower.draw(self.guiWin)

        for disk in self.disks:
            disk.draw(self.guiWin)

        if self.selectedDisk:
            x_delta, y_delta = self.selectedDiskDelta
            x, y = pygame.mouse.get_pos()
            x -= self.x_off
            y -= self.y_off
            self.selectedDisk.set_positions(x + x_delta, y + y_delta)
            self.selectedDisk.draw(self.guiWin)
        
        pygame.display.update()

    def button_click(self, button: Button):
        label = button.get_label().lower()

        if label.startswith('restart'):
            self.reset_disks()
        elif label.startswith('solve'):
            self.reset_disks()
            self.hanoi(self.numDisks, 1, 3, 2)
        elif label.startswith('up'):
            self.numDisks = min(self.numDisks + 1, 8)
            self.minMoves = 2 ** self.numDisks - 1
            self.moves = 0
            self.reset_disks()

        elif label.startswith('down'):
            self.numDisks = max(3, self.numDisks - 1)
            self.minMoves = 2 ** self.numDisks - 1
            self.moves = 0
            self.reset_disks()

    def placeDisk(self, x: int, y: int):
        x -= self.x_off
        y -= self.y_off

        if not self.selectedDisk:
            return None

        for tower in self.towers:
            if tower.in_tower(x, y):
                if tower.add_disk(self.selectedDisk):
                    if self.selectedDiskTower != tower:
                        self.moves += 1
                    return None
                
        self.selectedDiskTower.add_disk(self.selectedDisk)

    def hanoi(self, n: int, s: int, d: int, t: int):
        if n > 0:
            self.hanoi(n - 1, s, t, d)
            print(f"{n} disk moved {s} -> {d}")
            self.move(n, s, d)
            self.hanoi(n - 1, t, d, s)

    def move(self, index: int, s: int, d: int):
        disk = None
        src = None
        dest = None
        print(index, s, d, sep='\t')

        for dVar in self.disks:
            if dVar.get_index() == index:
                disk = dVar

        for t in self.towers:
            if t.get_index() == s:
                src = t
            if t.get_index() == d:
                dest = t
            
        print(src, dest, sep='\t')

        src.remove_disk(disk)
        xi, yi = disk.get_pos()
        xf, yf = dest.get_x(), dest.get_stack_height()
        xiter = xi
        xDelta = 2 if xi < xf else -2
        slope = (yf - yi) / (xf - xi)

        run = True
        while run and (abs(xiter - xi) <= abs(xf - xi)):
            self.clock.tick(self.fps)
            pos = pygame.mouse.get_pos()
            x, y = pos

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(x, y, self.win.get_at(pos), sep='\t')

                    for button in self.buttons:
                        if  button.in_button(pos):
                            button.press()
                            self.button_click(button)
                            self.run()


            for button in self.buttons:
                if button.in_button(pos):
                    button.hover()
                else:
                    button.unhover()

            self.draw()
            xiter += xDelta
            y = int(slope * (xiter - xi) + yi)
            disk.set_positions(xiter, y) 
            disk.draw(self.guiWin)
            # pygame.draw.line(self.guiWin, CHOCOLATE, (xi, yi), (xf, yf), 2)
            pygame.display.update()

        dest.add_disk(disk)
        self.moves += 1
                    

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

                    for button in self.buttons:
                        if  button.in_button(pos):
                            button.press()
                            self.button_click(button)
                            

                    # if event.button == 1:
                    #     # print(self.dblClickVar)
                    #     if self.dblClickVar == 0:
                    #         self.dblClickVar = 1
                    #     elif self.dblClickVar <= self.dblClickLimit:
                    #         pygame.event.post(self.dblClickEvent)

                    clickPos = x - self.x_off, y - self.y_off
                    for tower in self.towers:
                        disk = tower.get_top_disk()
                        
                        if disk and disk.in_disk(clickPos):
                            print(f"True: {disk.get_index()}")
                            self.selectedDisk = disk
                            diskX, diskY = disk.get_pos()

                            self.selectedDiskDelta = diskX - x + self.x_off, diskY - y + self.y_off
                            self.selectedDiskTower = disk.get_tower()
                            self.selectedDiskTower.remove_disk(self.selectedDisk)


                if event.type == pygame.MOUSEBUTTONUP:                    
                    for button in self.buttons:
                        if button.is_pressed():
                            button.unpress()

                    pos = pygame.mouse.get_pos()
                    self.placeDisk(pos[0], pos[1])
                    self.selectedDisk = None
                    self.selectedDiskDelta = None
                    self.selectedDiskTower = None

                if event.type == self.dblClickEvent.type:
                    print("DBL CLICK")
                    self.dblClickVar = 0

            for button in self.buttons:
                if button.in_button(pos):
                    button.hover()
                else:
                    button.unhover()

            if self.dblClickVar != 0:
                self.dblClickVar += 1
            
            if self.dblClickVar > self.dblClickLimit:
                self.dblClickVar = 0

            pygame.display.update()

        self.quit()


if __name__ == "__main__":
    X = gui()
    X.run()