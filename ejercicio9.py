"""EJERCICIO 9.-  Escribe un programa que pida un número entero entre uno y doce
e imprima el número de días que tiene el mes correspondiente"""

mes = int(input("\nIngrese un número entero entre el uno y doce\n"))

if mes == 1:
    print("30 días")
elif mes == 2:
    print("28 días")
elif mes == 3:
    print("31 días")
elif mes == 4:
    print("30 días")
elif mes == 5:
    print("31 días")
elif mes == 6:
    print("30 días")
elif mes == 7:
    print("31 días")
elif mes == 8:
    print("31 días")
elif mes == 9:
    print("30 días")
elif mes == 10:
    print("31 días")
elif mes == 11:
    print("30 días")
elif mes == 12:
    print("31 días")
else:
    print("Error ---> Rango permitido: 1-12")

