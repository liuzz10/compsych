from typing import Text
from manim import *
from style import *
from manim_fonts import *


RADIUS = 0.4
SM_RADIUS = 0.35
WIDTH = 4
TEXT_SIZE = 30  # Normal small text on screen
LG_TEXT_SIZE = 40   # For large text/questions on screen next to a graph
LINE_SPACING = 0.3  # For large text/questions on screen next to a graph
VALUE_SIZE = 25     # For a value in node
STROKE_WIDTH = 5    # For a node
SM_STROKE_WIDTH = 3     # For surrounding table
TABLE_STROKE_WIDTH = 4      # For table
TITLE_SIZE = 70     # For h1 title
TITLE_SHRINK_SIZE = 20      # For title shrinked to the left corner
SECONDARY_TITLE_SIZE = 60       # For h2 title
CHECKMARK_TABLE_BUFF = 0.4

# KARLA_PATH = "/Users/joyliu/Desktop/Joy/Github/compsych/heap/font/Karla/Karla-Bold.ttf"
FONT = "Karla"

# Zindex: line 0, circle 1, description text 2

class Heap(Scene):
    def create_tree(self, array):
        c1 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.2 * UP).set_z_index(1)
        t1 = Text(array[0], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c1.get_center()).set_z_index(2)
        ct1 = VDict([("c", c1), ("t", t1)])
        c2 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.1 * LEFT + 0.2 * DOWN).set_z_index(1)
        t2 = Text(array[1], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c2.get_center()).set_z_index(2)
        ct2 = VDict([("c", c2), ("t", t2)])
        c3 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.1 * RIGHT + 0.2 * DOWN).set_z_index(1)
        t3 = Text(array[2], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c3.get_center()).set_z_index(2)
        ct3 = VDict([("c", c3), ("t", t3)])
        c4 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.7 * LEFT + 1.6 * DOWN).set_z_index(1)
        t4 = Text(array[3], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c4.get_center()).set_z_index(2)
        ct4 = VDict([("c", c4), ("t", t4)])
        c5 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(0.5 * LEFT + 1.6 * DOWN).set_z_index(1)
        t5 = Text(array[4], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c5.get_center()).set_z_index(2)
        ct5 = VDict([("c", c5), ("t", t5)])
        c6 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(0.5 * RIGHT + 1.6 * DOWN).set_z_index(1)
        t6 = Text(array[5], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c6.get_center()).set_z_index(2)
        ct6 = VDict([("c", c6), ("t", t6)])
        l12 = Line(c1.get_center(), c2.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
        l13 = Line(c1.get_center(), c3.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
        l24= Line(c2.get_center(), c4.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
        l25 = Line(c2.get_center(), c5.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
        l36= Line(c3.get_center(), c6.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
        tree = VDict([("c1", ct1), ("l12", l12), ("c2", ct2), ("l13", l13), ("c3", ct3), ("l24", l24), ("c4", ct4), ("l25", l25), ("c5", ct5), ("l36", l36), ("c6", ct6)])
        return tree

    # def create_text(self, text, size):
    #     return Text(text, color=GRAY, weight="BOLD", font=FONT, font_size=size)

    def add_index(self, tree):
        animation = []
        for i, c in enumerate(["c1", "c2", "c3", "c4", "c5", "c6"]):
            node = tree[c]
            t = Text(str(i), color=BLUE1, weight="BOLD", font=FONT, font_size=VALUE_SIZE).next_to(node.get_center(), UP, buff=0.5).set_z_index(3)
            tree["i"+str(i)] = t
            animation.append(Write(t))
        return animation

    def show_title(self, text, up_mobject=None, title_scale=0.25):
        t, animation1, animation2 = None, None, None
        if not up_mobject:
            # The Title
            t = Paragraph(*text, color=GRAY, font=FONT, weight="BOLD", font_size=TITLE_SIZE)
            animation1 = Write(t)
            animation2 = t.animate.scale(title_scale).set_color(GRAY_OUT).to_edge(UL, buff=0.8).shift(0.2 * UP)
        else:
            # The secondary title
            t = Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=SECONDARY_TITLE_SIZE)
            animation1 = Write(t)
            animation2 = t.animate.scale(0.5).next_to(up_mobject, DOWN, buff=0.2).align_to(up_mobject, LEFT)
        return t, animation1, animation2
    
    def show_title_end(self, title_group, scale_value=1.5):
        new_title_group = title_group.copy().move_to(ORIGIN).scale(scale_value).set_color(GRAY)
        box = SurroundingRectangle(new_title_group, color=PINK2, buff=0.5, stroke_width=SM_STROKE_WIDTH)
        return new_title_group, box

    def highlight_node(self, mobject, secondary=False):
        if not secondary:
            return AnimationGroup(mobject["c"].animate.set_fill(PINK1).set_stroke(PINK1), mobject["t"].animate.set_color(BACKGROUND))
        else:
            return AnimationGroup(mobject["c"].animate.set_fill(PINK3).set_stroke(PINK3), mobject["t"].animate.set_color(BACKGROUND))

    def dehighlight_node(self, mobject):
        return AnimationGroup(mobject["c"].animate.set_fill(BACKGROUND).set_stroke(GRAY), mobject["t"].animate.set_color(GRAY))

    def exercise_title(self, size=TITLE_SHRINK_SIZE):
        t = Text("自测&交流", color=GRAY_OUT, font=FONT, weight="BOLD", font_size=size).to_edge(UL, buff=0.8).shift(0.2 * UP)
        return FadeIn(t)

    def exercise_question(self, text):
        t = Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=TEXT_SIZE)
        b = SurroundingRectangle(t, color=BLUE1, buff=0.2, stroke_width=SM_STROKE_WIDTH)
        return VGroup(t, b)

    def exercise_text(self, text):
        return Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=TEXT_SIZE)

        
    def construct(self):
        self.camera.background_color = BACKGROUND
        with RegisterFont(FONT) as fonts:
            watermark = Text("Compsyc", color=LIGHT_PINK, weight="BOLD", font=FONT, font_size=160).set_fill(opacity=0.03)
            self.add(watermark)
            text1 = Text("什么是", color=GRAY, font=FONT, weight="BOLD", font_size=80).shift(1 * LEFT)
            text2 = Text("堆？", color=GRAY, font=FONT, weight="BOLD", font_size=80).shift(1.54 * RIGHT)
            title_group = VGroup(text1, text2)
            self.play(Write(title_group))
            self.play(text1.animate.shift(0.9 * LEFT), text2.animate.shift(1.1 * RIGHT))
            
            binary = Text("(二叉)", color=PINK1, font=FONT, font_size=40).shift(0.8 * RIGHT)
            self.play(Write(binary))
            self.wait(1)
            self.play(Unwrite(binary))
            self.play(text1.animate.shift(0.9 * RIGHT), text2.animate.shift(1.1 * LEFT))
            self.wait(1)
            self.play(title_group.animate.scale(0.25).set_color(GRAY_OUT).to_edge(UL, buff=0.8).shift(0.2*UP))
            self.wait(1)

    ##########################
    ## 3 properties ##
    ##########################
        ## 1. Binary tree ##
            tree_text, title_animation1, title_animation2 = self.show_title("1. 二叉树", title_group)
            self.play(title_animation1)
            self.wait()
            self.play(title_animation2)
            self.wait()

            circle = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(2.5 * LEFT + 1 * UP).set_z_index(1)
            circle_left = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(3.7 * LEFT + 1 * DOWN).set_z_index(1)
            circle_right = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.3 * LEFT + 1 * DOWN).set_z_index(1)
            line_left = Line(circle.get_center(), circle_left.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
            line_right = Line(circle.get_center(), circle_right.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
            binary_tree = VGroup(circle, line_left, line_right, circle_left, circle_right)
            self.play(AnimationGroup(FadeIn(binary_tree)))

            circle2 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(2.5 * RIGHT + 1 * UP).set_z_index(1)
            circle2_left = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.3 * RIGHT + 1 * DOWN).set_z_index(1)
            circle2_mid = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(2.5 * RIGHT + 1 * DOWN).set_z_index(1)
            circle2_right = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(3.7 * RIGHT + 1 * DOWN).set_z_index(1)
            line2_left = Line(circle2.get_center(), circle2_left.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
            line2_mid = Line(circle2.get_center(), circle2_mid.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
            line2_right = Line(circle2.get_center(), circle2_right.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
            thirary_tree = VGroup(circle2, line2_left, line2_mid, line2_right, circle2_left, circle2_mid, circle2_right)
            self.play(AnimationGroup(FadeIn(thirary_tree)))
            self.play(binary_tree.animate.set_stroke(CORRECT_COLOR))
            self.play(thirary_tree.animate.set_stroke(MISTAKE_COLOR))
            self.wait()
            self.play(Unwrite(thirary_tree))
            self.play(binary_tree.animate.scale(0.1).next_to(tree_text, RIGHT).set_stroke(GRAY, width=1))
            self.play(binary_tree.animate.set_stroke(GRAY_OUT), tree_text.animate.set_color(GRAY_OUT))

        ## 2. Complete tree ##
            complete_tree_text, title_animation1, title_animation2 = self.show_title("2. 完全树", tree_text)
            self.play(title_animation1)
            self.wait()
            self.play(title_animation2)
            self.wait()

            arrow = Arrow(2.6*LEFT, 2.6*RIGHT, color=GRAY, max_stroke_width_to_length_ratio=0.8).shift(2.3 * DOWN)
            self.play(Write(arrow))

            complete_tree = self.create_tree(["","","","","",""]).shift(0.5*UP)
            c = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=CORRECT_COLOR).set_fill(BACKGROUND, opacity=1.0).shift(1.7 * RIGHT + 1.6 * DOWN).set_z_index(1).shift(0.5*UP)
            l37 = Line(complete_tree["c3"].get_center(), c.get_center()).set_stroke(color=CORRECT_COLOR, width=STROKE_WIDTH).set_z_index(0)
            complete_tree["c7"] = c
            complete_tree["l37"] = l37
            for e in ["c1", "l12", "c2", "l13", "c3", "l24", "c4", "l25", "c5", "l36", "c6","l37","c7"]:
                complete_tree[e].set_stroke(CORRECT_COLOR)
                self.play(Create(complete_tree[e]))
            self.play(AnimationGroup(complete_tree.animate.set_stroke(MISTAKE_COLOR), FadeOut(complete_tree["c5"], complete_tree["l25"])))
            temp_c5 = complete_tree["c5"]
            temp_l25 = complete_tree["l25"]
            complete_tree.remove("c5")
            complete_tree.remove("l25")
            self.wait(1)
            self.play(FadeOut(complete_tree["c2"], complete_tree["l12"], complete_tree["c4"], complete_tree["l24"]))
            complete_tree["c5"] = temp_c5.set_stroke(MISTAKE_COLOR)
            complete_tree["l25"] = temp_l25.set_stroke(MISTAKE_COLOR)
            self.wait(1)
            self.play(FadeIn(complete_tree["c5"], complete_tree["l25"], complete_tree["c2"], complete_tree["l12"], complete_tree["c4"], complete_tree["l24"]),
            FadeOut(complete_tree["c3"], complete_tree["l13"], complete_tree["l36"], complete_tree["c6"], complete_tree["l37"], complete_tree["c7"]))
            self.wait()
            self.play(FadeOut(complete_tree["c1"], complete_tree["c5"], complete_tree["l25"], complete_tree["c2"], complete_tree["l12"], complete_tree["c4"], complete_tree["l24"]))

            tri = Triangle().set_stroke(color=GRAY, width=STROKE_WIDTH).scale(2.6).shift(0.3 * UP)
            c2 = Cross(stroke_width=6, color=MISTAKE_COLOR, scale_factor=0.3).shift(0.5 * RIGHT + 0.9 * DOWN)
            c3 = Cross(stroke_width=6, color=MISTAKE_COLOR, scale_factor=0.3).shift(1.3 * RIGHT + 0.9 * DOWN)
            self.wait()
            self.play(FadeIn(tri, c2, c3))
            new_arrow = Arrow(0.4*LEFT, 0.4*RIGHT, color=GRAY, max_tip_length_to_length_ratio=0.4, max_stroke_width_to_length_ratio=6).next_to(complete_tree_text, RIGHT)
            self.wait()
            self.play(FadeOut(tri, c2, c3), ReplacementTransform(arrow, new_arrow))
            self.play(complete_tree_text.animate.set_color(GRAY_OUT), new_arrow.animate.set_fill(GRAY_OUT).set_stroke(GRAY_OUT))

    ## 3. Value ##
            value_text, title_animation1, title_animation2 = self.show_title("3. 值", complete_tree_text)
            self.play(title_animation1)
            self.wait()
            self.play(title_animation2)
            self.wait()

            max_heap = Text("最大堆", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(1 * LEFT + 2.3 * UP)
            self.play(Write(max_heap), run_time=2)
            tree = self.create_tree(["9","8","6","7","4","5"]).shift(1 * LEFT + 0 * UP)
            self.play(Create(tree))
            self.wait(1)
            min_heap = Text("最小堆", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(3.5 * RIGHT + 2.3 * UP)
            self.play(Write(min_heap), run_time=2)
            tree2 = self.create_tree(["1","2","4","3","6","5"]).shift(3.5 * RIGHT + 0 * UP)
            self.play(Create(tree2))
            self.wait(1)

            highlight1 = AnimationGroup(self.highlight_node(tree["c1"]), self.highlight_node(tree["c2"], True), self.highlight_node(tree["c3"], True))
            self.play(highlight1)
            dehighlight1 = AnimationGroup(self.dehighlight_node(tree["c1"]), self.dehighlight_node(tree["c2"]), self.dehighlight_node(tree["c3"]))
            self.play(dehighlight1)
            highlight1 = AnimationGroup(self.highlight_node(tree["c2"]), self.highlight_node(tree["c4"], True), self.highlight_node(tree["c5"], True))
            self.play(highlight1)
            dehighlight1 = AnimationGroup(self.dehighlight_node(tree["c2"]), self.dehighlight_node(tree["c4"]), self.dehighlight_node(tree["c5"]))
            self.play(dehighlight1)
            highlight1 = AnimationGroup(self.highlight_node(tree["c3"]), self.highlight_node(tree["c6"], True))
            self.play(highlight1)
            dehighlight1 = AnimationGroup(self.dehighlight_node(tree["c3"]), self.dehighlight_node(tree["c6"]))
            self.play(dehighlight1)
            self.wait(2)

            highlight2 = AnimationGroup(self.highlight_node(tree2["c1"]), self.highlight_node(tree2["c2"], True), self.highlight_node(tree2["c3"], True))
            self.play(highlight2)
            dehighlight2 = AnimationGroup(self.dehighlight_node(tree2["c1"]), self.dehighlight_node(tree2["c2"]), self.dehighlight_node(tree2["c3"]))
            self.play(dehighlight2)
            highlight2 = AnimationGroup(self.highlight_node(tree2["c2"]), self.highlight_node(tree2["c4"], True), self.highlight_node(tree2["c5"], True))
            self.play(highlight2)
            dehighlight2 = AnimationGroup(self.dehighlight_node(tree2["c2"]), self.dehighlight_node(tree2["c4"]), self.dehighlight_node(tree2["c5"]))
            self.play(dehighlight2)
            highlight2 = AnimationGroup(self.highlight_node(tree2["c3"]), self.highlight_node(tree2["c6"], True))
            self.play(highlight2)
            dehighlight2 = AnimationGroup(self.dehighlight_node(tree2["c3"]), self.dehighlight_node(tree2["c6"]))
            self.play(dehighlight2)

            self.wait()
            self.play(Uncreate(tree2), Unwrite(min_heap))
            self.play(max_heap.animate.move_to(1 * RIGHT + 2.3 * UP), tree.animate.move_to(0.7 * RIGHT + 0.3 * DOWN))

            self.wait()
            highlight3 = AnimationGroup(self.highlight_node(tree["c4"]), self.highlight_node(tree["c5"]), self.highlight_node(tree["c6"]))
            self.play(highlight3)
            self.wait()
            dehighlight3 = AnimationGroup(self.dehighlight_node(tree["c4"]), self.dehighlight_node(tree["c5"]), self.dehighlight_node(tree["c6"]))
            self.play(dehighlight3)
            self.wait()
            highlight4 = AnimationGroup(self.highlight_node(tree["c3"]), self.highlight_node(tree["c4"]))
            self.play(highlight4)
            self.wait()
            dehighlight4 = AnimationGroup(self.dehighlight_node(tree["c3"]), self.dehighlight_node(tree["c4"]))
            self.play(dehighlight4)
            self.wait()

            arrow_l = tree["l12"].copy().add_tip().set_color(PINK1).set_stroke(width=STROKE_WIDTH+1).set_z_index(3)
            arrow_r = tree["l13"].copy().add_tip().set_color(PINK1).set_stroke(width=STROKE_WIDTH+1).set_z_index(3)
            double_arrow = VGroup(arrow_l, arrow_r)
            self.play(Create(arrow_l))
            self.play(Create(arrow_r))
            arrow2_l = tree["l24"].copy().add_tip().set_color(PINK1).set_stroke(width=STROKE_WIDTH+1).set_z_index(3)
            arrow2_r = tree["l25"].copy().add_tip().set_color(PINK1).set_stroke(width=STROKE_WIDTH+1).set_z_index(3)
            self.play(Create(arrow2_l))
            self.play(Create(arrow2_r))
            arrow3_l = tree["l36"].copy().add_tip().set_color(PINK1).set_stroke(width=STROKE_WIDTH+1).set_z_index(3)
            self.play(Create(arrow3_l))
            temp_group = VGroup(arrow2_l, arrow2_r, arrow3_l)
            self.play(FadeOut(tree, max_heap))
            self.play(ReplacementTransform(temp_group, double_arrow))
            self.play(double_arrow.animate.scale(0.15).set_stroke(width=1).set_color(GRAY).next_to(value_text, RIGHT))

        ## End ##
            temp_group = VGroup(title_group, tree_text, complete_tree_text, value_text, new_arrow, double_arrow, binary_tree)
            new_title_group, box = self.show_title_end(temp_group)
            self.play(ReplacementTransform(temp_group, new_title_group))
            self.play(Create(box))
            self.wait(2)
            self.play(Uncreate(new_title_group), Uncreate(box))

            self.wait(2)

    ########################
    ## Array representation ##
    ########################
        # Opening ##
            array_text, title_animation1, title_animation2 = self.show_title(["堆的实现：数组"], title_scale=0.3)
            self.play(title_animation1)
            self.wait()
            self.play(title_animation2)
            self.play(Create(tree.move_to(0.2 * UP)), run_time=2)
            self.wait()
            array_table0 = Table([["9", "8", "6", "7", "4", "5"]], 
                row_labels=[Text("A[i]", font=FONT, weight="BOLD")], 
                include_outer_lines=True,
                element_to_mobject_config={"font": FONT},
                line_config={"stroke_width": TABLE_STROKE_WIDTH}
                ).scale(0.4).shift(0.2 * RIGHT + 2.4 * DOWN)
            self.play(array_table0.create(), run_time=2)
            self.wait()
            animation = self.add_index(tree)
            self.play(*animation)
            self.wait()

        # ## Parent ##
            condition_text = Text("已知数组A和索引i,", color=GRAY, font=FONT, weight="BOLD", font_size=LG_TEXT_SIZE).shift(2 * RIGHT + 1 * UP)
            rule1 = Text("A[i]的父节点是？", color=PINK1, font=FONT, weight="BOLD", font_size=LG_TEXT_SIZE).shift(1.5 * LEFT).next_to(condition_text, DOWN, buff=LINE_SPACING)
            tree_and_array = VGroup(tree, array_table0)
            self.play(tree_and_array.animate.shift(3.2 * LEFT))
            self.wait()
            self.play(Write(condition_text))
            self.play(Write(rule1))
            self.wait()
            temp_group = VGroup(condition_text, rule1)
            # self.play(temp_group.animate.shift(0.5 * UP))
            parent = Tex(r"$\lfloor \frac{(i-1)}{2} \rfloor$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=LG_TEXT_SIZE+30).next_to(rule1, DOWN, buff=0.6)
            parent_a = Tex(r"$A[\lfloor \frac{(i-1)}{2} \rfloor]$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=LG_TEXT_SIZE+30).next_to(rule1, DOWN, buff=0.6)
            self.play(Write(parent_a))
            self.wait()
            # array
            self.play(FadeOut(tree, temp_group, parent_a))
            self.play(array_table0.animate.scale(2).move_to(ORIGIN))
            array_table = Table([["9", "8", "6", "7", "4", "5"]], 
                row_labels=[Text("A[i]", font=FONT, weight="BOLD")], 
                include_outer_lines=True,
                element_to_mobject_config={"font": FONT},
                line_config={"stroke_width": TABLE_STROKE_WIDTH}
                ).scale(0.4).scale(2)
            i_text = Tex(r"$i$", color=BLUE1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+30).shift(1.04 * LEFT + 1 * UP)
            arrow_parent = CurvedArrow([1, 1, 0], [-0.3, 1, 0], color=GRAY, stroke_width=4).flip(RIGHT).shift(2 * LEFT + 1.95 * DOWN)
            array_table.add_highlighted_cell((1,3), color=BLUE1)
            parent.scale(0.9).move_to(2.34 * LEFT + 1.2 * UP)  
            self.play(Write(i_text), array_table.animate.get_highlighted_cell((1,3)))
            self.wait()
            self.play(Create(arrow_parent))
            array_table.add_highlighted_cell((1,2), color=TABLE_PINK_FILL)
            self.play(FadeIn(parent), array_table.animate.get_highlighted_cell((1,2)))
            self.wait()
            self.play(FadeOut(array_table, array_table0, i_text, arrow_parent))
            self.play(parent.animate.scale(1.1).move_to(4.3 * RIGHT + 2.2 * UP), FadeIn(tree.move_to(3.8 * LEFT)))

            parent_table = Table(
                [["0", "floor()))"], ["0", ""],["1", ""],["1", ""], ["2", ""]],
                row_labels=[Text("1", font=FONT), Text("2", font=FONT), Text("3", font=FONT), Text("4", font=FONT), Text("5", font=FONT)],
                col_labels=[Text(" 父亲的索引", font=FONT), Text(" ", font=FONT)],
                line_config={"stroke_width": TABLE_STROKE_WIDTH, "color": GRAY, "stroke_opacity": 0.2},
                element_to_mobject_config={"font": FONT},
                include_outer_lines=False,
                top_left_entry=Text("i", font=FONT)
                ).scale(0.7).next_to(tree, RIGHT, buff=0.8).shift(0.2 * DOWN)
            for entry in parent_table.get_entries_without_labels():
                entry.set_color(BACKGROUND)   # Ad-hoc way to create an empty table
            self.play(parent_table.create())
            self.wait()
            self.play(self.highlight_node(tree["c2"], True))
            self.play(self.highlight_node(tree["c1"]))
            self.wait()

            self.play(parent_table.get_entries((2, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            c1 = Tex(r"$\lfloor \frac{0}{2} \rfloor = 0$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 0.4)
            self.wait()
            self.play(Write(c1))
            self.play(FadeIn(tree))
            ch1 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c1, buff=CHECKMARK_TABLE_BUFF)
            self.play(FadeIn(ch1))
            self.wait()

            self.play(self.dehighlight_node(tree["c2"]), self.highlight_node(tree["c3"], True))
            self.play(parent_table.get_entries((3, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c2 = Tex(r"$\lfloor \frac{1}{2} \rfloor = 0$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 1.3).align_to(c1, LEFT)
            self.play(Write(c2))
            self.play(FadeIn(tree))
            ch2 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c2).align_to(ch1, LEFT)
            self.play(FadeIn(ch2))
            self.wait()

            self.play(self.dehighlight_node(tree["c3"]), self.dehighlight_node(tree["c1"]))
            self.play(self.highlight_node(tree["c4"], True))
            self.play(self.highlight_node(tree["c2"]))
            self.play(parent_table.get_entries((4, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c3 = Tex(r"$\lfloor \frac{2}{2} \rfloor = 1$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 2.2).align_to(c1, LEFT)
            self.play(Write(c3))
            self.play(FadeIn(tree))
            ch3 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c3).align_to(ch1, LEFT)
            self.play(FadeIn(ch3))
            self.wait()
        
            self.play(self.dehighlight_node(tree["c4"]), self.highlight_node(tree["c5"], True))
            self.play(parent_table.get_entries((5, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c4 = Tex(r"$\lfloor \frac{3}{2} \rfloor = 1$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 3.1).align_to(c1, LEFT)
            self.play(Write(c4))
            self.play(FadeIn(tree))
            ch4 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c4).align_to(ch1, LEFT)
            self.play(FadeIn(ch4))
            self.wait()

            self.play(self.dehighlight_node(tree["c5"]), self.dehighlight_node(tree["c2"]))
            self.play(self.highlight_node(tree["c6"], True))
            self.play(self.highlight_node(tree["c3"]))
            self.play(parent_table.get_entries((6, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c5 = Tex(r"$\lfloor \frac{4}{2} \rfloor = 2$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 4).align_to(c1, LEFT)
            self.play(Write(c5))
            self.play(FadeIn(tree))
            ch5 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c5).align_to(ch1, LEFT)
            self.play(FadeIn(ch5))
            self.wait()
            self.play(self.dehighlight_node(tree["c6"]), self.dehighlight_node(tree["c3"]))
            self.wait()
            self.play(FadeOut(parent_table, c1, c2, c3, c4, c5, parent, ch1, ch2, ch3, ch4, ch5))

        ## Left child ##
            self.play(Write(condition_text.move_to(2 * RIGHT + 1 * UP)))
            rule2 = Text("A[i]的左孩子是？", color=PINK1, weight="BOLD", font=FONT, font_size=LG_TEXT_SIZE).shift(1.5 * LEFT).next_to(condition_text, DOWN, buff=LINE_SPACING)
            self.play(Write(rule2))
            self.wait()
            temp_group = VGroup(condition_text, rule2)
            # self.play(temp_group.animate.shift(0.5 * UP))
            left_child = Tex(r"$2i+1$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+15).next_to(temp_group, DOWN, buff=0.6)
            left_child_a = Tex(r"$A[2i+1]$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+15).next_to(temp_group, DOWN, buff=0.6)
            self.play(Write(left_child_a))
            self.wait()
            # array
            self.play(FadeOut(tree, temp_group, left_child_a))
            array_table = Table([["9", "8", "6", "7", "4", "5"]], 
                row_labels=[Text("A[i]", font=FONT, weight="BOLD")], 
                include_outer_lines=True,
                element_to_mobject_config={"font": FONT},
                line_config={"stroke_width": TABLE_STROKE_WIDTH}
                ).scale(0.4).scale(2)
            arrow_left = CurvedArrow([1, 1, 0], [-1.6, 1, 0], color=GRAY, stroke_width=4).rotate(180*DEGREES).shift(0.6 * RIGHT +2.2 * DOWN)
            array_table.add_highlighted_cell((1,3), color=BLUE1)
            i_text.move_to(1.05 * LEFT + 1.2 * UP)
            left_child.scale(0.9).move_to(0.97 * LEFT + 1.2 * UP).shift(2.5 * RIGHT)
            self.play(FadeIn(array_table))
            self.play(Write(i_text), array_table.animate.get_highlighted_cell((1,3)))
            self.wait()
            self.play(Create(arrow_left))
            array_table.add_highlighted_cell((1,5), color=TABLE_PINK_FILL)
            self.play(FadeIn(left_child), array_table.animate.get_highlighted_cell((1,5)))
            self.wait()
            self.play(FadeOut(array_table, arrow_left, i_text))
            self.play(FadeIn(tree.move_to(3.8 * LEFT)), left_child.animate.move_to(4.7 * RIGHT + 1.1 * UP))
            self.wait()

            left_child_table = Table(
                [["1", "floor())"], ["3", ""],["5", ""]],
                row_labels=[Text("0", font=FONT, weight="BOLD"), Text("1", font=FONT, weight="BOLD"), Text("2", font=FONT, weight="BOLD")],
                col_labels=[Text(" 左孩子的索引", font=FONT), Text(" ", font=FONT)],
                line_config={"stroke_width": TABLE_STROKE_WIDTH, "color": GRAY, "stroke_opacity": 0.2},
                element_to_mobject_config={"font": FONT},
                include_outer_lines=False,
                top_left_entry=Text("i", font=FONT, weight="BOLD")
                ).scale(0.7).next_to(tree, RIGHT, buff=0.8).shift(0.2 * DOWN)
            for entry in left_child_table.get_entries_without_labels():
                entry.set_color(BACKGROUND)
            self.play(left_child_table.create())
            self.play(self.highlight_node(tree["c1"], True))
            self.play(self.highlight_node(tree["c2"]))
            self.play(left_child_table.get_entries((2, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c1 = Tex(r"$2\times0+1=1$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(left_child, DOWN, buff = 0.65)
            self.play(Write(c1))
            self.play(FadeIn(tree))
            ch1 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c1, buff=CHECKMARK_TABLE_BUFF)
            self.play(FadeIn(ch1))
            self.wait()

            self.play(self.dehighlight_node(tree["c1"]), self.highlight_node(tree["c2"], True))
            self.play(self.highlight_node(tree["c4"]))
            self.play(left_child_table.get_entries((3, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c2 = Tex(r"$2\times1+1=3$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(left_child, DOWN, buff = 1.6).align_to(c1, LEFT)
            self.play(Write(c2))
            self.play(FadeIn(tree))
            ch2 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c2).align_to(ch1, LEFT)
            self.play(FadeIn(ch2))
            self.wait()

            self.play(self.dehighlight_node(tree["c2"]), self.dehighlight_node(tree["c4"]))
            self.play(self.highlight_node(tree["c3"], True))
            self.play(self.highlight_node(tree["c6"]))
            self.play(left_child_table.get_entries((4, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c3 = Tex(r"$2\times2+1=5$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(left_child, DOWN, buff = 2.45).align_to(c1, LEFT)
            self.play(Write(c3))
            self.play(FadeIn(tree))
            ch3 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c3).align_to(ch1, LEFT)
            self.play(FadeIn(ch3))
            self.wait()
            self.play(self.dehighlight_node(tree["c6"]), self.dehighlight_node(tree["c3"]))
            self.wait()
            self.play(FadeOut(left_child_table, c1, c2, c3, left_child, ch1, ch2, ch3))


        ## Right child ##
            self.play(Write(condition_text.move_to(2 * RIGHT + 1 * UP)))
            rule3 = Text("A[i]的右孩子是？", color=PINK1, weight="BOLD", font=FONT, font_size=LG_TEXT_SIZE).next_to(condition_text, DOWN, buff=0.4)
            self.play(Write(rule3))
            self.wait()
            temp_group = VGroup(condition_text, rule3)
            # self.play(temp_group.animate.move_to(2 * RIGHT + 0.5 * UP))
            right_child = Tex(r"$2i+2$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+15).next_to(temp_group, DOWN, buff=0.6)
            right_child_a = Tex(r"$A[2i+2]$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+15).next_to(temp_group, DOWN, buff=0.6)
            self.play(Write(right_child_a))
            self.wait()
            # array
            self.play(FadeOut(tree, temp_group, right_child_a))
            array_table = Table([["9", "8", "6", "7", "4", "5"]], 
                row_labels=[Text("A[i]", font=FONT, weight="BOLD")], 
                include_outer_lines=True,
                element_to_mobject_config={"font": FONT},
                line_config={"stroke_width": TABLE_STROKE_WIDTH}
                ).scale(0.4).scale(2)
            arrow_right = CurvedArrow([1, 1, 0], [-2.8, 1, 0], color=GRAY, stroke_width=4).rotate(180*DEGREES).shift(1.8 * RIGHT +2.43 * DOWN)
            array_table.add_highlighted_cell((1,3), color=BLUE1)
            i_text.move_to(1.05 * LEFT + 1.2 * UP)
            right_child.scale(0.9).move_to(0.97 * LEFT + 1.2 * UP).shift(3.8 * RIGHT)
            self.play(FadeIn(array_table))
            self.play(Write(i_text), array_table.animate.get_highlighted_cell((1,3)))
            self.wait()
            self.play(Create(arrow_right))
            array_table.add_highlighted_cell((1,6), color=TABLE_PINK_FILL)
            self.play(FadeIn(right_child), array_table.animate.get_highlighted_cell((1,6)))
            self.wait()
            self.play(FadeOut(array_table, arrow_right, i_text))
            self.play(FadeIn(tree.move_to(3.8 * LEFT)), right_child.animate.move_to(4.7 * RIGHT + 0.7 * UP))
            self.wait()

            right_child_table = Table(
                [["2", "floor())"], ["4", ""]],
                row_labels=[Text("0", font=FONT, weight="BOLD"), Text("1", font=FONT, weight="BOLD")],
                col_labels=[Text(" 右孩子的索引", font=FONT), Text(" ", font=FONT)],
                line_config={"stroke_width": TABLE_STROKE_WIDTH, "color": GRAY, "stroke_opacity": 0.2},
                element_to_mobject_config={"font": FONT},
                include_outer_lines=False,
                top_left_entry=Text("i", font=FONT, weight="BOLD")
                ).scale(0.7).next_to(tree, RIGHT, buff=0.8).shift(0.2 * DOWN)
            for entry in right_child_table.get_entries_without_labels():
                entry.set_color(BACKGROUND)   # Ad-hoc way to create an empty table
            self.play(right_child_table.create())
            self.wait()
            self.play(self.highlight_node(tree["c1"], True))
            self.play(self.highlight_node(tree["c3"]))
            self.play(right_child_table.get_entries((2, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c1 = Tex(r"$2\times0+2=2$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(right_child, DOWN, buff = 0.65)
            self.play(Write(c1))
            self.play(FadeIn(tree))   
            ch1 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c1, buff=CHECKMARK_TABLE_BUFF)
            self.play(FadeIn(ch1))
            self.wait()

            self.play(self.dehighlight_node(tree["c1"]), self.dehighlight_node(tree["c3"]))
            self.play(self.highlight_node(tree["c2"], True), self.highlight_node(tree["c5"]))
            self.play(right_child_table.get_entries((3, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            self.wait()
            c2 = Tex(r"$2\times1+2=4$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(right_child, DOWN, buff = 1.58).align_to(c1, LEFT)
            self.play(Write(c2))
            self.play(FadeIn(tree))
            ch2 = SVGMobject("check.svg").set_fill(CORRECT_COLOR).scale(0.2).next_to(c2).align_to(ch1, LEFT)
            self.play(FadeIn(ch2))
            self.wait()

            self.play(FadeOut(tree, right_child_table, c1, c2, right_child, ch1, ch2))

            array_table = Table([["9", "8", "6", "7", "4", "5"]], 
                row_labels=[Text("A[i]", font=FONT, weight="BOLD")], 
                include_outer_lines=True,
                element_to_mobject_config={"font": FONT},
                line_config={"stroke_width": TABLE_STROKE_WIDTH}
                ).scale(0.4).scale(2)
            self.play(Create(array_table))
            i_text.move_to(1.05 * LEFT + 1.2 * UP)
            parent.scale(0.9).move_to(1.1 * LEFT + 1.2* UP).shift(1.26 * LEFT)
            left_child.scale(0.9).move_to(0.97 * LEFT + 1.2 * UP).shift(2.5 * RIGHT)
            right_child.scale(0.9).move_to(0.97 * LEFT + 1.2 * UP).shift(3.8 * RIGHT)
            arrow_parent = CurvedArrow([1, 1, 0], [-0.3, 1, 0], color=GRAY, stroke_width=4).flip(RIGHT).shift(2 * LEFT + 1.95 * DOWN)
            arrow_left = CurvedArrow([1, 1, 0], [-1.6, 1, 0], color=GRAY, stroke_width=4).rotate(180*DEGREES).shift(0.6 * RIGHT +2.2 * DOWN)
            arrow_right = CurvedArrow([1, 1, 0], [-2.8, 1, 0], color=GRAY, stroke_width=4).rotate(180*DEGREES).shift(1.8 * RIGHT +2.43 * DOWN)
        
        ## Array ##
            array_table.add_highlighted_cell((1,3), color=BLUE1)
            self.play(Write(i_text), array_table.animate.get_highlighted_cell((1,3)))
            self.wait()
            
            self.play(Create(arrow_parent))
            array_table.add_highlighted_cell((1,2), color=TABLE_PINK_FILL)
            self.play(Write(parent), array_table.animate.get_highlighted_cell((1,2)))
            self.wait()

            self.play(Create(arrow_left))
            array_table.add_highlighted_cell((1,5), color=TABLE_PINK_FILL)
            self.play(Write(left_child), array_table.animate.get_highlighted_cell((1,5)))
            self.wait()

            self.play(Create(arrow_right))
            array_table.add_highlighted_cell((1,6), color=TABLE_PINK_FILL)
            self.play(Write(right_child), array_table.animate.get_highlighted_cell((1,6)))
            self.wait()

            self.play(FadeOut(array_table, i_text, parent, left_child, right_child, arrow_parent, arrow_left, arrow_right))

        ## End ##
            new_title_group, box = self.show_title_end(array_text, scale_value=3)
            self.play(ReplacementTransform(array_text, new_title_group))
            self.play(Create(box))
            self.wait()
            self.play(Uncreate(new_title_group), Uncreate(box))

            self.wait(2)

    #########################
    # Exercise ##
    #########################
            self.play(self.exercise_title())
        ## 1 ##
            q1 = self.exercise_question("下面哪个是最大堆？").to_edge(UP, 1.5)
            a = self.exercise_text("A")
            tree3 = self.create_tree(["5","4","2","1","x","0"]).scale(0.9).next_to(a, UP, buff=0.5)
            tree3["c5"]["c"].set_stroke(BACKGROUND)
            tree3["c5"]["t"].set_color(BACKGROUND)
            tree3["l25"].set_color(BACKGROUND)
            a_group = VGroup(a, tree3).move_to(ORIGIN).shift(4 * LEFT + 0.7 * DOWN)

            b = self.exercise_text("B")
            tree4 = self.create_tree(["3","2","2","2","-1","1"]).scale(0.9).next_to(b, UP, buff=0.5)
            b_group = VGroup(b, tree4).move_to(ORIGIN).shift(0.7 * DOWN)

            c = self.exercise_text("C")
            tree5 = self.create_tree(["6","4","3","1","5","2"]).scale(0.9).next_to(c, UP, buff=0.5)
            c_group = VGroup(c, tree5).move_to(ORIGIN).shift(4 * RIGHT + 0.7 * DOWN)

            self.play(FadeIn(q1, a_group, b_group, c_group))
            self.wait(2)
            self.play(FadeOut(q1, a_group, b_group, c_group))
            
        ## 2 ##
            q2 = self.exercise_question("已知数组A[0,...,n]，A[8]的父节点是？").to_edge(UP, buff=1.5)
            a2 = self.exercise_text("A. 1      B. 2      C. 3      D. 4").next_to(q2, DOWN, buff=0.4)
            q3 = self.exercise_question("A[8]的左孩子的 i 是？").next_to(a2, DOWN, buff=0.4)
            a3 = self.exercise_text("A. 16      B. 17      C. 18      D. 19").next_to(q3, DOWN, buff=0.4)
            q4 = self.exercise_question("A[8]的右孩子的 i 是？").next_to(a3, DOWN, buff=0.4)
            a4 = self.exercise_text("A. 16      B. 17      C. 18      D. 19").next_to(q4, DOWN, buff=0.4)
            self.play(FadeIn(q2, q3, q4, a2, a3, a4))