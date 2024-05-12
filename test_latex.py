from manim import * 
import random

config.background_color = WHITE


class BackwardProp(Scene):
    def construct(self):
        input_layer_circles_1 = VGroup()

        for _ in range(8):
            input_layer_circles_1.add(Circle(radius=0.15, color=GREY))

        input_layer_circles_1.arrange(DOWN, buff=0.15)
        
        self.add(input_layer_circles_1.shift(LEFT*4))
        # Add vertical dots to the left of the first VGroup
        vdots = VGroup()
        for i in range(3):
            vdot = Dot(point=input_layer_circles_1[4].get_left() + LEFT*0.5 + DOWN*i*0.2, radius=0.05, color=BLACK)
            vdots.add(vdot)
        # Add a brace to the left of the first VGroup
        brace = Brace(input_layer_circles_1, direction=LEFT*7, color=BLACK)
        self.add(brace)
        text = Text("Input Features (n)", color=BLACK, font_size=20).shift(LEFT*5.75)
        self.add(text)
        
        input_layer_circles_2 = VGroup()

        for _ in range(16):
            input_layer_circles_2.add(Circle(radius=0.15, color=GREY))

        input_layer_circles_2.arrange(DOWN, buff=0.15)
        
        label = Text("Hidden Layer", font_size=20,color=BLACK).next_to(input_layer_circles_2, UP*.4).shift(LEFT*2)
        self.add(input_layer_circles_2.shift(LEFT*2))
        self.add(label)
        
        connections_1 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [1, 1.6, 2.4, 3]
        for i, input_circle in enumerate(input_layer_circles_1):
            for j, hidden_circle in enumerate(input_layer_circles_2):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=GRAY,
                            stroke_width=thickness)
                connections_1.add(line)
        
        self.play(Create(connections_1), run_time=1)
        