import pygame as py
import random
from game_settings import *

class Platform(py.sprite.Sprite):
    def __init__(self, load_img, x, y, width, moving, speed=1):
        super().__init__()
        self.load_img=load_img
        self.image=py.transform.scale(self.load_img, (width,45))
        self.moving=moving
        self.move_counter=random.randint(0,50)
        self.direction=random.choice([-1,1])
        self.speed=2+speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    
    def update(self, surface, scroll, group):
        # ----------------------------moving side to side
        if self.moving:
            self.move_counter+=1
            self.rect.x+=self.direction*self.speed

        # ----------------------------change platform direction
        if self.rect.left<0 or self.rect.right>SCREEN_WIDTH or self.move_counter>=250:
            self.direction*=-1
            self.move_counter=0

        # ----------------------------platform vertical position
        self.rect.y+=scroll

        # ----------------------------if platform zniknie
        if self.rect.top>SCREEN_HEIGHT:
            self.kill()
        else:   
            group.draw(surface)
