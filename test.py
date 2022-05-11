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
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyImgs = []
enemyXs = []
enemyYs = []
enemyX_changes = []
enemyY_changes = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImgs.append(enemyImg)
    enemyXs.append(random.randint(0,756))
    enemyYs.append(random.randint(50,150))
    enemyX_changes.append(4)
    enemyY_changes.append(40)


# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Functions
def player(x,y):
    screen.blit(playerImg, (playerX, playerY))



def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

# Game Loop
running = True
while running:
    
    # Background Image
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Current playerX
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Change player position
    playerX = playerX + playerX_change  
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Change bullet position
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change # <=> bulletY = bulletY - bulletY_change
        

    player(playerX, playerY)
    pygame.display.update()

pygame.quit()

