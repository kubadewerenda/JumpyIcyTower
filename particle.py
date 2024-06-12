import pygame as py
import random
from game_settings import *

class Particle(py.sprite.Sprite):
    def __init__(self, x, y, player_name):
        super().__init__()
        self.x=x
        self.y=y
        self.size=random.randint(3,7)
        self.random_r=random.randint(20,246)
        self.random_g=random.randint(20,204)
        # ---------------------------- setting kolorow particle pod gracza
        if player_name==PLAYER1_N:
            self.color=(self.random_r, 0, self.random_r+random.randint(1,8))
        else:
            self.color=(0, self.random_g, self.random_g+48)
        self.gravity=PARTICLES_GRAV
        self.vel_x=random.uniform(-2,2)
        self.vel_y=random.uniform(-2,2)
    
    def update(self):
        # ---------------------------- works
        self.vel_y+=self.gravity
        self.x+=self.vel_x
        self.y+=self.vel_y
        self.size-=0.1
        if self.size<0:
            self.kill()

    def draw(self, surface):
        py.draw.circle(surface, self.color, (self.x,self.y), self.size)
    
