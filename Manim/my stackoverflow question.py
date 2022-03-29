from manim import *
import numpy as np

class transformation(LinearTransformationScene):
    def construct(self):
        matrix = [[1, 0], [1, 1]]
        # self.apply_matrix(matrix)                        # <========================

        self.apply_nonlinear_transformation(self.func)   # <========================

        self.wait()

    def func(self, dot):
        return np.array((max(dot[0], 0), max(dot[1], 0), dot[2]))
