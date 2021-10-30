def generador_fichas():
    # shuffle(fichas) Esto serviria para la aleatoriedad mas adelante

    fichas = ["D", "D", "s", "s"]  # FICHAS DADAS POR ENUNCIADO

    return fichas


def ocultar_fichas(fichas):
    fichas_ocultas = []

    for numeros in range(len(fichas)):  # ITERO SEGUN LA LONGITUD DE LAS FICHAS DADAS PARA OCULTARLAS COMO NUMEROS
        fichas_ocultas.append(str([numeros]))

    return fichas_ocultas


def seleccionar_posiciones(fichas, fichas_ocultas):
    print("Fichas y posiciones:", *fichas_ocultas)

    primer_posicion = int(input("1er posición: "))

    fichas_ocultas = mostrar_ficha(primer_posicion, fichas, fichas_ocultas)

    segunda_posicion = int(input("2da posición: "))

    fichas_ocultas = mostrar_ficha(segunda_posicion, fichas, fichas_ocultas)

    resultado = comparar_fichas(primer_posicion, segunda_posicion, fichas)
   
    if resultado:
        primer_posicion = int(input("1er posición: "))

        fichas_ocultas = mostrar_ficha(primer_posicion, fichas, fichas_ocultas)

        segunda_posicion = int(input("2da posición: "))

        fichas_ocultas = mostrar_ficha(segunda_posicion, fichas, fichas_ocultas)

        print(*fichas_ocultas)

    else:
        print("Intenta nuevamente")

        fichas = generador_fichas()

        nuevas_fichas_ocultas = ocultar_fichas(fichas)

        primer_posicion = int(input("1er posición: "))

        nuevas_fichas_ocultas = mostrar_ficha(primer_posicion, fichas, nuevas_fichas_ocultas)

        segunda_posicion = int(input("2da posición: "))

        nuevas_fichas_ocultas = mostrar_ficha(segunda_posicion, fichas, nuevas_fichas_ocultas)

def comparar_fichas(primera_posicion, segunda_posicion, fichas):
    # nos fijamos si el contenido en ambas posiciones es igual
    return fichas[primera_posicion] == fichas[segunda_posicion]

def mostrar_ficha(posicion, fichas, fichas_ocultas):
    fichas_ocultas = [i.replace(str(posicion), fichas[posicion]) for i in fichas_ocultas]

    print("Fichas y posiciones:", *fichas_ocultas)

    return fichas_ocultas

def main():
    fichas = generador_fichas()
    fichas_ocultas = ocultar_fichas(fichas)
    seleccionar_posiciones(fichas, fichas_ocultas)


main()
