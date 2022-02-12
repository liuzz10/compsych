from turtle import circle
from manim import *
from style import *
from manim_fonts import *

RADIUS = 0.4
SM_RADIUS = 0.35
WIDTH = 4
TEXT_SIZE = 30
LG_TEXT_SIZE = 40
VALUE_SIZE = 25
STROKE_WIDTH = 5
TABLE_STROKE_WIDTH = 5
LINE_SPACING = 0.3
TITLE_SIZE = 80

KARLA_PATH = "/Users/joyliu/Desktop/Joy/Github/compsych/heap/font/Karla/Karla-Regular.ttf"
FONT = "Karla"


class Heap(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        friend = Paragraph("""
        你
        朋
        友
        """)
        self.add(friend)
