import pygame

# Initialize the pygame
pygame.init()

# Create the screen
sizeX = 800
sizeY = 600
screen = pygame.display.set_mode((sizeX,sizeY))

# Caption and icon
pygame.display.set_caption("Game Jam")

# Game Loop
running = True
while running :

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False