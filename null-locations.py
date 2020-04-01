import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """"Returns the function where you're looking for zero spots"""
    return np.sin(x)**2 + np.sin((x+1)**2)


class FindZeroSpot:
    def __init__(self, func, x1=0.8, x2=1.2, precision=1e-3):
        """
        :param func: defined function to examine
        :param x1: the beginning of the area under investigation
        :param x2: end of the area under investigation
        :param precision: precision of searching for zero place
        """
        N = 300
        self.x_min = -5
        self.x_max = 5
        self.precision = precision
        self.function = func
        self.interval_list = [[x1, x2, 0]]

        self.x_points = np.linspace(self.x_min, self.x_max, N)
        self.y_points = self.function(self.x_points)

    def steps(self, act_interval):
        f1 = self.function(act_interval[0])
        f2 = self.function(act_interval[1])
        x0 = (act_interval[0] * f2 - act_interval[1] * f1) / (f2 - f1)
        f0 = self.function(x0)

        if f0 * f1 > 0:
            return [x0, act_interval[1], x0]
        else:
            return [act_interval[0], x0, x0]

    def count(self):
        """
        counts the coordinates of the zero place
        :return:x coordinate, y coordinate
        """

        def new_interval(interval_list):
            return interval_list.append(self.steps(interval_list[-1]))

        def check_precision_condition(interval_list, precision):
            new_interval(interval_list)
            if abs(interval_list[-1][2] - interval_list[-2][2]) < precision:
                return False
            return True

        while check_precision_condition(self.interval_list, self.precision):
            pass

        x_result = self.interval_list[-1][2]
        y_result = self.function(x_result)
        print(self.interval_list)
        return x_result, y_result

    def figure(self, x_result, y_result):
        """
        draws a graph of functions, interval, point

        :param x_result: x coordinate of the result
        :param y_result: y coordinate of the result
        :return: null
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.x_points, self.y_points, "-b")
        ax.plot([self.x_points[0], self.x_points[-1]], [0, 0], '-k')
        ax.plot([self.interval_list[0][0], self.interval_list[0][0]], [-0.5, 0.5], '-y')
        ax.plot([self.interval_list[0][1], self.interval_list[0][1]], [-0.5, 0.5], '-y')
        ax.plot(x_result, y_result, 'or')
        plt.show()


example = FindZeroSpot(f)
x, y = example.count()
print("coordinates of it \nx:{:5.2f} y:{:5.2f}".format(x, y))
example.figure(x, y)
