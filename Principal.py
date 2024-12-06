import pygame
from juego.Funciones import *
from juego.Constantes import *
from juego.Menu import *
from juego.Juego import *
from juego.Configuraciones import *
from Puntuaciones import *


pygame.init()
pygame.display.set_caption("JUEGO 314")
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"cantidad_vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":100,"respuestas_correctas_consecutivas": 0}
ventana_actual = "menu"
bandera_juego = False

while corriendo:
    #Gestion de Eventos -> No lo programamos aca
    #Actualizacion de estados -> No lo programamos aca
    #Imprimir en pantalla esa informacion -> No lo programamos aca
    cola_eventos = pygame.event.get()
    reloj.tick(FPS)
        
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            inciializar_juego(datos_juego,bandera_juego,cola_eventos,)
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuracion":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "puntuaciones":
        ventana_actual = mostrar_ranking(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        if datos_juego["nombre"]: 
            guardar_puntaje(datos_juego["nombre"], datos_juego["puntuacion"], "top_10.csv")
        ventana_actual = "menu" 
    elif ventana_actual == "salir":
        corriendo = False
    
    pygame.display.flip()
pygame.quit()
    
    