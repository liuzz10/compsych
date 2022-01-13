from manim import *

RADIUS = 0.4
SM_RADIUS = 0.35
LINE_COLOR = WHITE
WIDTH = 4
TEXT_COLOR = WHITE
TEXT_SIZE = 30
VALUE_SIZE = 25
FONT = "Open Sans"
CORRECT_COLOR = GREEN
MISTAKE_COLOR = RED
CIRCLE_COLOR = WHITE

# Zindex: line 0, circle 1, description text 2

class Heap(Scene):
    def create_tree(self, array):
        c1 = Circle(radius=SM_RADIUS).set_stroke(color=CIRCLE_COLOR).set_fill(BLACK, opacity=1.0).shift(1.2 * UP).set_z_index(1)
        t1 = Text(array[0], font=FONT, font_size=VALUE_SIZE).move_to(c1.get_center()).set_z_index(2)
        c2 = Circle(radius=SM_RADIUS).set_stroke(color=CIRCLE_COLOR).set_fill(BLACK, opacity=1.0).shift(1.1 * LEFT + 0.2 * DOWN).set_z_index(1)
        t2 = Text(array[1], font=FONT, font_size=VALUE_SIZE).move_to(c2.get_center()).set_z_index(2)
        c3 = Circle(radius=SM_RADIUS).set_stroke(color=CIRCLE_COLOR).set_fill(BLACK, opacity=1.0).shift(1.1 * RIGHT + 0.2 * DOWN).set_z_index(1)
        t3 = Text(array[2], font=FONT, font_size=VALUE_SIZE).move_to(c3.get_center()).set_z_index(2)
        c4 = Circle(radius=SM_RADIUS).set_stroke(color=CIRCLE_COLOR).set_fill(BLACK, opacity=1.0).shift(1.7 * LEFT + 1.6 * DOWN).set_z_index(1)
        t4 = Text(array[3], font=FONT, font_size=VALUE_SIZE).move_to(c4.get_center()).set_z_index(2)
        c5 = Circle(radius=SM_RADIUS).set_stroke(color=CIRCLE_COLOR).set_fill(BLACK, opacity=1.0).shift(0.5 * LEFT + 1.6 * DOWN).set_z_index(1)
        t5 = Text(array[4], font=FONT, font_size=VALUE_SIZE).move_to(c5.get_center()).set_z_index(2)
        c6 = Circle(radius=SM_RADIUS).set_stroke(color=CIRCLE_COLOR).set_fill(BLACK, opacity=1.0).shift(0.5 * RIGHT + 1.6 * DOWN).set_z_index(1)
        t6 = Text(array[5], font=FONT, font_size=VALUE_SIZE).move_to(c6.get_center()).set_z_index(2)
        l12 = Line(c1.get_center(), c2.get_center()).set_stroke(color=CIRCLE_COLOR, width=WIDTH).set_z_index(0)
        l13 = Line(c1.get_center(), c3.get_center()).set_stroke(color=CIRCLE_COLOR, width=WIDTH).set_z_index(0)
        l24= Line(c2.get_center(), c4.get_center()).set_stroke(color=CIRCLE_COLOR, width=WIDTH).set_z_index(0)
        l25 = Line(c2.get_center(), c5.get_center()).set_stroke(color=CIRCLE_COLOR, width=WIDTH).set_z_index(0)
        l36= Line(c3.get_center(), c6.get_center()).set_stroke(color=CIRCLE_COLOR, width=WIDTH).set_z_index(0)
        tree = VGroup(c1, t1, l12, c2, t2, l13, c3, t3, l24, c4, t4, l25, c5, t5, l36, c6, t6)
        return tree

    def construct(self):
        text1 = Text("WHAT IS ", gradient=(GREEN, BLUE), font=FONT, font_size=80).shift(1.5 * LEFT)
        text2 = Text("HEAP?", gradient=(BLUE, YELLOW), font=FONT, font_size=80).shift(2.6 * RIGHT)
        # for letter in text:
        #     letter.set_color(random_bright_color())
        title_group = VGroup(text1, text2)
        self.play(Write(title_group))
        self.play(text1.animate.move_to(2.8 * LEFT), text2.animate.move_to(3.6 * RIGHT))
        binary = Text("(Binary)", color=BLUE, font=FONT, font_size=40).shift(0.8 * RIGHT)
        self.play(Write(binary))
        title_group += binary
        self.play(title_group.animate.scale(0.5).to_edge(UL, buff=0.8))
        
        ### 1. Binary Tree ###

        tree_text = Text("1. Binary tree", gradient=(BLUE, GREEN), font=FONT, font_size=TEXT_SIZE).next_to(title_group, DOWN, buff=0.3).align_to(title_group, LEFT)
        self.play(Write(tree_text))

        # circle = Circle(radius=RADIUS).set_stroke(color=WHITE).set_fill(BLACK, opacity=1.0).shift(2.5 * LEFT + 0.5 * UP).set_z_index(1)
        # circle_left = Circle(radius=RADIUS).set_stroke(color=WHITE).set_fill(BLACK, opacity=1.0).shift(3.7 * LEFT + 1.5 * DOWN).set_z_index(1)
        # circle_right = Circle(radius=RADIUS).set_stroke(color=WHITE).set_fill(BLACK, opacity=1.0).shift(1.3 * LEFT + 1.5 * DOWN).set_z_index(1)
        # line_left = Line(circle.get_center(), circle_left.get_center()).set_stroke(color=LINE_COLOR, width=WIDTH).set_z_index(0)
        # line_right = Line(circle.get_center(), circle_right.get_center()).set_stroke(color=LINE_COLOR, width=WIDTH).set_z_index(0)
        # binary_tree = VGroup(circle, line_left, line_right, circle_left, circle_right)
        # self.play(AnimationGroup(FadeIn(binary_tree)))

        # circle2 = Circle(radius=RADIUS).set_stroke(color=WHITE).set_fill(BLACK, opacity=1.0).shift(2.5 * RIGHT + 0.5 * UP).set_z_index(1)
        # circle2_left = Circle(radius=RADIUS).set_stroke(color=WHITE).set_fill(BLACK, opacity=1.0).shift(1.3 * RIGHT + 1.5 * DOWN).set_z_index(1)
        # circle2_mid = Circle(radius=RADIUS).set_stroke(color=WHITE).set_fill(BLACK, opacity=1.0).shift(2.5 * RIGHT + 1.5 * DOWN).set_z_index(1)
        # circle2_right = Circle(radius=RADIUS).set_stroke(color=WHITE).set_fill(BLACK, opacity=1.0).shift(3.7 * RIGHT + 1.5 * DOWN).set_z_index(1)
        # line2_left = Line(circle2.get_center(), circle2_left.get_center()).set_stroke(color=LINE_COLOR, width=WIDTH).set_z_index(0)
        # line2_mid = Line(circle2.get_center(), circle2_mid.get_center()).set_stroke(color=LINE_COLOR, width=WIDTH).set_z_index(0)
        # line2_right = Line(circle2.get_center(), circle2_right.get_center()).set_stroke(color=LINE_COLOR, width=WIDTH).set_z_index(0)
        # thirary_tree = VGroup(circle2, line2_left, line2_mid, line2_right, circle2_left, circle2_mid, circle2_right)
        # self.play(AnimationGroup(FadeIn(thirary_tree)))
        # self.play(binary_tree.animate.set_stroke(GREEN))
        # self.play(thirary_tree.animate.set_stroke(RED))
        # self.play(binary_tree.animate.scale(0.1).next_to(tree_text, RIGHT))
        # self.play(Unwrite(thirary_tree))

        ## 2. Complete tree ##

        complete_tree_text = Text("2. Complete tree", gradient=(BLUE, GREEN), font=FONT, font_size=TEXT_SIZE).next_to(tree_text, DOWN, buff=0.2).align_to(title_group, LEFT)
        self.play(Write(complete_tree_text))

        arrow = Arrow(2.8*LEFT, 2.8*RIGHT, color=GREEN, max_tip_length_to_length_ratio=0.1, max_stroke_width_to_length_ratio=2).shift(2.8 * DOWN)
        self.play(Write(arrow))

        # c1 = Circle(radius=RADIUS).set_stroke(color=GREEN).set_fill(BLACK, opacity=1.0).shift(1.4 * UP).set_z_index(1)
        # c2 = Circle(radius=RADIUS).set_stroke(color=GREEN).set_fill(BLACK, opacity=1.0).shift(1.5 * LEFT + 0.2 * DOWN).set_z_index(1)
        # c3 = Circle(radius=RADIUS).set_stroke(color=GREEN).set_fill(BLACK, opacity=1.0).shift(1.5 * RIGHT + 0.2 * DOWN).set_z_index(1)
        # c4 = Circle(radius=RADIUS).set_stroke(color=GREEN).set_fill(BLACK, opacity=1.0).shift(2.3 * LEFT + 1.8 * DOWN).set_z_index(1)
        # c5 = Circle(radius=RADIUS).set_stroke(color=GREEN).set_fill(BLACK, opacity=1.0).shift(0.7 * LEFT + 1.8 * DOWN).set_z_index(1)
        # l12 = Line(c1.get_center(), c2.get_center()).set_stroke(color=GREEN, width=WIDTH).set_z_index(0)
        # l13 = Line(c1.get_center(), c3.get_center()).set_stroke(color=GREEN, width=WIDTH).set_z_index(0)
        # l24= Line(c2.get_center(), c4.get_center()).set_stroke(color=GREEN, width=WIDTH).set_z_index(0)
        # l25 = Line(c2.get_center(), c5.get_center()).set_stroke(color=GREEN, width=WIDTH).set_z_index(0)
        # tree3 = VGroup(c1, l12, c2, l13, c3, l24, c4, l25, c5)
        # for e in tree3:
        #     self.play(FadeIn(e))
        # c6 = Circle(radius=RADIUS).set_stroke(color=GREEN).set_fill(BLACK, opacity=1.0).shift(0.7 * RIGHT + 1.9 * DOWN).set_z_index(1)
        # c7 = Circle(radius=RADIUS).set_stroke(color=GREEN).set_fill(BLACK, opacity=1.0).shift(2.3 * RIGHT + 1.9 * DOWN).set_z_index(1)
        # l36= Line(c3.get_center(), c6.get_center()).set_stroke(color=GREEN, width=WIDTH).set_z_index(0)
        # l37 = Line(c3.get_center(), c7.get_center()).set_stroke(color=GREEN, width=WIDTH).set_z_index(0) 
        # self.play(FadeIn(l36, c6, l37, c7))
        # tree3 += c6
        # tree3 += l36
        # tree3 += c7
        # tree3 += l37
        # self.play(AnimationGroup(tree3.animate.set_stroke(RED), FadeOut(l25, c5)))
        # tree3 -= l25
        # tree3 -= c5
        # self.play(FadeOut(l12, c2, l24, c4))
        # tree3 += l25
        # tree3 += c5
        # self.play(FadeIn(l12, c2, l24, c4), FadeOut(l13, c3, l36, c6, l37, c7))
        # self.play(FadeOut(c1, l12, c2, l24, c4))

        tri = Triangle().set_stroke(color=GREEN).scale(2.5).shift(0.3*DOWN)
        c1 = Circle(radius=0.3).set_stroke(color=RED).set_fill(BLACK, opacity=1.0).shift(1.4 * DOWN)
        c2 = Circle(radius=0.3).set_stroke(color=RED).set_fill(BLACK, opacity=1.0).shift(0.6 * RIGHT + 1.4 * DOWN)
        c3 = Circle(radius=0.3).set_stroke(color=RED).set_fill(BLACK, opacity=1.0).shift(1.2 * RIGHT + 1.4 * DOWN)
        # self.play(FadeIn(tri, c1, c2, c3))

        new_arrow = Arrow(0.4*LEFT, 0.4*RIGHT, color=GREEN, max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=6).next_to(complete_tree_text, RIGHT)
        self.play(Transform(arrow, new_arrow), FadeOut(tri, c1, c2, c3))

        ## 3. Value ##
        value_text = Text("3. Value", gradient=(BLUE, GREEN), font=FONT, font_size=TEXT_SIZE).next_to(complete_tree_text, DOWN, buff=0.2).align_to(title_group, LEFT)
        self.play(Write(value_text))

        max_heap = Text("Max", color=TEXT_COLOR , font=FONT, font_size=TEXT_SIZE).shift(LEFT + 1.7 * UP)
        self.play(Write(max_heap))

        tree = self.create_tree(["9","7","8","6","5","7"]).shift(LEFT + 0.5 * DOWN)
        self.play(Create(tree))
        self.wait(1)

