import random

from manim import *


class CreateCircle(Scene):
    def construct(self):
        # Create input layer circles
        input_layer_circles = VGroup(
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
        ).arrange(DOWN, buff=0.4).shift(LEFT*4)
        
        # Create input layer labels
        input_layer_labels = VGroup(
            Text(f"{round(random.random(),2)}", font_size=20).move_to(
                input_layer_circles[0].get_center()),
            Text(f"{round(random.random(),2)}", font_size=20).move_to(
                input_layer_circles[1].get_center()),
            Text(f"{round(random.random(),2)}", font_size=20).move_to(
                input_layer_circles[2].get_center())
        )
        
        # Create input layer title
        input_title = Text("Input Layer", font_size=15).move_to(
            UP * 3).shift(4*LEFT)

        # Add input layer elements to the scene
        self.add(input_layer_circles, input_layer_labels, input_title)
        # self.add(input_layer_circles, input_title)

        # Create hidden 1 layer circles
        hidden_layer_circles_1 = VGroup(
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
        ).arrange(DOWN, buff=0.4).shift(2 * RIGHT).shift(LEFT*4)

        # Create 1st hidden layer title
        hidden_title_1 = Text("Hidden Layer", font_size=15).move_to(UP * 3.7)
        self.add(hidden_layer_circles_1, hidden_title_1)

        # Create hidden 2 layer circles
        hidden_layer_circles_2 = VGroup(
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
        ).arrange(DOWN, buff=0.4).shift(4 * RIGHT).shift(LEFT*4)

        # Create hidden layer title
        hidden_title_2 = Text("Hidden Layer", font_size=15).move_to(UP * 3.7).shift(LEFT*2)
        self.add(hidden_layer_circles_2, hidden_title_2)
        
        
        # Create 3rd hidden layer circles
        hidden_layer_circles_3 = VGroup(
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
        ).arrange(DOWN, buff=0.4).shift(RIGHT*2)

        hidden_title_3 = Text("Hidden Layer", font_size=15).move_to(
            UP * 3.7).shift(2*RIGHT)
        
        self.add(hidden_layer_circles_3, hidden_title_3)

        # Create output layer circles
        output_layer = VGroup(
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
        ).arrange(DOWN, buff=0.4).shift(RIGHT*4)
        
        output_title = Text("Output Layer", font_size=15).move_to(
            UP * 3.7).shift(4*RIGHT)

        # Add input layer elements to the scene
        self.add(output_layer, output_title)
        
        # make connections for all
        # for first layer to second layer
        connections1 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [0.8, 1.6, 2.4, 3]
        text_objects = []
        for i, input_circle in enumerate(input_layer_circles):
            for j, hidden_circle in enumerate(hidden_layer_circles_1):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=color,
                            stroke_width=thickness)
                connections1.add(line)
                if i == 2:
                    text = Text(f"{round(random.random(),2)}", font_size=20).move_to(
                        hidden_circle.get_center())
                    connections1.add(text)
                    
        # for second to third layer
        connections2 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [1, 1.6, 2.4, 3]
        for i, input_circle in enumerate(hidden_layer_circles_1):
            for j, hidden_circle in enumerate(hidden_layer_circles_2):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=color,
                            stroke_width=thickness)

                connections2.add(line)
                if i == 1:
                    text = Text(f"{round(random.random(),2)}", font_size=20).move_to(
                        hidden_circle.get_center())
                    connections2.add(text)
        
        # for third to fourth layer


