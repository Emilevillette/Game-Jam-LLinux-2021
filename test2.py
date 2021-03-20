import pygame
import random
import math
from Player import Player

# Initialize the pygame
pygame.init()

# Create the screen
sizeX = 800
sizeY = 600
screen = pygame.display.set_mode((sizeX,sizeY))

# Background
background = pygame.image.load('ressources/maps/test.png')

# Caption and icon
pygame.display.set_caption("Pog Pog Pog")
icon = pygame.image.load('ressources/images/pog.png')
pygame.display.set_icon(icon)

# Player
p = Player(pygame.image.load('ressources/images/player.png'),370,480,0.5)

def player():
    screen.blit(p.img,(p.X,p.Y)) #draw

# Enemies
enemyImg = []
sizeEnemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# Enemy
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ressources/images/joker.png'))
    sizeEnemy.append(64)
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,564))
    enemyX_change.append(0.3)
    enemyY_change.append(0)


def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y)) #draw

# Game Loop
running = True
while running :

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background,(0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.move(-1,0)
            elif event.key == pygame.K_RIGHT:
                p.move(1,0)
            elif event.key == pygame.K_DOWN:
                p.move(0,1)
            elif event.key == pygame.K_UP:
                p.move(0,-1)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p.stop()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                p.stop()

    p.update()

    for i in range (num_of_enemies):
        collision = p.isCollision(enemyX[i],enemyY[i])
        if collision:
            playerX-=playerX_change
            playerY-=playerY_change

    enemyX+=enemyX_change
    enemyY+=enemyY_change

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
        if enemyX[i] <= 0 :
            enemyX[i] = 0 
            enemyX_change[i] = -enemyX_change       
        elif enemyX[i] >= sizeX-sizeEnemy[i]:
            enemyX_change[i] = -enemyX_change
        # enemyX = sizeX-sizePlayer

        if enemyY[i] <= 0 :
            enemyX_change[i] = -enemyX_change
        elif enemyY[i] >= sizeY-sizeEnemy[i]:
            enemyY[i] = sizeY-sizeEnemy[i]

    for i in range (num_of_enemies):
        enemy(enemyX[i],enemyY[i],i)

    player()
    pygame.display.update()