from tkinter import *
from tkinter import messagebox
from registro import Registro
from juego import Juego
import tkinter as tk


class Interfaz:
    def __init__(self) -> None:
        self.raiz = tk.Tk()
        self.loginFrame = Frame(self.raiz, bg="#FFF")
        self.registroFrame = Frame(self.raiz, bg="#FFF")
        self.labelLogin = Label(self.loginFrame, text="", bg="#FFF", font=("Ubuntu", 12, "bold"))
        self.labelRegistro = Label(self.registroFrame, text="", bg="#FFF", font=("Ubuntu", 12, "bold"))
        self.empezarJuegoBotonLogin = Button(self.loginFrame, command=self.cerrar_interfaz, text="Empezar a jugar",
                                             bd=0, bg="#06bf78", font=("Ubuntu", 12), fg="#FFF")
        self.empezarJuegoBotonRegistro = Button(self.registroFrame, command=self.cerrar_interfaz,
                                                text="Empezar a jugar", bd=0, bg="#06bf78", font=("Ubuntu", 12),
                                                fg="#FFF")

    def cerrar_interfaz(self):
        """Cierra la interfaz de registro y login
        #Estrella Portocarrero"""
        self.raiz.destroy()

    def mostrar_empezar_juego(self):
        """Se ubica un boton en la interfaz del registro y login para empezar el juego
        # Estrella Portocarrero"""
        self.empezarJuegoBotonLogin.place(x=125, y=350, height=30, width=150)
        self.empezarJuegoBotonRegistro.place(x=130, y=420, height=30, width=150)

    def interfaz_registro(self, datos):
        """ Se genera un interfaz que permite a los jugadores registrarse 
        ingresando un nuevo usuario y contraseña (dos veces para confirmar)
        Además esta interfaz cuenta con botones para ver la configuración del juego, 
        condiciones de registro e iniciar sesión
        ## Juan Tejada
        ## Estrella Portocarrero"""
        self.registroFrame.pack(side="top", expand=True, fill="both")

        self.raiz.title("TP1 - Memotest - Registro")
        self.raiz.resizable(False, False)
        self.raiz.geometry("400x480")
        self.raiz.configure(bg='#FFF')
        titulo = Label(self.registroFrame, text="Ingrese sus datos para registrarse", bg="#FFF",
                       font=("Ubuntu", 14, "bold"),
                       fg="#47126b")
        titulo.place(x=40, y=30)
        label_usuario = Label(self.registroFrame, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
        label_primer_contrasena = Label(self.registroFrame, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"),
                                        fg="#47126b")
        label_segunda_contrasena = Label(self.registroFrame, text="Repita la contraseña:", bg="#FFF",
                                         font=("Ubuntu", 14, "bold"), fg="#47126b")
        label_usuario.place(x=10, y=100)
        label_primer_contrasena.place(x=10, y=150)
        label_segunda_contrasena.place(x=10, y=200)
        usuario_input = Entry(self.registroFrame, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
        usuario_input.place(x=220, y=100, height=30, width=170)
        primer_contrasena_input = Entry(self.registroFrame, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
        primer_contrasena_input.place(x=220, y=150, height=30, width=170)
        segunda_contrasena_input = Entry(self.registroFrame, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
        segunda_contrasena_input.place(x=220, y=200, height=30, width=170)
        boton_registrarse = Button(self.registroFrame,
                                   command=lambda: self.guardar_datos(datos, usuario_input,
                                                                      primer_contrasena_input,
                                                                      segunda_contrasena_input), text="Registrarse",
                                   bd=0, bg="#47126b",
                                   font=("Ubuntu", 12), fg="#FFF")
        boton_registrarse.place(x=150, y=300, height=30, width=100)
        boton_registrado = Button(self.registroFrame,
                                  command=lambda: [self.registroFrame.pack_forget(), self.interfaz_login(datos)],
                                  text="Ya estoy registrado",
                                  bd=0,
                                  bg="#47126b",
                                  font=("Ubuntu", 12), fg="#FFF")
        boton_registrado.place(x=125, y=340, height=30, width=150)
        boton_condicion_registro = Button(self.registroFrame, command=lambda: self.info_usuario_clave(),
                                          text="Condiciones de registro", bd=0, bg="#47126b", font=("Ubuntu", 12),
                                          fg='#FFF')
        boton_condicion_registro.place(x=110, y=380, height=30, width=180)
        boton_configuraciones = Button(self.registroFrame, command=lambda: self.info_configuraciones(),
                                       text="Configuraciones", bd=0, bg="#47126b", font=("Ubuntu", 12),
                                       fg='#FFF')
        boton_configuraciones.place(x=110, y=420, height=30, width=180)
        self.raiz.mainloop()

    def interfaz_login(self, datos):
        """Se genera un interfaz que permite a los jugadores iniciar sesión si ya estan registrados 
        ingresando su usuario y contraseña. Además esta interfaz cuenta con un botón para volver a la
        interfaz de registro.
        ## Juan Tejada
        ## Estrella Portocarrero"""
        self.loginFrame.pack(side="top", expand=True, fill="both")
        self.raiz.title("TP1 - Memotest - Ingreso")
        self.raiz.resizable(False, False)
        self.raiz.geometry("400x430")
        self.raiz.configure(bg='#FFF')
        titulo = Label(self.loginFrame, text="Ingrese sus datos para iniciar sesion", bg="#FFF",
                       font=("Ubuntu", 15, "bold"),
                       fg="#47126b")
        titulo.place(x=30, y=30)
        label_usuario = Label(self.loginFrame, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
        label_primer_contrasena = Label(self.loginFrame, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"),
                                        fg="#47126b")

        label_usuario.place(x=10, y=100)
        label_primer_contrasena.place(x=10, y=150)
        usuario_input = Entry(self.loginFrame, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
        usuario_input.place(x=140, y=100, height=30)
        primer_contrasena_input = Entry(self.loginFrame, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
        primer_contrasena_input.place(x=140, y=150, height=30)
        boton_registrado = Button(self.loginFrame,
                                  command=lambda: [self.loginFrame.pack_forget(), self.interfaz_registro(datos)],
                                  text="Registrarme",
                                  bd=0,
                                  bg="#47126b",
                                  font=("Ubuntu", 12), fg="#FFF")
        boton_registrado.place(x=125, y=300, height=30, width=150)

        boton_iniciar_sesion = Button(self.loginFrame, command=lambda: Registro().iniciar_sesion(usuario_input.get(),
                                                                                                 primer_contrasena_input.get(),
                                                                                                 self.mostrar_mensaje_login,
                                                                                                 self.mostrar_empezar_juego),
                                      text="Iniciar sesion", bd=0, bg="#47126b", font=("Ubuntu", 12), fg="#FFF")
        boton_iniciar_sesion.place(x=125, y=250, height=30, width=150)

    def guardar_datos(self, datos, usuario_input, primer_contrasena_input, segunda_contrasena_input):
        """Funcion que valida si el usuario ya está logueado, si está registrado y valida las contraseñas ingresadas.
        ## Juan Tejada
        """
        usuario = usuario_input.get()
        clave = primer_contrasena_input.get()
        segunda_clave = segunda_contrasena_input.get()
        if clave == segunda_clave:
            jugadores_logueados = Registro().jugadores_logueados
            jugadores_registrados = [usuario['usuario'] for usuario in Registro().obtener_usuarios()]

            if Registro().validar_usuario(usuario) is True and Registro().validar_clave(clave) is True:

                if usuario not in jugadores_registrados and clave == segunda_clave:
                    Registro().registrar_usuario({'usuario': usuario, 'clave': clave}, self.mostrar_empezar_juego)

                    usuario_input.delete(0, END)

                    primer_contrasena_input.delete(0, END)

                    segunda_contrasena_input.delete(0, END)

                    self.mostrar_mensaje_registro("Usuario registrado correctamente", True)
                else:
                    if usuario in jugadores_registrados:
                        self.mostrar_mensaje_registro("Ya está registrado", False)

                    elif usuario in jugadores_logueados:
                        self.mostrar_mensaje_registro("El jugador que intenta registrar ya esta logueado", False)

                    usuario_input.delete(0, END)

                    primer_contrasena_input.delete(0, END)

                    segunda_contrasena_input.delete(0, END)
            else:

                self.mostrar_mensaje_registro("Por favor lea las condiciones de registro.", False)

                self.interfaz_registro(datos)
        else:
            self.mostrar_mensaje_registro("Las contraseñas no coinciden", False)

    def mostrar_mensaje_login(self, mensaje, seLogueo):
        """Muestra un mensaje recibido como parámetro y el status del mismo (correcto o no)
        # Estrella Portocarrero"""
        self.labelLogin['text'] = mensaje
        if seLogueo:
            self.labelLogin['fg'] = "green"
        else:
            self.labelLogin['fg'] = "#e64040"
        self.labelLogin.place(x=10, y=200)

    def mostrar_mensaje_registro(self, mensaje, seRegistro):
        self.labelRegistro['text'] = mensaje
        if seRegistro:
            self.labelRegistro['fg'] = "green"
        else:
            self.labelRegistro['fg'] = "#e64040"
        self.labelRegistro.place(x=60, y=260)

    def info_configuraciones(self):
        config = Juego().leer_archivo_configuracion()
        datos = {"CANTIDAD_FICHAS": [16, 0], "MAXIMO_JUGADORES": [2, 0], "MAXIMO_PARTIDAS": [5, 0],
                 "REINICIAR_ARCHIV0_PARTIDAS": [False, 0]}
        mensaje = ""

        for parametro in config:

            if config[parametro][0] == str(datos[parametro][0]):

                mensaje += f"{parametro}: {config[parametro][0]} - Dado por defecto \n"

            else:

                mensaje += f"{parametro}: {config[parametro][0]} - Modificado por configuración \n"

        messagebox.showinfo(message=mensaje, title="Configuraciones")

    def info_usuario_clave(self):
        messagebox.showinfo(
            message="Su usuario debe tener una longitud entre 4 y 15 caracteres y estar formado sólo por letras, números y el bajo guion ' _ '"
                    "\nSu clave debe tener una longitud de 8 y 12 caraceteres, debe contener una letra mayus, una letra minus, un numero y los siguientes"
                    "caracteres: ' _ ' ' - '", title="¿Como obtengo un registro valido?")


def generar_interfaz():
    interfaz = Interfaz()
    datos = {}
    interfaz.interfaz_registro(datos)
