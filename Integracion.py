"Vargas Palencia Oscar Adrian"
"FAcultad de ingenieria, UNAM , Analisis Numerico"

from math import *

def evaluacion(x):
    copia = funcion.copy()
    for i in range(len(copia)):
        if copia[i] == "x":
            copia[i] = str(x)
    return eval("".join(copia))

print("Integracion Numerica: SIMPSON 1/3 ")

funcion = list(input("Ingresa la funcion \n "))  

x1 = float(input("ingresa el intervalo inferior de la integral: "))

x2 = float(input("ingresa el intervalo superior de la integral: "))

n = int(input("¿Cuál es el valor de n? "))

h = (x1 - x2) / n 
total = 0  


for k in range(1, n):  
    x = a + (k * h) 
    if k % 2 == 0:
        total += 2 * evaluacion(x)
    else:
        total += 4 * evaluacion(x)

total += evaluacion(a) + evaluacion(b)
total = total * ((1 / 3) * h)  
x
print( f"\n Resultado de la aproximación = {total}")