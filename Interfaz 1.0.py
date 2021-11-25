from tkinter import *

datos = {}


def interfaz_registro(datos):
    raiz = Tk()
    raiz.title("TP1 - Memotest - Registro")
    raiz.resizable(False, False)
    raiz.geometry("400x500")
    raiz.configure(bg='#FFF')
    titulo = Label(raiz, text="Ingrese sus datos para registrarse", bg="#FFF", font=("Ubuntu", 14, "bold"),
                   fg="#47126b")
    titulo.place(x=40, y=30)
    label_usuario = Label(raiz, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_primer_contrasena = Label(raiz, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_segunda_contrasena = Label(raiz, text="Ingrese su contraseña nuevamente:", bg="#FFF",
                                     font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_usuario.place(x=10, y=100)
    label_primer_contrasena.place(x=10, y=200)
    label_segunda_contrasena.place(x=10, y=300)
    usuario_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
    usuario_input.place(x=100, y=140, height=30)
    primer_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
    primer_contrasena_input.place(x=100, y=240, height=30)
    segunda_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
    segunda_contrasena_input.place(x=100, y=340, height=30)
    boton_registrado = Button(raiz, command=lambda: interfaz_login(datos),
                              text="Ya estoy registrado",
                              bd=0,
                              bg="#47126b",
                              font=("Ubuntu", 12), fg="#FFF")
    boton_registrado.place(x=125, y=400, height=30, width=150)
    boton_registrarse = Button(raiz, command=lambda: guardar_datos(usuario_input, primer_contrasena_input,
                                                                   segunda_contrasena_input), text="Registrarse",
                               bd=0, bg="#47126b",
                               font=("Ubuntu", 12), fg="#FFF")
    boton_registrarse.place(x=150, y=450, height=30, width=100)
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


def interfaz_login(datos):
    raiz = Tk()
    raiz.title("TP1 - Memotest - Ingreso")
    raiz.resizable(False, False)
    raiz.geometry("400x350")
    raiz.configure(bg='#FFF')
    titulo = Label(raiz, text="Ingrese sus datos para iniciar sesion", bg="#FFF", font=("Ubuntu", 13, "bold"),
                   fg="#47126b")
    titulo.place(x=50, y=30)
    label_usuario = Label(raiz, text="Usuario:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")
    label_primer_contrasena = Label(raiz, text="Contraseña:", bg="#FFF", font=("Ubuntu", 14, "bold"), fg="#47126b")

    label_usuario.place(x=10, y=100)
    label_primer_contrasena.place(x=10, y=200)
    usuario_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12))
    usuario_input.place(x=100, y=140, height=30)
    primer_contrasena_input = Entry(raiz, bd=0, bg="#d1fff4", font=("Ubuntu", 12), show="*")
    primer_contrasena_input.place(x=100, y=240, height=30)
    boton_iniciar_sesion = Button(raiz, command=lambda: obtener_nombres(raiz, usuario_input, primer_contrasena_input,
                                                                        ), text="Iniciar sesion",
                                  bd=0,
                                  bg="#47126b",
                                  font=("Ubuntu", 12), fg="#FFF")
    boton_iniciar_sesion.place(x=125, y=300, height=30, width=150)

    raiz.mainloop()


def validar_usuario(usuario):
    """Valida el usuario segun las condiciones dadas en el enunciado"""
    usuario_valido = False

    guion = 0
    numero = 0
    letra = 0

    if 4 <= len(usuario) <= 15:

        for caracter in usuario:

            if caracter == '_':

                guion += 1

            elif caracter.isnumeric() is True:

                numero += 1

            elif caracter.isalpha() is True:

                letra += 1

    if guion >= 1 and numero >= 1 and letra >= 1:
        usuario_valido = True

    return usuario_valido


def validar_clave(clave):
    """Valida la clave segun las condiciones dadas en el enunciado"""

    guiones = 0
    numeros = 0
    mayu_minu = 0
    acentos = 0
    tildes = ['ÁÉÍÓÚáéíóú']

    clave_valida = False

    if 8 < len(clave) < 12:

        for letra in clave:

            if letra == '-' or letra == '_':

                guiones += 1

            elif letra.isnumeric():

                numeros += 1

            elif letra.isupper() or letra.islower():

                mayu_minu += 1

            elif letra in tildes:

                acentos += 1

    if guiones >= 1 and numeros >= 1 and mayu_minu >= 2 and acentos == 0:
        clave_valida = True

    return clave_valida


def guardar_datos(usuario_input, primer_contrasena_input, segunda_contrasena_input):
    usuario = usuario_input.get()
    primer_clave = primer_contrasena_input.get()
    segunda_clave = segunda_contrasena_input.get()

    datos[usuario] = primer_clave



