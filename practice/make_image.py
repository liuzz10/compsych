from manim import *

# Make a subclass of scene, which will be the scene being rendered
# A scene is the canvas of the animation
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        # Add circle to the scene
        self.add(circle)