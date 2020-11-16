import pygame 
import neat 
import os 
import time 
import random 
import keyboard

# Window size
WIN_HIGHT = 600 
WIN_WIDTH = 400

# loading image
bg_img = pygame.image.load(os.path.join("imgs","bg.png"))
bg_img = pygame.transform.scale(bg_img, (WIN_HIGHT, WIN_WIDTH)) # resize the image to the size of the window
gameDisplay = pygame.display.set_mode((WIN_HIGHT,WIN_WIDTH))
pygame.display.set_caption("DEEP_R_BG")

gameDisplay.blit(bg_img, (0, 0)) 
pygame.display.update()

# window close if q is pressed or if x is click on
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keyboard.is_pressed('q'):
            running = False
            pygame.quit()
            exit()
      
            