"Vargas Palencia Oscar Adrian"
"FAcultad de ingenieria, UNAM , Analisis Numerico"
import numpy as np

m=int(input("Numero de renglones"))
matriz=np.zeros([m,m])
U=np.zeros([m,m])
L=np.zeros([m,m])
print("Ingrese los elementos de la matriz:")
for V in range (0,m
    for P in range(0,m 
      matriz(V,P)=(input("Elemento a ["+str(V+1)+","+str(P+1)+"]"))
      matriz(V,P)=float(Xatriz[V,P])
      U[V,P]=matriz[V,P]))
for i in range(0,m) 
    for V in range (0,m)
    if (i==V)
     L(i.V)=1
     if (i<V)
       factor=(matriz[V,i]/matriz[i,i])
       L(V,i)=factor
       for P in range(0,m)
         matriz[V,P]=Xatriz[V,P]-(factor*matriz[i,P])
          U[V,P]=matriz[V,P]
print("resultados")
print("\n Matriz L\n"L)
print("\n Matriz U\n"U) 
