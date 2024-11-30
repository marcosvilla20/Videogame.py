import pygame
from juego.Funciones import *
COLOR_BOTON = (0, 255, 0, 255)
COLOR_TEXTO = (0, 0, 0)

def crear_comodin(pantalla, boton, texto, fuente, activo):
    "funcion que se encarga de dibujar el comodin en la pantalla jugar"
    if activo:
        color = COLOR_BOTON
        pygame.draw.rect(pantalla, color, boton)
        texto_superficie = fuente.render(texto, True, COLOR_TEXTO)
        texto_rect = texto_superficie.get_rect(center=boton.center)
        pantalla.blit(texto_superficie, texto_rect)

    else:
       return False
def comprobar_click(pos, boton_rect, activo):
    "Funcion que verifica si un botón fue presionado."
    if activo and boton_rect.collidepoint(pos):
        return True
    else:
        return False