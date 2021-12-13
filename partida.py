from tkinter import *
import tkinter as tk
from tkinter import messagebox


class Partida:

    def __init__(self) -> None:
        self.partidas = []
        self.resumen = []

    def guardar_hora_finalizacion_partida(self, hora_finalizacion):
        self.hora_finalizacion = hora_finalizacion

    def guardar_fecha_partida(self, fecha_partida):
        self.fecha_partida = fecha_partida

    def generar_resumen_partida(self):
        nombres = set(list(self.partidas[0].keys()))

        for nombre in nombres:
            aciertos = sum([partida[nombre]['aciertos'] for partida in self.partidas])
            intentos = sum([partida[nombre]['intentos'] for partida in self.partidas])
            resumen_partida = {
                "fecha_partida": self.fecha_partida,
                "hora_finalizacion": self.hora_finalizacion,
                "nombre_jugador": nombre,
                "aciertos": aciertos,
                "intentos": intentos
            }
            self.resumen.append(resumen_partida)

        self.resumen = sorted(self.resumen, key=lambda x: x['aciertos'], reverse=True)

    def agregar_partida_terminada(self, partida):
        self.partidas.append(partida)

    def continuar_partida(self):
        return messagebox.askyesno(message="¿Desea jugar otra partida?", title="Memotest")

    def obtener_ganador_partida(self):
        ganador = self.resumen[0]
        max_cantidad_aciertos = self.resumen[0]['aciertos']
        misma_cantidad_aciertos = [jugador for jugador in self.resumen if jugador['aciertos'] == max_cantidad_aciertos]

        if len(misma_cantidad_aciertos) > 1:
            ganador = sorted(misma_cantidad_aciertos, key=lambda x: x['aciertos'])[0]

        return ganador

    def generar_ranking_partida(self):
        self.raiz = tk.Tk()
        self.raiz.title("TP2 - Memotest - Ranking")
        ganador = self.obtener_ganador_partida()
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
                esGanador = any(valor == ganador['nombre_jugador'] for valor in fila)
                Label(self.raiz, text=fila[indexCol], background='#8AFF93' if esGanador else 'white').grid(
                    row=indexFila, column=indexCol, sticky=NSEW)

        otra_partida = self.continuar_partida()

        self.raiz.mainloop()

        return otra_partida
