from tkinter import *
import tkinter as tk

class Ranking:
    def __init__(self) -> None:
        self.raiz = tk.Tk()
        self.ultima_partida = [{"usuario": "Estrella"}, {"usuario": "Juan"}, {"usuario": "Matias"}]
        self.partidas = []
        
    def agregar_partida_terminada(self, partida):
        self.ultima_partida = partida
        self.partidas.append(partida)
        self.calcular_promedio()
        
    def calcular_promedio():
        #aca se calcula el promedio
        pass
        
    def generar_ranking(self):  
        self.raiz.title("TP2 - Memotest - Ranking")
        columnas = ['Jugadores', 'Cantidad de aciertos', 'Total de intentos', 'Promedio de intentos']
        for column in columnas:
            index = columnas.index(column)
            self.raiz.grid_columnconfigure(index,  weight=1, pad=20)
            Label(self.raiz, text=column).grid(row=0, column=index, sticky=NSEW)
            
        for jugador in self.ultima_partida:    
            indexJugador = self.ultima_partida.index(jugador)
            for campo in jugador:
                indexCampo = list(jugador.keys()).index(campo)
                self.raiz.grid_columnconfigure(indexCampo, weight=1, pad=20)
                Label(self.raiz, text=jugador['usuario']).grid(row=indexJugador + 1, column=indexCampo, sticky=NSEW)
    
  
            
        self.raiz.mainloop()