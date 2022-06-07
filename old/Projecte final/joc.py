from operator import truediv
import pygame
import sys

pygame.init

WIDTH= 800
HEIGHT=600

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)







#player
player_pos=[300,400]
player_size=25
player_speed= 8

#enemy 1
enemy1_pos=[100,200]
enemy1_size= 40
speed_1= 5
#enemy 2
enemy2_pos=[700,0]
enemy2_size= 30
speed_2= 7

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen= pygame.display.set_mode((WIDTH,HEIGHT))

done= False
death=False

# Function to move the player
def player_move(event, p_pos, p_size, p_speed):

    x = p_pos[0]
    y = p_pos[1]

    if event.key == pygame.K_LEFT:
        x -= p_speed
        if x <0 :
            x=0
    elif event.key == pygame.K_RIGHT:
        x += p_speed 
        if x + p_size > WIDTH:
            x = WIDTH - p_size

    elif event.key == pygame.K_UP:
        y -= p_speed
        if y <0 :
            y=0
    elif event.key == pygame.K_DOWN:
        y += p_speed
        if y + p_size > HEIGHT:
            y = HEIGHT - p_size

    p_pos = [x,y]
    return p_pos



# Function to detect collison
def detect_collision(player_pos, player_size, enemy_pos, enemy_size):
    p_x = player_pos[0]
    p_y = player_pos[1]
    p_size = player_size

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    e_size = enemy_size

    #si el player entra per l'esquerra or el player entra per la dreta
    if ( p_x >= e_x and p_x < (e_x + e_size) ) or ( (p_x + p_size)> e_x and (p_x + p_size) < (e_x + e_size) ):
        # si el player esta dins per baix or el player esta dins per dalt
        if ( p_y < (e_y + e_size) and p_y >= e_y ) or ( (p_y + p_size) > e_y and (p_y + p_size) < (e_y + e_size) ):
            return True

    return False

# Function to move enemies vertically
def vertical_enemy_movement(enemy_pos, enemy_size, enemy_speed) :

    if enemy_pos[1] >= 0 and enemy_pos[1]+enemy_size<= HEIGHT:
        enemy_pos[1] += enemy_speed
        return enemy_pos, enemy_size, enemy_speed
        
    else:
        enemy_speed = enemy_speed*-1
        if enemy_pos[1]<0:
            enemy_pos[1]=0
        elif enemy_pos[1]+enemy_size > HEIGHT:
            enemy_pos[1]= HEIGHT- enemy_size
    return enemy_pos, enemy_size, enemy_speed

# Nivel 1 Tablero de cuadros 800x600
def draw_lvl_1():
    
    # Board
    size = [800,600]
    
    wide_div = int(25)
    hight_div = int(25)
    color = 0
    for i in range(0, size[0], wide_div):
        for j in range(0, 600, hight_div):
            if color % 2 == 0:
                pygame.draw.rect(screen, GREEN, [i, j, wide_div, hight_div], 0)
            else:
                pygame.draw.rect(screen, BLUE, [i, j, wide_div, hight_div], 0)
            color += 1
        color += 1


# -------- Main Program Loop -----------
while not done:

    # --- Event Processing
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        # Movimiento player si el jugador clica un boton
        if event.type== pygame.KEYDOWN:
            player_pos = player_move(event, player_pos, player_size, player_speed )
        

    # Logic

    # Movimiento enemy 1
    enemy1_pos, enemy1_size, speed_1 = vertical_enemy_movement(enemy1_pos, enemy1_size, speed_1)

    # Movimiento enemy 2
    enemy2_pos, enemy2_size, speed_2 = vertical_enemy_movement(enemy2_pos,enemy2_size, speed_2)   



    # Detect collision with enmemy 1
    if detect_collision(player_pos, player_size, enemy1_pos, enemy1_size):
        done=True
    #Detect collision with enemy 2
    if detect_collision(player_pos, player_size, enemy2_pos, enemy2_size):
        done=True    

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)
    
    # Tablero
    draw_lvl_1()

    # Draw the player
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw the enemy1
    pygame.draw.rect(screen, RED, (enemy1_pos[0], enemy1_pos[1], enemy1_size, enemy1_size))

    # Draw the enemy2
    pygame.draw.rect(screen, RED, (enemy2_pos[0], enemy2_pos[1], enemy2_size, enemy2_size))

    # --- Wrap-up
    # Limit to 60 frames per seconds
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()





# Close everything down
pygame.quit()
