import pygame
import sys


# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()


# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('1', True, color)

bg_img = pygame.image.load('images/lvlSelector.jfif')
bg_img = pygame.transform.scale(bg_img, (width, height))

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            mouse = pygame.mouse.get_pos()
            
            print('altura %d ancho %d' % (mouse[0], mouse[1]))
            
            

    # fills the screen with a color
    screen.fill((60, 25, 60))
    screen.blit(bg_img,(0,0))
    

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    

    # superimposing the text onto our button
    screen.blit(text, (width/2, height/2))

    # updates the frames of the game
    pygame.display.update()