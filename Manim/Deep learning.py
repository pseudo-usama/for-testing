import torch
import torch.nn as nn
from manim import *
from webcolors import rgb_to_hex


X = torch.randn(1000, 2)
H = torch.tanh(X)

x_min = -1
x_max = +1

colors = (X - x_min) / (x_max - x_min)
colors = (colors * 511).short().numpy()
colors = np.clip(colors, 0, 511)

model = nn.Sequential(nn.Linear(2, 100), nn.Linear(100, 2))


class lt(LinearTransformationScene):
    def construct(self):
        self.setup()

        np_dots = np.column_stack((
            np.random.rand(100, 2)*2,
            np.zeros(100)
        ))
        dots = VGroup(*[Dot(dot) for dot in np_dots])

        self.play(Write(dots))
        self.wait()

        self.add_foreground_mobjects(*dots)
        self.mobjects += dots
        self.apply_nonlinear_transformation(self.func)
        self.wait()

    def func(self, p):
        return np.array([p[0]*2, p[1], 0])


class RandomTransform(LinearTransformationScene):
    def construct(self):
        points = VGroup(*[
            Dot(2*np.array([point[0], point[1], 0]), color=YELLOW,
                radius=0.75*DEFAULT_DOT_RADIUS) for index, point in enumerate(H)
        ])

        self.show_basis_vectors = False

        self.setup()
        self.play(Write(points))
        self.wait()

        # self.add(*points)
        # self.mobjects += [*points]
        # self.add_moving_mobject(*points)
        self.add_foreground_mobjects(*points)
        self.apply_nonlinear_transformation(self.func)
        self.wait()

    def func(self, point):
        x, y, z = point
        inp = torch.tensor(point[:2], dtype=torch.float32)
        x, y = model.forward(inp).detach().numpy()
        return 5*(x * RIGHT + y * UP)


torch.manual_seed(8348)
model2 = nn.Sequential(nn.Linear(2, 100), nn.ReLU(), nn.Linear(100, 2))

class ReluTransform(RandomTransform):
    def func(self, point):
        x, y, z = point
        inp = torch.tensor(point[:2], dtype=torch.float32)
        x, y = model2.forward(inp).detach().numpy()
        return 5*(x * RIGHT + y * UP)

class AV(Scene):
    def construct(self):
        def polar2c(p):
            return np.array([
                p[0]*np.cos(p[1]),
                p[0]*np.sin(p[1]),
                0
                ])

        grid = NumberPlane(
            x_line_frequency=PI/4,
            y_line_frequency=PI/4,
            x_min=-PI,
            x_max=PI,
            y_min=-PI,
            y_max=PI
            )
        func = FunctionGraph(lambda x: 0.5*np.sin(5*x)+2,x_min=-PI,x_max=PI)
        grid.add(func)
        self.add(grid)
        # grid.faded_lines[4:9].fade(1)
        # grid.faded_lines[12:].fade(1)
        # grid.background_lines[4:9].fade(1)
        # grid.background_lines[12:].fade(1)
        # self.play(Rotating(func,radians=PI,axis=UR,about_point=ORIGIN,run_time=2,rate_func=smooth))
        grid.generate_target()
        grid.target.prepare_for_nonlinear_transform()
        grid.target.apply_function(lambda p: polar2c(p))

        self.play(
            MoveToTarget(grid,run_time=4)
        )
        self.wait(3)


class scene(Scene):
    def construct(self):
        def transform(p):
            return np.array([
                p[0]*3,
                p[0]*-1,
                0
            ])

        np_dots = np.column_stack((
            np.random.rand(100, 2),
            np.zeros(100)
        ))
        dots = VGroup(*[Dot(dot) for dot in np_dots])
        grid = NumberPlane()

        func = FunctionGraph(lambda x: 0.5*np.sin(5*x)+2,x_min=-PI,x_max=PI)

        grid.add(dots)
        grid.add(func)
        self.add(grid)


        grid.generate_target()
        grid.target.prepare_for_nonlinear_transform()
        grid.target.apply_function(lambda p: transform(p))

        self.play(
            MoveToTarget(grid,run_time=4)
        )

        self.wait(2)
