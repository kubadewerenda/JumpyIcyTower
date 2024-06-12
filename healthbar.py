import pygame as py
from game_settings import *


class Healthbar():
    def __init__(self, x, y, w_bar, h_bar, max_hp):
        # ---------------------------- hp bar
        self.x=x
        self.y=y
        self.w=w_bar
        self.h=h_bar
        self.hp=max_hp
        self.max_hp=max_hp
        # ---------------------------- Ustawienie zdjecia
        self.w_img=40
        self.h_img=40
        self.load_img=HEART_IMG
        self.image=py.transform.scale(self.load_img, (self.w_img,self.h_img))
        self.rect=self.image.get_rect()
        self.rect.center=SCREEN_WIDTH-30,30
    
    def draw(self,surface):
        # ---------------------------- obliczanie stanu paska
        ratio=self.hp/self.max_hp
        py.draw.rect(surface, "red", (self.x,self.y,self.w,self.h))
        py.draw.rect(surface, "purple", (self.x,self.y,self.w * ratio,self.h))
        # ---------------------------- Rysowanie serca
        surface.blit(self.image, self.rect)
    
    def update(self, surface, actual_hp):
        self.hp=actual_hp
        self.draw(surface)


