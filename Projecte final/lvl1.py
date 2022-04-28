import pygame
from pygame.locals import *
pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('images/lvl1.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))
clock = pygame.time.Clock()
 
i = 0
 
runing = True
while runing:  
    
    window.fill((0,0,0))
    window.blit(bg_img,(i,0))
    window.blit(bg_img,(width+i,0))
    if (i==-width):
        window.blit(bg_img,(width+i,0))
        i=0
    i-=1
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
            
    keys = pygame.key.get_pressed() 
    if keys[K_DOWN]: 
        print ("DOWN") 
    for e in pygame.event.get(): 
        pass
    pygame.display.update()
    clock.tick(500)
pygame.quit()