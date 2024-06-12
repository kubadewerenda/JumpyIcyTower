import pygame as py
import random
from game_settings import *

class Enemy(py.sprite.Sprite):
    def __init__(self, sprite_sheet, chance):
        super().__init__()
        self.SCREEN_WIDTH=SCREEN_WIDTH
        # ----------------------------variables
        self.animation_list=[]
        self.frame_index=0
        self.update_time=py.time.get_ticks()

        self.scale=1.2

        self.direction=random.choice([-1,1])

        if self.direction==-1:
            self.flip=True
        else:
            self.flip=False
        
        # ----------------------------load spreetsheet
        animation_steps=10
        for animation in range(animation_steps):
            image=sprite_sheet.get_image(animation, 70, 70, self.scale, (0,0,0))
            image=py.transform.flip(image, self.flip, False)
            image.set_colorkey((0,0,0))
            self.animation_list.append(image)
        
        # ---------------------------- starting img and rect
        self.image=self.animation_list[self.frame_index]
        self.rect=self.image.get_rect()
        if self.direction==1:
            self.rect.right=0
        else:
            self.rect.left=SCREEN_WIDTH
        
        # ----------------------------settings
        self.speed=2
        self.rect.y=random.randint(-100,100)

        # ----------------------------showing
        self.chance=chance
        if random.randint(1,self.chance)==1:
            self.showed=True
        else:
            self.showed=False

    def update(self, surface, scroll, group):
        # ----------------------------update anim
        ANIMATION_COOLDOWN=50
        self.image=self.animation_list[self.frame_index]
        if py.time.get_ticks()-self.update_time>ANIMATION_COOLDOWN:
            self.update_time=py.time.get_ticks()
            self.frame_index+=1
        if self.frame_index>=len(self.animation_list):
            self.frame_index=0
        
        # ----------------------------move enemy
        self.rect.x+=self.direction*self.speed
        self.rect.y+=scroll

        if self.rect.right<0 or self.rect.left>self.SCREEN_WIDTH or not self.showed:
            self.kill()
        else:
            group.draw(surface)

    
    
