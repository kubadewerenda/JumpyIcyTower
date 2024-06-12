import pygame as py
from spritesheet import SpriteSheet

py.init()
py.mixer.pre_init(44100,-16,2,512)


# ---------------------------- CONSTANS ------------------------------- #
SCREEN_WIDTH=650
SCREEN_HEIGHT=850
TITLE="JumpyIcyTower"
LEVELS=[2500,10000,15000,25000,50000,100000]

screen=py.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

# ---------------------------- SOUNDS ------------------------------- #
LOADING_S=py.mixer.Sound("sounds/loading_sound.mp3")
CHOOSE_S=py.mixer.Sound("sounds/choose_sound.mp3")
BUTTON_S=py.mixer.Sound("sounds/button_sound.mp3")
JUMP_B_S=py.mixer.Sound("sounds/jump_b.ogg")
HEALTH_B_S=py.mixer.Sound("sounds/health_b.mp3")
LEVEL_UP_S=py.mixer.Sound("sounds/level_up.mp3")
P1_JUMP=py.mixer.Sound("sounds/player1/jumpp1.mp3")
P1_HIT=py.mixer.Sound("sounds/player1/hitp1.mp3")
P2_JUMP=py.mixer.Sound("sounds/player2/jumpp2.mp3")
P2_HIT=py.mixer.Sound("sounds/player2/hitp2.mp3")

# ---------------------------- IMAGES ------------------------------- #
# ----------------------------BG
BG_IMG=py.image.load("images/bg.png").convert_alpha()
BG_MENU=py.image.load("images/bg_menu.png").convert_alpha()
BG_LOSE=py.image.load("images/bg_lose.png").convert_alpha()

# ----------------------------Load
LOAD_IMG=py.image.load("images/load_scr.png").convert_alpha()

#-----------------------------Logo
LOGO_IMG=py.image.load("images/logo.png").convert_alpha(BG_MENU)

# ----------------------------PLAYER1
PLAYER1_IMG=py.transform.scale(py.image.load("images/player1/player.png"), (150,150))
PLAYER1_STAND_IMG=py.image.load("images/player1/stand.png")
PLAYER1_JUMP_IMG=py.image.load("images/player1/jump.png")
PLAYER1_WALK_IMG=[py.transform.scale(py.image.load(f"images/player1/walk{i}.png"), (80,80)) for i in range(1,7)]
PLAYER1_N="squirrel"

# ----------------------------PLAYER2
PLAYER2_IMG=py.transform.scale(py.image.load("images/player2/player.png"), (150,150))
PLAYER2_STAND_IMG=py.image.load("images/player2/stand.png")
PLAYER2_JUMP_IMG=py.image.load("images/player2/jump.png")
PLAYER2_WALK_IMG=[py.transform.scale(py.image.load(f"images/player2/walk{i}.png"), (80,80))for i in range(1,7)]
PLAYER2_N="pingwin"

# ----------------------------ENEMY
ENEMY_SHEET_IMG=py.image.load("images/raven.png").convert_alpha(BG_IMG)
ENEMY_SHEET=SpriteSheet(ENEMY_SHEET_IMG)

# ----------------------------BONUS
HEART_IMG=py.image.load("images/bonus_heart.png").convert_alpha()
JUMP_IMG=py.image.load("images/bonus_jump.png").convert_alpha()
BONUS_IMGS=[HEART_IMG,JUMP_IMG]

# ----------------------------PLATFORMS
START_PLATF_IMG = py.image.load("images/check_point.png")
PLATFORM_0 = py.image.load("images/level_0.png")
PLATFORM_1 = py.image.load("images/level_1.png")
PLATFORM_2 = py.image.load("images/level_2.png")
PLATFORM_3 = py.image.load("images/level_3.png")
PLATFORM_4 = py.image.load("images/level_4.png")
PLATFORM_5 = py.image.load("images/level_5.png")
PLATFORM_6 = py.image.load("images/level_6.png")
PLATFORMS_LVLS=[PLATFORM_0,PLATFORM_1,PLATFORM_2,PLATFORM_3,PLATFORM_4,PLATFORM_5,PLATFORM_6]

# ----------------------------SCORE
SCORE_IMG=py.image.load("images/score.png").convert_alpha()

# ----------------------------PLATFORMS
LEVEL_LINE=py.transform.scale(py.image.load("images/line.png"), (650,30))

# ---------------------------- COLORS ------------------------------- #
WHITE=(255,255,255)
BLACK=(0,0,0,0)
GOLD=(250,208,0)
PURPLE=(82,20,100)
TURKUSOWY=(108,230,203)
BRAZOWY=(223,188,64)

# ----------------------------Framerate
clock=py.time.Clock()
FPS=60

# ----------------------------game var
PLAYER_GRAV=1
MAX_PLATFORMS=9
SCROLL_TRESH=200
PARTICLES_GRAV=0.2
PARTICLES_GRAV_JB=1


# ---------------------------- FONTS------------------------------- #
FONT_BTN_MENU=py.font.Font('fonts/pixelfont.ttf',85)
FONT_L_BTN_MENU=py.font.Font('fonts/pixelfont.ttf',60)
FONT_CH_TEXT=py.font.Font('fonts/pixelfont.ttf',60)
FONT_SMALL=py.font.SysFont('Lucida Sans',24)
FONT_BIG=py.font.SysFont('Lucida Sans',30)
FONT_SMALL=py.font.SysFont('comicsans',24)
FONT_BIG=py.font.SysFont('comicsans',32)
FONT_SCORE_BIG=py.font.SysFont('comicsans',45,"bold")