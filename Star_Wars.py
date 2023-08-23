# importando pygame
import pygame

#inicializar pygame
pygame.init()

#config window
screen= pygame.display.set_mode((800, 600))

#cargar imagen del fondo
imagen = pygame.image.load("fondo gerra galacrica.png")

#cargar imagen de icono
icono = pygame.image.load("icono cool.png")
pygame.display.set_icon(icono)

    #nombre de el juego
pygame.display.set_caption("STAR WARS")

#bala
bala_y = 470
bala_x = 350
bala_img = pygame.image.load("Sin título.png")
bala_x_change = 0
def bala(x, y):
    screen.blit(bala_img, (x, y))

    #player function
player_y = 470
player_x = 350
player_img = pygame.image.load("nave pixel.png")
player_x_change = 0
def player(x, y):
    screen.blit(player_img, (x, y))

        #enemy function
enemy_y = 100
enemy_x = 350
enemy_img = pygame.image.load("enemy_2.png")
enemy_x_change = 0.4
enemy_y_change = 40
def enemy(x, y):
    screen.blit(enemy_img, (x, y))
running = True
#bucle prinsipal
while running:
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            pygame.quit()
        if event1.type == pygame.KEYDOWN:
            if event1.key == pygame.K_LEFT:
                 player_x_change = -0.5
            
            if event1.key == pygame.K_RIGHT:
                 player_x_change = 0.5
            
            if event1.key == pygame.K_SPACE:
                bala(player_x,bala_y)
        
        if event1.type == pygame.KEYUP:
            if event1.key == pygame.K_LEFT:
                 player_x_change = 0
            
            if event1.key == pygame.K_RIGHT:
                 player_x_change = 0
                 
    screen.blit(imagen , (0, 0))
    player_x += player_x_change
    limite_izquierdo = -0.1
    limite_derecho = 750
     # Restringe el movimiento horizontal
    player(player_x,player_y)
    if player_x <= limite_izquierdo:  
        player_x = limite_izquierdo
    
    elif player_x >= limite_derecho:
        player_x = limite_derecho

    player_x_change == limite_izquierdo

    player_x_change == limite_derecho
         

#Restrinccion enemy
    enemy(enemy_x,enemy_y)
    enemy_x += enemy_x_change
    limite_izquierdo = -0.4
    limite_derecho = 730
    if enemy_x <= 0:  
        enemy_x_change = 0.4
        enemy_y += enemy_y_change
    
    elif enemy_x >= 736:
        enemy_x_change = -0.4
        enemy_y += enemy_y_change



    #Actualizar ventana
    pygame.display.flip()
pygame.quit()