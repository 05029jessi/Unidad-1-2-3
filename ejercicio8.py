"""EJERCICIO 8.-  Escribe un programa que lea un número e indique si es par o impar."""

import math                                     

print("\nNÚMERO PAR E IMPAR")
print("\nIngrese un número")
alto = int(input())                 #el int restringe a que solo se ingrese por teclado números enteros

if alto % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")