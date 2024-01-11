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
flying= False
gameOver = False

#load images
bg=pygame.image.load('Flappy-Bird---Pygame/img/bg.png')
ground=pygame.image.load('Flappy-Bird---Pygame/img/ground.png')

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img=pygame.image.load(f'Flappy-Bird---Pygame/img/bird{num}.png')
            self.images.append(img)
        
        self.image =self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center= [x,y]
        self.vel =0
        self.clicked = False
    
    def update(self):
        if flying == True:
            #gravity
            self.vel +=0.5
            if self.vel > 8:
                self.vel=8
            print(self.vel)
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        if gameOver == False:
        #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: 
                self.clicked= True
                self.vel = -10

            if pygame.mouse.get_pressed()[0] == 0 : 
                self.clicked =False


            #animation
            self.counter +=1
            flapCooldown = 5

            if self.counter > flapCooldown:
                self.counter = 0
                self.index += 1

                if self.index >= len(self.images):
                    self.index=0
            self.image=self.images[self.index]

            #rotation

            self.image = pygame.transform.rotate(self.images[self.index],self.vel* -2)

        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)

birdGroup =pygame.sprite.Group()

flappy= Bird(100,int(SCREEN_HEIGHT/2))

birdGroup.add(flappy)
run = True
while run:

    clock.tick(fps)
    screen.blit(bg,(0,0))
    birdGroup.draw(screen)
    birdGroup.update()

    screen.blit(ground,(groundScroll,768))

    #gameOver Logic

    if flappy.rect.bottom > 768: #it has hit ground
        gameOver = True
        flying = False
    #draw Logic
    if gameOver == False:
        groundScroll -= scrollSpeed
        if abs(groundScroll) > 35: #total pixel is 35 for the lined section
            groundScroll=0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and gameOver == False:
            flying =True
    pygame.display.update() #refresh
  
pygame.quit()   