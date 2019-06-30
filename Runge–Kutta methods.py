import numpy as np
import matplotlib.pyplot as plt


x0 = 0
xk = 10
y0 = 1
# 1 opcja
# dx = 0.1
# x = np.arange(x0, xk, dx)
# 2 opcja
Nx = 100
x = np.linspace(x0, xk, Nx)
dx = x[1]-x[0]


def f(x, y):
    return x**2 + y


def krok(x, y):
    k1 = f(x, y)
    k2 = f(x+dx/2, y+dx/2*k1)
    k3 = f(x+dx, y+2*dx*k2-dx*k1)
    return y+dx/6*(k1+4*k2+k3)


y = [y0]
for i in range(1, Nx):
    y.append(krok(x[i], y[-1]))
y = np.array(y)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, '-b')
ax.axhline(0, lw=0.5)
plt.show()