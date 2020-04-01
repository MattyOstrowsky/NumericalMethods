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


class RungeKutta45():
    def __init__(self, f, a, b, y_start, interval, tol, h_max, h_min):
        self.f = f
        self.a = a
        self.h = interval
        self.a = a
        self.y_start = y_start
        self.tol = tol
        self.h_max = h_max
        self.h_min = h_min
        self.b = b
        self.x = [a]
        self.y = []
        self.y.append(y_start)

    def RKF(self, a, y, h):
        k1 = h * self.f(a, y)
        k2 = h * self.f(a + (1 / 4) * h, y + (1 / 4) * k1)
        k3 = h * self.f(a + (3 / 8) * h, y + (3 / 32) * k1 + (9 / 32) * k2)
        k4 = h * self.f(a + (12 / 13) * h, y + (1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3)
        k5 = h * self.f(a + h, y + (439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4)
        k6 = h * self.f(a + (1 / 2) * h, y - (8 / 27) * k1 + 2 * k2 - (3544 / 2565) * k3 + (1859 / 4104) * k4 - (11 / 40) * k5)
        return (16 / 135) * k1 + (6656 / 12825) * k3 + (28561 / 56430) * k4 - (9 / 50) * k5 + ( 2 / 55) * k6, 25 / 216 * k1 + 1408 / 2565 * k3 + 2197 / 4104 * k4 - 1 / 5 * k5

    def runge(self):
        while self.a < self.b:
            r, p = self.RKF(self.a, self.y_start, self.h)
            self.y_start = self.y_start + r
            self.a = self.a + self.h
            s = 0.84 * (self.tol * self.h / np.abs(r - p)) ** 0.25

            if s > self.h_max:
                self.h = self.h_max
            elif s < self.h_min:
                self.h = self.h_min
            self.h = self.h * s
            self.x.append(self.a)
            self.y.append(self.y_start)

        return np.array(self.x), np.array(self.y)


# Example
#
# def f(x, y):
#     return np.exp(-2 * x) - 2 * y[0]
#
# a = 0
# b = 4
# xo = np.array([0.1])
# h = 0.2
# example = RungeKutta45(f, a, b, xo, h, 10e-6, 0.5, 0.1)
# x, y = example.runge()

# y1 = np.array([i[0] for i in y])
# plt.plot(x, y1, 'rs')
# plt.plot(x, y1)
# plt.legend(["Runge-Kutta-Fehlberg", "approximate solution"], loc=1)
# plt.grid(True)
# plt.show()
