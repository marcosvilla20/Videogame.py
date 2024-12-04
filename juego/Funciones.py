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

def crear_rectangulo(pantalla, color, lista):
    for item in lista:
        pygame.draw.rect(pantalla, color, item["rectangulo"], 2)


def mostrar_game_over(pantalla: pygame.Surface):
    # Configuración de colores
    COLOR_FONDO = (0, 0, 0)  # Negro
    COLOR_TEXTO = (255, 0, 0)  # Rojo

    # Llenar la pantalla con el fondo negro
    pantalla.fill(COLOR_FONDO)

    # Cargar la fuente y definir el texto
    fuente = pygame.font.Font(None, 74)  # Fuente predeterminada, tamaño 74
    texto = fuente.render("GAME OVER", True, COLOR_TEXTO)

    # Obtener el rectángulo del texto para centrarlo
    rect_texto = texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))

    # Dibujar el texto en la pantalla
    pantalla.blit(texto, rect_texto)

    # Actualizar la pantalla
    pygame.display.flip()

    # Pausar por un momento
    pygame.time.delay(2000)  # Pausa de 2 segundos


def pedir_nombre_usuario(ventana: pygame.Surface, fuente: pygame.font.Font, cantidad_respuestas_correctas: int, total: int):
    '''
    ¿Que hace? -> Muestra una pantalla en la que se solicita al usuario ingresar su nombre y muestra su puntaje final.

    ¿Que parametros recibe?
        -ventana:pygame.Surface -> Superficie en la que se dibuja el botón.
        -fuente:pygame.font.Font -> La fuente que se utiliza para renderizar el texto en el botón.
        -cantidad_respuestas_correctas:int -> El número de respuestas correctas del usuario.
        -total:int -> El número total de preguntas o respuestas.

    ¿Que retorna?:str -> El nombre ingresado por el usuario como una cadena de texto.
    '''
    nombre_ingresado = ""
    bandera_pedir_nombre = True

    while bandera_pedir_nombre:

        ventana.fill(COLOR_NEGRO)
        # Mostrar puntaje final
        resultado_texto = fuente.render(
            f"Puntaje final: {cantidad_respuestas_correctas}/{total}", True, COLOR_BLANCO)
        ventana.blit(resultado_texto, (ANCHO // 2 - resultado_texto.get_width(
        ) // 2, (ALTO // 3 - 50)))

        mensaje = fuente.render("Ingrese su nombre:", True, COLOR_AZUL_MARINO)
        ventana.blit(
            mensaje, (ANCHO // 2 - mensaje.get_width() // 2, ALTO // 3))

        nombre_texto = fuente.render(nombre_ingresado, True,COLOR_ROJO)
        ventana.blit(
            nombre_texto, (ANCHO // 2 - nombre_texto.get_width() // 2, ALTO // 2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    bandera_pedir_nombre = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[:-1]
                else:
                    nombre_ingresado += evento.unicode

    return nombre_ingresado