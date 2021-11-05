from os import system

def generador_fichas():
    # shuffle(fichas) Esto serviria para la aleatoriedad mas adelante

    fichas = ["D", "D", "s", "s"]  # FICHAS DADAS POR ENUNCIADO

    return fichas

def revisar_fichas(fichas, fichas_ocultas): 
    #funcion que revisa si todas las fichas estan descubiertas (si el jugador gano) y retorna True, en caso contrario retorna False
    # Estrella Portocarrero 
    return all(ficha == ficha_oculta[1] for ficha, ficha_oculta in zip(fichas, fichas_ocultas))

def ocultar_fichas(fichas):
    # Se itera segun la longitud de las fichas dadas para ocultarlas como numeros
    fichas_ocultas = []

    for numeros in range(len(fichas)):  
        fichas_ocultas.append(str([numeros]))

    return fichas_ocultas

def jugada(fichas, fichas_ocultas):
    #funcion principal que permite al jugador seguir jugando mientras encuentre pares iguales, caso contrario se resetean las fichas.
    #Estrella Portocarrero
    
    print("Fichas y posiciones:", *fichas_ocultas)
    gano = False
    while not gano:
        resultado, fichas_ocultas = seleccionar_posiciones(fichas, fichas_ocultas)
        if resultado:
            gano = revisar_fichas(fichas, fichas_ocultas)
        else:        
            system("cls")

            print("Intenta nuevamente")

            fichas = generador_fichas()

            fichas_ocultas = ocultar_fichas(fichas)

            print("Fichas y posiciones:", *fichas_ocultas)        

    print("Ganaste!")
    
def seleccionar_posiciones(fichas, fichas_ocultas):
    # funcion que permite el ingreso de las posiciones a descubrir en las fichas y retorna True en caso de que sean iguales, en caso contrario retorna False
    
    primer_posicion = input("1er posición: ")
    primer_es_valido = validar_ingreso(primer_posicion, fichas_ocultas)
    while not primer_es_valido:
      primer_posicion = input("1er posición: ")
      primer_es_valido = validar_ingreso(primer_posicion, fichas_ocultas)
    primer_posicion = int(primer_posicion)
    
    fichas_ocultas = mostrar_ficha(primer_posicion, fichas, fichas_ocultas)

    segunda_posicion = input("2da posición: ")
    segundo_es_valido = validar_ingreso(segunda_posicion, fichas_ocultas)
    while not segundo_es_valido:
        segunda_posicion = input("2da posición: ")
        segundo_es_valido = validar_ingreso(segunda_posicion, fichas_ocultas)
    segunda_posicion = int(segunda_posicion)

    fichas_ocultas = mostrar_ficha(segunda_posicion, fichas, fichas_ocultas)

    resultado = comparar_fichas(primer_posicion, segunda_posicion, fichas)

    return resultado, fichas_ocultas


def comparar_fichas(primera_posicion, segunda_posicion, fichas):
    # compara el contenido de la ficha en las dos posiciones recibidas, retorna True si son iguales, en caso contrario retorna False
    return fichas[primera_posicion] == fichas[segunda_posicion]

def mostrar_ficha(posicion, fichas, fichas_ocultas):
    # printea las fichas ocultas y las descubiertas por el usuario
    fichas_ocultas = [i.replace(str(posicion), fichas[posicion]) for i in fichas_ocultas]

    print("Fichas y posiciones:", *fichas_ocultas)

    return fichas_ocultas

def validar_ingreso(posicion, fichas_ocultas):    
    #Funcion que chequea que la posicion ingresada sea numerica  y sea menor o igual a la cantidad de fichas, falta validar que este disponible
    #Estrella Portocarrero
    if not posicion.isnumeric():
        print("Ingrese un valor numerico")
        return False
    else: 
        if int(posicion) > len(fichas_ocultas) - 1 or int(posicion) < 0:
            print("Ingrese un numero menor o igual a ",len(fichas_ocultas) - 1)
            return False
        elif not fichas_ocultas[int(posicion)][1].isnumeric():
            print("Esta ficha ({}) no esta disponible".format(fichas_ocultas[int(posicion)][1]))
            return False
            
    return True, ""

def main():
    fichas = generador_fichas()
    fichas_ocultas = ocultar_fichas(fichas)
    jugada(fichas, fichas_ocultas)


main()
