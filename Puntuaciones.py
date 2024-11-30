import pygame
from juego.Constantes import *
from juego.Funciones import *

pygame.init()

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "puntuaciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.fill(COLOR_BLANCO)
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))

    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"ACA DEBEN MOSTRAR EL TOP 10",(20,200),FUENTE_32,COLOR_NEGRO)

    return retorno