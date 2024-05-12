# from manim import *


# class CreateCircle(Scene):
#     def construct(self):
#         input_layer_c = VGroup(
#             Circle(radius=0.5, color=RED),
#             Circle(radius=0.5, color=RED)
#         ).arrange(DOWN, buff=0.5)

#         inpit_layer_t = VGroup(
#             Text("2", font_size=20).move_to(input_layer_c[0].get_center()),
#             Text("3", font_size=20).move_to(input_layer_c[1].get_center())
#         )
#         input_title = Text("Input Layer", font_size=20).move_to(UP * 3)
#         self.add(input_layer_c, inpit_layer_t, input_title)

#         hidden_layer_c = VGroup(
#             Circle(radius=0.5, color=RED),
#             Circle(radius=0.5, color=RED),
#             Circle(radius=0.5, color=RED),
#         ).arrange(DOWN, buff=0.5).shift(2*RIGHT)

#         hidden_layer_t = VGroup(
#             Text("2", font_size=20).move_to(hidden_layer_c[0].get_center()),
#             Text("3", font_size=20).move_to(hidden_layer_c[1].get_center()),
#             Text("4", font_size=20).move_to(hidden_layer_c[2].get_center())
#         )

#         hidden_title = Text("Hidden Layer", font_size=20).move_to(UP * 3).shift(RIGHT*2)

#         self.add(hidden_layer_c, hidden_layer_t, hidden_title)

#         output_layer_c = Circle(radius=0.5, color=RED).arrange(
#             DOWN, buff=0.5).shift(4*RIGHT)
#         output_layer_t = Text("4", font_size=20).move_to(
#             output_layer_c.get_center())
#         output_layer = Text("Output Layer", font_size=20).move_to(
#             UP * 3).shift(RIGHT*4)

#         self.add(output_layer_c, output_layer_t, output_layer)

import random

from manim import *
config.background_color = WHITE

class CreateCircle(Scene):
    def construct(self):
        # Create input layer circles
        input_layer_circles = VGroup(
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
            # Circle(radius=0.5, color=GREY),
        ).arrange(DOWN, buff=0.4).shift(LEFT*4)

        # # Create input layer labels
        # input_layer_labels = VGroup(
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         input_layer_circles[0].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         input_layer_circles[1].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         input_layer_circles[2].get_center())
        # )
        # Create input layer title
        input_title = Text("Input Layer", font_size=15, color=BLACK).move_to(
            UP * 3).shift(4*LEFT)

        # Add input layer elements to the scene
        # self.add(input_layer_circles, input_layer_labels, input_title)
        

        # Create hidden 1 layer circles
        # hidden_layer_circles_1 = VGroup(
        #     Circle(radius=0.5, color=GREY),
        #     Circle(radius=0.5, color=GREY),
        #     Circle(radius=0.5, color=GREY),
        #     Circle(radius=0.5, color=GREY),
        # ).arrange(DOWN, buff=0.4).shift(2 * RIGHT).shift(LEFT*4)

        # Create hidden layer labels
        # hidden_layer_labels_1 = VGroup(
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_1[0].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_1[1].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_1[2].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_1[3].get_center())
        # )
        # Create hidden layer title
        # hidden_title_1 = Text("Hidden Layer", font_size=15, color=BLACK).move_to(
        #     UP * 3.7)
        # # Add hidden layer elements to the scene
        # # self.add(hidden_layer_circles_1, hidden_layer_labels_1, hidden_title_1)
        # self.add(hidden_layer_circles_1, hidden_title_1)

        # Create hidden 2 layer circles
        hidden_layer_circles_2 = VGroup(
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
        ).arrange(DOWN, buff=0.4).shift(4 * RIGHT).shift(LEFT*5)

        # Create hidden layer labels
        # hidden_layer_labels_2 = VGroup(
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_2[0].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_2[1].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_2[2].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_2[3].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         hidden_layer_circles_2[4].get_center())
        # )

        # Create hidden layer title
        hidden_title_2 = Text("Hidden Layer", font_size=15, color=BLACK).move_to(
            UP * 3.7).shift(LEFT*1)

        # Add hidden layer elements to the scene
        # self.add(hidden_layer_circles_2, hidden_layer_labels_2, hidden_title_2)
        self.add(hidden_layer_circles_2, hidden_title_2)

        # Create input layer circles
        hidden_layer_circles_3 = VGroup(
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
        ).arrange(DOWN, buff=0.4).shift(RIGHT*2)

        # Create input layer labels
        # output_layer_labels = VGroup(
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         output_layer_circles[0].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         output_layer_circles[1].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         output_layer_circles[2].get_center()),
        # )
        # Create input layer title
        hidden_title_3 = Text("Hidden Layer", font_size=15, color=BLACK).move_to(
            UP * 3.7).shift(2*RIGHT)

        # Add input layer elements to the scene
        self.add(hidden_layer_circles_3, hidden_title_3)

        # Create input layer circles
        output_layer = VGroup(
            Circle(radius=0.5, color=GREY),
            Circle(radius=0.5, color=GREY),
        ).arrange(DOWN, buff=0.4).shift(RIGHT*5)

        # Create input layer labels
        # output_layer_labels = VGroup(
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         output_layer_circles[0].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         output_layer_circles[1].get_center()),
        #     Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #         output_layer_circles[2].get_center()),
        # )
        # Create input layer title
        output_title = Text("Output Layer", font_size=15,color=BLACK).move_to(
            UP * 3.7).shift(5*RIGHT)

        # Add input layer elements to the scene
        self.add(output_layer, output_title)

        connections1 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [0.8, 1.6, 2.4, 3]
        text_objects = []
        for i, input_circle in enumerate(input_layer_circles):
            for j, hidden_circle in enumerate(hidden_layer_circles_2):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=color,
                            stroke_width=thickness)
                connections1.add(line)
                # if i == 2:
                #     text = Text(f"{round(random.random(),2)}",color=BLACK, font_size=20).move_to(
                #         hidden_circle.get_center())
                #     connections1.add(text)

        connections2 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [1.3, 1.6, 2.4, 3]
        for i, input_circle in enumerate(hidden_layer_circles_2):
            for j, hidden_circle in enumerate(hidden_layer_circles_3):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=color,
                            stroke_width=thickness)

                connections2.add(line)
                # if i == 1:
                #     text = Text(f"{round(random.random(),2)}", font_size=20).move_to(
                #         hidden_circle.get_center())
                #     connections2.add(text)

        # connections3 = VGroup()
        # colors = [RED, GREEN, BLUE]
        # thicknesses = [1, 1.6, 2.4, 3]
        # for i, input_circle in enumerate(hidden_layer_circles_3):
        #     for j, hidden_circle in enumerate(hidden_layer_circles_):
        #         color = random.choice(colors)
        #         thickness = random.choice(thicknesses)
        #         line = Line(input_circle.get_right(), hidden_circle.get_left(),
        #                     buff=0, color=color,
        #                     stroke_width=thickness)

        #         connections3.add(line)
        #         if i == 2:
        #             text = Text(f"{round(random.random(),2)}", font_size=20).move_to(
        #                 hidden_circle.get_center())
        #             connections3.add(text)

        connections4 = VGroup()
        colors = [RED, GREEN, BLUE]
        thicknesses = [1.3, 1.6, 2.4, 3]
        for i, input_circle in enumerate(hidden_layer_circles_3):
            for j, hidden_circle in enumerate(output_layer):
                color = random.choice(colors)
                thickness = random.choice(thicknesses)
                line = Line(input_circle.get_right(), hidden_circle.get_left(),
                            buff=0, color=color,
                            stroke_width=thickness)

                connections4.add(line)
        # text1 = Text("0", font_size=20).move_to(
        #     output_layer[0].get_center())
        # text2 = Text("1", font_size=20).move_to(
        #     output_layer[1].get_center())
        # connections4.add(text1, text2, color=BLACK)

        # Add connections to the scene
        # self.wait(1)
        self.begin_animations(input_layer_circles, input_title)
        
        self.play(Create(connections1), run_time=2)
        self.play(Create(connections2), run_time=2)
        # self.play(Create(connections3), run_time=2)
        self.play(Create(connections4), run_time=2)
        # self.renderer.write_to_png('demo.png')
