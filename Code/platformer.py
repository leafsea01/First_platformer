
import pygame
from pygame.locals import *
pygame.init()


clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption('Hello there')
width,height = 1920,1080
window = pygame.display.set_mode((width,height))


tile_size = 80
number_tile_y = (width/tile_size) + 1
number_tile_x = (height/tile_size) + 1



#load images
bg_img = pygame.image.load('../Bilder/bg.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))
grass_img = pygame.image.load('../Bilder/grass.png')
knight_img = pygame.image.load('../Bilder/knight.png')
knight_img = pygame.transform.scale(knight_img,(tile_size,0.833*tile_size))




#define colours
white = (255, 255, 255)
green = (144, 201, 120)



def draw_grid():
	for c in range(int(number_tile_y)):
		#vertical lines
		pygame.draw.line(window, white, (c * tile_size, 0), (c * tile_size, height))


	for c in range(int(number_tile_x)):
	
		#horizontal lines
		pygame.draw.line(window, white, (0, c * tile_size), (width, c * tile_size))

#main game loop
runing = True
while runing:


    clock.tick(fps)


    
    #draw background
    window.blit(bg_img,(0,0))
    
    
    draw_grid()
    window.blit(knight_img,(0,20))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()