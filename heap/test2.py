from manim import *
from colors import *

RADIUS = 0.4
SM_RADIUS = 0.45
WIDTH = 4
TEXT_SIZE = 30
LG_TEXT_SIZE = 40
VALUE_SIZE = 25
STROKE_WIDTH = 6
TABLE_STROKE_WIDTH = 5
LINE_SPACING = 0.3
TITLE_SIZE = 80
CIRCLE_COLOR = PINK3

KARLA_PATH = "/Users/joyliu/Desktop/Joy/Github/compsych/heap/font/Karla/Karla-Regular.ttf"
FONT = "Karla"

class Heap(Scene):
    def create_circle(self):
        return Circle(radius=3, stroke_width=3).set_stroke(color=PINK3).set_fill(BACKGROUND, opacity=1.0).set_z_index(1)

    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=CIRCLE_COLOR).set_fill(BACKGROUND, opacity=1.0).shift(2.5 * LEFT + 1 * UP).set_z_index(1)
        circle_left = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=CIRCLE_COLOR).set_fill(BACKGROUND, opacity=1.0).shift(3.7 * LEFT + 1 * DOWN).set_z_index(1)
        circle_right = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=CIRCLE_COLOR).set_fill(BACKGROUND, opacity=1.0).shift(1.3 * LEFT + 1 * DOWN).set_z_index(1)
        line_left = Line(circle.get_center(), circle_left.get_center()).set_stroke(color=CIRCLE_COLOR, width=STROKE_WIDTH).set_z_index(0)
        line_right = Line(circle.get_center(), circle_right.get_center()).set_stroke(color=CIRCLE_COLOR, width=STROKE_WIDTH).set_z_index(0)
        binary_tree = VGroup(circle, line_left, line_right, circle_left, circle_right).move_to(ORIGIN)
        self.add(binary_tree)