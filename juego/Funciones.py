from juego.Constantes import *
import random
import pygame

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def crear_boton(color,tamaño,posicion)-> dict:
    boton = {}
    boton["superficie"] = pygame.Surface(tamaño)
    boton["rectangulo"] = boton["superficie"].get_rect(topleft=posicion)
    boton["superficie"].fill(color)
    return boton

def bordear_boton(pantalla,boton, color, mouse_pos):
    if boton["rectangulo"].collidepoint(mouse_pos):
        pygame.draw.rect(pantalla, color, boton["rectangulo"], 4) 

# Parameters
# surface (Surface) -- surface to draw on
# color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
# rect (Rect) -- rectangle to draw, position and dimensions
# width (int) --

tiempo_inicial = 0
def manejar_tiempo(pantalla, datos_juego):
    tiempo_inicial

    if tiempo_inicial == 0: 
        tiempo_inicial = pygame.time.get_ticks()
    else:
        tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicial) // 1000
        contador = FUENTE_22.render(f"Tiempo: {tiempo_transcurrido} SEG", True, (120, 70, 0))
        pantalla.blit(contador, (10, 10)) 



def crear_rectangulo(pantalla, color, lista,):
    pygame.draw.rect(pantalla,color,lista["rectangulo"],2)
    pygame.draw.rect(pantalla,color,lista[0]["rectangulo"],2)
    pygame.draw.rect(pantalla,color,lista[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,color,lista[2]["rectangulo"],2)