# import libraries
from logging import logMultiprocessing
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
enemy_speed = 4

for i in range(num_of_enemies):
    enemyImgs.append(enemyImg)
    enemyXs.append(random.randint(0,756))
    enemyYs.append(random.randint(50,150))
    enemyX_changes.append(enemy_speed)
    enemyY_changes.append(40)

# Ally
allyImg = pygame.image.load("ally.png")
allyX = random.randint(0,756)
allyY = random.randint(50,150)
allyY_change = 1


# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Fonts
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

over_font = pygame.font.Font("freesansbold.ttf", 64)

# Functions
def show_score():
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (10 ,10))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg, (playerX, playerY))

def drawEnemy(x,y,i):
    screen.blit(enemyImgs[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # c = sqrt(a^2 + b^2)
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
game_state = "playing"
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

    if game_state == "playing":
        # Change player position
        playerX = playerX + playerX_change  
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Handle Enemy
        for i in range(num_of_enemies):

            # Game Over
            if enemyYs[i] > 440:
                for j in range(num_of_enemies):
                    enemyYs[j] = 2000
                
                break

            # Change enemy position
            enemyXs[i] = enemyXs[i] + enemyX_changes[i]
            if enemyXs[i] <= 0:
                enemyX_changes[i] = enemy_speed
                enemyYs[i] = enemyYs[i] + enemyY_changes[i]
            elif enemyXs[i] >= 736:
                enemyX_changes[i] = -enemy_speed
                enemyYs[i] = enemyYs[i] + enemyY_changes[i]

            # Collision
            collision = isCollision(enemyXs[i], enemyYs[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bulletState = "ready"
                score_value = score_value + 1
                enemyXs[i] = random.randint(0, 736)
                enemyYs[i] = random.randint(50, 150)

            drawEnemy(enemyXs[i], enemyYs[i], i)

        # Handle Ally
        allyY = allyY + allyY_change
        if allyY > 600:
            allyX = random.randint(0, 756)
            allyY = random.randint(50, 150)
        screen.blit(allyImg, (allyX, allyY))

        # Ally Collision
        collision = isCollision(allyX, allyY, bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bulletState = "ready"

        # Change bullet position
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"
        
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change # <=> bulletY = bulletY - bulletY_change
            
    elif game_state == "ended":
        game_over_text()

    player(playerX, playerY)
    show_score()
    pygame.display.update()

pygame.quit()
