import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)**2 + np.sin((x+1)**2)


xw0 = -5
xwk = 5
Nxw = 300
xw = np.linspace(xw0, xwk, Nxw)
yw = f(xw)

at = []
bt = []
a = -2
b = 4
at.append(a)
bt.append(b)
dok = 1e-5
n = int(np.ceil((np.log(2*dok)-np.log(b-a))/np.log(2/3)))

for i in range(n):
    t1 = 2*a/3 + b/3
    t2 = a/3 + 2*b/3

    f1 = f(t1)
    f2 = f(t2)

    if f1 < f2:
        b = t2
        bt.append(b)
    else:
        a = t1
        at.append(a)

wyn = (a+b)/2
bl = (b-a)/2
print("dokladnosc: {}  krokow: {} wynik: {}+/-{} ".format(dok, n, wyn, bl))

bty = []
for i in bt:
    bty.append(f(i))
aty = []
for i in at:
    aty.append(f(i))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xw, yw, "-b")
ax.plot(wyn, f(wyn), 'or')
ax.plot(bt, bty, 'or')
ax.plot(at, aty, 'og')
plt.show()
