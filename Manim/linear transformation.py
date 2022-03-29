from manim import *
import numpy as np


class graph(LinearTransformationScene):
    X_MIN = -1
    X_MAX = 1
    Y_MIN = -1
    Y_MAX = 1
    N_POINTS = 50
    
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            include_background_plane=False,
            include_foreground_plane=False,
            show_basis_vectors=False
        )

        # Foreground & background planes
        self.plane = NumberPlane()
        self.background_plane = NumberPlane()

    def construct(self):
        # Foreground plane
        self.transformable_mobjects.append(self.plane)
        self.play(Create(self.plane))
        # Background plane
        self.add_background_mobject(self.background_plane)
        self.wait(0.5)

        dots = self.random_dots()
        self.play(Create(VGroup(*dots)))
        self.wait(0.5)
        self.moving_mobjects = [*dots]

        matrix = [[1, 0], [1, 1]]
        # self.apply_matrix(matrix)
        # self.wait(0.5)

        self.apply_nonlinear_transformation(self.func)

        self.wait()

    def func(self, dot):
        return np.array((max(dot[0], 0), max(dot[1], 0), dot[2]))

    def random_dots(self):
        np_dots = np.column_stack((
            np.random.uniform(self.X_MIN, self.X_MAX, size=(self.N_POINTS)),
            np.random.uniform(self.Y_MIN, self.Y_MAX, size=(self.N_POINTS)),
            np.zeros(self.N_POINTS)
        ))

        return [Dot(dot, radius=0.05, color=YELLOW) for dot in np_dots]


class transformation(LinearTransformationScene):
    def construct(self):
        matrix = [[1, 0], [1, 1]]
        self.apply_matrix(matrix)

        self.apply_nonlinear_transformation(self.func)

        self.wait()

    def func(self, dot):
        return np.array((max(dot[0], 0), max(dot[1], 0), dot[2]))
