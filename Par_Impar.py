def es_par_o_impar(numero):

    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Ingrese un número para determinar si es par o impar: "))

resultado = es_par_o_impar(numero)

print("El número", numero, "es", resultado)

#se divide el numero que el usuario ingrese por 2 (%) y si es == 0 es par

