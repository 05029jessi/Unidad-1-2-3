"""EJERCICIO 15.- Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número 
entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor 
que el introducido. El programa termina cuando se acierta el número."""

adivinar=int(input("Ingresar el número a adivinar: "))
numero=int(input("Ingresar un número: "))

while numero!=adivinar:
    if numero>adivinar:
        print("El número a adivinar es menor que el introducido")
        numero=int(input("Ingresar un número: "))
    else:
        print("El número a adivinar es mayor que el introducido")
        numero=int(input("Ingresar un número: "))

print("Número correcto")