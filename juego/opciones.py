import pygame
import csv
from juego.Constantes import *
from juego.Funciones import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Preguntas")


# Colores personalizables
COLOR_TEXTO = (255, 255, 255)  # Blanco
COLOR_FONDO = (50, 50, 50)     # Fondo oscuro
COLOR_AZUL = (0, 120, 255)     # Azul para resaltado

preguntas = []


def guardar_pregunta(pregunta, opcion1, opcion2, opcion3, opcion4, cantidad_respuestas_correctas):
    """
    Que hace? ->    Guarda la pregunta en un archio vCSV.
    ¿Que parametros recibe?
        -ventana:pygame.Surface -> Superficie en la que se dibuja el botón.
        -fuente:pygame.font.Font -> La fuente que se utiliza para renderizar el texto en el botón.
        -cantidad_respuestas_correctas:int -> El número de respuestas correctas del usuario.
        -total:int -> El número total de preguntas o respuestas.

    ¿Que retorna?:str -> El nombre ingresado por el usuario como una cadena de texto.
    """
    with open(RUTA_PREGUNTAS, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([pregunta, opcion1, opcion2, opcion3, opcion4, cantidad_respuestas_correctas])

def agregar_pregunta():
    """
    Permite al usuario ingresar una pregunta junto con sus opciones de respuesta.
    """
    pregunta = ''
    opciones = []
    cantidad_respuestas_correctas = ''
    estado = "pregunta"
    input_active = True

    while input_active:
        screen.fill(COLOR_FONDO)

        if estado == "pregunta":
            mostrar_texto(screen, "Ingrese una pregunta y las respuestas:", (20, 20), FUENTE_32, COLOR_AZUL)
            mostrar_texto(screen, f"Pregunta: {pregunta}", (20, 100), FUENTE_27, COLOR_TEXTO)
            mostrar_texto(screen, " SIG => 'ENTER' ", (20, 150), FUENTE_27, COLOR_TEXTO)

        elif estado == "opciones":
            mostrar_texto(screen, "Ingrese opciones de respuesta (máximo 4):", (20, 100), FUENTE_32, COLOR_AZUL)
            for i, opcion in enumerate(opciones):
                mostrar_texto(screen, f"Opción {i + 1}: {opcion}", (20, 150 + i * 40), FUENTE_27, COLOR_TEXTO)
            if len(opciones) < 4:
                mostrar_texto(screen, "Presione ENTER para pasar a la respuesta correcta", (20, 350), FUENTE_27, COLOR_TEXTO)

        elif estado == "respuesta":
            mostrar_texto(screen, f"Respuesta correcta: {cantidad_respuestas_correctas}", (20, 100), FUENTE_27, COLOR_TEXTO)
            mostrar_texto(screen, "Presione ENTER para guardar la pregunta", (20, 150), FUENTE_27, COLOR_TEXTO)

        mostrar_texto(screen, "Salir=> ESC ", (600, 20), FUENTE_27, COLOR_AZUL)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
                return "salir"  # Si el evento es cerrar la ventana, salimos
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if estado == "pregunta" and pregunta:
                        CLICK_SONIDO.play()
                        estado = "opciones"
                    elif estado == "opciones" and len(opciones) == 4:
                        CLICK_SONIDO.play()
                        estado = "respuesta"
                    elif estado == "respuesta" and cantidad_respuestas_correctas:
                        preguntas.append({
                            'pregunta': pregunta,
                            'opciones': opciones,
                            'cantidad_respuestas_correctas': cantidad_respuestas_correctas
                        })
                        guardar_pregunta(pregunta, opciones[0], opciones[1], opciones[2], opciones[3], cantidad_respuestas_correctas)
                        mostrar_texto(screen, "Pregunta agregada!!!", (20, 400), FUENTE_27, COLOR_AZUL)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        input_active = False
                        CLICK_SONIDO.play()
                elif event.key == pygame.K_BACKSPACE:
                    if estado == "pregunta":
                        pregunta = pregunta[:-1]
                        CLICK_SONIDO.play()
                    elif estado == "opciones" and opciones:
                        opciones[-1] = opciones[-1][:-1]
                        CLICK_SONIDO.play()
                    elif estado == "respuesta":
                        cantidad_respuestas_correctas = cantidad_respuestas_correctas[:-1]
                elif event.key == pygame.K_ESCAPE:
                    input_active = False
                    return "salir"
                else:
                    if estado == "pregunta":
                        pregunta += event.unicode
                    elif estado == "opciones":
                        if len(opciones) < 4:
                            if len(opciones) == 0 or len(opciones[-1]) > 0:
                                opciones.append(event.unicode)
                            else:
                                opciones[-1] += event.unicode
                    elif estado == "respuesta":
                        cantidad_respuestas_correctas += event.unicode
            elif event.type == pygame.QUIT:
                  estado = "menu"