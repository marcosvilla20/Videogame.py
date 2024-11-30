import pygame
from juego.Constantes import *
from juego.Funciones import *

pygame.init()

cuadro_texto = {}
cuadro_texto["superficie"] = pygame.surface(CUADRO_TEXTO)
cuadro_texto["rectangulo"] = cuadro_texto["superficie"].get_rect()
cuadro_texto["superficie"].fill(COLOR_AZUL)
nombre = ""

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],dato):
    global nombre
    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
           retorno = "salir"
        
    pantalla.fill(COLOR_BLANCO)
    cuadro_texto["rectangulo"] = pantalla.blit(cuadro_texto["superficie"],)

