"""EJERCICIO 14.- Crea una aplicación que pida un número y calcule su factorial 
(El factorial de un número es el producto de todos los enteros entre 1 y el propio número y
se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120"""

numero = int(input("Ingresar un número: "))

if numero !=0:
    fact = 1
    for i in range(1,numero+1):      #range(inicio de i, fin de i (se debe añadir un número más)   )
        fact= i*fact
    print(f"El factorial de", numero,"! es:",fact)

else:
    print("Ha ingresado 0, por favor ingrese un valor positivo")

