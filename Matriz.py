def imprimir_matriz(matriz):

    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz generada:")
imprimir_matriz(matriz)

#use un tabulador que encontre igual en youtube el cual es "\t" que sirve para ordenar la lista en filas y columnas y quede diseñada como una matriz
