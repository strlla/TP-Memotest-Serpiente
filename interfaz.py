from tkinter import *
import tkinter as tk
from tkinter import messagebox
from login_registro import iniciar_sesion

class Interfaz:
    def __init__(self) -> None:
        self.raiz = tk.Tk()
        self.loginFrame = Frame(self.raiz, bg="#FFF")
        self.registroFrame = Frame(self.raiz, bg="#FFF")
        self.label_login = Label(self.loginFrame, text="", bg="#FFF", font=("Ubuntu", 12), fg="#e64040")


    def interfaz_registro(self, datos):
        self.registroFrame.pack(side="top", expand=True, fill="both")

        self.raiz.title("TP1 - Memotest - Registro")
        self.raiz.resizable(False, False)
        self.raiz.geometry("400x430")
        self.raiz.configure(bg='#FFF')
        titulo = Label(self.registroFrame, text="Ingrese sus datos para registrarse", bg="#FFF", font=("Ubuntu", 14, "bold"),
                    fg="#47126b")
        titulo.place(x=40, y=30)
        label_usuario = Label(self.registroFrame, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
        label_primer_contrasena = Label(self.registroFrame, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
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
        boton_registrarse = Button(self.registroFrame, command=lambda: self.guardar_datos(datos, self.raiz, usuario_input, primer_contrasena_input,
                                                                    segunda_contrasena_input), text="Registrarse",
                                bd=0, bg="#47126b",
                                font=("Ubuntu", 12), fg="#FFF")
        boton_registrarse.place(x=150, y=280, height=30, width=100)
        boton_registrado = Button(self.registroFrame, command=lambda: [self.registroFrame.pack_forget(), self.interfaz_login(datos)],
                                text="Ya estoy registrado",
                                bd=0,
                                bg="#47126b",
                                font=("Ubuntu", 12), fg="#FFF")
        boton_registrado.place(x=125, y=330, height=30, width=150)
        boton_condicion_registro = Button(self.registroFrame, command=lambda: self.info_usuario_clave(), text="Condiciones de registro", bd=0, bg="#47126b", font=("Ubuntu", 12), fg='#FFF')
        boton_condicion_registro.place(x=110, y=380, height=30, width=180)
        self.raiz.mainloop()      

    def interfaz_login(self, datos):
        self.loginFrame.pack(side="top", expand=True, fill="both")
        self.raiz.title("TP1 - Memotest - Ingreso")
        self.raiz.resizable(False, False)
        self.raiz.geometry("400x350")
        self.raiz.configure(bg='#FFF')
        titulo = Label(self.loginFrame, text="Ingrese sus datos para iniciar sesion", bg="#FFF", font=("Ubuntu", 15, "bold"),
                    fg="#47126b")
        titulo.place(x=30, y=30)
        label_usuario = Label(self.loginFrame, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
        label_primer_contrasena = Label(self.loginFrame, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")

        label_usuario.place(x=10, y=100)
        label_primer_contrasena.place(x=10, y=150)
        usuario_input = Entry(self.loginFrame, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
        usuario_input.place(x=140, y=100, height=30)
        primer_contrasena_input = Entry(self.loginFrame, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
        primer_contrasena_input.place(x=140, y=150, height=30)
        boton_registrado = Button(self.loginFrame, command=lambda: [self.loginFrame.pack_forget(), self.interfaz_registro(datos)],
                                text="Registrarme",
                                bd=0,
                                bg="#47126b",
                                font=("Ubuntu", 12), fg="#FFF")
        boton_registrado.place(x=125, y=250, height=30, width=150)

        boton_iniciar_sesion = Button(self.loginFrame, command=lambda: iniciar_sesion(usuario_input.get(), primer_contrasena_input.get(), self.mostrar_mensaje_login,), text="Iniciar sesion", bd=0, bg="#47126b", font=("Ubuntu", 12), fg="#FFF")
        boton_iniciar_sesion.place(x=125, y=300, height=30, width=150)
    
    def guardar_datos(self, raiz, datos, usuario_input, primer_contrasena_input, segunda_contrasena_input):
        usuario = usuario_input.get()
        clave = primer_contrasena_input.get()
        segunda_clave = segunda_contrasena_input.get()

        if self.validar_usuario(usuario) is True and self.validar_clave(clave) is True:

            if usuario not in datos and clave == segunda_clave:
                datos[usuario] = clave

                usuario_input.delete(0, END)

                primer_contrasena_input.delete(0, END)

                segunda_contrasena_input.delete(0, END)

        else:

            if self.datos_erroneos() is True:
                self.interfaz_registro(datos, self.raiz)

    def mostrar_mensaje_login(self, mensaje):
        self.label_login['text'] = mensaje      
        self.label_login.place(x=10, y=200)
        
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


    def datos_erroneos(self):
        return messagebox.askretrycancel(message="Por favor, lea las condiciones de registro de usuario y clave "
                                                "¿Desea reintentar?", title="Error")


    def info_usuario_clave(self):
        messagebox.showinfo(message="Su usuario debe tener una longitud entre 4 y 15 caracteres y estar formado sólo por letras, números y el bajo guion ' _ '"
                                    "\nSu clave debe tener una longitud de 8 y 12 caraceteres, debe contener una letra mayus, una letra minus, un numero y los siguientes"
                                    "caracteres: ' _ ' ' - '", title="¿Como obtengo un registro valido?")

      
def generar_interfaz():
    interfaz = Interfaz()
    datos = {}
    interfaz.interfaz_registro(datos)  