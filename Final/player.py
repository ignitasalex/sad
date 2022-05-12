import pygame
import key
from enemy import Enemy
from border import Border
from field import Field

class Player:

    def __init__(self, initial_pos, size, speed) :
        self.pos = initial_pos  # self.pos[0] --> x self.pos[1] --> y
        self.size = size        #tamany del player
        self.speed = speed      #velocitat del player
        self.deaths = 0         # cops que s'ha mort el player

    #Funcio per moure el player
    def move(self, keys, horizontal_borders, vertical_borders):
        #Si la fletxa esquerra esta clicada
        if keys[pygame.K_LEFT]  :
            self.pos[0] -= self.speed
            self.horizontal_border_collision(vertical_borders)
            
        #Si la fletxa dreta esta clicada
        elif keys[pygame.K_RIGHT] :
            self.pos[0] += self.speed
            self.horizontal_border_collision(vertical_borders)
            
        #Si la fletxa cap amunt esta clicada
        if keys[pygame.K_UP] :
            self.pos[1] -= self.speed
            self.vertical_border_collision(horizontal_borders)
            
        #Si la fletxa cap avall esta clicada
        elif keys[pygame.K_DOWN] :
            self.pos[1] += self.speed
            self.vertical_border_collision(horizontal_borders)
            
    #Funcio per detectar les colisions amb els bordes horitzontals
    def vertical_border_collision(self, horizontal_borders):
        #Rectangle del player
        pl= pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))  

        #Per cada borde horitzontal del nivell 
        for border in horizontal_borders :
            if pl.colliderect(border.rect):     #Mirem si el player colisiona amb el borde --> voldra dir que el player s'ha sortit dels bordes horitzontals del nivell
                print('Collison vertical detected')
                self.pos[1] = border.limit      #Posem la posició y del player altre cop dins del mapa del nivell just a la vora del borde

    #Function to detect collision with vertical borders of the level
    def horizontal_border_collision(self, vertical_borders):
        #Rectangle del player
        pl= pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))  

        #Per cada borde vertical del nivell 
        for border in vertical_borders :
            if pl.colliderect(border.rect):     #Mirem si el player colisiona amb el borde --> voldra dir que el player s'ha sortit dels bordes verticals del nivell
                print('Collison horizontal detected')
                self.pos[0] = border.limit      #Posem la posició x del player altre cop dins del mapa del nivell just a la vora del borde


    #Funccio per a dibuixar el player
    def draw(self, screen):        
        #Dibuixem el borde negre 
        pygame.draw.rect(screen, key.PLAYER_BORDER , (self.pos[0], self.pos[1], self.size, self.size))    
        #Dibuixem el quadrat vermell interior   
        pygame.draw.rect(screen, key.RED_PLAYER , (self.pos[0]+3, self.pos[1]+3, self.size-6, self.size-6))
    
    # Funcio per detectar colisions amb els enemics
    def detect_collision(self, enemies_list):
        # Rectangle del player
        pl= pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))  

        #Per tots els enemics del nivell comprovem si tenim colisio
        for enemy in enemies_list :
            # Rectangle del player
            en = pygame.Rect(enemy.pos[0], enemy.pos[1], enemy.size , enemy.size)

            # Comprovem si el player i el enemic colisiona
            if pl.colliderect(en) :
                self.deaths += 1    # Sumem 1 a les vegades que el player ha mort
                return True         # Hi ha colisio


        #Si no  hi ha colisio retornem false           
        return False

    #Funcio per a comprovar si el jugador ha superat el nivell
    def win(self, final_field):
        #Rectangle del player
        pl= pygame.Rect((self.pos[0], self.pos[1], self.size, self.size))
        
        
        return final_field.rect.contains(pl)    #Retorna True si el player esta dins del camp final, False si no
        
        
    #Funcio per a retornar el player a la posicio inicial quan colisiona amb un enemic
    def reset(self, initial_pos) :
        self.pos = initial_pos


    
