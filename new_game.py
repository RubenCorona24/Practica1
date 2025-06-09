import pygame
import random
import math
from pygame import mixer
import io


#Inicializar pygame
pygame.init()
#Crar la pantalla
pantalla = pygame.display.set_mode((800,600))

#Titulo e ícono
pygame.display.set_caption("Atrapapelotas")
fondo = pygame.image.load('Fondo.jpg')

#agregar música
mixer.music.load('musica_juego.mp3')
mixer.music.play(-1)

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







