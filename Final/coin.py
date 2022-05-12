import pygame
import key

class Coin:
    def __init__(self, pos, size, collected):
        self.pos = pos      # self.pos[0] --> x self.pos[1] --> y
        self.size = size    # tamany del enemic
        self.collected = collected  # recollida
        
    def draw(self, screen):
        #Dibuixa el borde negre del enemic
        pygame.draw.circle(screen, key.BLACK , [self.pos[0], self.pos[1]],self.size,0)
        pygame.draw.circle(screen, key.YELLOW_light , [self.pos[0], self.pos[1]],self.size-2,0)