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
background = pygame.image.load('background.png')

# main loop
running = True
while running:
    
    # Background Image
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


