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
                partida[jugador]['promedio'] = round(sum(lista_cantidad_de_intentos) / len(lista_cantidad_de_intentos),
                                                     2)

    def continuar_partida(self):
        return messagebox.askyesno(message="¿Desea jugar otra partida?", title="Memotest")

    def reiniciar_archivo(self, condicion):
        if condicion == 'True':
            archivo = open("partidas.csv", "w")
            archivo.close()

    def leer_archivo_configuracion(self):
        """Abre el archivo csv de configuracion, lee linea
        por linea y modifica los datos del archivo en el diccionario de datos por
        defecto, indicando con un 0 si es el valor por defecto (no se modifico) y con
        un 1 si el valor fue modificado por el archivo."""

        archivo = open("configuracion.csv", "r")
        datos = {"CANTIDAD_FICHAS": [16, 0], "MAXIMO_JUGADORES": [2, 0], "MAXIMO_PARTIDAS": [5, 0],
                 "REINICIAR_ARCHIV0_PARTIDAS": [False, 0]}
        linea = " "
        while linea:
            linea = archivo.readline()
            lista_de_palabras = self.lista_de_palabras_por_linea(linea)
            if len(lista_de_palabras) == 2:
                clave = lista_de_palabras[0]
                valor = lista_de_palabras[1]
                datos[clave][0] = valor
                datos[clave][1] = 1
        archivo.close()

        return datos

    def lista_de_palabras_por_linea(self, linea):
        """Toma una linea pasada como parametro y la
        procesa para devolver una lista con las palabras que hay en esa linea."""

        lista_de_palabras = []
        palabra = ""
        for caracter in linea:
            if caracter == ",":
                palabra = palabra.replace("\n", "")
                lista_de_palabras.append(palabra)
                palabra = ""
            else:
                palabra += caracter
        palabra = palabra.replace("\n", "")
        lista_de_palabras.append(palabra)

        return lista_de_palabras

    def obtener_ganador(self):
        ganador = self.resumen[0]
        max_cantidad_aciertos = self.resumen[0]['aciertos']
        misma_cantidad_aciertos = [jugador for jugador in self.resumen if jugador['aciertos'] == max_cantidad_aciertos]
        
        if len(misma_cantidad_aciertos) > 1:
            print(misma_cantidad_aciertos)
            ganador = sorted(misma_cantidad_aciertos, key=lambda x: x['intentos'])[0]
            
        return ganador

    def generar_ranking(self):
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
                Label(self.raiz, text=fila[indexCol], background='#8AFF93' if esGanador else 'white').grid(row=indexFila, column=indexCol, sticky=NSEW)
    
        self.raiz.mainloop()