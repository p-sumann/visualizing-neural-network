# from manim import *


# class TextAnimation(Scene):
#     def construct(self):
#         # Initial text
#         forward_prop = Text("Forward Prop").to_corner(UL)
#         self.play(forward_prop.animate(rate_func=linear))
#         self.wait(1)

#         # Transform to "Backward Prop"
#         backward_prop = Text("Backward Prop").to_corner(UL)
#         self.play(Transform(forward_prop, backward_prop))
#         self.wait(1)

#         # Transform back to "Forward Prop after Update"
#         forward_prop_update = Text("Forward Prop after Update").to_corner(UL)
#         self.play(FadeTransformPieces(backward_prop, forward_prop_update))
#         self.wait()


from manim import *


class TextAnimation(Scene):
    def construct(self):
        # Create the initial text
        text = Text("Forward Prop", color=WHITE).shift(UP*3 + RIGHT*3)

        # Add the text to the scene
        self.play(Write(text))

        # Define transformations
        to_backward_prop = Text("Backward Prop").next_to(
            text, aligned_edge=RIGHT).shift(LEFT*2)
        to_forward_prop_after_update = Text("Forward Prop after Update").next_to(
            text, aligned_edge=RIGHT).shift(LEFT*2.5)

        # Animation
        self.play(Transform(text, to_backward_prop))
        self.wait(1)
        self.play(Transform(text, to_forward_prop_after_update))
        self.wait(5)

        # # Play last scene for a few seconds
        # self.wait(3)
