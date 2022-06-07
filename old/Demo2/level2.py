import pygame
import sys
import key
from player import Player
from enemy import Enemy
from border import Border
from field import Field


class Lvl2:
    
    
    def level2():
        pygame.init
        #lvl size
        WIDTH=819
        HEIGHT=819
        #player
        initial_player_pos = [63,300]
        player_size = 25
        player_speed = 4
        player = Player(initial_player_pos, player_size, player_speed)

        #enemy 1
        initial_enemy1_pos=[181,326]
        enemy1_size= 30
        enemy_speed_1= 4
        enemy1 = Enemy(initial_enemy1_pos, enemy1_size, enemy_speed_1)
        #enemy 2
        initial_enemy2_pos=[610,365]
        enemy2_size= 30
        enemy_speed_2= 4
        enemy2 = Enemy(initial_enemy2_pos, enemy2_size, enemy_speed_2*-1)
        #enemy 3
        initial_enemy3_pos=[181,405]
        enemy3_size= 30
        enemy_speed_3= 4
        enemy3 = Enemy(initial_enemy3_pos, enemy3_size, enemy_speed_3)
        
        #enemy 4
        initial_enemy4_pos=[610,445]
        enemy4_size= 30
        enemy_speed_4= 4
        enemy4 = Enemy(initial_enemy4_pos, enemy4_size, enemy_speed_4)

        #Make a list of all the enemies of the level
        enemies = [enemy1, enemy2, enemy3, enemy4]

        #Final Field
        final_field = Field(660, 280 ,125, 236, key.BLUE)

        #HORIZONTAL BORDERS 
        hborder1 = Border(16,276,123,4,280)
        hborder2 = Border(16,516,208,4,516-player.size)
        hborder3 = Border(139,476,50,4,480)
        hborder4 = Border(189,313,388,4,317)
        hborder5 = Border(224,480,390,4,480-player.size)
        hborder6 = Border(614,317,46,4,317-player.size)
        hborder7 = Border(577,276,208,4,280)
        hborder8 = Border(660,516,125,4,516-player.size)
        #List of horizontal borders
        horizontal_borders = [hborder1,hborder2, hborder3, hborder4, hborder5, hborder6, hborder7, hborder8 ] 

        #VERTICAL BORDERS 
        vborder1 = Border(12,280,4,236,16)
        vborder2 = Border(139,280,4,200,139-player.size)
        vborder3 = Border(224,480,4,36,224-player.size)
        vborder4 = Border(185,319,4 ,161,189)
        vborder5 = Border(614,319,4,161,614-player.size)
        vborder6 = Border(573,280,4,36,577)
        vborder7 = Border(656,319,4,197,660)
        vborder8 = Border(785,280,4,236,785-player_size)
        #List of vertical borders
        vertical_borders = [vborder1,vborder2, vborder3, vborder4, vborder5, vborder6, vborder7, vborder8 ] 
           

        # To manage how fast the screen updates
        clock = pygame.time.Clock()

        #inicilaizamos la pantalla
        screen= pygame.display.set_mode((WIDTH,HEIGHT))


        done= False
        finished = False

        #carreguem el fitxer de l'imatge 
        nivell_1=pygame.image.load('images/nivell2.png')
        nivell_1= pygame.transform.scale(nivell_1,(WIDTH,HEIGHT))
        
        def draw() :
            # Set the screen background
            screen.fill(key.COLOUR)
            #Dibuixo el nivell1
            screen.blit(nivell_1, (0,0))
            

            #Draw the player
            player.draw(screen)
            #Draw the enemies
            enemy1.draw(screen)
            enemy2.draw(screen)
            enemy3.draw(screen)
            enemy4.draw(screen)

            #Draw the borders
            '''
            hborder1.draw(screen)
            hborder2.draw(screen)
            hborder3.draw(screen)
            hborder4.draw(screen)
            hborder5.draw(screen)
            hborder6.draw(screen)
            hborder7.draw(screen)
            hborder8.draw(screen)

            vborder1.draw(screen)
            vborder2.draw(screen)
            vborder3.draw(screen)
            vborder4.draw(screen)
            vborder5.draw(screen)
            vborder6.draw(screen)
            vborder7.draw(screen)
            vborder8.draw(screen)'''
            

            # Limit to 60 frames per seconds
            clock.tick(60) 
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
        def update_state() :

            #Mira el estado del teclado
            keys = pygame.key.get_pressed()
            #Move the player
            player.move(keys, horizontal_borders, vertical_borders)
             
            # Movimiento enemy 1 , 2 , 3 ,4 
            enemy1.move_horizontal(185, 610 - enemy1.size)
            enemy2.move_horizontal(185, 610 - enemy2.size)
            enemy3.move_horizontal(185, 610 - enemy3.size)
            enemy4.move_horizontal(185, 610 - enemy4.size)   

                
            
            #Detect collisions between player and enemies
            if player.detect_collision(enemies) :
                player.reset([63,300]) #posiciones x e y inicial del player  

            #return final_field.rect.contains(pygame.Rect(player.pos[0], player.pos[1], player.size, player.size))  
            return player.win(final_field)
             

        

                
        
    # -------- Main Program Loop -----------
        while not done:

            # --- Event Processing
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: #si letra a
                        done = True
            
            # Logic
            finished = update_state()

            ##print(event)

            # Draw
            draw()
            


            if finished :
                print("YOOOOOOOU WOOOOOOON")
                pygame.time.delay(1000)
                done = True


