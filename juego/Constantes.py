import pygame
import os

# Ruta absoluta al directorio del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Ruta al archivo de sonido
SONIDOS_DIR = os.path.join(BASE_DIR,"juego", "sonidos")

pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_AMARILLO = (239,255,0)
COLOR_VERDE_OSCURO = "#0B9827"
COLOR_FUCSIA = (255,0,255)
COLOR_GRIS = (128,128,128)
COLOR_LIMA =(0,255,0)
COLOR_MARRON = (128, 0, 0)
COLOR_DORADO = (255, 215, 0, 255)
COLOR_CELESTE = (0, 191, 255, 255)
COLOR_VERDE_AGUA = (102, 205, 170, 255)
COLOR_AZUL_MARINO = (0, 0, 128, 255)

ANCHO = 500
ALTO = 550
VENTANA = (ANCHO,ALTO)
FPS = 60

TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)


FUENTE_22 = pygame.font.SysFont("britannic",24)
FUENTE_25 = pygame.font.SysFont("britannic",38)
FUENTE_27 = pygame.font.SysFont("Arial",22)
FUENTE_30 = pygame.font.SysFont("Arial",30)
FUENTE_32 = pygame.font.SysFont("Arial",32)
FUENTE_50 = pygame.font.SysFont("Arial",50)


CLICK_SONIDO = pygame.mixer.Sound(os.path.join(SONIDOS_DIR, "click.mp3"))
ACIERTO_SONIDO = pygame.mixer.Sound(os.path.join(SONIDOS_DIR, "click.mp3"))
ERROR_SONIDO = pygame.mixer.Sound(os.path.join(SONIDOS_DIR, "error.mp3"))
ERROR_SONIDO_DOS = pygame.mixer.Sound(os.path.join(SONIDOS_DIR, "Error sound.mp3"))
SONIDO_3_SEG = pygame.mixer.Sound(os.path.join(SONIDOS_DIR, "3 seg.mp3"))
MUSIC_PATH = os.path.join(SONIDOS_DIR, "music.mp3")

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

BOTON_JUGAR = 0
BOTON_AJUSTES = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3