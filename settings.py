from colors import *
WIDTH = 1000
HEIGHT = 500
GUI_WIDTH = 930
GUI_HEIGHT = 400
X_OFF = (WIDTH - GUI_WIDTH) // 2
Y_OFF = int((HEIGHT - GUI_HEIGHT) * 0.8)
FPS = 60
TITLE_FONT = 'comicsansms'
TITLE_FONT_SIZE = 50
BUTTON_FONT = 'consolas'
BUTTON_FONT_SIZE = 20
BUTTON_PRESSED = 'button_p.png'
BUTTON_UNPRESS = 'button_up.png'
BUTTON_LABEL_COLOR = WHITE
BUTTON_LABEL_HOVER_COLOR = PERU
BUTTONS_Y = 90
DISKS = 8
BASE_X = 25
BASE_Y = GUI_HEIGHT - 80
BASE_WIDTH = GUI_WIDTH - BASE_X * 2
BASE_HEIGHT = 26
TOWER_Y = GUI_HEIGHT - 80
TOWER_X = 60
TOWER_WIDTH = 10
TOWER_HEIGHT = 175
TOWER_T_X = WIDTH // 2 - X_OFF
DELTA = (GUI_WIDTH - 2 * BASE_X) // 3
TOWER_S_X = TOWER_T_X - DELTA
TOWER_D_X = TOWER_T_X + DELTA
DISK_WIDTH_MULTIPLIER = DELTA // 8
DISK_HEIGHT = 20
EVENT_DBLCLICK = 25
print(TOWER_S_X, TOWER_T_X, TOWER_D_X, sep='\t')

