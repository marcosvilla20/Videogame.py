import pygame
from juego.Constantes import *
from juego.Funciones import *

pygame.init()

boton_volver = {
    "superficie": pygame.Surface(TAMAÑO_BOTON_VOLVER),
    "rectangulo": pygame.Surface(TAMAÑO_BOTON_VOLVER).get_rect()
}
boton_volver["superficie"].fill(COLOR_AZUL)

def cargar_top_10(archivo_csv="top_10.csv"):
    """
    recibe el archivo
    """
    lista_diccionarios = convertir_csv_a_lista_diccionarios(archivo_csv)
    
    lista_ordenada = ordenar_lista_diccionarios(lista_diccionarios)

    return lista_ordenada[:10]


def guardar_puntaje(nombre, puntaje, archivo_csv="top_10.csv"):

    top_10 = cargar_top_10(archivo_csv)
 
    top_10.append({"nombre": nombre, "puntaje": puntaje})

    top_10 = ordenar_lista_diccionarios(top_10)

    top_10 = top_10[:10]

    with open(archivo_csv, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["nombre", "puntaje"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader() 
        for jugador in top_10:
            writer.writerow(jugador) 

def mostrar_ranking(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    retorno = "puntuaciones"
    
    top_10 = cargar_top_10()
    
    fondo_ranking = cargar_fondo("juego/imagenes/fondo-ranking.jpg",(ANCHO,ALTO))
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.blit(fondo_ranking, (0, 0)) 


    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (30, 30))
    mostrar_texto(boton_volver["superficie"], "VOLVER", (5, 5), FUENTE_22, COLOR_BLANCO)

    mostrar_texto(pantalla, "TOP 10 PUNTOS", (20, 100), FUENTE_30, COLOR_NEGRO)

    y_pos = 150
    for i in range(len(top_10)):
        texto = f"{i + 1}. {top_10[i]['nombre']} - {top_10[i]['puntaje']} puntos"
        mostrar_texto(pantalla, texto, (20, y_pos), FUENTE_30, COLOR_NEGRO)
        y_pos += 40  # Espacio entre las entradas del ranking

    return retorno