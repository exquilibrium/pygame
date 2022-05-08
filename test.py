# import libraries
import math
import random

import pygame
from pygame import mixer                               

# Initialize pygame
pygame.init()      

# Create Display
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Sound
mixer.music.load("background.wav")
# mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
# icon = pygame.image.load("ufo.png")
# pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
player_change = 0

# Main Loop
running = True
while running:
    
    # Background Image
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -5

    playerX = playerX + player_change  

    screen.blit(playerImg, (playerX, playerY))
    pygame.display.update()

pygame.quit()

