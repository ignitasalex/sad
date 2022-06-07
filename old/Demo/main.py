import pygame
import sys
import key

from player import Player
from enemy import Enemy
from field import Field
from level1_final import Lvl1
from level2 import Lvl2

pygame.init

#Inicializamos la pantalla
screen= pygame.display.set_mode((key.WIDTH,key.HEIGHT))
# To manage how fast the screen updates
clock = pygame.time.Clock()

def main_menu():
    while True:
        # Set the screen background
        screen.fill(key.COLOUR)

        mouse_pos = pygame.mouse.get_pos()

        button_level_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

    
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #left button
                    click = True
        
        #Logic
        if button_level_1.collidepoint(mouse_pos):
            if click:
                Lvl1.level1()
                print("level1 click")
        if button_2.collidepoint(mouse_pos):
            if click:
                Lvl2.level2()
                pass
        #Draw
        pygame.draw.rect(screen, (255, 0, 0), button_level_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        # Update the screen with what we've drawn.
        pygame.display.flip()
        clock.tick(60)




    

    
   


main_menu()

# Close everything down
pygame.quit()
sys.exit()
    