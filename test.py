import pygame

# Initialize the pygame
pygame.init()

# Create the screen
sizeX = 800
sizeY = 600
screen = pygame.display.set_mode((sizeX,sizeY))

# Caption and icon
pygame.display.set_caption("Pog Pog Pog")
icon = pygame.image.load('ressources/images/pog.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ressources/images/player.png')
sizePlayer = 64
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('ressources/images/joker.png')
enemyX = 370
enemyY = 50
enemyX_change = 0
enemyY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y)) #draw

def enemy(x,y):
    screen.blit(enemyImg,(x,y)) #draw


# Game Loop
running = True
while running :

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
                # playerX-=20
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.1
                # playerX+=20
            elif event.key == pygame.K_DOWN:
                playerY_change = 0.1
                # playerY+=20
            elif event.key == pygame.K_UP:
                playerY_change = -0.1
                # playerY-=20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0

    playerX+=playerX_change
    playerY+=playerY_change

    # Boundaries
    if playerX <= 0 :
        playerX = 0
    elif playerX >= sizeX-sizePlayer:
        playerX = sizeX-sizePlayer

    if playerY <= 0 :
        playerY = 0
    elif playerY >= sizeY-sizePlayer:
        playerY = sizeY-sizePlayer

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()