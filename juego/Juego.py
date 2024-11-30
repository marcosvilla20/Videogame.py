import pygame 
import random
from juego.Funciones import *
from juego.Preguntas import *
from juego.comodines import *

pygame.init()
cuadro_pregunta = {}
cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
# cuadro_pregunta["superficie"] = pygame.image.load("fondo.jpg")
# cuadro_pregunta["superficie"] = pygame.transform.scale(fondo,TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()
cuadro_pregunta["superficie"].fill(COLOR_ROJO)

lista_respuestas = []

for i in range(3):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cuadro_respuesta["superficie"].fill(COLOR_AZUL)
    lista_respuestas.append(cuadro_respuesta)
    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
random.shuffle(lista_preguntas)

# Tiempos
TIEMPO_MAX_PREGUNTA = 10  # Tiempo límite en segundos
tiempo_inicial = pygame.time.get_ticks()
bandera_sonido_advertencia = False

# COMODINES
doble_chance_activado = False
doble_chance_usado = False
comodin_pasar_usado = False
boton_doble_chance = pygame.Rect(300, 180, 40, 40)
boton_pasar = pygame.Rect(355, 180, 40, 40)


def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    global tiempo_inicial
    global bandera_sonido_advertencia
    global doble_chance_activado
    global doble_chance_usado
    global comodin_pasar_usado

    retorno = "juego"

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = (tiempo_actual-tiempo_inicial) // 1000
    tiempo_restante = TIEMPO_MAX_PREGUNTA - tiempo_transcurrido
    
    if tiempo_restante == 4:
        SONIDO_3_SEG.play()
        bandera_advertencia = True

    if tiempo_restante <= 0:
        datos_juego["cantidad_vidas"] -= 1
        bandera_respuesta = True
        tiempo_inicial = pygame.time.get_ticks()  # Reiniciar el tiempo para la próxima pregunta
        bandera_sonido_advertencia = False
        SONIDO_3_SEG.stop()
        indice +=1
    
    if bandera_respuesta:
        pygame.time.delay(250)
        cuadro_pregunta["superficie"].fill(COLOR_ROJO)
        #Limpio la superficie
        # cuadro_pregunta["superficie"] = pygame.image.load("fondo.jpg")
        # cuadro_pregunta["superficie"] = pygame.transform.scale(fondo,TAMAÑO_PREGUNTA)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"].fill(COLOR_AZUL)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
        # COMODINES
            #DOBLE CHANCE
            if comprobar_click(evento.pos, boton_doble_chance, not doble_chance_usado):
                print("Comodín Doble Chance Activado")
                doble_chance_usado = True
                doble_chance_activado = True
            # PASAR
            elif comprobar_click(evento.pos,boton_pasar, not comodin_pasar_usado):
                print("Comodín Pasar Activado")
                comodin_pasar_usado = True
                indice +=1
                indice == len(lista_preguntas)
                indice = 0
                random.shuffle(lista_preguntas)

            # Reinicio todo xq se superpone la superficie
            tiempo_inicial = pygame.time.get_ticks()
            cuadro_pregunta["superficie"].fill(COLOR_ROJO)
            for respuesta in lista_respuestas:
                respuesta["superficie"].fill(COLOR_AZUL) 
            bandera_respuesta = True
            bandera_sonido_advertencia = False
            SONIDO_3_SEG.stop()
            
            # Acciones al seleccionar respuestas
            for i in range(len(lista_respuestas)):
                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    SONIDO_3_SEG.stop()
                    respuesta_seleccionada = i + 1
                    
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        print("RESPUESTA CORRECTA")
                        lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                    else:
                        if doble_chance_activado:
                            print("Comodin doble chance activado, segunda oportunidad")
                            lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                            doble_chance_activado = False
                            continue # Otra chance
                        ERROR_SONIDO.play()
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                        print("RESPUESTA INCORRECTA")
                    indice += 1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                        
                    bandera_respuesta = True
                    tiempo_inicial = pygame.time.get_ticks()
                    bandera_sonido_advertencia = False
    
    pantalla.fill(COLOR_VIOLETA)
    #pantalla.blit(fondo,(0,0))
    
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}",(20,20),FUENTE_27,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[0]["superficie"],f"{pregunta_actual["respuesta_1"]}",(20,20),FUENTE_27,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],f"{pregunta_actual["respuesta_2"]}",(20,20),FUENTE_27,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],f"{pregunta_actual["respuesta_3"]}",(20,20),FUENTE_27,COLOR_BLANCO)
    
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(125,245))#r1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(125,315))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(125,385))#r3
    
    crear_rectangulo(pantalla,COLOR_BLANCO,lista_respuestas,2)

    crear_comodin(pantalla, boton_doble_chance, "Doble chance", FUENTE_22, not doble_chance_usado)
    crear_comodin(pantalla, boton_pasar, "Pasar", FUENTE_22, not comodin_pasar_usado)    
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_27,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_27,COLOR_NEGRO)
    mostrar_texto(pantalla,f"TIEMPO: {tiempo_restante}s",(220,40),FUENTE_27,COLOR_NEGRO)

    return retorno