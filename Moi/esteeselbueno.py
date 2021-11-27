import pygame
from pygame.locals import *
 
pygame.init()
 
pantalla = pygame.display.set_mode((800,780),0,32)
imagen = pygame.image.load("Moi\Vacio.jpg")
 
x=10
y=10
i=0

reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed()
 
    if pulsada[K_w]:
        i += 1
    if pulsada[K_s]:
        i -= 1

    if i== 1:
        imagen = pygame.image.load("Moi\Vacio.jpg")
    if i==2:
        imagen = pygame.image.load("Moi\Segunda.jpg")
    if i ==3:
        imagen = pygame.image.load("Moi\Tercera.jpg")
    if i ==4:
        imagen = pygame.image.load("Moi\Cuarta.jpg")
    if i ==5:
        imagen= pygame.image.load("Moi\Quinta.jpg")
    if i ==6:
        imagen= pygame.image.load("Moi\Sexta.jpg")

    reloj.tick(25)
    pantalla.fill((0,0,0))
    pantalla.blit(imagen,(x,y))
    pygame.display.update()