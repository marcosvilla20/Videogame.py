import pygame
from juego.Constantes import *
from juego.Funciones import *

pygame.init()

# imagen fondo
fondo_config = pygame.image.load("fondo-config.jpg")
fondo_config = pygame.transform.scale(fondo_config, VENTANA)

# Imagenes botones
mute = pygame.image.load("unmute.png")
mute = pygame.transform.scale(mute, (70,70))
unmute = pygame.image.load("mute.png")
unmute = pygame.transform.scale(unmute, (70,70))

mutear = False

boton_suma = crear_boton(COLOR_VERDE_OSCURO,(70,60),(420,200))
boton_resta = crear_boton(COLOR_VERDE_OSCURO,(70,60),(20,200))
boton_volver = crear_boton(COLOR_AZUL,TAMAÑO_BOTON_VOLVER,(10,10))
boton_mute = crear_boton(COLOR_ROJO, (70, 70), (500, 300))
boton_unmute = crear_boton(COLOR_VERDE, (70, 70), (520, 300))

def subir_volumen(evento,datos_juego):
    CLICK_SONIDO.play()
    if datos_juego["volumen_musica"] < 100:
        datos_juego["volumen_musica"] += 5
    else:
        ERROR_SONIDO_DOS.play()

def bajar_volumen(evento,datos_juego):
    CLICK_SONIDO.play()
    if datos_juego["volumen_musica"] > 0:
        datos_juego["volumen_musica"] -= 5
    else:
        ERROR_SONIDO_DOS.play()

def mutear_volumen(datos_juego):
    global mutear
    CLICK_SONIDO.play()
    datos_juego["volumen_musica"] = 0 
    mutear = True
    CLICK_SONIDO.set_volume(0) 
    ACIERTO_SONIDO.set_volume(0)
    ERROR_SONIDO.set_volume(0)
    SONIDO_3_SEG.set_volume(0)
def desmutear_volumen(datos_juego):
    global mutear  
    CLICK_SONIDO.play()  
    datos_juego["volumen_musica"] = 100
    mutear = False  
    CLICK_SONIDO.set_volume(1)
    ACIERTO_SONIDO.set_volume(1)
    ERROR_SONIDO.set_volume(1) 

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                subir_volumen(evento,datos_juego)
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                bajar_volumen(evento,datos_juego)
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
            elif boton_mute["rectangulo"].collidepoint(evento.pos):
                mutear_volumen(datos_juego)
            elif boton_unmute["rectangulo"].collidepoint(evento.pos):
                desmutear_volumen(datos_juego)

    pantalla.blit(fondo_config,(0,0))
    
    #Rectangulo porcentaje
    pygame.draw.rect(pantalla,COLOR_VERDE_OSCURO,(200,200,140,58))

    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,200))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(420,200))    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_mute["rectangulo"] = pantalla.blit(mute, (20, 122))
    boton_unmute["rectangulo"] = pantalla.blit(unmute, (410, 122))
    
    mouse_pos = pygame.mouse.get_pos()
    bordear_boton(pantalla,boton_suma, COLOR_DORADO, mouse_pos)
    bordear_boton(pantalla,boton_resta, COLOR_DORADO, mouse_pos)
    bordear_boton(pantalla,boton_volver, COLOR_VERDE_AGUA, mouse_pos)
    bordear_boton(pantalla,boton_mute, COLOR_DORADO, mouse_pos)
    bordear_boton(pantalla,boton_unmute, COLOR_DORADO, mouse_pos)

    mostrar_texto(boton_suma["superficie"],"VOL+",(10,15),FUENTE_22,COLOR_AZUL_MARINO)
    mostrar_texto(boton_resta["superficie"],"VOL-",(10,15),FUENTE_22,COLOR_AZUL_MARINO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(220,210),FUENTE_25,COLOR_AZUL_MARINO)
    
    return retorno