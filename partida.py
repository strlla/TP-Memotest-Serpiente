from tkinter import *
import tkinter as tk
from tkinter import messagebox


class Partida:
    def __init__(self) -> None:
        self.partidas = []
        self.resumen = []

    def guardar_hora_finalizacion(self, hora_finalizacion):
        """Guarda la hora de finalizacion de una partida
        # Estrella Portocarrero"""
        self.hora_finalizacion = hora_finalizacion

    def guardar_fecha(self, fecha_partida):
        """Guarda la fecha de finalizacion de una partida
        # Estrella Portocarrero"""
        self.fecha_partida = fecha_partida

    def generar_resumen(self):
        """Genera un resumen por cada jugador durante la partida.
        Se incluye el nombre del jugador, aciertos, intentos, fecha y hora de finalizacion.
        # Estrella Portocarrero"""
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
        """Agrega la ultima partida finalizada al listado de partidas
        # Estrella Portocarrero"""
        self.partidas.append(partida)

    def continuar_partida(self):
        """Le pregunta al usuario si desea continuar partida despues de visualizar el ranking
        Juan Tejada"""
        return messagebox.askyesno(message="¿Desea jugar otra partida?", title="Memotest")

    def obtener_ganador(self):
        """Se busca el jugador con mayor cantidad de aciertos, si hubiese mas de uno se busca
        al que tiene la menor cantidad de intentos.
        # Estrella Portocarrero"""
        ganador = self.resumen[0]
        max_cantidad_aciertos = self.resumen[0]['aciertos']
        misma_cantidad_aciertos = [jugador for jugador in self.resumen if jugador['aciertos'] == max_cantidad_aciertos]

        if len(misma_cantidad_aciertos) > 1:
            ganador = sorted(misma_cantidad_aciertos, key=lambda x: x['intentos'])[0]

        return ganador

    def generar_ranking(self):
        """Generar una interfaz de Tkinter para mostrar el resumen de la partida
        por jugador en una tabla, resaltando con color al jugador. Luego de mostrarse el ranking
        se abre una ventana preguntando si se quiere jugar otra partida.
        ## Estrella Portocarrero
        ## Juan Tejada"""
        self.raiz = tk.Tk()
        self.raiz.title("TP2 - Memotest - Ranking")
        ganador = self.obtener_ganador()
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
