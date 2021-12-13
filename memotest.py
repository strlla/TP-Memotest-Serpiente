from random import shuffle
from datetime import datetime
import numpy as np
import pandas as pd
from tkinter import *
from interfaz import generar_interfaz
from registro import Registro
from juego import Juego
from partida import Partida
import math
import sys
import time


def obtener_nombres(raiz, primer_input, segundo_input, lista_de_nombres):
    """
    Se encarga guardar los nombres y cerrar la interfaz
    Estrella Portocarrero
    """
    lista_de_nombres.append(primer_input.get())
    lista_de_nombres.append(segundo_input.get())
    raiz.destroy()


def generador_fichas(config):
    """Genera las 16 fichas principales para dar inicio al juego y las devuelve aleatoriamente
        Juan Tejada
    """
    if int(config["CANTIDAD_FICHAS"][0]) % 2 == 0:
        fichas = ["D", "s"] * ((int(config["CANTIDAD_FICHAS"][0])) // 2)
        shuffle(fichas)
        return fichas
    else:
        sys.exit("Recuerde que la cantidad de fichas debe ser un número par!")


def revisar_fichas(fichas, fichas_ocultas):
    """Funcion que revisa si todas las fichas estan descubiertas (si el jugador gano) y retorna True, en caso contrario retorna False
    # Estrella Portocarrero """

    return all(ficha == ficha_oculta[1] for ficha, ficha_oculta in zip(fichas, fichas_ocultas))


def ocultar_fichas(fichas):
    """ Se itera segun la longitud de las fichas dadas para ocultarlas como numeros
    # Juan Tejada"""

    fichas_ocultas = [(str([numeros])) for numeros in range(len(fichas))]

    return fichas_ocultas


def imprimir_tablero(fichas_ocultas):
    """Imprime el tablero utilizando numpy y pandas
    Estrella Portocarrero
    Juan Tejada"""
    tablero = np.array([fichas_ocultas])
    newshape = obtener_newshape(len(fichas_ocultas))
    tablero_formado = np.reshape(tablero, newshape)
    print("Fichas y posiciones:\n", pd.DataFrame(tablero_formado))

    return


def obtener_newshape(cant_fichas):
    """
    Se recibe la cantidad de fichas que va a tener el juego y a partir de ese numero se define que forma va a tener el tablero.
    Se busca el pare de factores que formen ese número con menor diferencia entre ellos para que el tablero quede lo más parecido a un cuadrado.
    Estrella Portocarrero
    """
    raiz = math.sqrt(cant_fichas)
    multipliers = (0, cant_fichas)
    if int(raiz + 0.5) ** 2 == cant_fichas:
        return int(raiz), int(raiz)
    else:
        for i in range(1, int(pow(cant_fichas, 1 / 2)) + 1):
            if cant_fichas % i == 0:
                if (cant_fichas / i - i) < (multipliers[1] - multipliers[0]):
                    multipliers = (int(i), int(cant_fichas / i))
        return multipliers


def imprimir_asignacion_de_turnos():
    """Ordena aleatoriamente la lista de jugadores
    para asignar el orden de los turnos al azar.
    Estrella Portocarrero
    Juan Tejada"""
    lista_de_nombres = Registro().obtener_listado_de_nombres()
    shuffle(lista_de_nombres)

    for i in range(len(lista_de_nombres)):
        nro_turno = i + 1
        nombre_jugador = lista_de_nombres[i]
        print("El", nro_turno, "° turno es de ", nombre_jugador)

    return lista_de_nombres


def genera_dicc_jugadores():
    """genera_dicc_jugadores crea el diccionario que tiene como claves a los
    nombres de los jugadores y como valores los aciertos de cada jugador.
    Estrella Portocarrero
    Juan Tejada"""
    lista_de_nombres = Registro().obtener_listado_de_nombres()
    dicc_jugadores = {}
    for jugador in lista_de_nombres:
        dicc_jugadores |= {jugador: {"aciertos": 0, "intentos": 0}}  # ACIERTOS - INTENTOS - PROMEDIO INTENTOS

    return dicc_jugadores


def jugada(fichas, fichas_ocultas, dicc_jugadores, config, juego, partida):
    """La funcion jugada es la funcion principal en la que se lleva a cabo tod el juego. Tiene la variable 'nro_jugador'
    que se encarga de los turnos en el bucle. Tambien esta funcion posee el modulo 'time' que se encarga de guardar el tiempo transcurrido
    de la partida.
    Estrella Portocarrero
    Juan Tejada

    """
    MAX_PARTIDAS = int(config["MAXIMO_PARTIDAS"][0])
    REINICIAR_ARCHIVO = config["REINICIAR_ARCHIV0_PARTIDAS"][0]
    NRO_JUGADOR = 0
    NRO_PARTIDA = 1
    FINALIZAR_JUEGO = False
    FINALIZAR_PARTIDA = False
    LISTA_DE_NOMBRES = Registro().obtener_listado_de_nombres()
    Juego().reiniciar_archivo_juego(REINICIAR_ARCHIVO)

    while not FINALIZAR_JUEGO:

        while not FINALIZAR_PARTIDA:

            print(f"*-----------------------*"
                  f"\nTurno del jugador {LISTA_DE_NOMBRES[NRO_JUGADOR]}")
            fichas_originales = fichas_ocultas

            imprimir_tablero(fichas_ocultas)

            resultado, fichas_ocultas = seleccionar_posiciones(fichas, fichas_ocultas)

            fichas_descubiertas_totalmente = revisar_fichas(fichas, fichas_ocultas)

            if resultado is True:

                print(f"¡Acertaste! {LISTA_DE_NOMBRES[NRO_JUGADOR]}")

                NRO_JUGADOR = NRO_JUGADOR

                dicc_jugadores[LISTA_DE_NOMBRES[NRO_JUGADOR]]["aciertos"] += 1

                if fichas_descubiertas_totalmente is True:
                    FINALIZAR_PARTIDA = True
            else:
                dicc_jugadores[LISTA_DE_NOMBRES[NRO_JUGADOR]]["intentos"] += 1
                print(f"Fallaste {LISTA_DE_NOMBRES[NRO_JUGADOR]}")
                time.sleep(1)
                fichas_ocultas = fichas_originales
                if NRO_JUGADOR == len(LISTA_DE_NOMBRES) - 1:

                    NRO_JUGADOR = 0

                else:

                    NRO_JUGADOR += 1

                if fichas_descubiertas_totalmente:
                    FINALIZAR_PARTIDA = True
        partida.agregar_partida_terminada(dicc_jugadores)
        juego.agregar_partida_terminada(dicc_jugadores)
        dicc_jugadores = genera_dicc_jugadores()

        if NRO_PARTIDA == MAX_PARTIDAS:

            datos_partida(partida)

            FINALIZAR_JUEGO = True

            print("El juego ha finalizado, se supero el maximo de partidas.")

        else:
            NRO_PARTIDA += 1
            otra_partida = datos_partida(partida)

            if otra_partida:
                FINALIZAR_PARTIDA = False
                fichas = generador_fichas(config)
                fichas_ocultas = ocultar_fichas(fichas)

            else:
                FINALIZAR_JUEGO = True
                print("El juego ha finalizado")

    datos_juego(juego)


def datos_juego(juego):
    juego.guardar_hora_finalizacion_juego(datetime.time(datetime.now()))
    juego.guardar_fecha_juego(datetime.date(datetime.now()))
    juego.generar_resumen_juego()
    juego.guardar_juego()


def datos_partida(partida):
    partida.guardar_hora_finalizacion_partida(datetime.time(datetime.now()))
    partida.guardar_fecha_partida(datetime.date(datetime.now()))
    partida.generar_resumen_partida()
    ranking = partida.generar_ranking_partida()

    return ranking


def seleccionar_posiciones(fichas, fichas_ocultas):
    """Funcion que permite el ingreso de las posiciones a descubrir en las fichas y retorna True en caso de que sean
    iguales, en caso contrario retorna False
    Estrella Portocarrero
    Juan Tejada"""
    primer_posicion = input("1er posición: ")
    primer_es_valido = validar_ingreso(primer_posicion, fichas_ocultas)
    while not primer_es_valido:
        primer_posicion = input("1er posición: ")
        primer_es_valido = validar_ingreso(primer_posicion, fichas_ocultas)
    primer_posicion = int(primer_posicion)

    fichas_ocultas = mostrar_ficha(primer_posicion, fichas, fichas_ocultas)

    segunda_posicion = input("2da posición: ")
    segundo_es_valido = validar_ingreso(segunda_posicion, fichas_ocultas)
    while not segundo_es_valido:
        segunda_posicion = input("2da posición: ")
        segundo_es_valido = validar_ingreso(segunda_posicion, fichas_ocultas)
    segunda_posicion = int(segunda_posicion)

    fichas_ocultas = mostrar_ficha(segunda_posicion, fichas, fichas_ocultas)

    resultado = comparar_fichas(primer_posicion, segunda_posicion, fichas)

    return resultado, fichas_ocultas


def comparar_fichas(primera_posicion, segunda_posicion, fichas):
    """Compara el contenido de la ficha en las dos posiciones recibidas, retorna True si son iguales, en caso contrario retorna False
    Juan Tejada"""
    return fichas[primera_posicion] == fichas[segunda_posicion]


def mostrar_ficha(posicion, fichas, fichas_ocultas):
    """Printea las fichas ocultas y las descubiertas por el usuario
    Juan Tejada"""
    fichas_ocultas = [i.replace(str(posicion), fichas[posicion]) if fichas_ocultas.index(i) == posicion else i for i in
                      fichas_ocultas]
    imprimir_tablero(fichas_ocultas)
    return fichas_ocultas


def validar_ingreso(posicion, fichas_ocultas):
    """Funcion que chequea que la posicion ingresada sea numerica  y sea menor o igual a la cantidad de fichas, falta validar que este disponible
    Estrella Portocarrero"""
    if not posicion.isnumeric():
        print("Ingrese un valor numerico")
        return False
    else:
        if int(posicion) > len(fichas_ocultas) - 1 or int(posicion) < 0:
            print("Ingrese un numero menor o igual a ", len(fichas_ocultas) - 1)
            return False
        elif not fichas_ocultas[int(posicion)][1].isnumeric():
            print("Esta ficha ({}) no esta disponible".format(fichas_ocultas[int(posicion)][1]))
            return False

    return True


def main():
    # generar_interfaz(lista_de_nombres)
    config = Juego().leer_archivo_configuracion()
    juego = Juego()
    partida = Partida()
    generar_interfaz()
    fichas = generador_fichas(config)
    fichas_ocultas = ocultar_fichas(fichas)
    imprimir_asignacion_de_turnos()
    dicc_jugadores = genera_dicc_jugadores()
    jugada(fichas, fichas_ocultas, dicc_jugadores, config, juego, partida)


main()
