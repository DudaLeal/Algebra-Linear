import numpy as np

A = np.array([[1, 2, 3],[-1, 2, 1],[-2, 1, 1]], dtype=float)
b = np.array([6, 2, 0], dtype=float)

A = np.array([[0,1,2],[1,1,1],[2,1,1]], dtype=float)

b = np.array([3.0, 3.0, 4.0], dtype=float)


n = len(A)
p = n*[0]

# Vetor de permutações p quue representa a ordem inicial das linhas
for i in range(n):
  p[i] = i

# Usando a eliminação gaussiana com pivotação parcial na matriz A
for k in range(n - 1):
  pivo = abs(A[k, k])
  linha_pivo = k
  for i in range(k + 1, n):
    if abs(A[i, k]) > pivo:
      pivo = abs(A[i, k])
      linha_pivo = i

  if pivo == 0:
      print("A matriz é singular")

  if linha_pivo != k:
      p[k], p[linha_pivo] = p[linha_pivo], p[k]
      for j in range(n):
          A[k, j], A[linha_pivo, j] = A[linha_pivo, j], A[k, j]

  for i in range(k + 1, n):
      m = A[i, k] / A[k, k]
      A[i, k] = m
      for j in range(k + 1, n):
        A[i, j] = A[i, j] - m * A[k, j]

#criando arrays vazios para armazenar os valores de c, y e x
c = np.zeros(n)
y = np.zeros(n)
x = np.zeros(n)

#Atribuindo os valores do vetor b ao vetor c na nova ordem definida pelo vetor de permutação -> c = Pb
for i in range(n):
  aux = p[i]
  c[i] = b[aux]

#Resolvendo Ly = c usando substituição progressiva
for i in range(n):
  soma = 0
  for j in range(n - 1):
    soma += A[i, j] * y[j]
  y[i] = c[i] - soma

#Resolvendo Ux = y  usando substituição regressiva
for i in range(n - 1, -1, -1):
  soma = 0
  for j in range(i + 1, n):
    soma += A[i, j] * x[j]
  x[i] = (y[i] - soma) / A[i, i]

print(f"A solução desse sistema é {x}\nSendo: ")
for i in range(n):
    print(f"x[{i+1}] = {x[i]:.1f}")

