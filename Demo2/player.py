import pygame
import key
from enemy import Enemy
from border import Border
from field import Field

class Player:
    def __init__(self, initial_pos, size, speed) :
        self.pos = initial_pos
        self.size = size
        self.speed = speed
        self.deaths = 0

    # Function to move the player
    def move(self, keys, horizontal_borders, vertical_borders):
        #x = self.pos[0]
        #y = self.pos[1]

        if keys[pygame.K_LEFT]  :
            self.pos[0] -= self.speed
            self.horizontal_border_collision(vertical_borders)
            

        elif keys[pygame.K_RIGHT] :
            self.pos[0] += self.speed
            self.horizontal_border_collision(vertical_borders)
            

        if keys[pygame.K_UP] :
            self.pos[1] -= self.speed
            self.vertical_border_collision(horizontal_borders)
            

        elif keys[pygame.K_DOWN] :
            self.pos[1] += self.speed
            self.vertical_border_collision(horizontal_borders)
            


        #pygame.event.pump()


    
    def vertical_border_collision(self, horizontal_borders):
        #Rectangulo del player
        pl= pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))  

        for border in horizontal_borders :
            if pl.colliderect(border.rect):
                print('Collison vertical detected')
                self.pos[1] = border.limit

    def horizontal_border_collision(self, vertical_borders):
        #Rectangulo del player
        pl= pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))  

        for border in vertical_borders :
            if pl.colliderect(border.rect):
                print('Collison horizontal detected')
                self.pos[0] = border.limit


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

    def win(self, final_field):
        #Rectangulo del player
        pl= pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))
        
        return final_field.rect.contains(pl)
        
        

    def reset(self, initial_pos) :
        self.pos = initial_pos


    
