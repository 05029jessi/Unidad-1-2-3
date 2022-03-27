""" EJERCICIO 6.- Calcular el área y el perímetro de un Rectángulo
En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo, para ello deberemos crear las siguientes variables:
alto (int)
ancho (int)
El usuario debe proporcionar los valores de largo y ancho, y después se debe imprimir el resultado en el siguiente formato(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):
Proporciona el alto:
Proporciona el ancho:
Area: <area>
Perímetro: <perimetro>"""

import math                                      # librería que propoprciona funciones matemáticas como pi, factorial, e

print("\nCÁLCULO DEL ÁREA Y PERÍMETRO DE UN RECTÁNGULO")
print("\nIngrese el alto")
alto = int(input())          #el int restringe a que solo se ingrese por teclado números enteros

print("Ingrese el ancho")
ancho = int(input())  

A =  alto*ancho
P =  (2*alto)+(2*ancho)
#print("El perímetro es:", round(P, 3),"cm\n")

print(f"\nProporciona el alto: {alto}cm")
print(f"Proporciona el ancho: {ancho}cm")
print(f"Área: <{A}cm>")
print(f"Perímetro: <{P}cm>\n")
