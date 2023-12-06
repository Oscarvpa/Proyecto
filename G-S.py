"Vargas Palencia Oscar Adrian"
"FAcultad de ingenieria, UNAM , Analisis Numerico"

from pprint import pprint
# ingrese la matriz acomodada en diagonalmente dominante
def distinf(V,P):
    
    return max([abs(V[i] - P[i]) for i in range(len(V))])



def gauss_seidel_solver(A, b, V0, tol=1e-2, max_iter=100):
   
    n = len(A)
    V = V0.copy()

    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x0[j] for j in range(i + 1, n))
            V[i] = (b[i] - sum1 - sum2) / A[i][i]
        pprint(V)
        if distinf(V, V0) < tol:
            print("La solucion es=", tol)
            return V

        V0 = V.copy()

    print("se acabo las iteraciones ")
    return None

def main():
   
    rows_A = int(input("Número de filas de A: "))
    cols_A = int(input("Número de columnas de A: "))
    A = [[float(input(f"Coeficiente A[{i+1}][{j+1}]: ")) for j in range(cols_A)] for i in range(rows_A)]

    b = [float(input(f"Término constante b[{i+1}]: ")) for i in range(rows_A)]
    V0 = [float(input(f"Aproximación inicial x0[{i+1}]: ")) for i in range(rows_A)]

    print("\nMatriz A:")
    pprint(A)
    print("Vector b:")
    pprint(b)
    print("Semilla x0:")
    pprint(V0)
    print("Iteración de Gauss-Seidel")
    gauss_seidel_solver(A, b, V0)

if __name__ == "__main__":
    main()
