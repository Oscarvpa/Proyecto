"Vargas Palencia Oscar Adrian"
"FAcultad de ingenieria, UNAM , Analisis Numerico,"

import numpy as np
def f(V,P, func_str):
    np_functions = {"exp": np.exp, "sin": np.sin, "cos": np.cos, "tan": np.tan, "log": np.log, "sqrt": np.sqrt}
    return eval(func_str, {"V": V, "P": P}, np_functions)


func_str = input("Ingrese la función f(x, y): ")

V_0 = float(input("Ingrese el valor inicial de V: "))
P_0 = float(input("Ingrese el valor inicial de P: "))
n = int(input("Ingrese el valor de n: "))
h = float(input("Ingrese el valor de h: "))

V = np.zeros(n+1)
P = np.zeros(n+1) 
k1 = np.zeros(n+1)
k2 = np.zeros(n+1)
k3 = np.zeros(n+1)
k4 = np.zeros(n+1)
V[0]=V_0
P[0]=P_0

print('{:^12} {:^20}'.format('V','P_numerica'))
print('{:10.5f} {:20.5f}'.format(V[0], P[0]))

for i in range(1, n+1):
    V[i] = V[i - 1] + h
    k1[i] = h * f(V[i - 1], P[i - 1], func_str)
    k2[i] = h * f(V[i - 1] + (h / 2), P[i - 1] + (k1[i] / 2), func_str)
    k3[i] = h * f(V[i - 1] + (h / 2), P[i - 1] + (k2[i] / 2), func_str)
    k4[i] = h * f(V[i - 1] + h, P[i - 1] + k3[i], func_str)
    P[i] = P[i - 1] + (1 / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
    print('{:10.5f} {:20.5f}'.format(V[i], P[i]))
