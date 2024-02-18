import math

def calcular_area_circulo(radio):

    area = math.pi * radio**2
    return area

radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area)

#Profe hola, como estas? si lees esta nota quiero pedirle perdon por usar Pycharm, se que ud quiere
#que trabajemos en VisualStudio pero tengo muchos problemas y no he podido con esa APP, le pido me entienda
#y permita almenos en esta ocasion trabajar en Pycharm, que sigue siendo un buen ambiente para programar.
