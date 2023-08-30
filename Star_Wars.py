# importando pygame
import pygame
import random
import math

from pygame import mixer

#inicializar pygame
pygame.init()

#config window
screen= pygame.display.set_mode((800, 600))

# background sounds
mixer.music.load("y2mate.com - Imperial march Star Wars La guerra de las galaxias.wav")
mixer.music.play(-1)



#score font
score_font = pygame.font.Font("SuperMario256.ttf", 32)


#varoable score
score = 0

#position tect in screen
text_y = 10
text_x = 10

# Condicion game over 
go_yes = True

#game over font
go_x= 290
go_y = 250
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
bala_y_change = 8
bala_state=True


def bala(x, y):
    global bala_state
    bala_state=False

    screen.blit(bala_img, (x, y))


    #player function
player_y = 470
player_x = 350
player_img = pygame.image.load("nave pixel.png")
player_x_change = 0
def player(x, y):
    screen.blit(player_img, (x, y))

        #enemy function
enemy_y =[]
enemy_x = []
enemy_img = []
enemy_x_change = []
enemy_y_change = []
number_enemy = 15
for item in range(number_enemy):


    enemy_img.append(pygame.image.load("enemy_2.png"))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(50,90))
    enemy_x_change.append(2)
    enemy_y_change.append(40)
def enemy(x, y, item):
    screen.blit(enemy_img [item], (x, y))
running = True
clock = pygame.time.Clock()
#colision
def is_collision (b_x, b_y, e_x, e_y):
    distance = math.sqrt((e_x - b_x)**2 + (e_y - b_y)**2)
    if distance < 27:
        return True
    else:
        return False
#funciones de texto
def game_over (x,y):
 go_text = score_font.render("Game Over",True,(255,0,0))
 screen.blit(go_text, (x,y))

def show_score (x,y):
  score_text = score_font.render("SCORE:   " + str(score),True,(255,255,255))
  screen.blit(score_text, (x,y))

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
            
            if event1.key == pygame.K_SPACE and bala_state == True:
                bala_x = player_x
                #bulet sound
                bala_sound = mixer.Sound("LaserBlastQuick PE1095107 (1).wav")
                bala_sound.play()
        
                bala(player_x, player_y)
        
        if event1.type == pygame.KEYUP:
            if event1.key == pygame.K_LEFT:
                 player_x_change = 0
            
            if event1.key == pygame.K_RIGHT:
                 player_x_change = 0
                 
    screen.blit(imagen , (0, 0))
    #bala moments

    if bala_state == False:
           bala(player_x, bala_y)
           bala_y -= bala_y_change

    if bala_y <= 0:
        bala_y = 480
        bala_state = True
    for item in range (number_enemy):

        if enemy_y[item] > 400 :
          for j in range (number_enemy):
            enemy_y[j] = 2000
          if go_yes :    
            game_over_sound = mixer.Sound("game-over-1-gameover.wav")
            game_over_sound.play(1)
            go_yes = False
          game_over(go_x,go_y)
          break
          
        collision = is_collision (bala_x, bala_y, enemy_x[item], enemy_y[item])
        if collision:
          bala_y=400
          bala_state = True
          score += 50
          collision_sound = mixer.Sound("mi_explosion_03_hpx (1).wav")
          collision_sound.play()
          enemy_x [item] = random.randint(0,200)
          enemy_y [item] = random.randint(0,50)

        enemy_x[item] += enemy_x_change[item]
        limite_izquierdo = -0.3
        limite_derecho = 730
        if enemy_x[item] <= 0:  
            enemy_x_change[item] = 2
            enemy_y[item] += enemy_y_change[item]
        
        elif enemy_x[item] >= 736:
            enemy_x_change[item] = -2
            enemy_y[item] += enemy_y_change[item]
            #enemy blit
        enemy(enemy_x[item], enemy_y[item], item)

    
        
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
         
    #Actualizar ventana

    clock.tick(5000)
    show_score(text_x, text_y)
    pygame.display.flip()
pygame.quit()