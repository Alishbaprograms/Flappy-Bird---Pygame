import pygame
from pygame.locals import *
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Alishba- Flappy Bird')
#player=pygame.Rect(x,y,width,height)
player = pygame.Rect(300,250,50,50)
run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),player)

    key=pygame.key.get_pressed()
    if key[pygame.K_a]==True:
        player.move_ip(-1,0)
    elif key[pygame.K_d]==True:
        player.move_ip(1,0)
    elif key[pygame.K_w]==True:
        player.move_ip(0,-1)
    elif key[pygame.K_s]==True:
        player.move_ip(0,1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update() #refresh
  
pygame.quit()   