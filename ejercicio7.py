"""EJERCICIO 7.- Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero."""


a = int(input("\nIngrese el valor de a: "))       #Imprime el texto a la misma vez que se ingresa por teclado
b = int(input("Ingrese el valor de b: "))

suma = a+b

if suma > 0:
    print("Es un valor positivo")
elif suma < 0:
    print("Es un valor negativo")
else:
    print("El valor es 0")

    