import random

def generar_lista_numeros_aleatorios(longitud, limite_inferior, limite_superior):

    return [random.randint(limite_inferior, limite_superior) for _ in range(longitud)]

longitud = int(input("Ingrese la longitud de la lista de números aleatorios: "))
limite_inferior = int(input("Ingrese el límite inferior para los números aleatorios: "))
limite_superior = int(input("Ingrese el límite superior para los números aleatorios: "))

numeros_aleatorios = generar_lista_numeros_aleatorios(longitud, limite_inferior, limite_superior)

print("Lista de números aleatorios:")
print(numeros_aleatorios)

#aca con una libreria importo numeros randoms y quise añadirle que el usuario pida numero menos, mayor y la cantidad de valores
