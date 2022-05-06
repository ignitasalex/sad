import pygame
import sys
import key

from player import Player
from enemy import Enemy
from field import Field

pygame.init

#Inicializamos la pantalla
screen= pygame.display.set_mode((key.WIDTH,key.HEIGHT))
# To manage how fast the screen updates
clock = pygame.time.Clock()

def main_menu():
    while True:
        # Set the screen background
        screen.fill(key.COLOUR)

        mouse_pos = pygame.mouse.get_pos()

        button_level_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

    
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #left button
                    click = True
        
        #Logic
        if button_level_1.collidepoint(mouse_pos):
            if click:
                level1()
        if button_2.collidepoint(mouse_pos):
            if click:
                pass
        #Draw
        pygame.draw.rect(screen, (255, 0, 0), button_level_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        # Update the screen with what we've drawn.
        pygame.display.flip()
        clock.tick(60)


def level1():
    pygame.display.set_caption("Level 1")
    #carreguem el fitxer de l'imatge 
    nivell_1=pygame.image.load('nivell1.png')
    nivell_1= pygame.transform.scale(nivell_1,(key.WIDTH,key.HEIGHT))
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

    # initial field
    initial_field = Field(161,416, 111, 88, key.GREEN)
    # final Field
    final_field = Field(441, 131 , 101, 75, key.GREEN)


    done= False

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

        # Update the screen with what we've drawn.
        pygame.display.flip()


    def update_state() :
        #Mira el estado del teclado
        keys = pygame.key.get_pressed()
        #Move the player
        player.move(keys)

        # Movimiento enemy 1 , 2 ,3
        enemy1.move_horizontal(161, 542 - enemy1.size)
        enemy2.move_horizontal(161, 542 - enemy2.size)
        enemy3.move_horizontal(161, 542 - enemy3.size)
        

        #Detect collisions between player and enemies
        enemies= [enemy1, enemy2,enemy3]  #añadimos todos los  enemigos del nivel a la lista
        if player.detect_collision(enemies) :
            player.reset([188,442]) #posiciones x e y inicial del player 

    # -------- Loop level1 -----------
    while not done:

        # --- Event Processing
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: #si letra a
                    main_menu() #volvemos al menu prinicipal

        # Logic
        update_state()
        # Draw
        draw()
        # Limit to 60 frames per seconds
        clock.tick(60) 


main_menu()

# Close everything down
pygame.quit()
sys.exit()
    