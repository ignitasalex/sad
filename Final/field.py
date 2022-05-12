import pygame
import key

class Field :
    def __init__(self, x, y , width , height) :
        self.rect = pygame.Rect(x,y,width,height) # Rectangle del camp 

    # Funcio per a dibuixar el camp a la pantalla
    def draw(self,screen) :
        pygame.draw.rect(screen, key.FIELD_COLOUR , self.rect)

    