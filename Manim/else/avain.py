class LinearTransformationScene(VectorScene):
    """
    This scene contains special methods that make it
    especially suitable for showing Linear Transformations.
    """

    def __init__(
        self,
        include_background_plane=True,
        include_foreground_plane=True,
        background_plane_kwargs={
            "color": GREY,
            "axis_config": {
                "color": GREY,
            },
            "background_line_style": {
                "stroke_color": GREY,
                "stroke_width": 1,
            },
        },
        show_coordinates=False,
        show_basis_vectors=True,
        basis_vector_stroke_width=6,
        i_hat_color=X_COLOR,
        j_hat_color=Y_COLOR,
        leave_ghost_vectors=False,
        t_matrix=[[3, 0], [1, 2]],
        **kwargs
    ):
        VectorScene.__init__(self, **kwargs)

        self.include_background_plane = include_background_plane
        self.include_foreground_plane = include_foreground_plane
        self.background_plane_kwargs = background_plane_kwargs
        self.show_coordinates = show_coordinates
        self.show_basis_vectors = show_basis_vectors
        self.basis_vector_stroke_width = basis_vector_stroke_width
        self.i_hat_color = i_hat_color
        self.j_hat_color = j_hat_color
        self.leave_ghost_vectors = leave_ghost_vectors
        self.t_matrix = t_matrix

        self.foreground_plane_kwargs = {
            "x_max": config["frame_width"] / 2,
            "x_min": -config["frame_width"] / 2,
            "y_max": config["frame_width"] / 2,
            "y_min": -config["frame_width"] / 2,
            "faded_line_ratio": 1,
        }

    def setup(self):
        # The has_already_setup attr is to not break all the old Scenes
        if hasattr(self, "has_already_setup"):
            return
        self.has_already_setup = True
        self.background_mobjects = []
        self.foreground_mobjects = []
        self.transformable_mobjects = []
        self.moving_vectors = []
        self.transformable_labels = []
        self.moving_mobjects = []

        self.t_matrix = np.array(self.t_matrix)
        self.background_plane = NumberPlane(**self.background_plane_kwargs)

        if self.show_coordinates:
            self.background_plane.add_coordinates()
        if self.include_background_plane:
            self.add_background_mobject(self.background_plane)
        if self.include_foreground_plane:
            self.plane = NumberPlane(**self.foreground_plane_kwargs)
            self.add_transformable_mobject(self.plane)
        if self.show_basis_vectors:
            self.basis_vectors = self.get_basis_vectors(
                i_hat_color=self.i_hat_color,
                j_hat_color=self.j_hat_color,
            )
            self.moving_vectors += list(self.basis_vectors)
            self.i_hat, self.j_hat = self.basis_vectors
            self.add(self.basis_vectors)

    def add_special_mobjects(self, mob_list, *mobs_to_add):
        """
        Adds mobjects to a separate list that can be tracked,
        if these mobjects have some extra importance.

        Parameters
        ----------
        mob_list : list
            The special list to which you want to add
            these mobjects.

        *mobs_to_add : Mobject
            The mobjects to add.

        """
        for mobject in mobs_to_add:
            if mobject not in mob_list:
                mob_list.append(mobject)
                self.add(mobject)

    def add_background_mobject(self, *mobjects):
        """
        Adds the mobjects to the special list
        self.background_mobjects.

        Parameters
        ----------
        *mobjects : Mobject
            The mobjects to add to the list.
        """
        self.add_special_mobjects(self.background_mobjects, *mobjects)

    # TODO, this conflicts with Scene.add_fore
    def add_foreground_mobject(self, *mobjects):
        """
        Adds the mobjects to the special list
        self.foreground_mobjects.

        Parameters
        ----------
        *mobjects : Mobject
            The mobjects to add to the list
        """
        self.add_special_mobjects(self.foreground_mobjects, *mobjects)

    def add_transformable_mobject(self, *mobjects):
        """
        Adds the mobjects to the special list
        self.transformable_mobjects.

        Parameters
        ----------
        *mobjects : Mobject
            The mobjects to add to the list.
        """
        self.add_special_mobjects(self.transformable_mobjects, *mobjects)

    def add_moving_mobject(self, mobject, target_mobject=None):
        """
        Adds the mobject to the special list
        self.moving_mobject, and adds a property
        to the mobject called mobject.target, which
        keeps track of what the mobject will move to
        or become etc.

        Parameters
        ----------
        mobject : Mobject
            The mobjects to add to the list

        target_mobject : Mobject, optional
            What the moving_mobject goes to, etc.
        """
        mobject.target = target_mobject
        self.add_special_mobjects(self.moving_mobjects, mobject)

    def get_unit_square(self, color=YELLOW, opacity=0.3, stroke_width=3):
        """
        Returns a unit square for the current NumberPlane.

        Parameters
        ----------
        color : str, optional
            The string of the hex color code of the color wanted.

        opacity : float, int, optional
            The opacity of the square

        stroke_width : int, float, optional
            The stroke_width in pixels of the border of the square

        Returns
        -------
        Square
        """
        square = self.square = Rectangle(
            color=color,
            width=self.plane.get_x_unit_size(),
            height=self.plane.get_y_unit_size(),
            stroke_color=color,
            stroke_width=stroke_width,
            fill_color=color,
            fill_opacity=opacity,
        )
        square.move_to(self.plane.coords_to_point(0, 0), DL)
        return square

    def add_unit_square(self, animate=False, **kwargs):
        """
        Adds a unit square to the scene via
        self.get_unit_square.

        Parameters
        ----------
        animate (bool)
            Whether or not to animate the addition
            with DrawBorderThenFill.
        **kwargs
            Any valid keyword arguments of
            self.get_unit_square()

        Returns
        -------
        Square
            The unit square.
        """
        square = self.get_unit_square(**kwargs)
        if animate:
            self.play(
                DrawBorderThenFill(square), Animation(Group(*self.moving_vectors))
            )
        self.add_transformable_mobject(square)
        self.bring_to_front(*self.moving_vectors)
        self.square = square
        return self

    def add_vector(self, vector, color=YELLOW, **kwargs):
        """
        Adds a vector to the scene, and puts it in the special
        list self.moving_vectors.

        Parameters
        ----------
        vector : Arrow,list,tuple,np.ndarray
            It can be a pre-made graphical vector, or the
            coordinates of one.

        color : str
            The string of the hex color of the vector.
            This is only taken into consideration if
            'vector' is not an Arrow. Defaults to YELLOW.

        **kwargs
            Any valid keyword argument of VectorScene.add_vector.

        Returns
        -------
        Arrow
            The arrow representing the vector.
        """
        vector = VectorScene.add_vector(self, vector, color=color, **kwargs)
        self.moving_vectors.append(vector)
        return vector

    def write_vector_coordinates(self, vector, **kwargs):
        """
        Returns a column matrix indicating the vector coordinates,
        after writing them to the screen, and adding them to the
        special list self.foreground_mobjects

        Parameters
        ----------
        vector : Arrow
            The arrow representing the vector.

        **kwargs
            Any valid keyword arguments of VectorScene.write_vector_coordinates

        Returns
        -------
        Matrix
            The column matrix representing the vector.
        """
        coords = VectorScene.write_vector_coordinates(self, vector, **kwargs)
        self.add_foreground_mobject(coords)
        return coords

    def add_transformable_label(
        self, vector, label, transformation_name="L", new_label=None, **kwargs
    ):
        """
        Method for creating, and animating the addition of
        a transformable label for the vector.

        Parameters
        ----------
        vector : Vector
            The vector for which the label must be added.

        label : Union[:class:`~.MathTex`, :class:`str`]
            The MathTex/string of the label.

        transformation_name : Union[:class:`str`, :class:`~.MathTex`], optional
            The name to give the transformation as a label.

        new_label : Union[:class:`str`, :class:`~.MathTex`], optional
            What the label should display after a Linear Transformation

        **kwargs
            Any valid keyword argument of get_vector_label

        Returns
        -------
        :class:`~.MathTex`
            The MathTex of the label.
        """
        label_mob = self.label_vector(vector, label, **kwargs)
        if new_label:
            label_mob.target_text = new_label
        else:
            label_mob.target_text = "%s(%s)" % (
                transformation_name,
                label_mob.get_tex_string(),
            )
        label_mob.vector = vector
        label_mob.kwargs = kwargs
        if "animate" in label_mob.kwargs:
            label_mob.kwargs.pop("animate")
        self.transformable_labels.append(label_mob)
        return label_mob

    def add_title(self, title, scale_factor=1.5, animate=False):
        """
        Adds a title, after scaling it, adding a background rectangle,
        moving it to the top and adding it to foreground_mobjects adding
        it as a local variable of self. Returns the Scene.

        Parameters
        ----------
        title : Union[:class:`str`, :class:`~.MathTex`, :class:`~.Tex`]
            What the title should be.

        scale_factor : int, float, optional
            How much the title should be scaled by.

        animate : bool
            Whether or not to animate the addition.

        Returns
        -------
        LinearTransformationScene
            The scene with the title added to it.
        """
        if not isinstance(title, Mobject):
            title = Tex(title).scale(scale_factor)
        title.to_edge(UP)
        title.add_background_rectangle()
        if animate:
            self.play(Write(title))
        self.add_foreground_mobject(title)
        self.title = title
        return self

    def get_matrix_transformation(self, matrix):
        """
        Returns a function corresponding to the linear
        transformation represented by the matrix passed.

        Parameters
        ----------
        matrix : np.ndarray, list, tuple
            The matrix.
        """
        return self.get_transposed_matrix_transformation(np.array(matrix).T)

    def get_transposed_matrix_transformation(self, transposed_matrix):
        """
        Returns a function corresponding to the linear
        transformation represented by the transposed
        matrix passed.

        Parameters
        ----------
        matrix : np.ndarray, list, tuple
            The matrix.
        """
        transposed_matrix = np.array(transposed_matrix)
        if transposed_matrix.shape == (2, 2):
            new_matrix = np.identity(3)
            new_matrix[:2, :2] = transposed_matrix
            transposed_matrix = new_matrix
        elif transposed_matrix.shape != (3, 3):
            raise ValueError("Matrix has bad dimensions")
        return lambda point: np.dot(point, transposed_matrix)

    def get_piece_movement(self, pieces):
        """
        This method returns an animation that moves an arbitrary
        mobject in "pieces" to its corresponding .target value.
        If self.leave_ghost_vectors is True, ghosts of the original
        positions/mobjects are left on screen

        Parameters
        ----------
        pieces : list, tuple, np.array
            The pieces for which the movement must be shown.

        Returns
        -------
        Animation
            The animation of the movement.
        """
        start = VGroup(*pieces)
        target = VGroup(*[mob.target for mob in pieces])
        if self.leave_ghost_vectors:
            self.add(start.copy().fade(0.7))
        return Transform(start, target, lag_ratio=0)

    def get_moving_mobject_movement(self, func):
        """
        This method returns an animation that moves a mobject
        in "self.moving_mobjects"  to its corresponding .target value.
        func is a function that determines where the .target goes.

        Parameters
        ----------

        func : function
            The function that determines where the .target of
            the moving mobject goes.

        Returns
        -------
        Animation
            The animation of the movement.
        """
        for m in self.moving_mobjects:
            if m.target is None:
                m.target = m.copy()
            target_point = func(m.get_center())
            m.target.move_to(target_point)
        return self.get_piece_movement(self.moving_mobjects)

    def get_vector_movement(self, func):
        """
        This method returns an animation that moves a mobject
        in "self.moving_vectors"  to its corresponding .target value.
        func is a function that determines where the .target goes.

        Parameters
        ----------

        func : function
            The function that determines where the .target of
            the moving mobject goes.

        Returns
        -------
        Animation
            The animation of the movement.
        """
        for v in self.moving_vectors:
            v.target = Vector(func(v.get_end()), color=v.get_color())
            norm = np.linalg.norm(v.target.get_end())
            if norm < 0.1:
                v.target.get_tip().scale_in_place(norm)
        return self.get_piece_movement(self.moving_vectors)

    def get_transformable_label_movement(self):
        """
        This method returns an animation that moves all labels
        in "self.transformable_labels" to its corresponding .target .

        Returns
        -------
        Animation
            The animation of the movement.
        """
        for label in self.transformable_labels:
            label.target = self.get_vector_label(
                label.vector.target, label.target_text, **label.kwargs
            )
        return self.get_piece_movement(self.transformable_labels)

    def apply_matrix(self, matrix, **kwargs):
        """
        Applies the transformation represented by the
        given matrix to the number plane, and each vector/similar
        mobject on it.

        Parameters
        ----------
        matrix : np.ndarray, list, tuple
            The matrix.
        **kwargs
            Any valid keyword argument of self.apply_transposed_matrix()
        """
        self.apply_transposed_matrix(np.array(matrix).T, **kwargs)

    def apply_inverse(self, matrix, **kwargs):
        """
        This method applies the linear transformation
        represented by the inverse of the passed matrix
        to the number plane, and each vector/similar mobject on it.

        Parameters
        ----------
        matrix : np.ndarray, list, tuple
            The matrix whose inverse is to be applied.
        **kwargs
            Any valid keyword argument of self.apply_matrix()
        """
        self.apply_matrix(np.linalg.inv(matrix), **kwargs)

    def apply_transposed_matrix(self, transposed_matrix, **kwargs):
        """
        Applies the transformation represented by the
        given transposed matrix to the number plane,
        and each vector/similar mobject on it.

        Parameters
        ----------
        matrix : np.ndarray, list, tuple
            The matrix.
        **kwargs
            Any valid keyword argument of self.apply_function()
        """
        func = self.get_transposed_matrix_transformation(transposed_matrix)
        if "path_arc" not in kwargs:
            net_rotation = np.mean(
                [angle_of_vector(func(RIGHT)), angle_of_vector(func(UP)) - np.pi / 2]
            )
            kwargs["path_arc"] = net_rotation
        self.apply_function(func, **kwargs)

    def apply_inverse_transpose(self, t_matrix, **kwargs):
        """
        Applies the inverse of the transformation represented
        by the given transposed matrix to the number plane and each
        vector/similar mobject on it.

        Parameters
        ----------
        matrix : np.ndarray, list, tuple
            The matrix.
        **kwargs
            Any valid keyword argument of self.apply_transposed_matrix()
        """
        t_inv = np.linalg.inv(np.array(t_matrix).T).T
        self.apply_transposed_matrix(t_inv, **kwargs)

    def apply_nonlinear_transformation(self, function, **kwargs):
        """
        Applies the non-linear transformation represented
        by the given function to the number plane and each
        vector/similar mobject on it.

        Parameters
        ----------
        function : Function
            The function.
        **kwargs
            Any valid keyword argument of self.apply_function()
        """
        self.plane.prepare_for_nonlinear_transform()
        self.apply_function(function, **kwargs)

    def apply_function(self, function, added_anims=[], **kwargs):
        """
        Applies the given function to each of the mobjects in
        self.transformable_mobjects, and plays the animation showing
        this.

        Parameters
        ----------
        function : Function
            The function that affects each point
            of each mobject in self.transformable_mobjects.

        added_anims : list, optional
            Any other animations that need to be played
            simultaneously with this.

        **kwargs
            Any valid keyword argument of a self.play() call.
        """
        if "run_time" not in kwargs:
            kwargs["run_time"] = 3
        anims = (
            [
                ApplyPointwiseFunction(function, t_mob)
                for t_mob in self.transformable_mobjects
            ]
            + [
                self.get_vector_movement(function),
                self.get_transformable_label_movement(),
                self.get_moving_mobject_movement(function),
            ]
            + [Animation(f_mob) for f_mob in self.foreground_mobjects]
            + added_anims
        )
        self.play(*anims, **kwargs)
