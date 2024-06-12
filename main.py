import pygame as py
from player import Player
from level import Level
from button import Button
from button import Chooseplayer
from text import Text
from game_settings import *

# ---------------------------- WINDOW ------------------------------- #
screen=py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption(TITLE)

# ---------------------------- CHOOSEP. BUTTONS ------------------------------- #
PLAYER1_BTN=Chooseplayer(PLAYER1_IMG, pos=(240,500), alpha=80, border_radius=10, clicked=True)
PLAYER2_BTN=Chooseplayer(PLAYER2_IMG, pos=(410,500), alpha=80, border_radius=10, clicked=False)


# ---------------------------- FUNCTIONS------------------------------- #
def draw_bg(bg_scroll):
    screen.blit(BG_IMG,(0, 0+bg_scroll))
    screen.blit(BG_IMG,(0, -SCREEN_HEIGHT+bg_scroll))

def main_menu():
    global game_menu, game_active, game_on
    screen.blit(BG_MENU,(0,0))

    # ---------------------------- OBIECTS MAIN MENU ------------------------------- #
    MENU_MOUSE_POS=py.mouse.get_pos()

    MENU_L_RECT=LOGO_IMG.get_rect(center=(SCREEN_WIDTH/2, 220))

    PLAY_BUTTON=Button(None, pos=(150,695), text_input="Play", font=FONT_BTN_MENU, base_color=PURPLE, hovering_color=TURKUSOWY, alpha=50)
    QUIT_BUTTON=Button(None, pos=(500,695), text_input="Quit", font=FONT_BTN_MENU, base_color=PURPLE, hovering_color=TURKUSOWY, alpha=50)
    CHOOSE_CHAMP_TXT=Text(SCREEN_WIDTH/2, 380, FONT_CH_TEXT, TURKUSOWY, "PICK  CHAMPION")

    CHOOSE_CHAMP_TXT.draw(screen)

    for button in [PLAY_BUTTON, QUIT_BUTTON]:
        button.change_color(MENU_MOUSE_POS)
        button.update(screen)

    for button in [PLAYER1_BTN,PLAYER2_BTN]:
        button.change_color(MENU_MOUSE_POS,screen)
        button.update(screen)

    for event in py.event.get():
        if event.type==py.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                BUTTON_S.play()
                game_active=True
                game_menu=False
            if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                BUTTON_S.play()
                game_on=False
            if PLAYER1_BTN.check_for_input(MENU_MOUSE_POS):
                CHOOSE_S.play()
                PLAYER1_BTN.clicked=True
                PLAYER2_BTN.clicked=False
                player.update_champ(PLAYER1_STAND_IMG,PLAYER1_JUMP_IMG,PLAYER1_WALK_IMG,PLAYER1_N,P1_JUMP,P1_HIT)
            if PLAYER2_BTN.check_for_input(MENU_MOUSE_POS):
                CHOOSE_S.play()
                PLAYER1_BTN.clicked=False
                PLAYER2_BTN.clicked=True
                player.update_champ(PLAYER2_STAND_IMG,PLAYER2_JUMP_IMG,PLAYER2_WALK_IMG,PLAYER2_N,P2_JUMP,P2_HIT)
        if event.type==py.QUIT:
            game_on=False
    

    screen.blit(LOGO_IMG,MENU_L_RECT)

def play():
    global scroll, bg_scroll, game_menu, game_active, game_on

    scroll=player.move(level.platform_group)

    # ---------------------------- BG DRAW
    bg_scroll+=scroll
    if bg_scroll>=SCREEN_HEIGHT:
        bg_scroll=0
    draw_bg(bg_scroll)

    # ---------------------------- LEVEL CONTROL
    level.add_enemy(ENEMY_SHEET)  
    level.update(screen, scroll, player)

    # ---------------------------- DRAW SPRITES
    player.draw(screen)  


    # ---------------------------- GAME OVER
    if player.rect.top>SCREEN_HEIGHT:
        game_active=False
    
    if player.lives==0:
        game_active=False
    
    #------------------------------Pause
    key=py.key.get_pressed()
    if key[py.K_ESCAPE]:
        game_active=False    

def stop_play():
    global scroll, bg_scroll, game_menu, game_active, fade_couter, game_on

    # ---------------------------- OBJ. END MENU ------------------------------- #
    MENU_L_MOUSE_POS=py.mouse.get_pos()

    BACK_MENU_BTN=Button(None, (150,720), "Menu", FONT_L_BTN_MENU, PURPLE,TURKUSOWY, alpha=50, border_radius=20)
    QUIT_BTN=Button(None, (500,720), "Quit", FONT_L_BTN_MENU, PURPLE, TURKUSOWY, alpha=50, border_radius=20)
    PLAY_AGAIN=Button(None, (SCREEN_WIDTH/2,620), "Play Again", FONT_L_BTN_MENU, PURPLE, TURKUSOWY, alpha=50, border_radius=20)
    SCORE_T=Text(SCREEN_WIDTH/2,515, FONT_SCORE_BIG, BRAZOWY, f"{level.scoreboard.score} | {level.scoreboard.high_score}")

    PUCHAR_IMG=py.transform.scale(SCORE_IMG,(100,100))
    PUCHAR_RECT=PUCHAR_IMG.get_rect(center=(SCREEN_WIDTH/2,435))
    
    if fade_couter<SCREEN_HEIGHT:
        fade_couter+=25
        screen.blit(BG_LOSE,(0, -SCREEN_HEIGHT+fade_couter))
    else:
        screen.blit(BG_LOSE, (0,0))
        screen.blit(PUCHAR_IMG, PUCHAR_RECT)
        SCORE_T.draw(screen)

        for button in [BACK_MENU_BTN, QUIT_BTN,PLAY_AGAIN]:
            button.change_color(MENU_L_MOUSE_POS)
            button.update(screen)

        #-----------------------------Events
        for event in py.event.get():
            if event.type==py.MOUSEBUTTONDOWN:
                if BACK_MENU_BTN.check_for_input(MENU_L_MOUSE_POS): 
                    BUTTON_S.play()
                    # ----------------------------reset variabldes                                   
                    game_menu=True
                    scroll=0
                    fade_couter=0
                    
                    player.lives=5
                    player.rect.center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-100)
                    player.particles_group.empty()

                    level.reset()

                if QUIT_BTN.check_for_input(MENU_L_MOUSE_POS):
                    BUTTON_S.play()
                    game_on=False
                if PLAY_AGAIN.check_for_input(MENU_L_MOUSE_POS):
                    BUTTON_S.play()
                    game_active=True
                    scroll=0
                    fade_couter=0
                    
                    player.lives=5
                    player.rect.center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-100)
                    player.particles_group.empty()

                    level.reset()
            if event.type==py.QUIT:
                game_on=False

        # ----------------------------high score
        level.scoreboard.save_hs()

        key=py.key.get_pressed()
        if key[py.K_SPACE]:
            # ----------------------------reset variabldes
            game_active=True
            scroll=0
            fade_couter=0
            player.lives=5

            # ----------------------------position startplayer
            player.rect.center=(SCREEN_WIDTH//2, SCREEN_HEIGHT-100)
            
            # ----------------------------reset enemy
            level.reset()
        if key[py.K_ESCAPE]:
            game_on=False

def game_control():
    if game_active:
        play()
    else:
        stop_play()

def loading_screen():
    LOADING_S.play()
    
    LOAD_IMG_RECT=LOAD_IMG.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    start_time=py.time.get_ticks()
    loading_time=5000

    while py.time.get_ticks()-start_time<loading_time:
        screen.blit(LOAD_IMG,LOAD_IMG_RECT)
        py.display.update()


# ---------------------------- SPRITE GROUPS------------------------------- #
player=Player(SCREEN_WIDTH//2, SCREEN_HEIGHT-100)

level=Level(ENEMY_SHEET, BONUS_IMGS, player.lives)

# ---------------------------- VARIABLES------------------------------- #
clock=py.time.Clock()

scroll=0
bg_scroll=0
fade_couter=0

# ---------------------------- GAME LOOP------------------------------- #
game_load=True
game_menu=True
game_active=False
game_on=True

# ----------------------------LOADING SCREEN------------------------------- #
loading_screen()

while game_on:
    clock.tick(FPS)
    if game_menu==True:
        main_menu()
    else:
        game_control()                

    # ----------------------------event handler
    for event in py.event.get():
        if event.type == py.QUIT:
            game_on=False
    
    py.display.update()

py.quit()
