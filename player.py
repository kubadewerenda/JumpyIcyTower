import pygame as py
import random
from particle import Particle
from game_settings import *
from math import floor

class Player(py.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.player_name=PLAYER1_N
        self.image_jump=py.transform.scale(PLAYER1_JUMP_IMG, (80,80))
        self.image_walk=PLAYER1_WALK_IMG
        self.image_stand=py.transform.scale(PLAYER1_STAND_IMG, (80, 80))
        self.jump_s=P1_JUMP
        self.hit_s=P1_HIT
        self.width=self.image_stand.get_width()
        self.height=self.image_stand.get_height()
        self.rect=py.Rect(0, 0, self.width, self.height-5)
        self.rect.center=(x, y)
        self.speed=10
        self.jump_val=20
        self.vel_y=0
        self.flip=False
        self.moving=False
        self.walk_index=0
        self.lives=5
        self.particles_group=py.sprite.Group()
    
    def update_champ(self, player_s, player_j, player_w, name,jump_s, hit_s):
        self.image_jump=py.transform.scale(player_j, (80,80))
        self.image_walk=player_w
        self.image_stand=py.transform.scale(player_s, (80, 80))
        self.player_name=name
        self.jump_s=jump_s
        self.hit_s=hit_s
    

    def move(self, platform_group):
        scroll=0
        dx=0
        dy=0

        # ---------------------------- Gravity gracza
        self.vel_y+=PLAYER_GRAV
        dy+=self.vel_y

        key=py.key.get_pressed()
        if key[py.K_a]:
            if self.rect.left>0:
                dx=-self.speed
                self.flip=True
            else:
                dx=0
        if key[py.K_d]:
            if self.rect.right<=SCREEN_WIDTH:
                dx=self.speed
                self.flip=False
            else:
                dx=0

        # ---------------------------- Combo od sciany
        if SCREEN_WIDTH-10<self.rect.right<=SCREEN_WIDTH:
            if key[py.K_SPACE]:
                if key[py.K_a]:
                    self.jump_s.play()
                    dx=-self.speed
                    self.vel_y=-self.jump_val
                    dy+=self.vel_y
        if 0<=self.rect.left<10:
            if key[py.K_SPACE]:
                if key[py.K_d]:
                    self.jump_s.play()
                    dx=self.speed
                    self.vel_y=-self.jump_val
                    dy+=self.vel_y

        # --------------------------- Sprawdzanie ruchu
        if dx!=0:
            self.moving=True
        else:
            self.moving=False
        
        # ---------------------------- Kolizja platformy
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom<platform.rect.centery:
                    if self.vel_y>0:
                        self.rect.bottom=platform.rect.top
                        dy=0
                        self.vel_y=0
                        if key[py.K_SPACE]:
                            self.jump_s.play()
                            self.vel_y=-self.jump_val
                            dy+=self.vel_y

        # ---------------------------- Scrolling w gore
        if self.rect.top<=SCROLL_TRESH:
            if self.vel_y<0:
                scroll=-dy

        # ---------------------------- Obsluga particles
        if self.vel_y!=0:
            self.add_particles()
            if self.vel_y<-self.jump_val:
                for particle_jb in self.particles_group:
                    particle_jb.gravity=PARTICLES_GRAV_JB
          

        # ---------------------------- Update rect
        self.rect.x+=dx
        self.rect.y+=dy+scroll
        # ---------------------------- Update mask
        self.mask=py.mask.from_surface(self.image_stand)

        return scroll
    def jump_bonus(self):
        self.vel_y-=self.jump_val*random.randint(2,4)
    
    def add_particles(self):
        for _ in range(5):
            particle=Particle(self.rect.centerx, self.rect.bottom, self.player_name)
            self.particles_group.add(particle)
        
    def update_particles(self):
        # ---------------------------- Update particles
        for particle in self.particles_group:
            particle.update()  

    def moving_animation(self,surface):
        # ---------------------------- Animacje gracza
        if self.vel_y!=0:
            surface.blit(py.transform.flip(self.image_jump,self.flip,False), (self.rect.x, self.rect.y))
        elif self.moving:
            surface.blit(py.transform.flip(self.image_walk[floor(self.walk_index)],self.flip,False), (self.rect.x, self.rect.y))
            self.walk_index+=0.2
            if self.walk_index>5:
                self.walk_index=0
        else:
            surface.blit(py.transform.flip(self.image_stand,self.flip,False), (self.rect.x, self.rect.y))



    def draw(self,surface):
        for particle in self.particles_group:
            particle.draw(surface)
        self.moving_animation(surface)
        self.update_particles()