import pygame
from colors import *
from settings import *

class Button:

    pygame.font.init()
    font = pygame.font.SysFont(BUTTON_FONT, BUTTON_FONT_SIZE)

    def __init__(self, x: int, y: int, text: str):
        self.x = x
        self.y = y
        self.text = text
    
