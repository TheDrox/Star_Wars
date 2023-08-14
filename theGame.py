# Importing pygame 
import pygame 

#intalizatin pygame 
pygame.init() 

# wowndow slize 

screen_width = 800 
screen_height = 600 

# size variable 
size = (screen_width, screen_height)  

# Title 
pygame.display.set_caption("Sapace Invaders by TheDrox")

# icon
icon = pygame.image.load("images.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode(size) 

running = True

while running: 
    for event  in pygame.event.get(): 
        if event.type == pygame.QUIT: 
         running = False 
