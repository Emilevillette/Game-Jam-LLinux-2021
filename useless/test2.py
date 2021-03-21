import pygame as pg
import random
import math
from Player import Player
from Enemy import Enemy

# Initialize the pg
pg.init()

# Create the screen
sizeX = 800
sizeY = 600
screen = pg.display.set_mode((sizeX,sizeY))

# Background
background = pg.image.load('ressources/maps/test.png')

# Caption and icon
pg.display.set_caption("Pog Pog Pog")
icon = pg.image.load('ressources/images/pog.png')
pg.display.set_icon(icon)

# Player
p = Player(pg.image.load('ressources/images/player.png'),370,480,0.5)

def player():
    screen.blit(p.img,(p.X,p.Y)) #draw

# Enemies
enemies = []
num_of_enemies = 6

# Enemy
for i in range(num_of_enemies):
    enemies.append(Enemy(pg.image.load('ressources/images/joker.png'),random.randint(0,736),random.randint(0,564),0.3))

def enemy(i):
    screen.blit(enemies[i].img, (enemies[i].X, enemies[i].Y)) #draw

# Game Loop
running = True
while running :

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background,(0,0))
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                p.move(-1,0)
            elif event.key == pg.K_RIGHT:
                p.move(1,0)
            elif event.key == pg.K_DOWN:
                p.move(0,1)
            elif event.key == pg.K_UP:
                p.move(0,-1)

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                p.stop()
            elif event.key == pg.K_DOWN or event.key == pg.K_UP:
                p.stop()

    p.update()

    for i in range (len(enemies)):
        collision = p.isCollision(enemies[i].X,enemies[i].Y)
        if collision:
            p.cancel()

    # Boundaries player
    if p.X <= 0 :
        p.X = 0
    elif p.X >= sizeX-p.size:
        p.X = sizeX-p.size

    if p.Y <= 0 :
        p.Y = 0
    elif p.Y >= sizeY-p.size:
        p.Y = sizeY-p.size

    for i in range (6) :
        # Boundaries enemy
        if enemies[i].X <= 0 :
            enemies[i].X = 0 
            enemies[i].cancel()     
        elif enemies[i].X >= sizeX-enemies[i].size:
            enemies[i].cancel()     
        # enemyX = sizeX-sizePlayer

        if enemies[i].Y <= 0 :
            enemies[i].cancel()
        elif enemies[i].Y >= sizeY-enemies[i].size:
            enemies[i].Y = sizeY-enemies[i].size

    for i in range (num_of_enemies):
        enemy(i)

    player()
    pg.display.update()