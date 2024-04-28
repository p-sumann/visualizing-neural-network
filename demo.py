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
        hidden_title_1 = Text("Hidden Layer", font_size=15).move_to(
            UP * 3.7)
        # Add hidden layer elements to the scene
        # self.add(hidden_layer_circles_1, hidden_layer_labels_1, hidden_title_1)
        self.add(hidden_layer_circles_1, hidden_title_1)

        # Create hidden 2 layer circles
        hidden_layer_circles_2 = VGroup(
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
            Circle(radius=0.5, color=WHITE),
        ).arrange(DOWN, buff=0.4).shift(4 * RIGHT).shift(LEFT*4)
