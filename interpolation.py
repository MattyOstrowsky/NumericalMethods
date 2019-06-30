"""
Mateusz Ostrowski
216708
"""
import numpy as np
from matplotlib import pyplot as plt


def funk(x):
    return np.sin(x**2-2**x/np.exp(2*x+x**2))


def czebyszew(n, xmin, xmax):     #
    c = np.array([np.cos((2*i-1)*np.pi/(n*2)) for i in range(1, n+1)])
    c = c + 1 + xmin
    return c * (xmax - xmin)/2


def neville(x0, x):
    N = len(x)
    L = np.zeros((N, N))
    result = []
    for i in range(0, N):
        L[i][0] = funk(x[i])

    for j in x0:
        for i in range(1, N):
            L[:N-i, i] = ((j-x[i:])*L[:N-i, i-1]+(x[:N-i]-j)*L[1:N+1-i, i-1])\
                         / (x[:N-i]-x[i:])
        result.append(L[0, -1])

    return np.array(result)


lp = 12  # #liczba znanych punktów
x = np.linspace(0, 10, 500)
y = funk(x)

xd = np.linspace(0, 10, lp+1)
yd = funk(xd)

xdC = czebyszew(lp, 0, 10)
ydC = funk(xdC)

xi = np.linspace(0, 10, 3*lp)
yi = neville(xi, xd)
yiC = neville(xi, xdC)

plt.plot(xi, yi, '-b', label='interpolacja punktów równomiernych')
plt.plot(xi, yiC, '-g', label='interpolacja punktów Czebyszewa')
plt.plot(xi, yi, '+b')
plt.plot(xi, yiC, '+g')
plt.plot(xd, yd, 'ob', label="znane współrzędne punktów równomiernych")
plt.plot(xdC, ydC, 'og', label='znane współrzędne punktów Czebyszewa')
plt.plot(x, y,'-r', label='funkcja wejściowa')
plt.legend()
plt.show()
