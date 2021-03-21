import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 768#1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 512#768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Metal Trump Solid V : The vote Pain"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


#Mob settings
MOB_IMG = "Guarde Droite\guarde1.png"
MOB_SPEED = 300
MOB_HIT_RECT = pg.Rect(0, 0, 640, 640)

# Player settings
PLAYER_SPEED = 250
PLAYER_IMG = 'trump1sprite.png'
PLAYER_RADIUS = (128,128)
PLAYER_HIT_RECT = pg.Rect(0, 0, 32, 32)

# Effects
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (1200,1200)
LIGHT_MASK = "light_350_soft.png"
LIGHT_MASK_MED = "light_350_med.png"

#Music
BG_MUSIC = "gamejam.mp3"
HIT_SOUND = ["hit1.mp3","hit2.mp3","hit3.mp3"]
WIN_SOUND = "win1.mp3"
RICH_SOUND = "rich1.mp3"