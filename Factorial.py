def factorial(numero):

    if numero == 0 or numero == 1:
        return 1
    else:

        resultado = 1

        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)

#si el numero es 0 o 1 el resultado es 1, de lo contrario se resuelve tal cual la formula que investigue, la cual es iniciar en 1 y multipilcar todos los valores desde 2
