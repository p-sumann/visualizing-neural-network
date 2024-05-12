from manim import *


class demo(Scene):

    # def construct(self):

    #     text = Text("I am Suman",color='red',)

    #     self.play(Create(text))
    #     self.wait()
    #     self.play(Unwrite(text))

    def construct(self):

        input_layer = [Circle(radius=0.4, color=WHITE) for _ in range(3)]
        input_layer_vg = VGroup(*input_layer).arrange(DOWN, buff=0.2).shift(4.5*LEFT)
        
        hidden_layer = [Circle(radius=0.4, color=WHITE) for _ in range(5)]
        hidden_layer_vg = VGroup(
            *hidden_layer).arrange(DOWN, buff=0.2).shift(3*LEFT)
        
        output_layer = [Circle(radius=0.4, color=WHITE) for _ in range(2)]
        output_layer_vg = VGroup(
            *output_layer).arrange(DOWN, buff=0.2).shift(1.5*LEFT)
        # cir1 = Circle(radius=0.4, color=WHITE)
        # cir2 = Circle(radius=0.4, color=WHITE)
        # cir3 = Circle(radius=0.4, color=WHITE)
        
        self.play(Create(input_layer_vg),run_time=.5)
        self.play(Create(hidden_layer_vg), run_time=.5)
        self.play(Create(output_layer_vg), run_time=.5)