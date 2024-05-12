from manim import *

config.background_color = WHITE


class NeuralNetworkAnimation(Scene):

    def construct(self):
        # Create input layer

        input_layer = VGroup(*[Circle(radius=0.4, color=GREEN_C)
                             for _ in range(2)]).arrange(DOWN, buff=0.3)

        # Create hidden layer
        hidden_layer = VGroup(*[Circle(radius=0.4, color=RED)
                              for _ in range(5)]).arrange(DOWN, buff=0.2)

        # Create output layer
        output_layer = VGroup(*[Circle(radius=0.4, color=RED)
                              for _ in range(2)]).arrange(DOWN, buff=0.2)

        # # Position the layers
        hidden_layer.shift(2 * RIGHT)
        output_layer.shift(4 * RIGHT)

        # # Create edges
        # edges_input_hidden = VGroup()
        # edges_hidden_output = VGroup()

        # for input_node in input_layer:
        #     for hidden_node in hidden_layer:
        #         edge = Line(input_node.get_center(),
        #                     hidden_node.get_center(), color=GRAY)
        #         edges_input_hidden.add(edge)

        # for hidden_node in hidden_layer:
        #     for output_node in output_layer:
        #         edge = Line(hidden_node.get_center(),
        #                     output_node.get_center(), color=GRAY)
        #         edges_hidden_output.add(edge)

        # Animate the neural network
        self.play(Create(input_layer))
        self.play(Create(hidden_layer))
        self.play(Create(output_layer))
        # self.play(Create(edges_input_hidden), run_time=2)
        # self.play(Create(edges_hidden_output), run_time=2)
        self.wait()
