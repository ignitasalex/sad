import pygame

import key
from player import Player
from enemy import Enemy


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

        

        # To manage how fast the screen updates
        clock = pygame.time.Clock()

        screen= pygame.display.set_mode((WIDTH,HEIGHT))

        done= False
        death=False

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
            

            # Limit to 60 frames per seconds
            clock.tick(60) 
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
        def update_state() :
            #Mira el estado del teclado
            keys = pygame.key.get_pressed()
            #Move the player
            pos_update = player.move(keys)
            new_pos = player_move_border_col(pos_update)
            player.move_border(new_pos)
             

            # Movimiento enemy 1 , 2 ,3
            enemy1.move_horizontal(185, 610 - enemy1.size)
            enemy2.move_horizontal(185, 610 - enemy2.size)
            enemy3.move_horizontal(185, 610 - enemy3.size)
            enemy4.move_horizontal(185, 610 - enemy4.size)

            

            #Detect collisions between player and enemies
            enemies= [enemy1, enemy2, enemy3, enemy4]  #añadimos todos los  enemigos del nivel a la lista
            if player.detect_collision(enemies) :
                player.reset([63,300]) #posiciones x e y inicial del player  
                
        def player_move_border_col(pos): 
            #esquema limits mapa 
            x=pos[0]
            y=pos[1] 
            #left border         
            if x<16:
                x=16
            #spawn verde
            if x>15 and x<122 and y<480:
                if y<280:
                    y=280
                    
                if x>115:
                    x=115
                return x,y
            if x>15 and x<122 and y>480:
                if y>492:
                    y=492
                if x<16:
                    x=16
                
                return x,y
            #pasillo spawn campo        
                
            
            
            new_pos=[x,y]
            return new_pos
        
    # -------- Main Program Loop -----------
        while not done:

            # --- Event Processing
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            # Logic
            update_state()

            print(event)

            # Draw
            draw()

        

