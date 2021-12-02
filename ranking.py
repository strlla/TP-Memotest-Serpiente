from tkinter import *
import tkinter as tk

class Ranking:
    def __init__(self) -> None:
        self.raiz = tk.Tk()
        # self.partidas = [{'Estrella2+': {'aciertos': 5, 'intentos': 1}, 'Martin4_': {'aciertos': 3, 'intentos': 1}}, {'Estrella2+': {'aciertos': 5, 'intentos': 6}, 'Martin4_': {'aciertos': 3, 'intentos': 4}}]
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
        self.raiz.title("TP2 - Memotest - Ranking")
        columnas = ['Jugadores', 'Cantidad de aciertos', 'Total de intentos', 'Promedio de intentos']
        for column in columnas:
            index = columnas.index(column)
            self.raiz.grid_columnconfigure(index,  weight=1, pad=20)
            Label(self.raiz, text=column).grid(row=0, column=index, sticky=NSEW)
            ultima_partida = self.partidas[-1]
            for jugador in ultima_partida:  
                valores_fila = []
                valores_fila.append(jugador)
                for campo in list(ultima_partida[jugador].keys()):
                    valores_fila.append(ultima_partida[jugador][campo])
                    for valor_fila in valores_fila:
                        Label(self.raiz, text=valor_fila).grid(row=int(list(ultima_partida.keys()).index(jugador)) + 1, column=valores_fila.index(valor_fila), sticky=NSEW)
                
        self.raiz.mainloop()