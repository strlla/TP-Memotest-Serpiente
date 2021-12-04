import tkinter
from tkinter import *
import tkinter as tk


class Ranking:
    def __init__(self) -> None:
        self.partidas = []

    def agregar_partida_terminada(self, partida):
        self.partidas.append(partida)
        self.calcular_promedio()

    def calcular_promedio(self):
        for partida in self.partidas:
            for jugador in list(partida.keys()):
                lista_cantidad_de_intentos = [partida[jugador]['intentos'] for partida in self.partidas]
                partida[jugador]['promedio'] = sum(lista_cantidad_de_intentos) / len(lista_cantidad_de_intentos)

    def generar_ranking(self):
        self.raiz = tk.Tk()
        self.raiz.title("TP2 - Memotest - Ranking")

        # self.raiz.configure(bg="#fff")

        valores_tabla = [['Jugadores', 'Cantidad de aciertos', 'Total de intentos', 'Promedio de intentos']]
        ultima_partida = self.partidas[-1]
        for jugador in ultima_partida:
            valores_fila = [jugador]
            for campo in list(ultima_partida[jugador].keys()):
                valores_fila.append(ultima_partida[jugador][campo])
            valores_tabla.append(valores_fila)

        for indexFila in range(len(valores_tabla)):
            fila = valores_tabla[indexFila]
            for indexCol in range(len(fila)):
                Label(self.raiz, text=fila[indexCol]).grid(row=indexFila, column=indexCol, sticky=NSEW)
        Ranking.terminar_juego(self)
        Ranking.nueva_partida(self)

    def terminar_juego(self):

        Terminar_Juego = tkinter.Button(self.raiz, text="Juegar nueva partida", command=True)
        Terminar_Juego.grid(row=4, column=0)

    def nueva_partida(self):
        Nueva_Partida = tkinter.Button(self.raiz, text="Juegar nueva partida", command=True)
        Nueva_Partida.grid(row=4, column=3)

        self.raiz.mainloop()
