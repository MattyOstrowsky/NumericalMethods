import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(np.log(x)/x)


def pf(x):
    return(1/x**2-np.log(x)/x**2)*np.cos(np.log(x)/x)


def krok_newton(x):
    return x - f(x) / pf(x)

xw0 = 0.1
xwk = 2
nxw = 100
xw = np.linspace(xw0,xwk,nxw)

yw = f(xw)
pyw = pf(xw)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([xw[0],xw[-1]],[0,0], '-k')
ax.plot(xw, yw, "-b")
# ax.plot(xw, pyw, 'or')


x0 = 1.6


x = x0
dok = 1e-10
jeszcze = True
licz = 0
while jeszcze:
    licz += 1
    x = krok_newton(x)
    if abs(f(x)) < dok:
        jeszcze = False

ax.plot(x, 0, 'xr', x, f(x), 'xr')
plt.show()