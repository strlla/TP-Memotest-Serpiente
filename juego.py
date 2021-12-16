import csv


class Juego:

    def __init__(self) -> None:
        self.partidas = []
        self.resumen = []

    def guardar_hora_finalizacion(self, hora_finalizacion_juego):
        self.hora_finalizacion_juego = hora_finalizacion_juego

    def guardar_fecha(self, fecha_partida_juego):
        self.fecha_partida_juego = fecha_partida_juego

    def generar_resumen(self):
        nombres = set(list(self.partidas[0].keys()))

        for nombre in nombres:
            aciertos = sum([partida[nombre]['aciertos'] for partida in self.partidas])
            intentos = sum([partida[nombre]['intentos'] for partida in self.partidas])
            resumen_juego = {
                "fecha_partida": self.fecha_partida_juego,
                "hora_finalizacion": self.hora_finalizacion_juego,
                "nombre_jugador": nombre,
                "aciertos": aciertos,
                "intentos": intentos
            }
            self.resumen.append(resumen_juego)

        self.resumen = sorted(self.resumen, key=lambda x: x['aciertos'], reverse=True)

    def guardar_juego(self):
        """Abre el archivo csv de partidas y guarda un resumen del juego por jugador
        Estrella Portocarrero
        """
        fieldnames = ["fecha_partida", "hora_finalizacion", "nombre_jugador", "aciertos", "intentos"]

        with open('partidas.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for jugador in self.resumen:
                writer.writerow(jugador)
            csvfile.close()

    def reiniciar_archivo(self, condicion):
        """Vacia el archivo de partida
         Juan Tejada
        """
        if condicion == 'True':
            archivo = open("partidas.csv", "w")
            archivo.close()

    def leer_archivo_configuracion(self):
        """Abre el archivo csv de configuracion, lee linea
        por linea y modifica los datos del archivo en el diccionario de datos por
        defecto
        Juan Tejada"""

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
        procesa para devolver una lista con las palabras que hay en esa linea.
        Juan Tejada"""

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

    def agregar_partida_terminada(self, partida):
        """Funcion que agrega al final de una lista la partida finalizada
        y luego invoca la funcion para calcular el promedio de intentos por jugador
        Estrella Portocarrero"""
        self.partidas.append(partida)
        self.calcular_promedio()

    def calcular_promedio(self):
        """Calcula el promedio de intentos de cada jugador
        y lo guarda en un campo del diccionario por partida
        Estrella Portocarrero"""
        for partida in self.partidas:
            for jugador in list(partida.keys()):
                lista_cantidad_de_intentos = [partida[jugador]['intentos'] for partida in self.partidas]
                partida[jugador]['promedio'] = round(sum(lista_cantidad_de_intentos) / len(lista_cantidad_de_intentos),
                                                     2)

    def obtener_ultima_partida(self):
        """Retorna la ultima partida guardada en el listado
        Estrella Portocarrero"""
        return self.partidas[-1]
