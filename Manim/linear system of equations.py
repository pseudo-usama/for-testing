import numpy as np
import copy
from manim import *


class cls(Scene):
    def construct(self):
        # eq1 = MathTex(r'x+y+z&=6').shift(UP)
        # eq2 = MathTex(r'2x+5y&=-4')
        # eq3 = MathTex(r'2x+5y-z&=27').shift(DOWN)
        # self.add(eq1, eq2, eq3)


        # Writing system of equations
        eq = MathTex(r' x+ y+ z&=6\\ 2x+5y&=-4\\ 2x+5y-z&=27')
        self.play(Write(eq))
        self.wait()


        # Creating matrix form of equation
        big_mat = Matrix(matrix=np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]]))
        var_mat = Matrix(matrix=np.array([['x'], ['y'], ['z']])).next_to(big_mat, RIGHT)
        equal_sign = MathTex(r'=').next_to(var_mat, RIGHT)
        val_mat = Matrix(matrix=np.array([[6], [-4], [27]])).next_to(equal_sign, RIGHT)
        mat_sys = VGroup(big_mat, var_mat, equal_sign, val_mat).center()


        # Transform from equation system to matrix system
        self.play(ReplacementTransform(eq, mat_sys))
        self.wait(0.5)


        # Displaying AX = B equation
        axb_eq = MathTex('A', 'X', '=', 'B').shift(DOWN)
        self.play(
            mat_sys.animate.shift(UP),
            FadeInFrom(axb_eq, UP),
        )
        self.wait(0.5)


        # Moving matrix system to Top left corner
        line = Line(
            (-config['frame_width']/2+0.3, config['frame_height']/2-2, 0),
            (config['frame_width']/2-0.3, config['frame_height']/2-2, 0)
        ).set_color(YELLOW_C).set_opacity(0.3)

        self.play(
            mat_sys.animate.scale(0.5).to_corner(UL),
            axb_eq.animate.scale(1.5).shift(UP),
            FadeIn(line)
        )
        self.wait()


        # Showing X matrix equation
        axb_inverse_eq = MathTex('X', '=', 'A^{-1}', 'B').scale(1.5)
        self.play(TransformMatchingTex(axb_eq, axb_inverse_eq, path_arc=PI/2))
        self.wait()


        # Showing A inverse formula
        a_inverse_eq = MathTex('A^{-1}', '=', r'\frac{Adj(A)}{|A|}').scale(1.5)
        self.play(TransformMatchingTex(axb_inverse_eq, a_inverse_eq, path_arc=PI/2))
        self.wait(0.5)
        self.play(a_inverse_eq.animate.scale(0.666).to_corner(UR))
        self.wait(0.2)


        # Showing values for determinant and adjoint
        # TODO: Displaying properly. But I'm not satisfied with this method
        det_txt = Text('Determinant of A is', size=0.7).shift(LEFT*2.4)
        det_val = MathTex(r'-\frac{1}{12}').next_to(det_txt, RIGHT).shift(RIGHT*2)

        adj_mat = Matrix(matrix=np.array([[-27, 6, 3], [10, -3, -5], [-4, -3, 2]]))
        adj_txt = Text('Adjoint of A is', size=0.7).next_to(det_txt, DOWN).align_to(det_txt, LEFT).shift(DOWN*1.3)

        adj_mat.next_to(det_val, DOWN)

        self.play(
            TransformFromCopy(big_mat, det_val),
            TransformFromCopy(big_mat, adj_mat),
            FadeIn(det_txt),
            FadeIn(adj_txt),
        )
        self.wait()


        # Putting determinant value & adjoint in formula
        a_inverse_mathTex = MathTex(r'A^{-1}=').shift(LEFT)
        det_val_plc_hldr = det_val.copy().next_to(a_inverse_mathTex)
        adj_mat_plc_hldr = adj_mat.copy().next_to(det_val_plc_hldr)
        VGroup(a_inverse_mathTex, det_val_plc_hldr, adj_mat_plc_hldr).center(),
        self.play(
            TransformMatchingTex(a_inverse_eq, a_inverse_mathTex),
            det_val.animate.next_to(a_inverse_mathTex, RIGHT),
            adj_mat.animate.next_to(det_val_plc_hldr, RIGHT),
            FadeOut(det_txt),
            FadeOut(adj_txt)
        )
        

        a_mat_inverse = Matrix(matrix=np.array([
            [MathTex(r'\frac{27}{21}'), MathTex(r'\frac{-3}{7}'), MathTex(r'\frac{-1}{7}')],
            [MathTex(r'\frac{-10}{21}'), MathTex(r'\frac{1}{7}'), MathTex(r'\frac{5}{21}')],
            [MathTex(r'\frac{4}{21}'), MathTex(r'\frac{1}{7}'), MathTex(r'\frac{-2}{21}')]
        ], dtype=MathTex))
        # self.play(Transform(VGroup(det_val, adj_mat), a_mat_inverse))

        self.wait(2)
