import pygame
import key
from enemy import Enemy

class Player:
    def __init__(self, initial_pos, size, speed) :
        self.pos = initial_pos
        self.size = size
        self.speed = speed
        self.deaths = 0

    # Function to move the player
    def move(self, keys):
        x = self.pos[0]
        y = self.pos[1]

        if keys[pygame.K_LEFT]  :
            x -= self.speed
            

        elif keys[pygame.K_RIGHT] :
            x += self.speed
            

        if keys[pygame.K_UP] :
            y -= self.speed
            

        elif keys[pygame.K_DOWN] :
            y += self.speed
            


        pygame.event.pump()

        self.pos[0]= x
        self.pos[1]= y
        pos=[x,y]
        return pos
    
    def move_border(self, pos):
        self.pos[0]= pos[0]
        self.pos[1]= pos[1]
            


        

    #Function to draw the player
    def draw(self, screen):
        pygame.draw.rect(screen, key.RED , (self.pos[0], self.pos[1], self.size, self.size))
    
    # Function to detect collison with an enemy
    def detect_collision(self, enemies_list):
        p_x = self.pos[0]
        p_y = self.pos[1]
        p_size = self.size

        for enemy in enemies_list :
            e_x = enemy.pos[0]
            e_y = enemy.pos[1]
            e_size = enemy.size

            #si el player esta dins per l'esquerra or el player entra per la dreta del enemic
            if ( p_x >= e_x and p_x < (e_x + e_size) ) or ( (p_x + p_size)> e_x and (p_x + p_size) < (e_x + e_size) ):
                # si el player esta dins per baix or el player esta dins per dalt del enemic
                if ( p_y < (e_y + e_size) and p_y >= e_y ) or ( (p_y + p_size) > e_y and (p_y + p_size) < (e_y + e_size) ):
                    return True
        #si no xoca amb ningu no hi ha colisio           
        return False

    def reset(self, initial_pos) :
        self.pos = initial_pos


    
