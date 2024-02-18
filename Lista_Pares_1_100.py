def generar_lista_pares():

    lista_pares = []
    for numero in range(2, 101, 2):
        lista_pares.append(numero)
    return lista_pares

numeros_pares = generar_lista_pares()

print("Lista de números pares entre 1 y 100:")
print(numeros_pares)

#el primer 2 es para iniciar desde ese numero, el 101 es donde termina, y el otro 2 es para que remarque solo los pares
