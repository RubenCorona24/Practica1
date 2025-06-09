import pygame
import random
import math
from pygame import mixer

#Inicializar pygame
pygame.init()
#Crar la pantalla
pantalla = pygame.display.set_mode((800,600))
        
#Titulo e ícono
pygame.display.set_caption("Invasión Espacial")
fondo = pygame.image.load('Fondo.jpg')

#agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)


#jugador variables
img_jugador = pygame.image.load("mi_cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#enemigo variables


img_enemigo = []
enemigo_x = []
enemigo_y = [] 
enemigo_x_cambio = []
enemigo_y_cambio = []
numero_enemigos = 8
for e in range(numero_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x .append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

#variables de la bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 10
texto_y = 10

#texto final
fuente_final = pygame.font.Font('freesansbold.ttf',40)
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO",True,(100,150,150))
    pantalla.blit(mi_fuente_final,(60,200))

#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}",True,(255,255,255))
    pantalla.blit(texto,(x,y))

#función jugador
def jugador(x,y):
     pantalla.blit(img_jugador,(x,y))

#Función enemigo
def enemigo(x,y,ene):
     pantalla.blit(img_enemigo[ene],(x,y))

#Función disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x + 16,y + 10))

def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_2-x_1,2) + math.pow(y_2-y_1,2))
    if distancia <27:
        return True
    else:
        return False


#Loop del juego
se_ejecuta = True
while se_ejecuta:

    #Imagen de fondo
    pantalla.blit(fondo,(0,0))

    #iterar eventos
    for event in pygame.event.get():

        #evento cerrar
        if event.type ==  pygame.QUIT:
            se_ejecuta = False
        #evento presionar teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.3
            if event.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)
        #evento soltar flechas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar ubicación del jugador
    jugador_x += jugador_x_cambio

    #Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #modificar ubicación del enemigo
    for e in range(numero_enemigos):

        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(numero_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    #Mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        
            #colision
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)  
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break
        
        enemigo(enemigo_x[e], enemigo_y[e], e)
    #Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala,(bala["x"]+ 16, bala["y"] + 10))
        if bala ["y"] < 0:
            balas.remove(bala)

    


    
    jugador(jugador_x,jugador_y)  
    mostrar_puntaje(texto_x,texto_y)
    #Actualizar
    pygame.display.update()

