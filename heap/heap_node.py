from manim import *
from style import *
from manim_fonts import *
import math

class HeapNode:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.left = 2 * self.index + 1
        self.right = 2 * self.index + 2
        self.parent = math.floor((index - 1) / 2)
        self.offset = 0
        self.position_x = 0
        self.position_y = 0
        self.mobject = None
        self.text_mobject = self._create_text_mobject(value)
        self.line_mobject = None
    
    def _create_mobject(self):
        """
        Convert a node to an MObject so that it shows on the canvas
        """
        circle = Circle(radius=RADIUS).set_stroke(color=GRAY, width=STROKE_WIDTH).set_fill(BACKGROUND, opacity=1.0)
        text = Text(str(self.value), color=GRAY, font=FONT, weight="BOLD", font_size=VALUE_SIZE)
        key_mobject_list = [("circle", circle), ("text", text)]
        # If the node is on the left side of the root
        if self.position_x < 0:
            self.mobject = VDict(key_mobject_list).shift(LEFT * abs(self.position_x) + DOWN * self.position_y).set_z_index(1)
        # If the node is on the right side of the root
        else:
            self.mobject = VDict(key_mobject_list).shift(RIGHT * abs(self.position_x) + DOWN * self.position_y).set_z_index(1)

    def _create_text_mobject(self, value):
        return Text(str(value), color=GRAY, font=FONT, weight="BOLD", font_size=VALUE_SIZE)