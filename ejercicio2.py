""" EJERCICIO 2.- Calcular el perímetro y área de un círculo dado su radio"""
import math                                      # librería que propoprciona funciones matemáticas como pi, factorial, e

#VARIABLES
pi = math.pi                                     #Para imrpimir pi: print(pi)
r = 6                                            #radio

#print(type(r))                                     imprimir el tipo de dato
print("\nCÁLCULO DEL ÁREA Y PERÍMETRO DE UN CÍRCULO")
#print("El radio del círculo es"+" "+str(r)+"cm")   primera forma de imprimir
print("\nSi su radio es:", r,"cm")           #segunda forma de imprimir

A =  pi*math.pow(r,2)
print("\nEl área es:", round(A, 3),"cm")  

P =  2*pi*r
print("El perímetro es:", round(P, 3),"cm\n")
