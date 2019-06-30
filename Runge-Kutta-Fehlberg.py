"""
metoda Runge-Kutta-Fehlberg
"""
import numpy as np
import matplotlib.pyplot as plt

"""
       metoda Runge-Kutta-Fehlberg  y' = f(x,y) z y(x[0]) = x0.

       y, x = rkf(f, a, b, x0, tol, hmax, hmin)

       f     - równanie funkcji dy/dx = f(x,y)
       a     - początek przedzialu
       b     - koniec przedziału
       x0    - y(x[0]) = x0
       h     - krok

   """

def rungeKutta(f, a, xo, b, h,tol, hmax, hmin):

         def RKF(f, t, y, tau):
                  k1 = tau * f(t, y)
                  k2 = tau * f(t + (1 / 4) * tau, y + (1 / 4) * k1)
                  k3 = tau * f(t + (3 / 8) * tau, y + (3 / 32) * k1 + (9 / 32) * k2)
                  k4 = tau * f(t + (12 / 13) * tau, y + (1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3)
                  k5 = tau * f(t + tau, y + (439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4)
                  k6 = tau * f(t + (1 / 2) * tau, y - (8 / 27) * k1 + 2 * k2 - (3544 / 2565) * k3 + (1859 / 4104) * k4 - (11 / 40) * k5)

                  return (16/135)*k1+(6656/12825)*k3+(28561/56430)*k4-(9/50)*k5+(2/55)*k6, 25/216*k1+1408/2565*k3+2197/4104*k4-1/5*k5

         x = []
         y = []

         x.append(a)
         y.append(xo)

         while a < b:
                  r,p = RKF(f, a, xo, h)
                  xo = xo + r
                  a = a + h
                  s = 0.84 * (tol*h / np.abs(r-p)) ** 0.25

                  if s > hmax:
                      h = hmax
                  elif s < hmin:
                      h = hmin
                  h=h*s
                  x.append(a)
                  y.append(xo)

         return np.array(x), np.array(y)


def f(x, y):
    return np.exp(-2 * x) - 2 * y[0]

a = 0
b = 2
xo = np.array([0.1])
h = 0.2
x, y = rungeKutta(f, a, xo, b, h, 10e-6, 0.5, 0.1)


y1 = np.array([i[0] for i in y])
plt.plot(x, y1, 'rs')
plt.plot(x, y1)




plt.legend(["Runge-Kutta-Fehlberg", "Przybliżone rozwiązanie"], loc=1)
plt.grid(True)
plt.show()
