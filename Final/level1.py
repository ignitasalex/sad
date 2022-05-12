import pygame
import key
import sys
from player import Player
from enemy import Enemy
from field import Field
from border import Border

class Lvl1:
    
    
    def level1():

        # PLAYER
        # Característiques del player per aquest nivell 
        initial_player_pos = [188,442] 
        player_size = 25
        player_speed = 2
        #Inicialitzem el player del nivell amb les característiques corresponents 
        player = Player(initial_player_pos, player_size, player_speed)

        # ENEMICS DEL NIVELL
        # Enemic 1
        initial_enemy1_pos=[350,219]
        enemy1_size= 20
        enemy_speed_1= 5
        # Enemic 2
        initial_enemy2_pos=[350,270]
        enemy2_size= 20
        enemy_speed_2= 5
        # Enemic 3
        initial_enemy3_pos=[350,350]
        enemy3_size= 20
        enemy_speed_3= 5

        # Inicialitzem els enemics del nivell
        enemy1 = Enemy(initial_enemy1_pos, enemy1_size, enemy_speed_1)
        enemy2 = Enemy(initial_enemy2_pos, enemy2_size, enemy_speed_2*-1)
        enemy3 = Enemy(initial_enemy3_pos, enemy3_size, enemy_speed_3)
        # Fem una llista amb tots els enemics del nivell
        enemies= [enemy1, enemy2,enemy3]  

        #BORDERS
        # Inicialitzem els BORDES HORITZONTALS
        hborder1 = Border(161,127, 379,4,131)
        hborder2 = Border(161,504,379,4,504-player.size)
        # Fem una llista amb tots els bordes horitzontals del nivell
        horizontal_borders = [hborder1,hborder2] 

        # Inicialitzem els BORDES VERTICALS 
        vborder1 = Border(157,130,4,372,161)
        vborder2 = Border(542,130,4,372,542-player.size)       
        # Fem una llista amb tots els bordes verticals del nivell
        vertical_borders = [vborder1,vborder2] 

        # Inicialitzem el camp inicial
        initial_field = Field(161,416, 111, 88)
        # Inicialitzem el camp final
        final_field = Field(441, 131 , 101, 75)

        # Inicialitzem el rellotge per a controlar la velocitat d'actualitzacio de la pantalla
        clock = pygame.time.Clock()

        # Inicialitzem la pantalla
        screen= pygame.display.set_mode((key.WIDTH,key.HEIGHT))

        # SOUND
        # Carreguem el efecte sonor de xocar amb un enemic
        fail_effect = pygame.mixer.Sound('sound/fail_effect.wav')
        # Carreguem el efecte sonor de superar el nivell
        win_effect = pygame.mixer.Sound('sound/win_effect.wav')

        #carreguem el fitxer de l'imatge 
        #nivell_1=pygame.image.load('images/nivell1.png')
        #nivell_1= pygame.transform.scale(nivell_1,(key.WIDTH,key.HEIGHT))

        # Font 
        # Carreguem la font amb la que escriurem per la pantalla
        font = pygame.font.Font('fonts/fuente.ttf', 30) 
        

        # True si s'ha de sortir del nivell, False si no
        done= False
        # Boolean per saber si s' ha completat el nivell
        finished = False

        # Funcio per dibuixar el nivell
        def draw() :
            # Estableix el color del background
            screen.fill(key.COLOUR)
            
            #Dibuixo el nivell1
            #screen.blit(nivell_1, (0,0))

            # Dibuixa el mapa del nivell
            pygame.draw.rect(screen, key.WHITE, (161 , 131 , 381, 373 ) )            
            
            # Dibuixa el camp inicial 
            initial_field.draw(screen)
            # Dibuixa el camp final 
            final_field.draw(screen)
            # Dibuixa el player
            player.draw(screen)
            # Dibuixa els enemics
            enemy1.draw(screen)
            enemy2.draw(screen)
            enemy3.draw(screen)
            
            # Estableix el text que informa sobre el nombre de morts del player
            deaths_text = font.render("Deaths= " + str(player.deaths), True, key.BLACK)
            # Printa el text de quantes morts porta el player
            screen.blit(deaths_text, (251,64))

            # Actualitza la pantalla amb el que s'ha dibuixat 
            pygame.display.flip()
            # Limita a 60 fps
            clock.tick(60) 
            
        # Funcio per a actualitzar l'estat del nivell
        def update_state() :
            # Mira el estat del teclat
            keys = pygame.key.get_pressed()

            # Mou el jugador
            player.move(keys, horizontal_borders, vertical_borders)

            # Moviment dels enemics del nivell 
            enemy1.move_horizontal(161, 542 - enemy1.size)
            enemy2.move_horizontal(161, 542 - enemy2.size)
            enemy3.move_horizontal(161, 542 - enemy3.size)
            enemy2.move_vertical(161, 450- enemy2.size )
            
            # Detectem si hi ha colisions entre el player i els enemics del nivell 
            if player.detect_collision(enemies) :
                fail_effect.play()
                player.reset([188,442])     # resituem el player a la seva posicio inicial en el nivell  

            return player.win(final_field)  # Comprovem si el player ha guanyat
        

        # LOOP del nivell 1, fins que no s'hagi de sortir del nivell
        while not done:

            # Processem els possibles events que poden succeir
            for event in pygame.event.get():
                # Si el usuari tanca la pestanya
                if event.type == pygame.QUIT:
                    pygame.quit     # tanquem pygame
                    sys.exit()      # sortim
                # Si el usuari clica un boto del teclat
                if event.type == pygame.KEYDOWN:
                    # Si el boto es el escape
                    if event.key == pygame.K_ESCAPE:  
                        return False
                    # Si el boto es la lletra a    
                    if event.key == pygame.K_a:
                        done = True     # sortim del nivell

            # Actualitza l'estat del nivell
            finished= update_state()

            # Dibuixa el nivell
            draw()

            print(event)

            # Si s'ha superat el nivell
            if finished :
                win_effect.play()                
                pygame.time.delay(1000)                
                return True          







  

       
       
        
        


   

    
    