from tkinter import *
import tkinter as tk

class Ranking:
    def __init__(self) -> None:
        self.raiz = tk.Tk()
        
    def generar_ranking(self):  
        self.raiz.title("TP2 - Memotest - Ranking")
        n_rows = 6
        n_columns = 3
        t_columns = ['Jugadores','Cantidad de aciertos', 'Total de intentos', 'Promedio de intentos']
        for i in range(n_rows):
            self.raiz.grid_rowconfigure(i,  weight=1)
        for column in t_columns:
            index = t_columns.index(column)
            self.raiz.grid_columnconfigure(index,  weight=1, pad=50)
            Label(self.raiz, text=column).grid(row=1, column=index, sticky=NSEW)

        self.raiz.mainloop()