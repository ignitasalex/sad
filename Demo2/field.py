import pygame
import key

class Field :
    def __init__(self, x, y , width , height , colour) :
        self.rect = pygame.Rect(x,y,width,height)
        self.colour = colour
        
    def draw(self,screen) :
        pygame.draw.rect(screen, self.colour , self.rect)

    