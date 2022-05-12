import pygame
import sys
import key
from player import Player
from enemy import Enemy
from border import Border
from field import Field


class Lvl2:
    
    
    def level2():

        # PLAYER
        # Característiques del player per aquest nivell 
        initial_player_pos = [63,300]
        player_size = 25
        player_speed = 2
        #Inicialitzem el player del nivell amb les característiques corresponents 
        player = Player(initial_player_pos, player_size, player_speed)

        # ENEMICS DEL NIVELL
        # Enemic 1
        initial_enemy1_pos=[181,326]
        enemy1_size= 20
        enemy_speed_1= 5        
        # Enemic 2
        initial_enemy2_pos=[610,365]
        enemy2_size= 20
        enemy_speed_2= 5
        # Enemic 3
        initial_enemy3_pos=[181,405]
        enemy3_size= 20
        enemy_speed_3= 5
        # Enemic 4
        initial_enemy4_pos=[610,445]
        enemy4_size= 20
        enemy_speed_4= 5
        # Inicialitzem els enemics del nivell
        enemy1 = Enemy(initial_enemy1_pos, enemy1_size, enemy_speed_1)
        enemy2 = Enemy(initial_enemy2_pos, enemy2_size, enemy_speed_2*-1)
        enemy3 = Enemy(initial_enemy3_pos, enemy3_size, enemy_speed_3)
        enemy4 = Enemy(initial_enemy4_pos, enemy4_size, enemy_speed_4)
        # Fem una llista amb tots els enemics del nivell
        enemies = [enemy1, enemy2, enemy3, enemy4]

        # Inicialitzem el camp final
        final_field = Field(680, 330 ,80, 180)

        #BORDERS
        # Inicialitzem els BORDES HORITZONTALS
        hborder1 = Border(16,276,124,4,280)
        hborder2 = Border(16,517,208,4,517-player.size)
        hborder3 = Border(140,476,49,4,480)
        hborder4 = Border(189,315,387,4,319)
        hborder5 = Border(225,478,390,4,478-player.size)
        hborder6 = Border(614,317,46,4,317-player.size)
        hborder7 = Border(577,276,208,4,280)
        hborder8 = Border(660,516,125,4,516-player.size)
        # Fem una llista amb tots els bordes HORITZONTALS del nivell
        horizontal_borders = [hborder1,hborder2, hborder3, hborder4, hborder5, hborder6, hborder7, hborder8 ] 

        # Inicialitzem els BORDES VERTICALS 
        vborder1 = Border(12,280,4,236,16)
        vborder2 = Border(140,280,4,200,140-player.size)
        vborder3 = Border(225,480,4,36,225-player.size)
        vborder4 = Border(185,319,4 ,161,189)
        vborder5 = Border(614,319,4,161,614-player.size)
        vborder6 = Border(572,280,4,36,576)
        vborder7 = Border(656,319,4,197,660)
        vborder8 = Border(785,280,4,236,785-player_size)
        # Fem una llista amb tots els bordes VERTICALS del nivell
        vertical_borders = [vborder1,vborder2, vborder3, vborder4, vborder5, vborder6, vborder7, vborder8 ] 
           

        # Inicialitzem el rellotge per a controlar la velocitat d'actualitzacio de la pantalla
        clock = pygame.time.Clock()

        # Inicialitzem la pantalla
        screen= pygame.display.set_mode((key.WIDTH_LVL2,key.HEIGHT_LVL2))

        # carreguem el fitxer de l'imatge 
        nivell_2=pygame.image.load('images/nivell2.png')
        # L'escalem per al tamany de la pantalla
        nivell_2= pygame.transform.scale(nivell_2,(key.WIDTH_LVL2,key.WIDTH_LVL2))

 
        # SOUND
        # Carreguem el efecte sonor de xocar amb un enemic
        fail_effect = pygame.mixer.Sound('sound/fail_effect.wav')
        # Carreguem el efecte sonor de superar el nivell
        win_effect = pygame.mixer.Sound('sound/win_effect.wav')

        # Font 
        # Carreguem la font amb la que escriurem per la pantalla
        font = pygame.font.Font('fonts/fuente.ttf', 30) 

        # True si s'ha de sortir del nivell, False si no
        done= False
        # Boolean per saber si s' ha completat el nivell
        finished = False

        # Funcio per dibuixar el nivell 
        def draw() :

            # Printo el mapa del el nivell 2
            screen.blit(nivell_2, (0,0))
            

            # Dibuixa el player
            player.draw(screen)
            # Dibuixa els enemics
            enemy1.draw(screen)
            enemy2.draw(screen)
            enemy3.draw(screen)
            enemy4.draw(screen)            
           

            # Estableix el text que informa sobre el nombre de morts del player
            deaths_text = font.render("Deaths= " + str(player.deaths), True, key.BLACK)
            # Printa el text de quantes morts porta el player
            screen.blit(deaths_text, (270, 175))

            # Dibuixem aqui els bordes si estem fent proves com a dissenyador del joc
            
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
            enemy1.move_horizontal(185, 610 - enemy1.size)
            enemy2.move_horizontal(185, 610 - enemy2.size)
            enemy3.move_horizontal(185, 610 - enemy3.size)
            enemy4.move_horizontal(185, 610 - enemy4.size)   

                
            
            # Detectem si hi ha colisions entre el player i els enemics del nivell 
            if player.detect_collision(enemies) :
                fail_effect.play()
                player.reset([63,300])  # resituem el player a la seva posicio inicial en el nivell   

            return player.win(final_field)  # Comprovem si el player ha guanyat
             
       
        # LOOP del nivell 1, fins que no s'hagi de sortir del nivell
        while not done:

            # Processem els possibles events que poden succeir
            for event in pygame.event.get():
                # Si el usuari tanca la pestanya
                if event.type == pygame.QUIT:
                    pygame.quit    # tanquem pygame
                    sys.exit()     # sortim
                # Si el usuari clica un boto del teclat
                if event.type == pygame.KEYDOWN:
                    # Si el boto es el escape
                    if event.key == pygame.K_ESCAPE:  
                        done=True
                    # Si el boto es la lletra a
                    if event.key == pygame.K_a: 
                        done = True     # sortim del nivell
            
            # Actualitza l'estat del nivell actualitza si s'ha completat el nivell
            finished = update_state()

            # Dibuixa el nivell
            draw()

            print(event)

            # Si s'ha superat el nivell
            if finished :
                win_effect.play()                
                pygame.time.delay(1000)                
                screen= pygame.display.set_mode((key.WIDTH,key.HEIGHT))  
                return True


