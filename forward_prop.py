from manim import * 

class CreateCircle(Scene):
    def construct(self):
        # Create input layer circles
        input_layer_circles = VGroup(
            Circle(radius=0.5, color=RED),
            Circle(radius=0.5, color=RED)
        ).arrange(DOWN, buff=0.5)