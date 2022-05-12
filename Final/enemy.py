import math
import pygame
import key

class Enemy:
    def __init__(self, pos, size, speed):
        self.pos = pos      # self.pos[0] --> x self.pos[1] --> y
        self.size = size    # tamany del enemic
        self.speed = speed  # velocitat del enemic
        self.t=speed        #radians moviment circular

    # Funcio per dibuixar l'enemic
    def draw(self, screen):
        #Dibuixa el borde negre del enemic
        pygame.draw.rect(screen, key.BLACK_BORDER , (self.pos[0], self.pos[1], self.size, self.size))
        #Dibuixa el interior del enemic
        pygame.draw.rect(screen, key.ENEMY_COLOUR , (self.pos[0]+3, self.pos[1]+3, self.size-6, self.size-6))


    # Funcio per a moure el enemic horitzontalment
    def move_horizontal(self, x1, x2) :

        # Mou el enemic hortizontalment
        self.pos[0] += self.speed
        # Si es passa del limit per l'esquerra 
        if self.pos[0] <= x1 :
            self.pos[0] = x1                # Posa la posicio x del enemic el maxima a l' esquerra que pot estar
            self.speed = -1 * self.speed    # Canvia de sentit la velocitat
        # Si es passa del limit per l'esquerra
        elif self.pos[0] >= x2 :
            self.pos[0] = x2                # Posa la posicio x del enemic el maxima a la dreta que pot estar
            self.speed = -1 * self.speed    # Canvia de sentit la velocitat
            
        


    # Funcio per moure el enemic verticalment
    def move_vertical(self, y1, y2) :
        
        # Mou el enemic verticalment
        self.pos[1] += self.speed
        # Si es passa del limit per dalt
        if self.pos[1] <= y1 :
            self.pos[1] = y1            # Posa la posicio y del enemic el maxim amunt que pot estar
            self.pos[1] += self.speed   # Canvia de sentit la velocitat
        # Si es passa del limit per baix
        elif self.pos[1] >= y2 :
            self.pos[1] = y2            # Posa la posicio y del enemic el maxim avall que pot estar
            self.pos[1] += self.speed   # Canvia de sentit la velocitat
            
    
    # Funcio per moure el enemic circularment
    def move_circ(self,a,b,r):
        t=math.radians(self.t)
        self.pos[0] = r * math.cos(t) + a
        self.pos[1] = r * math.sin(t) + b
        self.t += 2
        if self.t >= 360:
            self.t = 0
        
    


        
    