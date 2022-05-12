import pygame
import sys
import key

from level1 import Lvl1
from level2 import Lvl2
from level3 import Lvl3

# Inicialitzem pygame
pygame.init
# Inicialitzem el mixer per poder reproduir sons
pygame.mixer.init()
# Inicialitzem font per a poder escriure a la pantalla
pygame.font.init()
# Inicialitzem la pantalla
screen= pygame.display.set_mode((key.WIDTH,key.HEIGHT))
# Inicialitzem el rellotge per a controlar la velocitat d'actualitzacio de la pantalla
clock = pygame.time.Clock()
# Carreguem la musica del joc
music = pygame.mixer.music.load('sound/game_music.wav')

current_lvl=0


# Definim la funcio del menu principal
def main_menu():
    #Funcio per controlar si es clica algun nivell
    def update_state():
        next=False
        current_lvl=0
        # Si el mouse esta sobre les coordenades del boto del nivell 1
        if button_level_1.collidepoint(mouse_pos):
            if click:   # Si el boto esquerre del mouse esta clicat
                current_lvl=1

        # Si el mouse esta sobre les coordenades del boto del nivell 2
        if button_level_2.collidepoint(mouse_pos):
            if click:   # Si el boto esquerre del mouse esta clicat
                current_lvl=2
        
        # Si el mouse esta sobre les coordenades del boto del nivell 2
        if button_level_3.collidepoint(mouse_pos):
            if click:   # Si el boto esquerre del mouse esta clicat                
                current_lvl=3
        
        next=False
        if current_lvl==0:
            return
        if current_lvl==1:
            next=Lvl1.level1()
            if next:
                current_lvl+=1
        if current_lvl==2:
            next=Lvl2.level2()
            if next:
                current_lvl+=1
        if current_lvl==3:
            next=Lvl3.level3()
            if next:
                current_lvl=0
        else:
            current_lvl=0
                 
                
    
    
        
                
                

    def draw() :
        # Dibuixem el boto del nivell 1
        pygame.draw.rect(screen, (255, 0, 0), button_level_1)
        # Dibuixem el boto del nivell 2
        pygame.draw.rect(screen, (255, 0, 0), button_level_2)
        # Dibuixem el boto del nivell 3
        pygame.draw.rect(screen, (255, 0, 0), button_level_3)

        # Estableix el text de menu principal
        title = title_font.render("MAIN MENU", True, key.BLACK)
        # Printa el text de MAIN MENU
        screen.blit(title, (220,64))
        # Estableix el text dels nivells
        level1_title = level_font.render("LEVEL 1", True, key.BLACK)
        level2_title = level_font.render("LEVEL 2", True, key.BLACK)
        level3_title = level_font.render("LEVEL 3", True, key.BLACK)
        # Printa a la pantalla el text dels nivells
        screen.blit(level1_title, (150,285))
        screen.blit(level2_title, (550,285))
        screen.blit(level3_title, (150,385))

        # Actualitza la pantalla amb el que s'ha dibuixat 
        pygame.display.flip()
 
    # Font 
    # Carreguem la font amb la que escriurem per la pantalla
    title_font = pygame.font.Font('fonts/fuente.ttf', 60) 
    level_font = pygame.font.Font('fonts/fuente.ttf', 20) 
        
    while True:
        # Omplim el background del menu amb el color desitjat
        screen.fill(key.COLOUR)

        # Obtenim la posicio del mous
        mouse_pos = pygame.mouse.get_pos()

        #Creem els rectangles que utilitzarem com a botons
        button_level_1 = pygame.Rect(100, 270, 200, 50)
        button_level_2 = pygame.Rect(492, 270, 200, 50)
        button_level_3 = pygame.Rect(100, 370, 200, 50)

    
        click = False   #boolean que controla si el botó esquerre del mouse esta clicat

        # Processem els possibles events que poden succeir
        for event in pygame.event.get():
            # Si el usuari tanca la pestanya
            if event.type == pygame.QUIT:
                pygame.quit()   #tanquem pygame
                sys.exit()      #sortim
            
            #Si el usuari clica un boto del teclat
            if event.type == pygame.KEYDOWN:
                # Si el boto es el escape
                if event.key == pygame.K_ESCAPE:  
                    pygame.quit()   #tanquem pygame
                    sys.exit()      #sortim
            #Si el usuari clica un boto del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #si es el boto esquerre
                    click = True
        
        # Actualitza l'estat del menu
        update_state()
        # Dibuixa el menu
        draw()
        
        # Limita a 60 fps
        clock.tick(60)

# Posem a reproduir la musica del joc
pygame.mixer.music.play(-1) 
# Executem menu principal
main_menu()

    