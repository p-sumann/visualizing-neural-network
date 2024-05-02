from manim import * 
import random

config.background_color = WHITE

class BackwardProp(Scene):
    def construct(self):
        input_layer_circles_1 = VGroup()

        for _ in range(16):
            input_layer_circles_1.add(Circle(radius=0.15, color=GREY))

            input_layer_circles_1.arrange(DOWN, buff=0.15)
            
        self.add(input_layer_circles_1.shift(LEFT*4))
        
        input_layer_circles_2 = VGroup()

        for _ in range(12):
            input_layer_circles_2.add(Circle(radius=0.15, color=GREY))

            input_layer_circles_2.arrange(DOWN, buff=0.15)
            
        self.add(input_layer_circles_2.shift(LEFT*2))
        
            
        input_layer_circles_3 = VGroup()

        for _ in range(8):
            input_layer_circles_3.add(Circle(radius=0.15, color=GREY))

            input_layer_circles_3.arrange(DOWN, buff=0.15)
        
        self.add(input_layer_circles_3)
        
            
        input_layer_circles_4 = VGroup()

        for _ in range(4):
            input_layer_circles_4.add(Circle(radius=0.15, color=GREY))

            input_layer_circles_4.arrange(DOWN, buff=0.15)
        self.add(input_layer_circles_4.shift(RIGHT*2))
        
        
        input_layer_circles_5 = VGroup()

        for _ in range(2):
            input_layer_circles_5.add(Circle(radius=0.15, color=GREY))

            input_layer_circles_5.arrange(DOWN, buff=0.15)
            
        self.add(input_layer_circles_5.shift(RIGHT*4))



        # Create hidden layer title
        # hidden_title = Text("Hidden Layer", font_size=20).move_to(
        #     UP * 3).shift(RIGHT * 2)

        # # Add hidden layer elements to the scene
        # # self.add(hidden_layer_circles, hidden_layer_labels, hidden_title)
        # self.add(hidden_layer_circles, hidden_title)

        # Create connections between input and hidden layers
        # connections = VGroup()
        
        # for input_circle in input_layer_circles:
            
        #     for hidden_circle in hidden_layer_circles:
                
        #         connection = Line(input_circle.get_right(),
        #                           hidden_circle.get_left(), buff=0, color=GRAY)
        #         connections.add(connection)

        # # Backward prop
        
        # connections1 = VGroup()
        # for hidden_circle in hidden_layer_circles:
            
        #     for input_circle in input_layer_circles:
                
        #         connection_1 = Line(hidden_circle.get_left(),
        #                           input_circle.get_right(),buff=0, color=ORANGE)
        #         connections1.add(connection_1)
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
                if i == 2:
                    text = Text(f"{round(random.random(),2)}", font_size=20).move_to(
                        hidden_circle.get_center())
                    connections_1.add(text)

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

        
        self.play(Create(connections_1),run_time=2)
        self.play(Create(connections_2),run_time=2)
        self.play(Create(connections_3),run_time=3)
        self.play(Create(connections_4),run_time=1)
        self.play(Create(backward_prop_1),run_time=0.5)
        self.play(Create(backward_prop_2),run_time=0.5)
        
        self.wait()
        # self.play(Create(connections_5),run_time=5)
        
        
        
        
        
        # self.play(Create(connections1), run_time=2)
        
        
        
        
                