import pygame
import key
import sys
from player import Player
from enemy import Enemy
from field import Field
from border import Border

class Lvl1:
    
    
    def level1():
        pygame.init
        #player
        initial_player_pos = [188,442]
        player_size = 25
        player_speed = 4
        player = Player(initial_player_pos, player_size, player_speed)

        #enemy 1
        initial_enemy1_pos=[350,219]
        enemy1_size= 30
        enemy_speed_1= 7
        enemy1 = Enemy(initial_enemy1_pos, enemy1_size, enemy_speed_1)
        #enemy 2
        initial_enemy2_pos=[350,270]
        enemy2_size= 30
        enemy_speed_2= 7
        enemy2 = Enemy(initial_enemy2_pos, enemy2_size, enemy_speed_2*-1)
        #enemy 3
        initial_enemy3_pos=[350,350]
        enemy3_size= 30
        enemy_speed_3= 7
        enemy3 = Enemy(initial_enemy3_pos, enemy3_size, enemy_speed_3)
        
        #Make a list with all the enemies
        enemies= [enemy1, enemy2,enemy3]  #añadimos todos los  enemigos del nivel a la lista


        #BORDERS
        #HORIZONTAL BORDERS
        hborder1 = Border(161,126, 379,4,130)
        hborder2 = Border(161,502,379,4,502-player.size)
        #List of horizontal borders
        horizontal_borders = [hborder1,hborder2] 
        #VERTICAL BORDERS 
        vborder1 = Border(157,130,4,372,161)
        vborder2 = Border(540,130,4,372,540-player.size)       
        #List of vertical borders
        vertical_borders = [vborder1,vborder2] 

        # initial field
        initial_field = Field(161,416, 111, 88, key.GREEN)
        # final Field
        final_field = Field(441, 131 , 101, 75, key.GREEN)

        # To manage how fast the screen updates
        clock = pygame.time.Clock()

        screen= pygame.display.set_mode((key.WIDTH,key.HEIGHT))

        done= False
        finished = False


        #carreguem el fitxer de l'imatge 
        nivell_1=pygame.image.load('images/nivell1.png')
        nivell_1= pygame.transform.scale(nivell_1,(key.WIDTH,key.HEIGHT))
        
        def draw() :
            # Set the screen background
            screen.fill(key.COLOUR)
            #Dibuixo el nivell1
            screen.blit(nivell_1, (0,0))
            #Draw initial field
            initial_field.draw(screen)
            #Draw final field
            final_field.draw(screen)

            #Draw the player
            player.draw(screen)
            #Draw the enemies
            enemy1.draw(screen)
            enemy2.draw(screen)
            enemy3.draw(screen)
            

            '''
            hborder1.draw(screen)
            hborder2.draw(screen)


            vborder1.draw(screen)
            vborder2.draw(screen)

            '''
            # Limit to 60 frames per seconds
            clock.tick(60) 
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
        def update_state() :
            #Mira el estado del teclado
            keys = pygame.key.get_pressed()
            #Move the player
            player.move(keys, horizontal_borders, vertical_borders)

            # Movimiento enemy 1 , 2 ,3
            enemy1.move_horizontal(161, 542 - enemy1.size)
            enemy2.move_horizontal(161, 542 - enemy2.size)
            enemy3.move_horizontal(161, 542 - enemy3.size)
            
            #Detect collisions between player and enemies 
            if player.detect_collision(enemies) :
                player.reset([188,442]) #posiciones x e y inicial del player  

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
            finished= update_state()

            #print(event)

            # Draw
            draw()

            if finished :
                print("YOOOOOOOU WOOOOOOON")
                pygame.time.delay(1000)
                done = True            







  

       
       
        
        


   

    
    