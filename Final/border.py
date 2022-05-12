import pygame
from zmq import XSUB
import key

class Border:
    def __init__(self, x, y, width ,length,  limit):
        self.rect = pygame.Rect(x, y, width, length)    # Rectangle del borde 
        self.limit = limit                              # Posicio de la vora del borde on ha d'anar parar el player si xoca amb aquest borde
        self.x =x
        self.y = y
        self.width=width
        self.length=length

    # Funcio per a dibuixar el borde 
    def draw(self, screen):
        pygame.draw.rect(screen, key.BLUE, self.rect)
        
    def draw(self, screen):
        #Dibuixa el borde negre del enemic
        pygame.draw.rect(screen, key.RED , (self.x, self.y,self.width , self.length))