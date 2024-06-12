import pygame as py
import os
from text import Text
from game_settings import *


class Scoreboard(py.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.load_img=SCORE_IMG
        self.width=40
        self.height=30
        self.image=py.transform.scale(self.load_img, (self.width,self.height))
        self.rect=self.image.get_rect()
        self.rect.center=x,y
        self.score=0
        self.score_t=Text(55, 8, FONT_SMALL, WHITE)
        self.hs_t=Text(0, 0, FONT_SMALL, WHITE)
        # ---------------------------- Ładowanie pliku jezeli istnieje
        if os.path.exists("data/score.txt"):
            with open("data/score.txt","r") as file:
                self.high_score=int(file.read())
        else:
            self.high_score=0
    
    def save_hs(self):
        # ---------------------------- zapisywanie do pliku
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data/score.txt","w") as file:
                file.write(str(self.high_score))
    
    def draw_hs(self, surface):
        line_y=self.score-self.high_score+SCROLL_TRESH
        py.draw.line(surface,WHITE,(0,line_y),(SCREEN_WIDTH,line_y),3)
        self.hs_t.update(surface,f"HIGH SCORE: {self.high_score}",line_y)
    
        
    def update(self, surface, scroll):
        # ---------------------------- Rysowanie pucharu
        surface.blit(self.image, self.rect)
        if scroll>0:
            self.score+=scroll
        self.score_t.update(surface, f"{self.score}")
    
    def reset(self):
        self.score=0