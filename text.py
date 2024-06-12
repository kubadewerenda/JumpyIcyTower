import pygame as py
from game_settings import *

class Text():
    def __init__(self, x, y, font, font_color=WHITE, text=""):
        self.x=x
        self.y=y
        self.text=text
        self.font_color=font_color
        self.font=font
        # ---------------------------- Img text
        self.image=self.font.render(self.text, 1, self.font_color)
        self.rect=self.image.get_rect(center=(self.x,self.y))

    def update(self, surface, text="", y=0):
        # ---------------------------- czy zmiana y
        if y!=0:
            self.y=y
        self.text=text
        # ---------------------------- czy zmiana textu
        if text!="":
            self.text=text
        self.image=self.font.render(self.text, 1, self.font_color)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.draw(surface)
    
    
    def draw(self, surface):
        surface.blit(self.image,self.rect)


    