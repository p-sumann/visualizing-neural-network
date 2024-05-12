from manim import *

class GradientDescent2D(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[0, 9],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Define the function
        def func(x):
            return x**2

        # Create the graph
        graph = axes.plot(func, color=WHITE)
        graph_label = axes.get_graph_label(graph, label='x^2')

        # Initial point
        dot = Dot(color=RED).move_to(axes.c2p(2, func(2)))
        dot_label = Text("x_0").next_to(dot, UP)

        # Gradient descent updates
        learning_rate = 0.25
        steps = 5

        self.add(axes, labels, graph, graph_label, dot, dot_label)
        self.wait(1)

        for _ in range(steps):
            x = dot.get_center()[0]
            x_val = axes.p2c(x)[0]
            new_x_val = x_val - learning_rate * 2 * x_val
            new_dot = Dot(color=RED).move_to(axes.c2p(new_x_val, func(new_x_val)))

            self.play(
                MoveAlongPath(dot, Line(start=dot.get_center(), end=new_dot.get_center())),
                run_time=1
            )
            self.wait(0.5)

        self.wait(2)