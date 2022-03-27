"""EJERCICIO 10.- Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, sino se da un error."""

nombre = input("Usuario: ")
contraseña = input("Contraseña: ")

if nombre == "pepe" and contraseña == "passwd#":
    print("Has entrado al sistema")
else:
    print("Error")
