from os import system

def generador_fichas():
    # shuffle(fichas) Esto serviria para la aleatoriedad mas adelante

    fichas = ["D", "D", "s", "s"]  # FICHAS DADAS POR ENUNCIADO

    return fichas


def ocultar_fichas(fichas):
    fichas_ocultas = []

    for numeros in range(len(fichas)):  # ITERO SEGUN LA LONGITUD DE LAS FICHAS DADAS PARA OCULTARLAS COMO NUMEROS
        fichas_ocultas.append(str([numeros]))

    return fichas_ocultas

def jugada(fichas, fichas_ocultas):
    print("Fichas y posiciones:", *fichas_ocultas)
    
    while True:
        resultado = seleccionar_posiciones(fichas, fichas_ocultas)

        if resultado:
            break 
        else:        
            system("cls")

            print("Intenta nuevamente")

            fichas = generador_fichas()

            fichas_ocultas = ocultar_fichas(fichas)

            print("Fichas y posiciones:", *fichas_ocultas)        

def seleccionar_posiciones(fichas, fichas_ocultas):
    # funcion que permite el ingreso de las posiciones a descubrir en las fichas y retorna True en caso de que sean iguales, en caso contrario retorna False
    primer_posicion = int(input("1er posición: "))

    fichas_ocultas = mostrar_ficha(primer_posicion, fichas, fichas_ocultas)

    segunda_posicion = int(input("2da posición: "))

    fichas_ocultas = mostrar_ficha(segunda_posicion, fichas, fichas_ocultas)

    resultado = comparar_fichas(primer_posicion, segunda_posicion, fichas)

    return resultado


def comparar_fichas(primera_posicion, segunda_posicion, fichas):
    # compara el contenido de la ficha en las dos posiciones recibidas, retorna True si son iguales, en caso contrario retorna False
    return fichas[primera_posicion] == fichas[segunda_posicion]

def mostrar_ficha(posicion, fichas, fichas_ocultas):
    # printea las fichas ocultas y las descubiertas por el usuario
    fichas_ocultas = [i.replace(str(posicion), fichas[posicion]) for i in fichas_ocultas]

    print("Fichas y posiciones:", *fichas_ocultas)

    return fichas_ocultas

def main():
    fichas = generador_fichas()
    fichas_ocultas = ocultar_fichas(fichas)
    jugada(fichas, fichas_ocultas)


main()
