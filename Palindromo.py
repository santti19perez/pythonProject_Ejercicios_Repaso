def es_palindromo(cadena):

    cadena = cadena.lower().replace(" ", "")

    return cadena == cadena[::-1]

cadena = input("Ingrese una cadena de texto para verificar si es un palíndromo: ")

if es_palindromo(cadena):
    print("La cadena '{}' es un palíndromo.".format(cadena))
else:
    print("La cadena '{}' no es un palíndromo.".format(cadena))

#este me dio mucha lidia pero simplemente uso un operador inverso para que lea la palabra al derecho y al revez e identifique si es o no es palindromo
