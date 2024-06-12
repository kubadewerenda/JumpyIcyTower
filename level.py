import pygame as py
import random
from bonus import Bonus
from enemy import Enemy
from platforms import Platform
from scoreboard import Scoreboard
from healthbar import Healthbar
from text import Text
from game_settings import *

class Level(py.sprite.Sprite):
    def __init__(self, enemy_sheet, bonus_imgs,p_lives):
        super().__init__()
        self.enemy_sheet = enemy_sheet
        self.bonus_imgs = bonus_imgs
        self.enemy_group = py.sprite.Group()
        self.bonus_group = py.sprite.Group()
        self.platform_group = py.sprite.Group()
        self.scoreboard=Scoreboard(x=30, y=22)
        self.healthbar=Healthbar(x=420, y=20, w_bar=200, h_bar=20, max_hp=p_lives)
        self.l_platform = Platform(START_PLATF_IMG, 0, SCREEN_HEIGHT-30, SCREEN_WIDTH, False)
        self.platform_group.add(self.l_platform)
        self.level_up_points=LEVELS
        self.level=1
        self.level_t=Text(SCREEN_WIDTH/2-55,0,FONT_BIG,BRAZOWY)
        # ---------------------------- Szanse na przeciwnika sett
        self.bonus_chance=9
        self.enemy_chance=8192

    def add_enemy(self, enemy_sheet):
        if len(self.enemy_group)==0:
            enemy=Enemy(enemy_sheet, self.enemy_chance)
            self.enemy_group.add(enemy)

    def level_up(self):
        self.level+=1
        self.bonus_chance-=1
        self.enemy_chance=int(self.enemy_chance / 4)

    def add_platforms(self):
        p_width=random.randint(150, 300)
        p_x=random.randint(0, SCREEN_WIDTH - p_width)
        p_y=self.l_platform.rect.y - random.randint(180, 210)
        p_moving=self.set_moving_p()
        if p_y>-100: 
            new_platform=Platform(PLATFORMS_LVLS[self.level-1], p_x, p_y, p_width, p_moving, self.level-1)
            self.platform_group.add(new_platform)
            self.l_platform=new_platform

    def set_moving_p(self):
        if self.level>len(self.level_up_points):
            return True
        elif self.level==1:
            return False
        else:
            if random.randint(1,9-self.level)==1:
                return True
            else:
                return False
            
    def draw_text(self, surface, text, font, text_col, x, y):
        img=font.render(text, True, text_col)
        surface.blit(img, (x ,y))
    
    def draw_lines(self, surface, player):
        milestone=self.level_up_points[self.level-1]
        line_y=self.scoreboard.score-milestone+SCROLL_TRESH
        # ---------------------------- Optymalizacja rysowania linii lvlu
        if line_y>-2000:
            level_line_rect=LEVEL_LINE.get_rect(center=(SCREEN_WIDTH/2, line_y))
            surface.blit(LEVEL_LINE, level_line_rect)
            self.level_t.update(surface,f"Level: {self.level+1}", line_y-55)
            # ---------------------------- Kolizja z levelem
            if level_line_rect.colliderect(player.rect):
                LEVEL_UP_S.play()
                self.level_up()

    def update(self, surface, scroll, player):
        # ---------------------------- Generowanie platform
        if len(self.platform_group)<MAX_PLATFORMS:
            self.add_platforms()
                
        # ---------------------------- Generowanie bonusów
        if len(self.bonus_group)==0:
            bonus = Bonus(self.bonus_imgs, self.bonus_chance)
            if not py.sprite.spritecollide(bonus, self.platform_group, False):
                self.bonus_group.add(bonus)

        # ---------------------------- Aktualizacja grup
        self.platform_group.update(surface,scroll,self.platform_group)
        self.bonus_group.update(surface,scroll, self.bonus_group)
        self.enemy_group.update(surface, scroll, self.enemy_group)

        # ---------------------------- Rysowanie linii poziomu
        if self.level<=len(self.level_up_points):
            self.draw_lines(surface, player)

        # ---------------------------- Aktualizacja scoreboardu
        self.scoreboard.update(surface, scroll)
        self.scoreboard.draw_hs(surface)

        # ---------------------------- Aktualizacja healthbara
        self.healthbar.update(surface, player.lives)


        # ---------------------------- Kolizje z wrogami
        if py.sprite.spritecollide(player, self.enemy_group, True, py.sprite.collide_mask):
            player.lives-=1
            player.hit_s.play()

        # ---------------------------- Zbieranie bonusów
        collided_bonuses=py.sprite.spritecollide(player, self.bonus_group, True, py.sprite.collide_mask)
        for bonus in collided_bonuses:
            if bonus.name=="HEART":
                # ----------------------------Dzwiek bonusu
                HEALTH_B_S.play()
                if player.lives<5:
                    player.lives+=1
            else:
                # ----------------------------Dzwiek bonusu
                JUMP_B_S.play()
                player.jump_bonus()

    def reset(self):
        # ---------------------------- Oproznianie spritegroup
        self.enemy_group.empty()
        self.bonus_group.empty()
        self.platform_group.empty()

        # ---------------------------- Platforma startowa
        self.l_platform = Platform(START_PLATF_IMG, 0, SCREEN_HEIGHT-30, SCREEN_WIDTH, False)
        self.platform_group.add(self.l_platform)
        
        # ---------------------------- zerowanie zmiennych
        self.level=1
        self.bonus_chance=9
        self.enemy_chance=8192

        self.scoreboard.reset()