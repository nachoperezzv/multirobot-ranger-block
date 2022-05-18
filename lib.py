import pygame
import os 

# Directory Name
DIR_PATH    = os.path.dirname(os.path.abspath(__file__)) 
FONTS_PATH  = DIR_PATH + "/fonts/ds_digital/"

DS_DIGI     = FONTS_PATH + "DS-DIGI.ttf"

# Window sizes
WINDOW_SIZE = [400,400]

# Colors
BLACK       = [0,0,0]
SUPER_GREEN = [100,255,100]
GREEN       = [150,250,150]
LIGHT_GREEN = [200,255,200]
SUPER_RED   = [255,100,100]
RED         = [250,150,150]
LIGHT_RED   = [255,200,200]
GREY        = [180,180,180]
LIGHT_GREY  = [200,200,200]



class Button:
    def __init__(self,text,pos,width,height,elevation,font, color_on, color_off):
    #Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        self.color_on = color_on
        self.color_off = color_off

        # top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = self.color_off

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
        #text
        self.text_surf = font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen, function):
    # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 6)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 6)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click(function)

    def check_click(self, function):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.color_on
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    function()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = self.color_off
        
    def get_Rect(self):
        return self.top_rect
 