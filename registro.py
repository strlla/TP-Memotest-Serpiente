import csv
import pandas as pd
import os
from juego import Juego


class Registro:
    jugadores_logueados = []

    def obtener_listado_de_nombres(self):
        """Retorna un listado con los nombres de todos los jugadores registrados
        # Estrella Portocarrero"""
        return [jugador['usuario'] for jugador in self.jugadores_logueados]

    def agregar_jugador_logueado(self, jugador):
        """Recibe un jugador y lo agrega al listado de jugadores registrados para jugar
        # Estrella Portocarrero"""
        self.jugadores_logueados.append(jugador)

    def registrar_usuario(self, usuario, mostrar_empezar_juego):
        """Recibe un usuario y lo agrega al final del archivo
        # Estrella Portocarrero
        """
        config = Juego().leer_archivo_configuracion()
        fieldnames = ['usuario', 'clave']
        with open('usuarios.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(usuario)
            csvfile.close()
        self.agregar_jugador_logueado(usuario)
        if len(self.jugadores_logueados) >= int(config["MAXIMO_JUGADORES"][0]):
            mostrar_empezar_juego()
            
        print(pd.DataFrame(self.obtener_listado_de_nombres(), columns=['Usuario']))

    def obtener_usuarios(self):
        """Retorna un listado con todos los usuarios y sus correspondientes claves del archivo usuarios.csv
        ## Estrella Portocarrero
        ## Juan Tejada
        """

        usuarios = []
        with open('usuarios.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
            for fila in spamreader:
                try:
                    if fila:
                        usuarios.append({"usuario": fila[0], "clave": fila[1]})
                except IndexError:
                    pass

        return usuarios[1:len(usuarios)]

    def iniciar_sesion(self, usuario, contrasenia, mostrar_mensaje, mostrar_empezar_juego):
        """Valida que se haya ingresado un usuario y contraseña, si ya está logueado o registrado. 
        En caso de que su contraseña sea correcta se agrega al usuario al listado de usuarios logueados.
        #Estrella Portocarrero
        """
        config = Juego().leer_archivo_configuracion()
        if len(self.jugadores_logueados) + 1 > int(config["MAXIMO_JUGADORES"][0]):
            mostrar_mensaje("Se alcanzó el número máximo de jugadores", False)
        else: 
            usuarios = self.obtener_usuarios()
            if not usuario or not contrasenia:
                mostrar_mensaje("Por favor, complete los dos campos", False)
                return
            usuarioEncontrado = next((x for x in usuarios if x["usuario"] == usuario), None)
            if not usuarioEncontrado:
                mostrar_mensaje("No está registrado", False)
            elif usuarioEncontrado['clave'] == contrasenia:
                usuarioLogueado = next((x for x in self.jugadores_logueados if x["usuario"] == usuario), None)
                if usuarioLogueado:
                    mostrar_mensaje("Ya está logueado", False)
                else:
                    os.system("cls")                    
                    mostrar_mensaje("Se logueo correctamente", True)
                    self.agregar_jugador_logueado(usuarioEncontrado)
                    print(pd.DataFrame(self.obtener_listado_de_nombres(), columns=['Usuario']))
                    if len(self.jugadores_logueados) >= 2:
                        mostrar_empezar_juego()

            else:
                mostrar_mensaje("Contraseña incorrecta", False)

    def validar_usuario(self, usuario):
        """Valida el usuario segun las condiciones dadas en el enunciado. Si cumple las condiciones devuelve True de lo contrario False"""

        caracteres_permitidos = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        letras_y_numeros = 0

        usuario_valido = False

        if 4 <= len(usuario) <= 15:

            if '_' in usuario:

                for caracter in usuario:

                    if caracter in caracteres_permitidos:
                        letras_y_numeros += 1

        if (letras_y_numeros + 1) == len(usuario):
            usuario_valido = True

        return usuario_valido

    def validar_clave(self, clave):
        """Valida la clave segun las condiciones dadas en el enunciado. Si cumple las condiciones devuelve True de lo contrario False"""
        caracteres_permitidos = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'
        mayus = 0
        minus = 0
        numer = 0
        nopermit = 0
        clave_valida = False

        if 8 <= len(clave) <= 12:

            if '-' in clave or '_' in clave:

                for caracter in clave:

                    if caracter.isupper():

                        mayus += 1

                    elif caracter.islower():

                        minus += 1

                    elif caracter.isnumeric():

                        numer += 1

                    elif caracter not in caracteres_permitidos:

                        nopermit += 1

        if mayus >= 1 and minus >= 1 and numer >= 1 and nopermit == 0:
            clave_valida = True

        return clave_valida
