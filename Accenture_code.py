# -*- coding: utf-8 -*-
"""

Created on Fri Sep 17 10:46:50 2021

@author: CarinaG
"""

'''Haga un programa que lea un número indeterminado de valores, correspondientes a notas,
 finalizando la entrada de datos cuando se ingresa un valor de -1 (que no debe almacenarse).
Después de esta entrada de datos, haga:

. Muestra la cantidad de valores que se han leído;

. Mostrar todos los valores en el orden en que se informaron, uno al lado del otro;

. Mostrar todos los valores en el orden inverso al que fueron informados, uno debajo del otro;

. Calcule y muestre la suma de los valores;

. Calcular y mostrar el promedio de los valores;

. Calcule y muestre la cantidad de valores por encima del promedio calculado;

. Calcule y muestre el número de valores por debajo de siete;

. Termine el programa con un mensaje;'''


lista=[]
num=int(input("Ingresa un valor: "))
while num != -1:
   
    lista.append(num)
    num=int(input("Ingresa un valor: "))
    
cant=len(lista)
print("La cantidad de valores que se han ingresado es: ", cant)
print("Se ingresaron lo siguientes números en este orden: ",lista)
print("La lista de valores en orden inverso es: ", lista.reverse())
suma=sum(lista)
print("la suma de los valores ingresados es: ", suma)
prom=suma/cant
print("El promedio de los valores es: ",suma/cant)


#funcion que muestra los valores ingresados menores que 7
def mayor7(lista):return lista<7
t=filter(mayor7, lista)
print("El listado de números ingresados que cumplen con el requisito de ser menores a 7 son: ",list(t))
#. Calcule y muestre la cantidad de valores por encima del promedio calculado;
def mayor_prom(lista):return lista > prom
to=filter(mayor_prom, lista)
print("El listado de valores ingresados que son superiores al promedio son: ",list(to))