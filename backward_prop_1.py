from manim import * 
import random

config.background_color = WHITE

class Backward(Scene):
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
        
            
        input_layer_circles_3 = VGroup()

        for _ in range(12):
            input_layer_circles_3.add(Circle(radius=0.15, color=GREY))

        input_layer_circles_3.arrange(DOWN, buff=0.15)
        
        self.add(input_layer_circles_3)
        
        label = Text("Hidden Layer", font_size=20,color=BLACK).next_to(input_layer_circles_3, UP*.4)
        # self.add(input_layer_circles_3.shift(LEFT*2))
        self.add(label)
            
        input_layer_circles_4 = VGroup()

        for _ in range(6):
            input_layer_circles_4.add(Circle(radius=0.15, color=GREY))

        input_layer_circles_4.arrange(DOWN, buff=0.15)
        self.add(input_layer_circles_4.shift(RIGHT*2))
        
        label_4 = Text("Hidden Layer", font_size=20,color=BLACK).next_to(input_layer_circles_4, UP*.6)
        # self.add(input_layer_circles_3.shift(LEFT*2))
        self.add(label_4)
        
        
        input_layer_circles_5 = VGroup()

        for _ in range(2):
            input_layer_circles_5.add(Circle(radius=0.15, color=GREY))

        input_layer_circles_5.arrange(DOWN, buff=0.15)            
        self.add(input_layer_circles_5.shift(RIGHT*4))
        
        outout_layer = Text("Output Layer", font_size=20,color=BLACK).next_to(input_layer_circles_5, UP*.5)
        # self.add(input_layer_circles_3.shift(LEFT*2))
        self.add(outout_layer)


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
        
        connections_2 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [1, 1.6, 2.4, 3]
        for i, input_circle in enumerate(input_layer_circles_2):
            for j, hidden_circle in enumerate(input_layer_circles_3):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=GRAY,
                            stroke_width=thickness)

                connections_2.add(line)
                
        connections_3 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [1, 1.6, 2.4, 3]
        for i, input_circle in enumerate(input_layer_circles_3):
            for j, hidden_circle in enumerate(input_layer_circles_4):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=GRAY,
                            stroke_width=thickness)

                connections_3.add(line)
                
        connections_4 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [1, 1.6, 2.4, 3]
        for i, input_circle in enumerate(input_layer_circles_4):
            for j, hidden_circle in enumerate(input_layer_circles_5):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=GRAY,
                            stroke_width=thickness)

                connections_4.add(line)
                
        # Backward prop
        
        backward_prop_1 = VGroup()
        for hidden_circle in input_layer_circles_5:
            for input_circle in input_layer_circles_4:
                colors = [RED, GREEN, BLUE]
                thicknesses = [1, 1.6, 2.4]
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                connection_1 = Line(hidden_circle.get_left(),
                                  input_circle.get_right(),buff=0, color=color,stroke_width=thickness)
                backward_prop_1.add(connection_1)
                
        backward_prop_2 = VGroup()
        for i, hidden_circle in enumerate(input_layer_circles_4):
            for input_circle in input_layer_circles_3:
                colors = [RED, GREEN, BLUE, ORANGE]
                thicknesses = [1, 1.2, 1.4, 0.7]
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                connection_1 = Line(hidden_circle.get_left(),
                                  input_circle.get_right(),buff=0, color=color,stroke_width=thickness)
                backward_prop_2.add(connection_1)

        backward_prop_3 = VGroup()
        for i, hidden_circle in enumerate(input_layer_circles_3):
            for input_circle in input_layer_circles_2:
                colors = [RED, GREEN, BLUE, ORANGE]
                thicknesses = [1, 1.2, 1.4, 0.7]
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                connection_1 = Line(hidden_circle.get_left(),
                                  input_circle.get_right(),buff=0, color=color,stroke_width=thickness)
                backward_prop_3.add(connection_1)
                
        backward_prop_4 = VGroup()
        for i, hidden_circle in enumerate(input_layer_circles_2):
            for input_circle in input_layer_circles_1:
                colors = [RED, GREEN, BLUE, ORANGE]
                thicknesses = [1, 1.2, 1.4, 0.7]
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                connection_1 = Line(hidden_circle.get_left(),
                                  input_circle.get_right(),buff=0, color=color,stroke_width=thickness)
                backward_prop_4.add(connection_1)
        
        text = Text("Forward Prop", color=BLACK, font_size=15).shift(UP*3 + RIGHT*4)
        self.play(Write(text))
        self.play(Create(connections_1),run_time=1)
        self.play(Create(connections_2),run_time=1)
        self.play(Create(connections_3),run_time=1)
        self.play(Create(connections_4),run_time=1.5)
        self.wait(0.5)
        to_backward_prop = Text("Backward Prop", color=BLACK, font_size=15).next_to(
            text, aligned_edge=RIGHT).shift(LEFT*1)
        self.play(Transform(text, to_backward_prop))
        
        self.play(Create(backward_prop_1),run_time=1.5)
        self.play(Create(backward_prop_2),run_time=1.5)
        self.play(Create(backward_prop_3),run_time=1.5)
        self.play(Create(backward_prop_4),run_time=1.5)
        # self.wait(1)
        # self.play(Create(connections_1),run_time=0.5)
        # self.play(Create(connections_2),run_time=0.5)
        # self.play(Create(connections_3),run_time=0.5)
        # self.play(Create(connections_4),run_time=0.5)
        
        self.wait()
        # self.play(Create(connections_5),run_time=5)
        
        
        
        
        
        # self.play(Create(connections1), run_time=2)
        
        
        
        
                