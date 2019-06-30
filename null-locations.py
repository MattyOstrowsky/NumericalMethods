import numpy as np
import matplotlib.pyplot as plt


def f(x):
    #f = np.sin(np.log(x) / x)
    return np.sin(x)**2 + np.sin((x+1)**2)


xw0 = -5
xwk = 5
Nxw = 300
xw = np.linspace(xw0, xwk, Nxw)
yw = f(xw)

x1 = 0.8
x2 = 1.2
x12 = [[x1, x2, 0]]


def krok(x12):
    x1 = x12[0]
    x2 = x12[1]
    f1 = f(x1)
    f2 = f(x2)

    x0 = (x1*f2-x2*f1)/(f2-f1)
    f0 = f(x0)

    if f0*f1 > 0:
        return [x0, x2, x0]
    else:
        return [x1, x0, x0]


dok = 1e-3
licz = 0
while True:
    licz += 1
    x12.append(krok(x12[-1]))
    if abs(x12[-1][2] - x12[-2][2]) < dok:
        break

wyn = x12[-1][2]
fw = f(wyn)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xw, yw, "-b")
ax.plot([xw[0], xw[-1]], [0, 0], '-k')
ax.plot([x12[0][0],x12[0][0]],[-0.5,0.5],'-y')
ax.plot([x12[0][1],x12[0][1]],[-0.5,0.5],'-y')
ax.plot(wyn,fw,'or')

#ax.plot(wyn, f(wyn), 'or')
#ax.plot(bt, bty, 'or')
#ax.plot(at, aty, 'og')
plt.show()

