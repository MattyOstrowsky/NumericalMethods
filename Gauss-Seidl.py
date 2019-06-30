"""
Mateusz Ostrowski

Metoda Gaussa-Seidla
"""
import numpy as np
from numpy.linalg import inv

A = np.matrix([[10., -1., 2., 0.],
       [-1., 11., -1., 3.],
       [2., -1., 10., -1.],
       [0.0, 3., -1., 8.]])

b = np.matrix([[6.],
             [ 25.],
             [-11.],
             [15.]])
L = np.zeros_like(A)
U = np.zeros_like(A)
D = np.diag(np.diag(A, k=0), k=0)

for i  in range(1, A.shape[0]-1):
    X = np.diag(np.diag(A, k=-i), k=-i)
    L += X

for i in range(1, A.shape[0] - 1):
    X = np.diag(np.diag(A, k=i), k=i)
    U += X


B = inv(-(L+D))*U
c = inv(-(L+D))*b
x = B+c
licz = 0
while True:
    xn = B*x+c
    licz+=1
    print("Aktualne rozwiązanie:")
    print(x[0:, 0])
    if np.allclose(x, xn, rtol=1e-8):
        break
    x = xn


print('')
print("ilość iteracji:",licz)
print("ostateczny wynik to:")
print(x[0:,0])

spr = -(A@x)
print("Sprawdzenie:")
print(np.around(spr[0:,0]))