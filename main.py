import pygame
from pygame.locals import *
pygame.init()

SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Alishba- Flappy Bird')
#player=pygame.Rect(x,y,width,height)
#load images
bg=pygame.image.load('Flappy-Bird---Pygame/img/bg.png')
ground=pygame.image.load('Flappy-Bird---Pygame/img/ground.png')
run = True
while run:
    screen.blit(bg,(0,0))
    screen.blit(ground,(0,768))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update() #refresh
  
pygame.quit()   