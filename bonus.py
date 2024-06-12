import pygame as py
import random
from game_settings import *

class Bonus(py.sprite.Sprite):
    def __init__(self,image_l,chance):
        super().__init__()
        self.width=60
        self.height=60
        self.image_l=image_l
        self.image=None
        self.set_bonus()
        self.rect=self.image.get_rect()
        self.rect.center=(self.width/2,self.height/2)
        self.rect.x=random.randint(0,600)
        self.rect.bottom=0+random.randint(-300,-50)
        self.chance=chance
        self.showed=random.randint(1,self.chance)
    
    def set_bonus(self):
        self.name=random.choice(["HEART","JUMP"])
        if self.name=="HEART":
            self.image=self.image_l[0]
        else:
            self.image=self.image_l[1]

    def update(self,screen,scroll,group):        
        self.rect.y+=scroll
        if self.showed==1:
            group.draw(screen)
        else:
            self.kill()
        if self.rect.bottom>850:
            self.kill()
