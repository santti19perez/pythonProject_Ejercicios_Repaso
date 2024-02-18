def fahrenheit_a_celsius(grados_fahrenheit):

    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print("La temperatura en grados Celsius es:", celsius)

#la operacion la encontre en un libro de operaciones, la cual es Grados F - 32 * 5/9


