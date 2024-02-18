def encontrar_extremos(lista):

    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = [11, 10, 15, 20]
maximo, minimo = encontrar_extremos(numeros)
print("El número más grande en la lista es:", maximo)
print("El número más pequeño en la lista es:", minimo)

#El max y el Min son operadores que ya conocia, que toman el valor menor y el valor mayor de la (lista)
