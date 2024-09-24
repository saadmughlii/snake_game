#importing shit

import pygame
import time
import random

#spid of snek
snake_speed = 15

#window size
window_y = 720
window_x = 480

#giving colours and shit
black = pygame.Color(0,0,0) #rgb values
white = pygame.Color(255,255,255)
red = pygame.Color (255,0,0)
green = pygame.Color (0,255,0)
blue = pygame.Color (0,0,255)

#intialize the pygame
pygame.init()

#initialize game window
pygame.display.set_caption('snek yay')
game_window = pygame.display.set_mode((window_x,window_y))

#FPS controller
fps = pygame.time.Clock()

#snek default position
snake_position = [100,50]

#defining first 4 blocks of snake
#body
snake_body = [ [100,50], [90,50], [80,50], [70,50] ]

#fruit position
fruit_position = [ random.randrange(1, (window_x//10))*10,
                   random.randrange(1, (window_y//10))*10 ] #this randomly places fruits in range of the window size.
fruit_spawn = True

#default snake direction towards right at spawn
direction = 'RIGHT'
change_to = direction

#initial score
score = 0

def show_score(choice, color, font, size):
  
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the 
    # text surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)