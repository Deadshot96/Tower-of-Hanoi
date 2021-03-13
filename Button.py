import pygame
from pygame import Surface
from colors import *
from settings import *
from typing import Tuple

class Button:

    pygame.font.init()
    font = pygame.font.SysFont(BUTTON_FONT, BUTTON_FONT_SIZE)

    def __init__(self, x: int, y: int, label: str, button_p: Surface, button_up: Surface):
        self.x = x
        self.y = y
        self.label = label
        self.width = 0
        self.height = 0
        self.label_width = 0
        self.label_height = 0
        self.w_mul = 1.4
        self.h_mul = 1.5
        self.buttonRect = None
        self.labelTextHover = None
        self.labelText = None
        self.button_pressed_img = button_p
        self.button_unpress_img = button_up
        self.isHover = False
        self.isPressed = False

        self.set_label_and_size()

    def set_label_and_size(self) -> None:
        self.labelText = self.font.render(self.label, 1, BUTTON_LABEL_COLOR)
        self.labelTextHover = self.font.render(self.label, 1, BUTTON_LABEL_HOVER_COLOR)

        self.label_width = max(self.labelText.get_width(), self.labelTextHover.get_width())
        self.label_height = max(self.labelText.get_height(), self.labelTextHover.get_height()) 

        self.width = int(self.label_width * self.w_mul)
        self.height = int(self.label_height * self.h_mul)

        self.button_pressed_img = pygame.transform.scale(self.button_pressed_img, (self.width, self.height))
        self.button_unpress_img = pygame.transform.scale(self.button_unpress_img, (self.width, self.height))

        self.buttonRect = pygame.Rect(self.x + X_OFF, self.y + Y_OFF, self.width, self.height)


    def draw(self, win: Surface):

        destX = self.x + (self.width - self.label_width) // 2 + 2
        destY = self.y + (self.height - self.label_height) // 2 + 2

        if self.is_pressed():
            win.blit(self.button_pressed_img, (self.x, self.y))
            win.blit(self.labelText, (destX, destY))
        else:
            win.blit(self.button_unpress_img, (self.x, self.y))
            if self.is_hover():
                win.blit(self.labelTextHover, (destX, destY))
            else:
                win.blit(self.labelText, (destX, destY))

    def is_hover(self) -> bool:
        return self.isHover

    def hover(self):
        self.isHover = True

    def unhover(self):
        self.isHover = False
    
    def is_pressed(self) -> bool:
        return self.isPressed

    def press(self):
        self.isPressed = True

    def unpress(self):
        self.isPressed = False

    def get_dims(self) -> Tuple:
        return self.width, self.height

    def get_pos(self) -> Tuple:
        return self.x, self.y

    def get_label(self) -> str:
        return self.label

    def in_button(self, pos: Tuple) -> bool:
        return self.buttonRect.collidepoint(pos)

    def set_multipliers(self, w_mul: float, h_mul: float) -> None:
        self.w_mul = w_mul
        self.h_mul = h_mul
        
        self.set_label_and_size()
        