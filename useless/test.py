import pygame
import random
import math

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
playerImg = pygame.image.load('ressources/images/player.png')
sizePlayer = 64
playerX = 370
playerY = 480
playerSpeed = 0.5
playerX_change = 0
playerY_change = 0

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

def player(x,y):
    screen.blit(playerImg,(x,y)) #draw

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y)) #draw

def isCollision(X,Y,other_X,other_Y):
    distance = math.sqrt(math.pow(X-other_X,2) + math.pow(Y-other_Y,2))
    return (distance < 64)

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
                playerX_change = -playerSpeed
                # playerX-=20
            elif event.key == pygame.K_RIGHT:
                playerX_change = playerSpeed
                # playerX+=20
            elif event.key == pygame.K_DOWN:
                playerY_change = playerSpeed
                # playerY+=20
            elif event.key == pygame.K_UP:
                playerY_change = -playerSpeed
                # playerY-=20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0

    playerX+=playerX_change
    playerY+=playerY_change

    for i in range (num_of_enemies):
        collision = isCollision(playerX,playerY,enemyX[i],enemyY[i])
        if collision:
            playerX-=playerX_change
            playerY-=playerY_change

    enemyX+=enemyX_change
    enemyY+=enemyY_change

    # Boundaries player
    if playerX <= 0 :
        playerX = 0
    elif playerX >= sizeX-sizePlayer:
        playerX = sizeX-sizePlayer

    if playerY <= 0 :
        playerY = 0
    elif playerY >= sizeY-sizePlayer:
        playerY = sizeY-sizePlayer

    for i in range (6) :
        # Boundaries enemy
        if enemyX[i] <= 0 :
            enemyX[i] = 0 
            enemyX_change[i] = -enemyX_change       
        elif enemyX[i] >= sizeX-sizePlayer:
            enemyX_change[i] = -enemyX_change
        # enemyX = sizeX-sizePlayer

        if enemyY[i] <= 0 :
            enemyX_change[i] = -enemyX_change
        elif enemyY[i] >= sizeY-sizeEnemy[i]:
            enemyY[i] = sizeY-sizeEnemy[i]

    for i in range (num_of_enemies):
        enemy(enemyX[i],enemyY[i],i)

    player(playerX,playerY)
    pygame.display.update()