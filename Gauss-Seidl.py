
import numpy as np
from numpy.linalg import inv


class GaussSeidel:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.diag_A = np.diag(np.diag(self.A, k=0), k=0)
        self.diag_up_A = np.zeros_like(A)
        self.diag_down_A = np.zeros_like(A)

        for i in range(1, self.A.shape[0] - 1):
            X = np.diag(np.diag(self.A, k=-i), k=-i)
            self.diag_down_A += X
        for i in range(1, self.A.shape[0] - 1):
            X = np.diag(np.diag(self.A, k=i), k=i)
            self.diag_up_A += X
        self.b = inv(-(self.diag_down_A + self.diag_A)).dot(self.diag_up_A)
        self.c = inv(-(self.diag_down_A + self.diag_A)).dot(self.B)
        print(self.b)
        print(self.c)

    def result(self, actual_result=True):
        def print_actual_result():
            print("Aktualne rozwiązanie:")
            print(x)

        def determine_how_close():
            return np.allclose(x, result_x, rtol=1e-8)

        x = self.b + self.c
        print(x)
        steps = 0
        while True:
            result_x = self.b.dot(x) + self.c
            if actual_result:
                print_actual_result()
            steps += 1
            if determine_how_close():
                break
            x = result_x
        return steps, x

    def verification(self, x):
        return np.around(-(self.A @ x))

    def print_result(self, result, steps , verification):
        print("number of iterations:", steps)
        print("the final result is:")
        print(result[:, 0])
        print("verification:")
        print(verification[:, 0])


# Example result of Ax = B
#
# A = np.array([[10., -1., 2., 0.],
#       [-1., 11., -1., 3.],
#       [2., -1., 10., -1.],
#       [0.0, 3., -1., 8.]])
#
# B = np.array([[6.],
#             [25.],
#             [-11.],
#             [15.]])
#
#
# example = GaussSeidel(A, B)
# steps, result = example.result(True)
# verification = example.verification(result)
# example.print_result(result, steps, verification)
