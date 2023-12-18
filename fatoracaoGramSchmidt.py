import numpy as np

#Fatoração de Gram-Schmidt
def fat_gs(A):
    m, n = A.shape #Definindo tamanho de m e n de acordo com tamanho de A

    #Inicializando as matriz Q e R como matrizes nulas
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    #Percorrendo as colunas da matriz A
    for j in range(n):
        v = A[:, j]
        for k in range(j):
            r = np.dot(Q[:, k], v)
            R[k, j] = r
            v = v - r * Q[:, k]
        r = np.linalg.norm(v)
        R[j, j] = r
        Q[:, j] = v / r

    return Q, R

# Matriz A
A = np.array([[1, -1, 4],
              [1, 4, -2],
              [1, 4, 2],
              [1, -1, 0]])

# Matriz Q e R após a fatoração de Gram-Schmidt
Q, R = fat_gs(A)

#Função para deixar uma o print no formato da matriz
def formatar_matriz(matriz):
    m, n = matriz.shape
    for i in range(m):
        print("[", end="")
        for j in range(n):
            print("{:.2f}".format(matriz[i, j]), end=" ")
        print("]")

#Exibindo as matrizes Q e R
print("Matriz Q\n")
formatar_matriz(Q)

print("\nMatriz R\n")
formatar_matriz(R)

