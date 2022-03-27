"""EJERCICIO 13.- Pedir un número por teclado y mostrar la tabla de multiplicar"""

numero = int(input("Ingresar un número: "))

for i in range (1,13):
    mult=i*numero
    print(f"{i}*{numero}={mult}")

