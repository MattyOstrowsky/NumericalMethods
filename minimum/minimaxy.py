import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (np.sqrt(x**4-2*x**2*y**2+y**4+4)/(x+y))+x+y


def grad_x(x, y):
    return((x+y)**2*np.sqrt(x**4 - 2*x**2*y**2 + y**4 + 4) + x**4 + 2*x**3*y - 2*x*y**3 - y**4 - 4)/((x+y)**2*np.sqrt(x**4 - 2*x**2*y**2 + y**4 + 4))


def grad_y(x, y):
    return((x+y)**2*np.sqrt(x**4 - 2*x**2*y**2 + y**4 + 4) - x**4 - 2*x**3*y + 2*x*y**3 + y**4 - 4)/((x+y)**2*np.sqrt(x**4 - 2*x**2*y**2 + y**4 + 4))


x_min = 0.707106
y_min = x_min

x = [2.25]
y = [3]
pkt = [f(x[-1], y[-1])]
# x = np.array([2.25])
# y = np.array([3])
# pkt = np.array([f(x[-1], y[-1])])

krok = 1
dok = 1e-5
licz = 0
jeszcze = True
while jeszcze:
    licz += 1

    grx = grad_x(x[-1], y[-1])
    gry = grad_y(x[-1], y[-1])
    nx = x[-1] - grx * krok
    ny = y[-1] - gry * krok
    npkt = f(nx, ny)

    if npkt < pkt[-1]:
        x.append(nx)
        y.append(ny)
        pkt.append(npkt)
        # np.append(x, [nx])
        # np.append(y, [ny])
        # np.append(pkt, [npkt])
    else:
        x.append(x[-1])
        y.append(y[-1])
        pkt.append(pkt[-1])
        # np.append(x, [x[-1]])
        # np.append(y, [y[-1]])
        # np.append(pkt, [pkt[-1]])
        krok /= 2
        bl = npkt/(np.sqrt(grx**2+gry**2))

    if krok < dok :
        jeszcze = False


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, '-k')
ax.plot(x_min, y_min, 'xb')
ax.plot(x[-1], y[-1], '+k')
ax.axis('equal')
x0 = 0.1
xk = 3
Nx = 500
x = np.linspace(x0, xk,Nx)
y0=0.1
yk= 2.5
Ny = 500
y = np.linspace(y0, yk, Ny)
X,Y = np.meshgrid(x,y)
Z= f(X,Y)
ax.contour(X,Y,Z,15)
plt.show()
