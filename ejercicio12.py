"""EJERCICIO 12.- Programa que lea un carácter por teclado y compruebe si es una letra mayúscula."""

caracter = input("Ingresar caracter: ")		

if caracter >= "A" and caracter <= "Z":
    print("Es una letra mayúscula")
else:
    print("El  caracter no es una letra mayúscula")