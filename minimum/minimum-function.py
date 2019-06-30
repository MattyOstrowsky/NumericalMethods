"""
Znaleść kąt á, przy którym zasięg skoku z wahadła będzie maksymalny. Należy
posłużyć się metodą złotego podziału.

Mateusz Ostrowski
Index:216708
"""
import matplotlib.pyplot as plt
import numpy as np


class Zloty_podzial:
    def __init__(self, h, line, a0):
        tau = (np.sqrt(5) - 1) / 2
        a = 0.2
        b = 0.7
        dok = 1e-9

        self.xw = self.st_rad(np.linspace(1, int(a0)-1, int(a0)-1))
        self.line = float(line)
        self.h = float(h)
        self.a0 = float(self.st_rad(int(a0)))

        n = int(np.ceil((np.log(2 * dok) - np.log(b - a)) / np.log(tau)))

        wynik, blad = self.steps(n, tau, a, b)
        print("dokladnosc: {}  krokow: {}\nZasięg skoku będzie maksymalny dla kąta: {} +/- {} stopni.".format(dok, n, '{0:.9f}'.format(self.rad_st(wynik)), "{0:.9f}".format(self.rad_st(blad))))

    def steps(self, n, tau, a, b):
        for i in range(n):
            t1 = a + (1 - tau) * (b - a)
            t2 = b - (1 - tau) * (b - a)
            f1 = self.f(t1, self.a0, self.h, self.line)
            f2 = self.f(t2, self.a0, self.h, self.line)

            if f1 > f2:
                b = t2

                plt.text(b, self.f(b, self.a0, self.h, self.line), i, color="blue", fontsize=10)
                ax.plot(b, self.f(b, self.a0, self.h, self.line), 'ob', markersize=2)
            else:
                a = t1

                plt.text(a, self.f(a, self.a0, self.h, self.line), i, color="red", fontsize=10)
                ax.plot(a, self.f(a, self.a0, self.h, self.line), 'or', markersize=2)
        return (a+b)/2, (b-a)/2

    def st_rad(self, a):
        return a * (np.pi / 180)

    def rad_st(self, a):
        return a * (180 / np.pi)

    def f(self, a, a0, h, line):
        return line * np.sin(a) + 2 * line * (np.cos(a) - np.cos(a0)) * np.cos(a) * (np.sin(a) + np.sqrt(np.sin(a) ** 2 + ((h / line - np.cos(a)) / (np.cos(a) - np.cos(a0)))))


while True:
        h0 = input("podaj wysokosc:")
        line0 = input("podaj długość liny:")
        a00 = input("podaj amplitude wahañ W stopniach:")
        if int(line0) > int(h0):
            print("Error: wysokość mniejsza od długości liny!!!")
        else:
            break


fig = plt.figure()
ax = fig.add_subplot(111)
a = Zloty_podzial(h0, line0, a00)

ax.plot(a.xw, a.f(a.xw, a.a0, a.h, a.line), "-b")
plt.show()
