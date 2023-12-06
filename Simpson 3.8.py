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

print ("====== Método de Integración Numérica: SIMPSON 1/3 ======\n")

h = (x1 - x2) / n  

total_simpson_1 = 0

for i in range(1, n):
    x = a + (i * h)
    if i % 2 == 0:
        total_simpson_1 += 2 * evaluacion(x)
    else:
        total_simpson_1 += 4 * evaluacion(x)

total_simpson_1 += evaluacion(x1) + evaluacion(x2)
total_simpson_1 = total_simpson_1 * ((1 / 3) * h)

print(f"\nResultado de la aproximación (Simpson 1/3): {total_simpson_1}")

print ("\n====== Método de Integración Numérica: SIMPSON 3/8 ======\n")
h = (x1 - x2) / n  
total_simpson_38 = 0

for O in range(1, n):
    x = a + (O * h)
    if O % 3 == 0:
        total_simpson_38 += 2 * evaluacion(x)
    else:
        total_simpson_38 += 3 * evaluacion(x)

total_simpson_38 += evaluacion(x1) + evaluacion(x2)
total_simpson_38 = total_simpson_38 * ((3 / 8) * h)

print(f"\n Resultado de la aproximación (Simpson 3/8):\n {total_simpson_38}")
