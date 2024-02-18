def calcular_media(lista):

    if len(lista) == 0:
        return 0

    suma = sum(lista)

    media = suma / len(lista)
    return media

numeros = [5, 10, 15, 20]
resultado = calcular_media(numeros)
print("La media aritmética de la lista es:", resultado)

#el len es para leer la lista, la media se calcula sumando la lista y de ahi dividiendola por el numero de valores que hay, por eso el sum y el /
