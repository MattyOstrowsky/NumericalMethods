import numpy as np
import matplotlib.pyplot as plt


class RungeKuttaSimple:
    def __init__(self, x_start, x_finish, y_start, f, Nx):
        self.f = f
        self.y = [y_start]
        self.Nx = Nx
        self.x = np.linspace(x_start, x_finish, self.Nx)
        self.dx = self.x[1] - self.x[0]

    def step(self, x, y):
        k1 = self.f(x, y)
        k2 = self.f(x+self.dx/2, y+self.dx/2*k1)
        k3 = self.f(x+self.dx, y+2*self.dx*k2-self.dx*k1)
        return y+self.dx/6*(k1+4*k2+k3)

    def result(self):
        for i in range(1, self.Nx):
            self.y.append(self.step(self.x[i], self.y[-1]))
        return self.y, self.x

    def draw_chart(self, x, y):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y, 'rs')
        ax.plot(x, y, '-b')
        ax.axhline(0, lw=0.5)
        plt.show()

# Example
#
# def f(x, y):
#   return x**2 + y


# example = RungeKuttaSimple(0, 10, 1, f, Nx=10)
# y, x = example.result()
# example.draw_chart(x, y)
