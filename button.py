import pygame as py
from game_settings import *

class Button:
    def __init__(self, image, pos, text_input=None, font=None, base_color=None, hovering_color=None, alpha=255, border_radius=35):
        self.x_pos=pos[0]
        self.y_pos=pos[1]
        self.font=font
        self.base_color=base_color
        self.hovering_color=hovering_color
        self.text_input=text_input
        self.alpha=alpha
        self.alpha_hover=self.alpha+80
        self.border_radius=border_radius
        # ---------------------------- Sprawdzanie czy jest podany text
        if text_input and font:
            self.text=self.font.render(self.text_input, True, self.base_color)
            self.image=py.Surface((self.text.get_width()+10, self.text.get_height()), py.SRCALPHA)
        else:
            self.text=None
            if image:
                self.image=image
            else:
                self.image=py.Surface((200, 50), py.SRCALPHA)

        self.rect=self.image.get_rect(center=(self.x_pos, self.y_pos))
        if self.text:
            self.text_rect=self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.text_rect=None

    def update(self, surface):
        if self.image is not None:
            surface.blit(self.image, self.rect)
        if self.text:
            surface.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left,self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            return True
        else:
            return False

    def change_color(self, position):
        if self.check_for_input(position):
            if self.text:
                self.text=self.font.render(self.text_input, True, self.hovering_color)
            py.draw.rect(self.image, (255, 255, 255, self.alpha_hover), self.image.get_rect(), border_radius=self.border_radius)
        else:
            if self.text:
                self.text=self.font.render(self.text_input, True, self.base_color)
            py.draw.rect(self.image, (255, 255, 255, self.alpha), self.image.get_rect(), border_radius=self.border_radius)

class Chooseplayer(Button):
    def __init__(self, image_input, pos, alpha, border_radius, clicked):
        super().__init__(image_input, pos, None, None, None, None, alpha, border_radius)
        self.clicked=clicked
        self.image=image_input
        self.image_rect=self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.alpha_surface=py.Surface((self.image.get_width()+10, self.image.get_height()+10), py.SRCALPHA)
        self.alpha_surface_rect=self.alpha_surface.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, surface):
        surface.blit(self.alpha_surface, self.alpha_surface_rect)
        surface.blit(self.image, self.image_rect)

    def change_color(self, position, surface):
        if self.check_for_input(position) or self.clicked:
            py.draw.rect(self.alpha_surface, (0, 0, 0, self.alpha_hover), self.alpha_surface.get_rect(), border_radius=self.border_radius)
            surface.blit(self.image, self.image_rect)
        else:
            py.draw.rect(self.alpha_surface, (0, 0, 0, self.alpha), self.alpha_surface.get_rect(), border_radius=self.border_radius)
            surface.blit(self.image, self.image_rect)
