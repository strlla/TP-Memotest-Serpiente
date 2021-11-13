from os import system
from random import shuffle
import time
import numpy as np
import pandas as pd
from tkinter import *
import tkinter as tk

def generar_interfaz():
    raiz = Tk()
    raiz.title("TP1 - Memotest")
    raiz.resizable(False, False)
    raiz.geometry("300x200")
    raiz.configure(bg='#FFF')
    titulo = Label(raiz, text="Ingrese los jugadores:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    titulo.place(x=10, y=10)
    label_primer_jugador = Label(raiz, text="1º", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_segundo_jugador = Label(raiz, text="2º", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")    
    label_primer_jugador.place(x=10, y=50)
    label_segundo_jugador.place(x=10, y=100)
    primer_jugador_input = Entry(raiz, bd=0, bg="#edf2fb", font=("Ubuntu", 12))
    primer_jugador_input.place(x=45, y=53, height=30)
    segundo_jugador_input = Entry(raiz, bd=0, bg="#edf2fb", font=("Ubuntu", 12))
    segundo_jugador_input.place(x=45, y=103, height=30)
    boton_enviar = Button(raiz, command=lambda: obtener_nombres(primer_jugador_input, segundo_jugador_input), text="Jugar", bd=0, bg="#47126b", font=("Ubuntu", 12), fg="#FFF")
    boton_enviar.place(x=10, y=150, height=20, width=100)
    raiz.mainloop()
    
def obtener_nombres(primer_input, segundo_input):
    primer_nombre = primer_input.get()
    segund_nombre = segundo_input.get()
    print(primer_nombre)
    
def generador_fichas():
    """Genera las 16 fichas principales para dar inicio al juego y las devuelve aleatoriamente"""

    fichas = ["D", "D", "D", "D", "D", "D", "D", "D",
              "s", "s", "s", "s", "s", "s", "s", "s"]

    shuffle(fichas)

    return fichas


def revisar_fichas(fichas, fichas_ocultas):
    """Funcion que revisa si todas las fichas estan descubiertas (si el jugador gano) y retorna True, en caso contrario retorna False
    # Estrella Portocarrero """

    return all(ficha == ficha_oculta[1] for ficha, ficha_oculta in zip(fichas, fichas_ocultas))


def ocultar_fichas(fichas):
    """ Se itera segun la longitud de las fichas dadas para ocultarlas como numeros
    #Juan Tejada"""

    fichas_ocultas = [(str([numeros])) for numeros in range(len(fichas))]

    return fichas_ocultas


def imprimir_tablero(fichas, fichas_ocultas):
    """Imprime el tablero utilizando numpy y pandas
    #Juan Tejada"""
    tablero = np.array([fichas_ocultas])
    tablero_formado = np.reshape(tablero, (4, 4))
    print("Fichas y posiciones:\n", pd.DataFrame(tablero_formado))

    return


def obtener_nombres_de_jugadores():
    """Solicita que se ingrese los nombres de los
    jugadores, y los guarda en una lista. Se indica que para finalizar la carga
    hay que presionar ENTER.
    #Juan Tejada"""

    nombres_de_jugadores = []
    cantidad_de_ingresos = 0
    termino_ingreso = False
    while cantidad_de_ingresos < 2 and not termino_ingreso:
        nombre_ingresado = input("Ingrese el nombre de un jugador o presione ENTER para finalizar el ingreso: ")
        if nombre_ingresado == "":
            termino_ingreso = True
        else:
            nombres_de_jugadores.append(nombre_ingresado)
        cantidad_de_ingresos = len(nombres_de_jugadores)

    return nombres_de_jugadores


def imprimir_asignacion_de_turnos(lista_de_nombres):
    """Ordena aleatoriamente la lista de jugadores
    para asignar el orden de los turnos al azar.
    #Juan Tejada"""

    shuffle(lista_de_nombres)

    for i in range(len(lista_de_nombres)):
        nro_turno = i + 1
        nombre_jugador = lista_de_nombres[i]
        print("El", nro_turno, "° turno es de ", nombre_jugador)

    return lista_de_nombres


def jugada(fichas, lista_de_nombres):
    """Funcion que permite jugar a cada jugador en su orden correspondiente
    Estrella Portocarrero"""
    fichas_ocultas = ocultar_fichas(fichas)
    while True:
        for jugador in lista_de_nombres:
            print(f"Turno del jugador {jugador}")
            fichas_ocultas = jugada_por_jugador(fichas, fichas_ocultas)

def jugada_por_jugador(fichas, fichas_ocultas):
    """Funcion que permite al jugador seguir jugando mientras encuentre pares iguales, caso contrario se resetean las fichas.
    Tambien contiene una variable que permite guardar la cantidad de intentos y el tiempo transcurrido hasta ganar la partida. 
    Retorna las fichas del ultimo jugador. 
    Estrella Portocarrero"""

    intentos = 0
    tiempo_total = 0
    inicio_partida = time.time()
    gano = False
    imprimir_tablero(fichas, fichas_ocultas)
    while not gano:
        resultado, fichas_ocultas = seleccionar_posiciones(fichas, fichas_ocultas)
        if resultado:
            gano = revisar_fichas(fichas, fichas_ocultas)
            final_partida = time.time()
            tiempo_total = final_partida - inicio_partida
            if gano:
                print(
                    f"¡Felicitaciones! Lo lograste en {intentos} intentos y en un tiempo total de {(round(tiempo_total, 2))} segundos")
        else:
            # intentos += 1
            # print("Intenta nuevamente")
            system("cls")
            break
    return fichas_ocultas


def seleccionar_posiciones(fichas, fichas_ocultas):
    """Funcion que permite el ingreso de las posiciones a descubrir en las fichas y retorna True en caso de que sean 
    iguales, en caso contrario retorna False """
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
    """Compara el contenido de la ficha en las dos posiciones recibidas, retorna True si son iguales, en caso contrario retorna False"""
    return fichas[primera_posicion] == fichas[segunda_posicion]


def mostrar_ficha(posicion, fichas, fichas_ocultas):
    """Printea las fichas ocultas y las descubiertas por el usuario"""
    fichas_ocultas = [i.replace(str(posicion), fichas[posicion]) if fichas_ocultas.index(i) == posicion else i for i in
                      fichas_ocultas]

    imprimir_tablero(fichas, fichas_ocultas)

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
    generar_interfaz()
    fichas = generador_fichas()
    lista_de_nombres = obtener_nombres_de_jugadores()
    imprimir_asignacion_de_turnos(lista_de_nombres)
    jugada(fichas, lista_de_nombres)

main()
