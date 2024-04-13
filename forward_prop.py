from manim import * 

class CreateCircle(Scene):
    def construct(self):
        # Create input layer circles
        input_layer_circles = VGroup(
            Circle(radius=0.5, color=RED),
            Circle(radius=0.5, color=RED)
        ).arrange(DOWN, buff=0.5)
        
    # Create input layer labels
        input_layer_labels = VGroup(
            Text("2", font_size=20).move_to(
                input_layer_circles[0].get_center()),
            Text("3", font_size=20).move_to(
                input_layer_circles[1].get_center())
        )
        
    # Create input layer title
        input_title = Text("Input Layer", font_size=20).move_to(UP * 3)

        # Add input layer elements to the scene
        self.add(input_layer_circles, input_layer_labels, input_title)

        # Create hidden layer circles
        
        hidden_layer_circles = VGroup(
            Circle(radius=0.5, color=RED),
            Circle(radius=0.5, color=RED),
            Circle(radius=0.5, color=RED),
        ).arrange(DOWN, buff=0.5).shift(2 * RIGHT)

        # Create hidden layer labels
        hidden_layer_labels = VGroup(
            Text("2", font_size=20).move_to(
                hidden_layer_circles[0].get_center()),
            Text("3", font_size=20).move_to(
                hidden_layer_circles[1].get_center()),
            Text("4", font_size=20).move_to(
                hidden_layer_circles[2].get_center())
        )

        # Create hidden layer title
        hidden_title = Text("Hidden Layer", font_size=20).move_to(
            UP * 3).shift(RIGHT * 2)

        # Add hidden layer elements to the scene
        self.add(hidden_layer_circles, hidden_layer_labels, hidden_title)

        # Create connections between input and hidden layers
        connections = VGroup()
        
        for input_circle in input_layer_circles:
            for hidden_circle in hidden_layer_circles:
                connection = Line(input_circle.get_right(),
                                  hidden_circle.get_left(), buff=0, color=GRAY)
                connections.add(connection)

        # Add connections to the scene
        self.play(Create(connections), run_time=4)
