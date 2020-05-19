
def programa ():
    minusculas = 0
    mayusculas = 0
    espacio = 0
    numeros = 0
    cadena = input('Ingrese una cadena de texto')
    largo_cadena = len(cadena)
    for letra in cadena:
        if letra >= 'a' and letra <= 'z':
            minusculas += 1
        elif letra >= 'A' and letra <= 'Z':
            mayusculas += 1
        elif letra == ' ':
            espacio  += 1
        elif letra >= '0' and letra <= '9':
            numeros += 1


    print('Su texto tiene {} minusculas, {} mayusculas, {} espacios, {} numeros y tiene una logitud de {} '.format(minusculas, mayusculas, espacio, numeros, largo_cadena))



if __name__ == '__main__':
    continuar = 1
    while continuar == 1:
        programa()
        continuar = input('Desea ingresar otra cadena? (1 para continuar, 0 para terminar)')

