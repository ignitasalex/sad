from this import d
import pygame
import sys
import key
from player import Player
from enemy import Enemy
from border import Border
from field import Field
from coin import Coin


class Lvl3:
    
    
    def level3():

        # PLAYER
        # Característiques del player per aquest nivell 
        initial_player_pos = [154,472]
        player_size = 25
        player_speed = 3
        #Inicialitzem el player del nivell amb les característiques corresponents 
        player = Player(initial_player_pos, player_size, player_speed)

        # ENEMICS DEL NIVELL
        # Enemic 
        
        enemy1_size= 20   
        initial_enemy_pos0=[420,484]    
        initial_enemy_pos1=[420,484] 
        initial_enemy_pos2=[420,484] 
        initial_enemy_pos3=[420,484] 
        initial_enemy_pos4=[420,484] 
        
        initial_enemy_pos5=[420,484] 
        initial_enemy_pos6=[420,484] 
        initial_enemy_pos7=[420,484] 
        initial_enemy_pos8=[420,484] 
        
        initial_enemy_pos9=[420,484] 
        initial_enemy_pos10=[420,484] 
        initial_enemy_pos11=[420,484] 
        initial_enemy_pos12=[420,484] 
        
        initial_enemy_pos13=[420,484] 
        initial_enemy_pos14=[420,484] 
        initial_enemy_pos15=[420,484] 
        initial_enemy_pos16=[420,484] 

        # Inicialitzem els enemics del nivell
        enemy0 = Enemy(initial_enemy_pos0, enemy1_size, 0)
        
        enemy1 = Enemy(initial_enemy_pos1, enemy1_size, 0)
        enemy2 = Enemy(initial_enemy_pos2, enemy1_size, 0)
        enemy3 = Enemy(initial_enemy_pos3, enemy1_size, 0)
        enemy4 = Enemy(initial_enemy_pos4, enemy1_size, 0)
        
        enemy5 = Enemy(initial_enemy_pos5, enemy1_size, 90)
        enemy6 = Enemy(initial_enemy_pos6, enemy1_size, 90)
        enemy7 = Enemy(initial_enemy_pos7, enemy1_size, 90)
        enemy8 = Enemy(initial_enemy_pos8, enemy1_size, 90)
        
        enemy9 = Enemy(initial_enemy_pos9, enemy1_size, 180)
        enemy10 = Enemy(initial_enemy_pos10, enemy1_size, 180)
        enemy11 = Enemy(initial_enemy_pos11, enemy1_size, 180)
        enemy12 = Enemy(initial_enemy_pos12, enemy1_size, 180)
        
        enemy13 = Enemy(initial_enemy_pos13, enemy1_size, 270)
        enemy14 = Enemy(initial_enemy_pos14, enemy1_size, 270)
        enemy15 = Enemy(initial_enemy_pos15, enemy1_size, 270)
        enemy16 = Enemy(initial_enemy_pos16, enemy1_size, 270)
        # Fem una llista amb tots els enemics del nivell
        enemies = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10,enemy11,enemy12,enemy13,enemy14,enemy15,enemy16,enemy0]
        
        #inicialitzar coin
        coin_pos=[451,593]
        coin = Coin(coin_pos,8,False)
        coins=[coin]

        # Inicialitzem el camp final
        final_field = Field(390, 194 ,70, 80)

        #BORDERS
        # Inicialitzem els BORDES HORITZONTALS
        hborder1 = Border(244,390,46,4,395)
        hborder2 = Border(110,436,135,4,440)
        hborder3 = Border(288,345,48,4,349)
        hborder4 = Border(336,300,47,4,305)
        hborder5 = Border(384,164,95,4,168)
        hborder6 = Border(470,298,47,4,302)
        hborder7 = Border(517,346,47,4,350)
        hborder8 = Border(562,389,47,4,393)
        hborder9 = Border(562,571,47,4,571-player.size)
        hborder10 = Border(517,618,47,4,618-player.size)
        hborder11 = Border(335,664,180,4,664-player.size)
        hborder12 = Border(289,618,47,4,618-player.size)
        hborder13 = Border(244,572,47,4,572-player.size)
        hborder14 = Border(108,527,135,4,527-player.size)
                
        # Fem una llista amb tots els bordes HORITZONTALS del nivell
        horizontal_borders = [hborder1,hborder14,hborder13,hborder12,hborder11,hborder10,hborder9,hborder8,hborder2,hborder3,hborder4,hborder5,hborder6,hborder7]
         

        # Inicialitzem els BORDES VERTICALS 
        vborder1 = Border(243,393,4,47,245)
        vborder2 = Border(105,436,4,95,109)
        vborder3 = Border(287,347,4,45,291)
        vborder4 = Border(332,301,4,45,336)
        vborder5 = Border(379,166,4,135,383)
        vborder6 = Border(470,166,4,135,470-player.size)
        vborder7 = Border(516,301,4,45,516-player.size)
        vborder8 = Border(562,347,4,45,562-player.size)
        vborder9 = Border(607,391,4,180,607-player.size)
        vborder10 = Border(562,574,4,45,562-player.size)
        vborder11 = Border(517,618,4,45,517-player.size)
        vborder12 = Border(334,620,4,45,338)
        vborder13 = Border(288,572,4,45,292)
        vborder14 = Border(240,528,4,45,244)
        
        # Fem una llista amb tots els bordes VERTICALS del nivell        
        vertical_borders = [vborder1,vborder14,vborder13,vborder12,vborder11,vborder10,vborder9,vborder8,vborder2,vborder3,vborder4,vborder5,vborder6,vborder7] 
           

        # Inicialitzem el rellotge per a controlar la velocitat d'actualitzacio de la pantalla
        clock = pygame.time.Clock()

        # Inicialitzem la pantalla
        screen= pygame.display.set_mode((key.WIDTH_LVL2,key.HEIGHT_LVL2))

        # carreguem el fitxer de l'imatge 
        nivell_2=pygame.image.load('images/nivell3.png')
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

            # Printo el mapa del el nivell 3
            screen.blit(nivell_2, (0,0))
            
            
            # Dibuixa el player
            player.draw(screen)
            # Dibuixa els enemics
            enemy0.draw(screen)
            enemy1.draw(screen)
            enemy2.draw(screen)
            enemy3.draw(screen)
            enemy4.draw(screen)
            enemy5.draw(screen)
            enemy6.draw(screen)
            enemy7.draw(screen)
            enemy8.draw(screen)
            enemy9.draw(screen)
            enemy10.draw(screen)
            enemy11.draw(screen)
            enemy12.draw(screen)
            enemy13.draw(screen)
            enemy14.draw(screen)
            enemy15.draw(screen)
            enemy16.draw(screen)
            
            #draw coin
            if not coin.collected:
                coin.draw(screen)             
                      
                      

            # Estableix el text que informa sobre el nombre de morts del player
            deaths_text = font.render("Deaths=  " + str(player.deaths), False, key.BLACK)
            # Printa el text de quantes morts porta el player
            screen.blit(deaths_text, (100, 175))

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
            enemy0.move_circ(430,483,0) 
            enemy1.move_circ(430,483,50) 
            enemy2.move_circ(430,483,82) 
            enemy3.move_circ(430,483,115) 
            enemy4.move_circ(430,483,150) 
            enemy5.move_circ(430,483,50) 
            enemy6.move_circ(430,483,82) 
            enemy7.move_circ(430,483,115) 
            enemy8.move_circ(430,483,150)
            enemy9.move_circ(430,483,50) 
            enemy10.move_circ(430,483,82) 
            enemy11.move_circ(430,483,115) 
            enemy12.move_circ(430,483,150) 
            enemy13.move_circ(430,483,50) 
            enemy14.move_circ(430,483,82) 
            enemy15.move_circ(430,483,115) 
            enemy16.move_circ(430,483,150)  

                
            
            # Detectem si hi ha colisions entre el player i els enemics del nivell 
            if player.detect_collision(enemies) :
                fail_effect.play()
                player.reset([154,472])  # resituem el player a la seva posicio inicial en el nivell  
                coin.collected=False
                
            if player.detect_collision(coins) : 
                coin.collected=True

            if coin.collected:
                return player.win(final_field)  # Comprovem si el player ha guanyat
            return False 
       
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

            # Si s'ha superat el nivell
            if finished :
                win_effect.play()                
                pygame.time.delay(1000) 
                screen= pygame.display.set_mode((key.WIDTH,key.HEIGHT))
                return True  


