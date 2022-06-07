import pygame
import key

class Field :
    def __init__(self, x, y , width , length , colour) :
        self.pos = [x,y]
        self.width = width
        self.length = length
        self.colour = colour
        
    def draw(self,screen) :
        pygame.draw.rect(screen, self.colour , (self.pos[0], self.pos[1], self.width, self.length))

    