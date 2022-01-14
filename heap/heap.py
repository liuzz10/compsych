from manim import *
from manim.utils.color import color_gradient, Colors

RADIUS = 0.4
SM_RADIUS = 0.35
LINE_COLOR = WHITE
WIDTH = 4
TEXT_COLOR = WHITE
TEXT_SIZE = 30
LG_TEXT_SIZE = 40
VALUE_SIZE = 25
FONT = "Open Sans"
CORRECT_COLOR = Colors.teal_c.value
MISTAKE_COLOR = RED
CIRCLE_COLOR = WHITE
TEAL = Colors.teal_c.value
PINK = Colors.pink.value
GREEN_E = Colors.green_e.value
GRADIENT = color_gradient([Colors.blue_e.value, Colors.teal_e.value], 2)
GRAY_D = Colors.dark_gray.value
BLUE_E = Colors.blue_e.value
PINK_GRADIENT = color_gradient([GOLD, PINK], 2)

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
        tree = VDict([("c1", c1), ("t1", t1), ("l12", l12), ("c2", c2), ("t2", t2), ("l13", l13), ("c3", c3), ("t3", t3), ("l24", l24), ("c4", c4), ("t4", t4), ("l25", l25), ("c5", c5), ("t5", t5), ("l36", l36), ("c6", c6), ("t6", t6)])
        return tree

    def construct(self):
        text1 = Text("WHAT IS ", gradient=(GREEN, BLUE), font=FONT, font_size=80).shift(1.5 * LEFT)
        text2 = Text("HEAP?", gradient=(BLUE, YELLOW), font=FONT, font_size=80).shift(2.6 * RIGHT)
        # for letter in text:
        #     letter.set_color(random_bright_color())
        title_group = VGroup(text1, text2)
        # self.play(Write(title_group))
        # self.play(text1.animate.move_to(2.8 * LEFT), text2.animate.move_to(3.6 * RIGHT))
        binary = Text("(Binary)", color=BLUE, font=FONT, font_size=40).shift(0.8 * RIGHT)
        # self.play(Write(binary))
        title_group += binary
        self.play(title_group.animate.scale(0.25).set_fill(opacity = 0.8).to_edge(UL, buff=0.8))
        
        # ### 1. Binary Tree ###

        # tree_text = Text("1. Binary tree", gradient=(BLUE, GREEN), font=FONT, font_size=TEXT_SIZE).next_to(title_group, DOWN, buff=0.3).align_to(title_group, LEFT)
        # self.play(Write(tree_text))

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
        # self.play(binary_tree.animate.set_stroke(CORRECT_COLOR))
        # self.play(thirary_tree.animate.set_stroke(MISTAKE_COLOR))
        # self.play(binary_tree.animate.scale(0.1).next_to(tree_text, RIGHT))
        # self.play(Unwrite(thirary_tree))

        # ## 2. Complete tree ##

        # complete_tree_text = Text("2. Complete tree", gradient=(BLUE, GREEN), font=FONT, font_size=TEXT_SIZE).next_to(tree_text, DOWN, buff=0.2).align_to(title_group, LEFT)
        # self.play(Write(complete_tree_text))

        # arrow = Arrow(2.8*LEFT, 2.8*RIGHT, color=TEAL, max_tip_length_to_length_ratio=0.1, max_stroke_width_to_length_ratio=1).shift(2.8 * DOWN)
        # self.play(Write(arrow))

        # c1 = Circle(radius=RADIUS).set_stroke(color=CORRECT_COLOR).set_fill(BLACK, opacity=1.0).shift(1.4 * UP).set_z_index(1)
        # c2 = Circle(radius=RADIUS).set_stroke(color=CORRECT_COLOR).set_fill(BLACK, opacity=1.0).shift(1.5 * LEFT + 0.2 * DOWN).set_z_index(1)
        # c3 = Circle(radius=RADIUS).set_stroke(color=CORRECT_COLOR).set_fill(BLACK, opacity=1.0).shift(1.5 * RIGHT + 0.2 * DOWN).set_z_index(1)
        # c4 = Circle(radius=RADIUS).set_stroke(color=CORRECT_COLOR).set_fill(BLACK, opacity=1.0).shift(2.3 * LEFT + 1.8 * DOWN).set_z_index(1)
        # c5 = Circle(radius=RADIUS).set_stroke(color=CORRECT_COLOR).set_fill(BLACK, opacity=1.0).shift(0.7 * LEFT + 1.8 * DOWN).set_z_index(1)
        # l12 = Line(c1.get_center(), c2.get_center()).set_stroke(color=CORRECT_COLOR, width=WIDTH).set_z_index(0)
        # l13 = Line(c1.get_center(), c3.get_center()).set_stroke(color=CORRECT_COLOR, width=WIDTH).set_z_index(0)
        # l24= Line(c2.get_center(), c4.get_center()).set_stroke(color=CORRECT_COLOR, width=WIDTH).set_z_index(0)
        # l25 = Line(c2.get_center(), c5.get_center()).set_stroke(color=CORRECT_COLOR, width=WIDTH).set_z_index(0)
        # tree3 = VGroup(c1, l12, c2, l13, c3, l24, c4, l25, c5)
        # for e in tree3:
        #     self.play(FadeIn(e))
        # c6 = Circle(radius=RADIUS).set_stroke(color=CORRECT_COLOR).set_fill(BLACK, opacity=1.0).shift(0.7 * RIGHT + 1.8 * DOWN).set_z_index(1)
        # c7 = Circle(radius=RADIUS).set_stroke(color=CORRECT_COLOR).set_fill(BLACK, opacity=1.0).shift(2.3 * RIGHT + 1.8 * DOWN).set_z_index(1)
        # l36= Line(c3.get_center(), c6.get_center()).set_stroke(color=CORRECT_COLOR, width=WIDTH).set_z_index(0)
        # l37 = Line(c3.get_center(), c7.get_center()).set_stroke(color=CORRECT_COLOR, width=WIDTH).set_z_index(0) 
        # self.play(FadeIn(l36, c6, l37, c7))
        # tree3 += c6
        # tree3 += l36
        # tree3 += c7
        # tree3 += l37
        # self.play(AnimationGroup(tree3.animate.set_stroke(MISTAKE_COLOR), FadeOut(l25, c5)))
        # tree3 -= l25
        # tree3 -= c5
        # self.play(FadeOut(l12, c2, l24, c4))
        # tree3 += l25
        # tree3 += c5
        # self.play(FadeIn(l12, c2, l24, c4), FadeOut(l13, c3, l36, c6, l37, c7))
        # self.play(FadeOut(c1, l12, c2, l24, c4))

        # tri = Triangle().set_stroke(color=TEAL).scale(2.5).shift(0.3*DOWN)
        # c1 = Circle(radius=0.3).set_stroke(color=MISTAKE_COLOR).set_fill(BLACK, opacity=1.0).shift(1.4 * DOWN)
        # c2 = Circle(radius=0.3).set_stroke(color=MISTAKE_COLOR).set_fill(BLACK, opacity=1.0).shift(0.6 * RIGHT + 1.4 * DOWN)
        # c3 = Circle(radius=0.3).set_stroke(color=MISTAKE_COLOR).set_fill(BLACK, opacity=1.0).shift(1.2 * RIGHT + 1.4 * DOWN)
        # # self.play(FadeIn(tri, c1, c2, c3))

        # new_arrow = Arrow(0.4*LEFT, 0.4*RIGHT, color=TEAL, max_tip_length_to_length_ratio=0.5, max_stroke_width_to_length_ratio=6).next_to(complete_tree_text, RIGHT)
        # self.play(Transform(arrow, new_arrow), FadeOut(tri, c1, c2, c3))

        # ## 3. Value ##
        # value_text = Text("3. Value", gradient=(BLUE, GREEN), font=FONT, font_size=TEXT_SIZE).next_to(complete_tree_text, DOWN, buff=0.2).align_to(title_group, LEFT)
        # self.play(Write(value_text))

        # max_heap = Text("Max", color=TEXT_COLOR , font=FONT, font_size=TEXT_SIZE).shift(LEFT + 1.7 * UP)
        # self.play(Write(max_heap))
        tree = self.create_tree(["9","8","6","7","4","5"])
        # self.play(Create(tree.shift(LEFT + 0.5 * DOWN)))
        # self.wait(1)

        # min_heap = Text("Min", color=TEXT_COLOR , font=FONT, font_size=TEXT_SIZE).shift(4 * RIGHT + 1.7 * UP)
        # self.play(Write(min_heap))
        # tree2 = self.create_tree(["1","2","4","3","6","5"]).shift(4 * RIGHT + 0.5 * DOWN)
        # self.play(Create(tree2))
        # self.wait(1)

        # highlight1 = AnimationGroup(tree["c1"].animate.set_fill(GRADIENT), tree["c2"].animate.set_fill(GREEN_E), tree["c3"].animate.set_fill(GREEN_E))
        # self.play(highlight1)
        # dehighlight1 = AnimationGroup(tree["c1"].animate.set_fill(BLACK), tree["c2"].animate.set_fill(BLACK), tree["c3"].animate.set_fill(BLACK))
        # self.play(dehighlight1)
        # highlight2 = AnimationGroup(tree["c2"].animate.set_fill(GRADIENT), tree["c4"].animate.set_fill(GREEN_E), tree["c5"].animate.set_fill(GREEN_E))
        # self.play(highlight2)
        # dehighlight2 = AnimationGroup(tree["c2"].animate.set_fill(BLACK), tree["c4"].animate.set_fill(BLACK), tree["c5"].animate.set_fill(BLACK))
        # self.play(dehighlight2)
        # highlight3 = AnimationGroup(tree["c3"].animate.set_fill(GRADIENT), tree["c6"].animate.set_fill(GREEN_E))
        # self.play(highlight3)
        # dehighlight3 = AnimationGroup(tree["c3"].animate.set_fill(BLACK), tree["c6"].animate.set_fill(BLACK))
        # self.play(dehighlight3)

        # highlight2_1 = AnimationGroup(tree2["c1"].animate.set_fill(GREEN_E), tree2["c2"].animate.set_fill(GRADIENT), tree2["c3"].animate.set_fill(GRADIENT))
        # self.play(highlight2_1)
        # dehighlight2_1 = AnimationGroup(tree2["c1"].animate.set_fill(BLACK), tree2["c2"].animate.set_fill(BLACK), tree2["c3"].animate.set_fill(BLACK))
        # self.play(dehighlight2_1)
        # highlight2_2 = AnimationGroup(tree2["c2"].animate.set_fill(GREEN_E), tree2["c4"].animate.set_fill(GRADIENT), tree2["c5"].animate.set_fill(GRADIENT))
        # self.play(highlight2_2)
        # dehighlight2_2 = AnimationGroup(tree2["c2"].animate.set_fill(BLACK), tree2["c4"].animate.set_fill(BLACK), tree2["c5"].animate.set_fill(BLACK))
        # self.play(dehighlight2_2)
        # highlight2_3 = AnimationGroup(tree2["c3"].animate.set_fill(GREEN_E), tree2["c6"].animate.set_fill(GRADIENT))
        # self.play(highlight2_3)
        # dehighlight2_3 = AnimationGroup(tree2["c3"].animate.set_fill(BLACK), tree2["c6"].animate.set_fill(BLACK))
        # self.play(dehighlight2_3)

        # self.play(Uncreate(tree2), Unwrite(min_heap))
        # self.play(max_heap.animate.move_to(2 * RIGHT + 2.3 * UP), tree.animate.move_to(1.7 * RIGHT + 0.3 * DOWN))


        # highlight3 = AnimationGroup(tree["c4"].animate.set_fill(GRADIENT), tree["c5"].animate.set_fill(GRADIENT), tree["c6"].animate.set_fill(GRADIENT))
        # self.play(highlight3)
        # dehighlight3 = AnimationGroup(tree["c4"].animate.set_fill(BLACK), tree["c5"].animate.set_fill(BLACK), tree["c6"].animate.set_fill(BLACK))
        # self.play(dehighlight3)
        # highlight4 = AnimationGroup(tree["c3"].animate.set_fill(GRADIENT), tree["c4"].animate.set_fill(GRADIENT))
        # self.play(highlight4)
        # dehighlight4 = AnimationGroup(tree["c3"].animate.set_fill(BLACK), tree["c4"].animate.set_fill(BLACK))
        # self.play(dehighlight4)

        # self.play(Uncreate(tree), Uncreate(max_heap), Unwrite(value_text), Unwrite(complete_tree_text), Uncreate(new_arrow), Uncreate(arrow), Unwrite(tree_text), Uncreate(binary_tree))


        ## Array representation ##
        
        array_text = Text("Array representation", gradient=(GREEN, BLUE), font=FONT, font_size=TEXT_SIZE).shift(1.5 * LEFT).next_to(title_group, DOWN, buff=0.3).align_to(title_group, LEFT)
        self.play(Write(array_text))

        self.play(Create(tree.shift(2 * RIGHT + 1.2 * UP)))
        array_table = Table([["0", "1", "2", "3", "4", "5"], ["9", "8", "6", "7", "4", "5"]], 
            row_labels=[Text("i"), Text("A[i]")], 
            include_outer_lines=False,
            line_config={"stroke_width": 1}
            ).scale(0.5).shift(2 * RIGHT + 2 * DOWN)
        self.play(array_table.create())

        condition_text = Text("Given any index i,", gradient=(TEAL, GOLD, PINK), font=FONT, font_size=LG_TEXT_SIZE).shift(1.5 * LEFT).next_to(array_text, DOWN, buff=0.8).align_to(title_group, LEFT)
        rule1 = Text("what is the index", gradient=(TEAL, GOLD, PINK), font=FONT, font_size=LG_TEXT_SIZE).shift(1.5 * LEFT).next_to(condition_text, DOWN, buff=0.3).align_to(title_group, LEFT)
        rule1_2 = Text("of A[i]'s parent?", gradient=(TEAL, GOLD, PINK), font=FONT, font_size=LG_TEXT_SIZE).shift(1.5 * LEFT).next_to(rule1, DOWN, buff=0.3).align_to(rule1, LEFT)
        self.play(Write(condition_text))
        self.play(Write(rule1))
        self.play(Write(rule1_2))
        rec = Rectangle(width=0.7, height=1.3, color=PINK)
        self.play(Create(rec.shift(2.98 * RIGHT + 2 * DOWN)), tree["c4"].animate.set_fill(PINK))
        rec2 = Rectangle(width=0.7, height=1.3, color=GREEN_E)
        self.play(Create(rec2.shift(1.4 * RIGHT + 2 * DOWN)), tree["c2"].animate.set_fill(GREEN_E))

        parent = Tex(r"$\lfloor \frac{(i+1)}{2} \rfloor$", color=GREEN_E, font_size=LG_TEXT_SIZE+30).next_to(rule1_2, DOWN, buff=0.8).align_to(rule1, LEFT)
        parent.set_color_by_tex(" ", PINK_GRADIENT)
        self.play(Write(parent))

        dehighlight = AnimationGroup(tree["c4"].animate.set_fill(BLACK), tree["c2"].animate.set_fill(BLACK))
        self.play(Unwrite(condition_text), Unwrite(rule1), Unwrite(rule1_2), Uncreate(rec), Uncreate(rec2), dehighlight)

        tree_and_table = VGroup(tree, array_table)
        self.play(tree_and_table.animate.scale(0.8).next_to(array_text, DOWN, buff=0.5).align_to(array_text, LEFT), parent.animate.scale(0.8).move_to(1.8 * UP + 5 * RIGHT))
        
        parent_table = Table(
            [["aaaaaa", "aaaaaa"], ["         ", "         "],["         ", "         "],["         ", "         "]],
            row_labels=[Text("A[1]"), Text("A[2]"), Text("A[3]"), Text("A[4]")],
            col_labels=[Text("Parent's i"), Text(" ")],
            line_config={"stroke_width": 1, "color": TEAL},
            include_outer_lines=False
            ).scale(0.7).next_to(tree_and_table, RIGHT, buff=0.8).shift(0.3 * RIGHT + 0.2 * UP)
        # print("vertical", parent_table.get_vertical_lines())
        # parent_table.remove(*parent_table.get_vertical_lines())
        parent_table.get_entries((2, 2)).set_color(BLACK)   # Ad-hoc way to create an empty table
        parent_table.get_entries((2, 3)).set_color(BLACK)   # same
        self.play(parent_table.create())