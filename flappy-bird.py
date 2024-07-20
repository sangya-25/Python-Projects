import pygame
import random
#to initialize pyga,e
pygame.init()

#constants
screen_width=400
screen_height=600
bird_width=34
bird_height=24
pipe_width=52
pipe_height=320
gravity=0.5
flap_strength=10

#colours
white=(255,255,255)
black=(0,0,0)
#game variables
bird_x=50
bird_y=screen_height//2
bird_velocity=0
score=0

#pipe list
pipes=[]
pipe_frequency=1500  #miliseconds

#set up display
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("flappy bird")

#load assets
bird_img=pygame.Surface((bird_height,bird_width))
bird_img.fill((255,255,0)) #yellow bird
pipe_image=pygame.Surface((pipe_width,pipe_height))
pipe_image.fill((0,255,0))    #green pipe

#functions to create pipes
def create_pipe():
    height=random.randint(100,600)
    pipe_top=pipe_image.get_rect(topleft=(screen_width,height-pipe_height))
    pipe_bottom=pipe_image.get_rect(topleft=(screen_width,height+150))
    return pipe_top, pipe_bottom

#game loop:
running = True
clock=pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT,pipe_frequency)
pipes.append(create_pipe())
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_velocity=-flap_strength
        if event.type==pygame.USEREVENT:
            pipes.append(create_pipe())
        #update birds:
        bird_velocity+=gravity
        bird_y+=bird_velocity

        #move pipe:
        for pipe_pair in pipes:
            pipe_pair[0].x-=5
            pipe_pair[1].x-=5

        #remove off-screen pipes:
        pipe=[pipe for pipe in pipes if pipe[0].x>-pipe_width]

        #check for collisions;
        for pipe_pair in pipes:
            if pipe_pair[0].colliderect((bird_x,bird_y,bird_width,bird_height)) or pipe_pair[1].colliderect((bird_x,bird_y,bird_height,bird_width)):
                running= False
        #check if bird goes off-screen:
        if bird_y>screen_height or bird_y<0:
            running = False

        #fill screen
        screen.fill(white) 
        #draw bird
        screen.blit(bird_img,(bird_x,bird_y))
        #draw pipes:
        for pipe_pair in pipes:
            screen.blit(pipe_image,pipe_pair[0].topleft)
            screen.blit(pipe_image,pipe_pair[1].topleft) 
        #update display:
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
