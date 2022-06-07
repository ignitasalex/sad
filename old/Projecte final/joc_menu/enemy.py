import pygame
import key

class Enemy:
    def __init__(self, pos, size, speed):
        self.pos = pos
        self.size = size
        self.speed = speed

    #Function to draw an enemy
    def draw(self, screen):
        pygame.draw.rect(screen, key.YELLOW , (self.pos[0], self.pos[1], self.size, self.size))

    # Function to move enemies horizontally
    def move_horizontal(self, x1, x2) :
        if self.pos[0] <= x1 or self.pos[0] >= x2 :
            self.speed = -1 * self.speed
        self.pos[0] += self.speed
        if self.pos[0] < x1 :
            self.pos[0] = x1
        if self.pos[0] > x2 :
            self.pos[0] = x2
            
        


    # Function to move enemies vertically
    def move_vertical(self, y1, y2) :
        if self.pos[1] < y1 or self.pos[1] > y2 :
            self.speed = -1 * self.speed
        self.pos[1] += self.speed

    


        
    