import pygame
from pygame.locals import *
pygame.init()

clock=pygame.time.Clock()
fps=60

SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Alishba- Flappy Bird')

#game variables

groundScroll=0
scrollSpeed=4

#load images
bg=pygame.image.load('Flappy-Bird---Pygame/img/bg.png')
ground=pygame.image.load('Flappy-Bird---Pygame/img/ground.png')
run = True
while run:

    clock.tick(fps)
    screen.blit(bg,(0,0))
    screen.blit(ground,(groundScroll,768))
    groundScroll-=scrollSpeed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update() #refresh
  
pygame.quit()   