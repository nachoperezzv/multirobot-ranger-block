from aurigapy import *
from lib import *

import pygame, sys

# crear una interfaz

# cuando pulses botón start publicas en los topics que pueden empezar

# Creas un bucle infinito para que cuando recibas un mensaje de que han llegado
# a posicion subas uno en el contador 0/3, 1/3, 2/3, 3/3

# Cuando tengas 3/3

# Mandar mensaje de volver a casa a los robots que estén pulalando por ahí todavia


# Initializing pygame and the window
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Multirobot Ranger")

# Variable for the main loop
DoIt = True

# Setting the buttons 
btn_start   =   Button("START",[40,20], 320, 40, 3, pygame.font.Font(None,40), LIGHT_GREEN, GREEN)
btn_stop    =   Button("STOP", [40,20], 320, 40, 3, pygame.font.Font(None,40), LIGHT_RED, RED)

# Setting the panel
panel       =   pygame.Rect(40,80,320,300)
counter     =   pygame.Rect(50,90,300,280)

mode = 0    # Two modes: 
            #   0 for showing button start - robots are paused
            #   1 for showing button stop - robots are moving

moving = 0  # This is to block the button
            # 0 is not block
            # 1 is block

# How many robots we are going to launch
total_robots    = 3
current_robots  = 0

def set_start():
    global mode
    mode = 0

def set_stop():
    global mode
    mode = 1

def print_counter():
    global total_robots, current_robots, screen
    if total_robots > current_robots:
        color = SUPER_RED
    elif total_robots == current_robots:
        color = SUPER_GREEN
    
    counter_text = pygame.font.Font(DS_DIGI,200).render(str(current_robots) + "/" + str(total_robots),True, color)
    counter_rect = counter_text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))
    screen.blit(counter_text, counter_rect)

while DoIt:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DoIt = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, LIGHT_GREY, panel, 0, 3)
    pygame.draw.rect(screen, GREY, counter, 0, 3)

    if mode == 0:
        btn_start.draw(screen, set_stop)
    elif mode == 1:
        btn_stop.draw(screen, set_start)


    print_counter()



    pygame.display.flip()

pygame.quit()
sys.exit()



