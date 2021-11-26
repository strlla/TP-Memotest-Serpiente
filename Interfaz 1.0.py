from tkinter import *

datos = {}


def interfaz_registro(datos, raiz):
    frameRegistro = Frame(raiz)
    frameRegistro.pack(side="top", expand=True, fill="both")

    raiz.title("TP1 - Memotest - Registro")
    raiz.resizable(False, False)
    raiz.geometry("400x400")
    raiz.configure(bg='#FFF')
    titulo = Label(raiz, text="Ingrese sus datos para registrarse", bg="#FFF", font=("Ubuntu", 14, "bold"),
                   fg="#47126b")
    titulo.place(x=40, y=30)
    label_usuario = Label(raiz, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_primer_contrasena = Label(raiz, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_segunda_contrasena = Label(raiz, text="Repita la contraseña:", bg="#FFF",
                                     font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_usuario.place(x=10, y=100)
    label_primer_contrasena.place(x=10, y=150)
    label_segunda_contrasena.place(x=10, y=200)
    usuario_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
    usuario_input.place(x=220, y=100, height=30, width=170)
    primer_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
    primer_contrasena_input.place(x=220, y=150, height=30, width=170)
    segunda_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
    segunda_contrasena_input.place(x=220, y=200, height=30, width=170)
    boton_registrado = Button(raiz, command=lambda: [frameRegistro.pack_forget(), interfaz_login(datos, raiz)],
                              text="Ya estoy registrado",
                              bd=0,
                              bg="#47126b",
                              font=("Ubuntu", 12), fg="#FFF")
    boton_registrado.place(x=125, y=330, height=30, width=150)
    boton_registrarse = Button(raiz, command=lambda: guardar_datos(usuario_input, primer_contrasena_input,
                                                                   segunda_contrasena_input), text="Registrarse",
                               bd=0, bg="#47126b",
                               font=("Ubuntu", 12), fg="#FFF")
    boton_registrarse.place(x=150, y=280, height=30, width=100)
    raiz.mainloop()


def interfaz_registro_erroneo(datos):
    raiz = Tk()
    raiz.title("TP1 - Memotest - Registro")
    raiz.resizable(False, False)
    raiz.geometry("400x550")
    raiz.configure(bg='#FFF')
    titulo = Label(raiz, text="Ingrese sus datos para registrarse", bg="#FFF", font=("Ubuntu", 14, "bold"),
                   fg="#47126b")
    titulo.place(x=40, y=30)
    label_usuario = Label(raiz, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_primer_contrasena = Label(raiz, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_segunda_contrasena = Label(raiz, text="Ingrese su contraseña nuevamente:", bg="#FFF",
                                     font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_error = Label(raiz, text="Por favor, ingrese de nuevo su contraseña.\n "
                                   "Debe tener entre 8 y 12 caracteres alfanumericos \n 1 letra mayuscula, 1 minuscula"
                                   "\n y algunos de los siguientes caracteres '-' '_'", bg="#FFF",
                        font=("Ubuntu", 8, "bold"), fg="#47126b")
    label_usuario.place(x=10, y=100)
    label_primer_contrasena.place(x=10, y=200)
    label_segunda_contrasena.place(x=10, y=300)
    label_error.place(x=60, y=400)
    usuario_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
    usuario_input.place(x=100, y=140, height=30)
    primer_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
    primer_contrasena_input.place(x=100, y=240, height=30)
    segunda_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
    segunda_contrasena_input.place(x=100, y=340, height=30)

    boton_registrarse = Button(raiz, command=lambda: guardar_datos(usuario_input, primer_contrasena_input,
                                                                   segunda_contrasena_input), text="Registrarse",
                               bd=0, bg="#47126b",
                               font=("Ubuntu", 12), fg="#FFF")
    boton_registrarse.place(x=150, y=500, height=30, width=100)
    raiz.mainloop()


def interfaz_login(datos, raiz):
    frameLogin = Frame(raiz)
    frameLogin.pack(side="top", expand=True, fill="both")
    raiz.title("TP1 - Memotest - Ingreso")
    raiz.resizable(False, False)
    raiz.geometry("400x350")
    raiz.configure(bg='#FFF')
    titulo = Label(raiz, text="Ingrese sus datos para iniciar sesion", bg="#FFF", font=("Ubuntu", 15, "bold"),
                   fg="#47126b")
    titulo.place(x=30, y=30)
    label_usuario = Label(raiz, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_primer_contrasena = Label(raiz, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")

    label_usuario.place(x=10, y=100)
    label_primer_contrasena.place(x=10, y=150)
    usuario_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
    usuario_input.place(x=140, y=100, height=30)
    primer_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
    primer_contrasena_input.place(x=140, y=150, height=30)
    boton_registrado = Button(raiz, command=lambda: [frameLogin.pack_forget(), interfaz_registro(datos, raiz)],
                              text="Registrarme",
                              bd=0,
                              bg="#47126b",
                              font=("Ubuntu", 12), fg="#FFF")
    boton_registrado.place(x=125, y=250, height=30, width=150)

    boton_iniciar_sesion = Button(raiz, command=lambda: obtener_nombres(raiz, usuario_input, primer_contrasena_input,
                                                                        ), text="Iniciar sesion",
                                  bd=0,
                                  bg="#47126b",
                                  font=("Ubuntu", 12), fg="#FFF")
    boton_iniciar_sesion.place(x=125, y=300, height=30, width=150)

    raiz.mainloop()


def validar_usuario(usuario):
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


def validar_clave(clave):
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


def guardar_datos(usuario_input, primer_contrasena_input, segunda_contrasena_input):
    usuario = usuario_input.get()
    clave = primer_contrasena_input.get()
    segunda_clave = segunda_contrasena_input.get()

    if validar_usuario(usuario) is True and validar_clave(clave) is True:

        if usuario not in datos and clave == segunda_clave:
            datos[usuario] = clave

            usuario_input.delete(0, END)

            primer_contrasena_input.delete(0, END)

            segunda_contrasena_input.delete(0, END)

    else:

        interfaz_registro_erroneo(datos)


raiz = Tk()
interfaz_registro(datos, raiz)
print(datos)
