from turtle import circle
from manim import *
from style import *
from manim_fonts import *
from util import *

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

TEST_CODE = """EXTRACT-FIRST(A) {
    heapsize = length(A)
    Exchange A[1] with A[heapsize]
    Remove A[heapsize]
    HeapifyDown(A, 1)
    heapsize = length(A)
    Exchange A[1] with A[heapsize]
    Remove A[heapsize]
    HeapifyDown(A, 1)
    heapsize = length(A)
    Exchange A[1] with A[heapsize]
    Remove A[heapsize]
    HeapifyDown(A, 1)
}
"""


class Test(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        ch1 = ImageMobject("red.svg")
        self.play(FadeIn(ch1))
