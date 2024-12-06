from juego.Constantes import *
import random
import pygame
import csv
from generar_archivo import lista_preguntas
import os
def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    """
    Renderiza y dibuja texto en una superficie  
    respetando los límites de ancho y ajustando el texto a nuevas líneas si es necesario.
    """
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
    """
    Crea un botón como un diccionario con una superficie y un rectángulo asociado.
    """
    boton = {}
    boton["superficie"] = pygame.Surface(tamaño)
    boton["rectangulo"] = boton["superficie"].get_rect(topleft=posicion)
    boton["superficie"].fill(color)
    return boton

def bordear_boton(pantalla,boton, color, mouse_pos):
    """
    Dibuja un borde alrededor de un botón si el puntero del mouse está sobre él.
    """
    if boton["rectangulo"].collidepoint(mouse_pos):
        pygame.draw.rect(pantalla, color, boton["rectangulo"], 4) 

# Parameters
# surface (Surface) -- surface to draw on
# color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
# rect (Rect) -- rectangle to draw, position and dimensions
# width (int) --

tiempo_inicial = 0
def manejar_tiempo(pantalla, datos_juego):
    """
    Muestra un contador de tiempo en pantalla basado en el tiempo transcurrido desde que la función se llamó por primera vez.
    """
    tiempo_inicial

    if tiempo_inicial == 0: 
        tiempo_inicial = pygame.time.get_ticks()
    else:
        tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicial) // 1000
        contador = FUENTE_22.render(f"Tiempo: {tiempo_transcurrido} SEG", True, (120, 70, 0))
        pantalla.blit(contador, (10, 10)) 

def inciializar_juego(datos_juego,bandera_juego,cola_eventos):
    """
    Inicializa el juego configurando música, volumen, y estableciendo la bandera de inicio.
    """
    porcentaje_coma = datos_juego["volumen_musica"] / 100
    pygame.mixer.init()
    
    MUSIC_PATH = os.path.join(SONIDOS_DIR, "juego/sonidos/music.mp3")
    if not os.path.isfile(MUSIC_PATH):
        print("Error: No se encontró el archivo de música.")
        return
    
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.set_volume(porcentaje_coma)
    pygame.mixer.music.play(-1)  # Reproduce en bucle
    bandera_juego = True

def mostrar_game_over(pantalla):
    """"
    Muestra una pantalla de "Game Over" con una imagen de fondo.
    """
    fondo_game_over = cargar_fondo("juego/imagenes/game-over.jpg", (ANCHO,ALTO))

    pantalla.blit(fondo_game_over, (0,0))

    pygame.display.flip()
    pygame.time.delay(2000)  


def cargar_preguntas(nombre_archivo):
    """""
    Carga las preguntas desde un archivo CSV y las devuelve como una lista de diccionarios.
    """
    preguntas = []
    with open(nombre_archivo, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            preguntas.append({
                "pregunta": row["pregunta"],
                "respuesta_1": row["respuesta_1"],
                "respuesta_2": row["respuesta_2"],
                "respuesta_3": row["respuesta_3"],
                "respuesta_4": row["respuesta_4"], 
                "respuesta_correcta": int(row["respuesta_correcta"])  # Convertimos a entero
            })
    return preguntas

def mezclar_preguntas(lista_preguntas):
    random.shuffle(lista_preguntas)
    return lista_preguntas


def pedir_nombre_usuario(ventana: pygame.Surface, fuente: pygame.font.Font, cantidad_respuestas_correctas: int, total: int):
    '''
    Muestra una pantalla en la que se solicita al usuario ingresar su nombre y muestra su puntaje final
    '''
    nombre_ingresado = ""
    bandera_pedir_nombre = True

    while bandera_pedir_nombre:

        ventana.fill(COLOR_GRIS)
        # Mostrar puntaje final
        resultado_texto = fuente.render(
            f"Puntaje final: {cantidad_respuestas_correctas}", True, COLOR_BLANCO)
        ventana.blit(resultado_texto, (ANCHO // 2 - resultado_texto.get_width(
        ) // 2, (ALTO // 3 - 50)))

        mensaje = fuente.render("Ingrese su nombre: ", True, COLOR_AZUL_MARINO)
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

def convertir_csv_a_lista_diccionarios(path:str) -> list:
    """
    Funcion que recibe la ruta del csv lee sus lineas y las convierte en una lista de diccionarios, 
    entre las cabezeras y cada linea
    """
    lista_diccionarios = []
    
    with open(path, mode='r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        encabezados = lineas[0].strip().split(',') # cabecera
    
        for linea in lineas[1:]:
            valores = linea.strip().split(',')

            for i in range(len(valores)):
                valores[i] = valores[i].strip('"')

            fila_diccionario = dict(zip(encabezados, valores)) # -> devuelve tuplas
            lista_diccionarios.append(fila_diccionario)
    
    return lista_diccionarios

def obtener_puntaje_y_convertir_a_entero(diccionario: dict) -> int:
    '''
    Extrae el valor asociado a la clave 'puntaje' de un diccionario y
    lo convierte a un número entero.
    '''
    puntaje_a_entero = int(diccionario['puntaje'])
    return puntaje_a_entero

def ordenar_lista_diccionarios(lista:list) -> list:
    '''
    Funcion que ordena una lista de diccionarios en orden descendente según el puntaje, 
    convirtiendo dicho valor a entero antes de ordenar.
    sorted -> devuelve una lista ordenada de mayor a menor 
    '''
    lista_ordenada = sorted(lista, key=obtener_puntaje_y_convertir_a_entero, reverse=True) 
    return lista_ordenada

def verificar_respuesta(pantalla, respuesta_usuario, pregunta_correcta, datos_juego, fuente):
    if respuesta_usuario == pregunta_correcta: 
        datos_juego["respuestas_correctas_consecutivas"] += 1
        
        if datos_juego["respuestas_correctas_consecutivas"] == 5:
            datos_juego["cantidad_vidas"] += 1 
            datos_juego["respuestas_correctas_consecutivas"] = 0  

        return True  
    else:  
        datos_juego["respuestas_correctas_consecutivas"] = 0 
        return False  

# def avanzar_pregunta(indice, lista_preguntas):
#     """
#     Esta función avanza la pregunta al siguiente índice en la lista de preguntas.
#     Si llegamos al final de las preguntas, podemos reiniciar el juego o finalizarlo.
#     """
#     indice += 1
#     if indice >= len(lista_preguntas):
#         print("Se ha terminado el juego.")
#         return None 
#     return indice

def cargar_fondo(ruta: str, dimensiones: tuple) -> pygame.Surface:
    '''
    Funcion que carga una imagen desde una ruta y la escala a las dimensiones proporcionadas.
    '''
    fondo = pygame.image.load(ruta)
    return pygame.transform.scale(fondo, dimensiones)
