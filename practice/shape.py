from manim import *


class Shape(Scene):
    def create_node(self, number):
        radius = 0.25
        font_size = 0.4
        circle = Circle(radius=radius).set_stroke(color=WHITE)
        text = Text(str(number)).scale(font_size)
        text.add_updater(lambda m: m.move_to(circle.get_center()))
        return VGroup(circle, text)

    def construct(self):
        square = Square().shift(UP * 2 + RIGHT * 2)
        triangle = Triangle().shift(UP + RIGHT * 2)
        dot = Dot().shift(RIGHT * 4)

        circle1 = self.create_node(1)
        circle2 = self.create_node(2).shift(LEFT * 0.8 + DOWN)
        circle3 = self.create_node(3).shift(RIGHT * 0.8 + DOWN)

        line2 = Line(circle1, circle2)
        line3 = Line(circle1, circle3)

        self.add(square, triangle, dot, circle1, circle2, circle3, line2, line3)
        # self.embed()

