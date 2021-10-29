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

    fichas_ocultas = [i.replace(str(primer_posicion), fichas[primer_posicion]) for i in fichas_ocultas]

    print("Fichas y posiciones:", *fichas_ocultas)

    segunda_posicion = int(input("2da posición: "))

    fichas_ocultas = [i.replace(str(segunda_posicion), fichas[segunda_posicion]) for i in fichas_ocultas]

    if fichas_ocultas[primer_posicion] == fichas_ocultas[segunda_posicion]:
        print("Fichas y posiciones:", *fichas_ocultas)

        primer_posicion = int(input("1er posición: "))

        fichas_ocultas = [i.replace(str(primer_posicion), fichas[primer_posicion]) for i in fichas_ocultas]

        print("Fichas y posiciones:", *fichas_ocultas)

        segunda_posicion = int(input("2da posición: "))

        fichas_ocultas = [i.replace(str(segunda_posicion), fichas[segunda_posicion]) for i in fichas_ocultas]

        print(*fichas_ocultas)

    else:
        print("Intenta nuevamente")

        fichas = generador_fichas()

        nuevas_fichas_ocultas = ocultar_fichas(fichas)

        print("Fichas y posiciones:", *nuevas_fichas_ocultas)

        primer_posicion = int(input("1er posición: "))

        nuevas_fichas_ocultas = [i.replace(str(primer_posicion), fichas[primer_posicion]) for i in
                                 nuevas_fichas_ocultas]

        print("Fichas y posiciones:", *nuevas_fichas_ocultas)

        segunda_posicion = int(input("2da posición: "))

        nuevas_fichas_ocultas = [i.replace(str(segunda_posicion), fichas[segunda_posicion]) for i in nuevas_fichas_ocultas]

        print("Fichas y posiciones:", *nuevas_fichas_ocultas)


def main():
    fichas = generador_fichas()
    fichas_ocultas = ocultar_fichas(fichas)
    seleccionar_posiciones(fichas, fichas_ocultas)


main()
