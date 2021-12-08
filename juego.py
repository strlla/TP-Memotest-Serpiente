import tkinter
from tkinter import *
import tkinter as tk
import csv
from tkinter import messagebox


class Juego:
    def __init__(self) -> None:
        self.partidas = []
        self.resumen = []

    def guardar_hora_finalizacion(self, hora_finalizacion):
        self.hora_finalizacion = hora_finalizacion

    def guardar_fecha_partida(self, fecha_partida):
        self.fecha_partida = fecha_partida

    def generar_resumen_juego(self):
        nombres = set(list(self.partidas[0].keys()))

        for nombre in nombres:
            aciertos = sum([partida[nombre]['aciertos'] for partida in self.partidas])
            intentos = sum([partida[nombre]['intentos'] for partida in self.partidas])
            resumen_juego = {
                "fecha_partida": self.fecha_partida,
                "hora_finalizacion": self.hora_finalizacion,
                "nombre_jugador": nombre,
                "aciertos": aciertos,
                "intentos": intentos
            }
            self.resumen.append(resumen_juego)

        self.resumen = sorted(self.resumen, key=lambda x: x['aciertos'], reverse=True)

    def guardar_partida(self):
        self.generar_resumen_juego()
        for jugador in self.resumen:
            with open('partidas.csv', 'a') as csvfile:
                fieldnames = ["fecha_partida", "hora_finalizacion", "nombre_jugador", "aciertos", "intentos"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(jugador)
                csvfile.close()

    def agregar_partida_terminada(self, partida):
        self.partidas.append(partida)
        self.calcular_promedio()

    def calcular_promedio(self):
        for partida in self.partidas:
            for jugador in list(partida.keys()):
                lista_cantidad_de_intentos = [partida[jugador]['intentos'] for partida in self.partidas]
                partida[jugador]['promedio'] = round(sum(lista_cantidad_de_intentos) / len(lista_cantidad_de_intentos), 2)

    def continuar_partida(self):
        return messagebox.askyesno(message="¿Desea jugar otra partida?", title="Memotest")

    def generar_ranking(self):
        self.raiz = tk.Tk()
        self.raiz.title("TP2 - Memotest - Ranking")

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
        partida = self.continuar_partida()

        self.raiz.mainloop()

        return partida

