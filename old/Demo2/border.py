import pygame
import key

class Border:
    def __init__(self, x, y, width ,length,  limit):
        self.rect = pygame.Rect(x, y, width, length)
        self.limit = limit

    #Function to draw the border
    def draw(self, screen):
        pygame.draw.rect(screen, key.BLUE, self.rect)