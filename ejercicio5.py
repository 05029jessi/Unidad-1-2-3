""" EJERCICIO 5.- Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos"""

import math

print("\nIngrese la cantidad de minutos")     
in_min=int(input())                                    #int= convierte un dato string a entero
horas = in_min/60

deci, entero = math.modf(horas)                        #función que permite separar parte entera y decimal
minutos = deci*60
deci_min, entero_min = math.modf(minutos)

print(int(in_min),"minutos son",int(entero),"horas y", int(entero_min), "minutos.")     #int: imprime valores enteros

