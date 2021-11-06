import scipy as sp

w = sp.poly1d([1, 2, 3, 4])

# metoda trapezow
a = 1
b = 3


def ctN(a, b, Np):
    x = sp.linspace(a, b, Np + 1)
    y = w(x)
    dx = x[1] - x[0]

    return (sum(y[1:-1]) + (y[0] + y[-1]) / 2) * dx


def ctS(a, b, Np):
    x = sp.linspace(a, b, Np + 1)
    y = w(x)
    dx = x[1] - x[0]

    return sum((y[1:] + y[:-1]) / 2) * dx


def cS(a, b, Np):
    x = sp.linspace(a, b, Np + 1)
    y = w(x)
    dx = x[1] - x[0]
    return (y[0] + y[-1] + 2 * sum(y[2:-1:2]) + 4 * sum(y[1:-1:2])) * dx / 3


"""metoda newtona"""


def It38(a, b, Np):
    x = sp.linspace(a, b, Np + 1)
    y = w(x)
    dx = x[1] - x[0]
    return (y[0] + y[-1] + 2 * sum(y[3:-3:3]) + 3 * sum(y[1:Np:3]) + 3 * sum(y[2:-1:3])) * 3 * dx / 8


def cw(a, b):
    tmp = w.integ()
    return tmp(b) - tmp(a)


lp = [12, 24, 36, 60, 90]
wd = cw(a, b)
"""
for i in range(len(lp)):
    print("wartosc dokladna: {}".format(wd))
    c1 = ctN(a,b,lp[i])
    b1= (c1-wd)/wd
    c2 = ctN(a, b, lp[i]*2)
    b2 = (c2 - wd) / wd
    cr= 4*c2/3-c1/3
    br=(cr-wd)/wd
    print('liczby podzialu: {} i {}\nc1 = {}, b1 = {:6.2e}\nc = {}, b2 = {:6.2e}\n cr = {}, br = {:6.2e}'.format(lp[1],lp[i]*2,c1,b1,c2,b2,cr,br))
"""
for i in range(len(lp)):
    print("wartosc dokladna: {}".format(wd))
    c1 = It38(a, b, lp[i])
    b1 = (c1 - wd) / wd
    c2 = It38(a, b, lp[i] * 2)
    b2 = (c2 - wd) / wd
    cr = 10 * c2 / 15 - c1 / 15
    br = (cr - wd) / wd
    print('liczby podzialu: {} i {}\nc1 = {}, b1 = {:6.2e}\nc = {}, b2 = {:6.2e}\n cr = {}, br = {:6.2e}\n\n'.format(
        lp[1],
        lp[
            i] * 2,
        c1, b1,
        c2, b2,
        cr,
        br))
