from typing import Text
from manim import *
from manim.utils.color import color_gradient, Colors, rgb_to_color, hex_to_rgb
from colors import *
from manim_fonts import *


RADIUS = 0.4
SM_RADIUS = 0.35
LINE_COLOR = WHITE
WIDTH = 4
TEXT_SIZE = 30
LG_TEXT_SIZE = 40
VALUE_SIZE = 25
STROKE_WIDTH = 5
TABLE_STROKE_WIDTH = 2
LINE_SPACING = 0.3
TITLE_SIZE = 80

KARLA_PATH = "/Users/joyliu/Desktop/Joy/Github/compsych/heap/font/Karla/Karla-Bold.ttf"
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

    def show_title(self, text, up_mobject):
        t = Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=TITLE_SIZE)
        animation1 = Write(t)
        animation2 = t.animate.scale(0.4).next_to(up_mobject, DOWN, buff=0.2).align_to(up_mobject, LEFT)
        return t, animation1, animation2
    
    def show_title_end(self, title):
        return title.animate.scale(3).move_to(ORIGIN)

    def highlight_node(self, mobject, secondary=False):
        if not secondary:
            return AnimationGroup(mobject["c"].animate.set_fill(PINK1).set_stroke(PINK1), mobject["t"].animate.set_color(BACKGROUND))
        else:
            return AnimationGroup(mobject["c"].animate.set_fill(PINK3).set_stroke(PINK3), mobject["t"].animate.set_color(BACKGROUND))

    def dehighlight_node(self, mobject):
        return AnimationGroup(mobject["c"].animate.set_fill(BACKGROUND).set_stroke(GRAY), mobject["t"].animate.set_color(GRAY))

        
    def construct(self):
        self.camera.background_color = BACKGROUND
        with register_font(KARLA_PATH):
            # watermark0 = Text("Compsych", color=GRAY_, weight="BOLD", font=FONT, font_size=20).to_edge(UR, buff=0.5)
            watermark = Text("Compsych", color=LIGHT_PINK, weight="ULTRAHEAVY", font=FONT, font_size=150).set_fill(opacity=0.03)
            self.add(watermark)
            text1 = Text("WHAT IS ", color=GRAY, font=FONT, weight="BOLD", font_size=80).shift(1.5 * LEFT)
            text2 = Text("HEAP?", color=GRAY, font=FONT, weight="BOLD", font_size=80).shift(2.8 * RIGHT)
            title_group = VGroup(text1, text2)
            self.play(Write(title_group))
            self.play(text1.animate.shift(1.3 * LEFT), text2.animate.shift(1 * RIGHT))
            
            binary = Text("(Binary)", color=PINK1, font=FONT, font_size=40).shift(0.8 * RIGHT)
            self.play(Write(binary))
            self.play(Unwrite(binary))
            self.play(text1.animate.shift(1.3 * RIGHT), text2.animate.shift(1 * LEFT))
            self.play(title_group.animate.scale(0.25).set_color(GRAY_OUT).to_edge(UL, buff=0.8))
        
    ##########################
    ## 3 properties ##
    ##########################
    #     ## 1. Binary tree ##
    #         tree_text, title_animation1, title_animation2 = self.show_title("1. Binary tree", title_group)
    #         self.play(title_animation1)
    #         self.play(title_animation2)

    #         circle = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(2.5 * LEFT + 1 * UP).set_z_index(1)
    #         circle_left = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(3.7 * LEFT + 1 * DOWN).set_z_index(1)
    #         circle_right = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.3 * LEFT + 1 * DOWN).set_z_index(1)
    #         line_left = Line(circle.get_center(), circle_left.get_center()).set_stroke(color=LINE_COLOR, width=STROKE_WIDTH).set_z_index(0)
    #         line_right = Line(circle.get_center(), circle_right.get_center()).set_stroke(color=LINE_COLOR, width=STROKE_WIDTH).set_z_index(0)
    #         binary_tree = VGroup(circle, line_left, line_right, circle_left, circle_right)
    #         self.play(AnimationGroup(FadeIn(binary_tree)))

    #         circle2 = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(2.5 * RIGHT + 1 * UP).set_z_index(1)
    #         circle2_left = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.3 * RIGHT + 1 * DOWN).set_z_index(1)
    #         circle2_mid = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(2.5 * RIGHT + 1 * DOWN).set_z_index(1)
    #         circle2_right = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(3.7 * RIGHT + 1 * DOWN).set_z_index(1)
    #         line2_left = Line(circle2.get_center(), circle2_left.get_center()).set_stroke(color=LINE_COLOR, width=STROKE_WIDTH).set_z_index(0)
    #         line2_mid = Line(circle2.get_center(), circle2_mid.get_center()).set_stroke(color=LINE_COLOR, width=STROKE_WIDTH).set_z_index(0)
    #         line2_right = Line(circle2.get_center(), circle2_right.get_center()).set_stroke(color=LINE_COLOR, width=STROKE_WIDTH).set_z_index(0)
    #         thirary_tree = VGroup(circle2, line2_left, line2_mid, line2_right, circle2_left, circle2_mid, circle2_right)
    #         self.play(AnimationGroup(FadeIn(thirary_tree)))
    #         self.play(binary_tree.animate.set_stroke(CORRECT_COLOR))
    #         self.play(thirary_tree.animate.set_stroke(MISTAKE_COLOR))
    #         self.play(Unwrite(thirary_tree))
    #         self.play(binary_tree.animate.scale(0.1).set_stroke(GRAY, width=1).next_to(tree_text, RIGHT))
    #         self.play(binary_tree.animate.set_stroke(GRAY_OUT), tree_text.animate.set_color(GRAY_OUT))

    #     ## 2. Complete tree ##
    #         complete_tree_text, title_animation1, title_animation2 = self.show_title("2. Complete tree", tree_text)
    #         self.play(title_animation1)
    #         self.play(title_animation2)

    #         arrow = Arrow(2.6*LEFT, 2.6*RIGHT, color=GRAY, max_tip_length_to_length_ratio=0.1, max_stroke_width_to_length_ratio=1).shift(2.3 * DOWN)
    #         self.play(Write(arrow))

    #         complete_tree = self.create_tree(["","","","","",""]).shift(0.5*UP)
    #         c = Circle(radius=SM_RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=CORRECT_COLOR).set_fill(BACKGROUND, opacity=1.0).shift(1.7 * RIGHT + 1.6 * DOWN).set_z_index(1).shift(0.5*UP)
    #         l37 = Line(complete_tree["c3"].get_center(), c.get_center()).set_stroke(color=CORRECT_COLOR, width=STROKE_WIDTH).set_z_index(0)
    #         complete_tree["c7"] = c
    #         complete_tree["l37"] = l37
    #         for e in ["c1", "l12", "c2", "l13", "c3", "l24", "c4", "l25", "c5", "l36", "c6","l37","c7"]:
    #             complete_tree[e].set_stroke(CORRECT_COLOR)
    #             self.play(Create(complete_tree[e]))
    #         self.play(AnimationGroup(complete_tree.animate.set_stroke(MISTAKE_COLOR), FadeOut(complete_tree["c5"], complete_tree["l25"])))
    #         temp_c5 = complete_tree["c5"]
    #         temp_l25 = complete_tree["l25"]
    #         complete_tree.remove("c5")
    #         complete_tree.remove("l25")
    #         self.play(FadeOut(complete_tree["c2"], complete_tree["l12"], complete_tree["c4"], complete_tree["l24"]))
    #         complete_tree["c5"] = temp_c5.set_stroke(MISTAKE_COLOR)
    #         complete_tree["l25"] = temp_l25.set_stroke(MISTAKE_COLOR)
    #         self.play(FadeIn(complete_tree["c5"], complete_tree["l25"], complete_tree["c2"], complete_tree["l12"], complete_tree["c4"], complete_tree["l24"]),
    #         FadeOut(complete_tree["c3"], complete_tree["l13"], complete_tree["l36"], complete_tree["c6"], complete_tree["l37"], complete_tree["c7"]))
    #         self.play(FadeOut(complete_tree["c1"], complete_tree["c5"], complete_tree["l25"], complete_tree["c2"], complete_tree["l12"], complete_tree["c4"], complete_tree["l24"]))

    #         tri = Triangle().set_stroke(color=GRAY, width=6).scale(2.6).shift(0.3 * UP)
    #         c1 = Cross(stroke_width=6, color=MISTAKE_COLOR, scale_factor=0.2).shift(0.3 * RIGHT + 1 * DOWN)
    #         c2 = Cross(stroke_width=6, color=MISTAKE_COLOR, scale_factor=0.2).shift(0.9 * RIGHT + 1 * DOWN)
    #         c3 = Cross(stroke_width=6, color=MISTAKE_COLOR, scale_factor=0.2).shift(1.5 * RIGHT + 1 * DOWN)
    #         self.play(FadeIn(tri, c1, c2, c3))
    #         new_arrow = Arrow(0.4*LEFT, 0.4*RIGHT, color=GRAY, max_tip_length_to_length_ratio=0.4, max_stroke_width_to_length_ratio=6).next_to(complete_tree_text, RIGHT)
    #         self.play(FadeOut(tri, c1, c2, c3), Transform(arrow, new_arrow))
    #         self.play(complete_tree_text.animate.set_color(GRAY_OUT), new_arrow.animate.set_fill(GRAY_OUT).set_stroke(GRAY_OUT))

    # ## 3. Value ##
    #         value_text, title_animation1, title_animation2 = self.show_title("3. Value", complete_tree_text)
    #         self.play(title_animation1)
    #         self.play(title_animation2)

    #         max_heap = Text("Max", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(1 * LEFT + 2.3 * UP)
    #         self.play(Write(max_heap))
            tree = self.create_tree(["9","8","6","7","4","5"]).shift(1 * LEFT + 0 * UP)
    #         self.play(Create(tree))
    #         self.wait(1)
    #         min_heap = Text("Min", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(3.5 * RIGHT + 2.3 * UP)
    #         self.play(Write(min_heap))
    #         tree2 = self.create_tree(["1","2","4","3","6","5"]).shift(3.5 * RIGHT + 0 * UP)
    #         self.play(Create(tree2))
    #         self.wait(1)

    #         highlight1 = AnimationGroup(self.highlight_node(tree["c1"]), self.highlight_node(tree["c2"], True), self.highlight_node(tree["c3"], True))
    #         self.play(highlight1)
    #         dehighlight1 = AnimationGroup(self.dehighlight_node(tree["c1"]), self.dehighlight_node(tree["c2"]), self.dehighlight_node(tree["c3"]))
    #         self.play(dehighlight1)
    #         highlight1 = AnimationGroup(self.highlight_node(tree["c2"]), self.highlight_node(tree["c4"], True), self.highlight_node(tree["c5"], True))
    #         self.play(highlight1)
    #         dehighlight1 = AnimationGroup(self.dehighlight_node(tree["c2"]), self.dehighlight_node(tree["c4"]), self.dehighlight_node(tree["c5"]))
    #         self.play(dehighlight1)
    #         highlight1 = AnimationGroup(self.highlight_node(tree["c3"]), self.highlight_node(tree["c6"], True))
    #         self.play(highlight1)
    #         dehighlight1 = AnimationGroup(self.dehighlight_node(tree["c3"]), self.dehighlight_node(tree["c6"]))
    #         self.play(dehighlight1)

    #         highlight2 = AnimationGroup(self.highlight_node(tree2["c1"]), self.highlight_node(tree2["c2"], True), self.highlight_node(tree2["c3"], True))
    #         self.play(highlight2)
    #         dehighlight2 = AnimationGroup(self.dehighlight_node(tree2["c1"]), self.dehighlight_node(tree2["c2"]), self.dehighlight_node(tree2["c3"]))
    #         self.play(dehighlight2)
    #         highlight2 = AnimationGroup(self.highlight_node(tree2["c2"]), self.highlight_node(tree2["c4"], True), self.highlight_node(tree2["c5"], True))
    #         self.play(highlight2)
    #         dehighlight2 = AnimationGroup(self.dehighlight_node(tree2["c2"]), self.dehighlight_node(tree2["c4"]), self.dehighlight_node(tree2["c5"]))
    #         self.play(dehighlight2)
    #         highlight2 = AnimationGroup(self.highlight_node(tree2["c3"]), self.highlight_node(tree2["c6"], True))
    #         self.play(highlight2)
    #         dehighlight2 = AnimationGroup(self.dehighlight_node(tree2["c3"]), self.dehighlight_node(tree2["c6"]))
    #         self.play(dehighlight2)

    #         self.play(Uncreate(tree2), Unwrite(min_heap))
    #         self.play(max_heap.animate.move_to(1 * RIGHT + 2.3 * UP), tree.animate.move_to(0.7 * RIGHT + 0.3 * DOWN))

    #         highlight3 = AnimationGroup(self.highlight_node(tree["c4"]), self.highlight_node(tree["c5"]), self.highlight_node(tree["c6"]))
    #         self.play(highlight3)
    #         dehighlight3 = AnimationGroup(self.dehighlight_node(tree["c4"]), self.dehighlight_node(tree["c5"]), self.dehighlight_node(tree["c6"]))
    #         self.play(dehighlight3)
    #         highlight4 = AnimationGroup(self.highlight_node(tree["c3"]), self.highlight_node(tree["c4"]))
    #         self.play(highlight4)
    #         dehighlight4 = AnimationGroup(self.dehighlight_node(tree["c3"]), self.dehighlight_node(tree["c4"]))
    #         self.play(dehighlight4)

    #         self.play(FadeOut(tree, max_heap, value_text, complete_tree_text, new_arrow, arrow, tree_text, binary_tree))

    # ##########################
    # ## Array representation ##
    # ##########################
        # ## Opening ##
            array_text, title_animation1, title_animation2 = self.show_title("Array representation", title_group)
            self.play(title_animation1)
            self.play(title_animation2)
            self.play(Create(tree.move_to(0.2 * UP)))
            array_table = Table([["9", "8", "6", "7", "4", "5"]], 
                row_labels=[Text("A[i]")], 
                include_outer_lines=True,
                line_config={"stroke_width": TABLE_STROKE_WIDTH}
                ).scale(0.4).shift(0.2 * RIGHT + 2.4 * DOWN)
            self.play(array_table.create())
            animation = self.add_index(tree)
            self.play(*animation)

        ## Parent ##
            condition_text = Text("Given any index i,", color=GRAY, font=FONT, weight="BOLD", font_size=LG_TEXT_SIZE).shift(2 * RIGHT + 1 * UP)
            condition_text2 = Text("what is A[i]'s ", color=GRAY, font=FONT, weight="BOLD", font_size=LG_TEXT_SIZE).shift(1.5 * LEFT).next_to(condition_text, DOWN, buff=LINE_SPACING)
            rule1 = Text("parent?", color=PINK1, font=FONT, weight="BOLD", font_size=LG_TEXT_SIZE).shift(1.5 * LEFT).next_to(condition_text2, DOWN, buff=LINE_SPACING)
            tree_and_array = VGroup(tree, array_table)
            self.play(tree_and_array.animate.shift(3 * LEFT + 0.3 * DOWN))
            self.play(Write(condition_text))
            self.play(Write(condition_text2))
            self.play(Write(rule1))
            temp_group = VGroup(condition_text, condition_text2, rule1)
            self.play(temp_group.animate.shift(0.5 * UP))
            parent = Tex(r"$\lfloor \frac{(i-1)}{2} \rfloor$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=LG_TEXT_SIZE+30).next_to(rule1, DOWN, buff=0.6)
            self.play(Write(parent))
            self.play(FadeOut(tree, temp_group, parent))
            self.play(array_table.animate.scale(2).move_to(0 * LEFT + 0.6 * DOWN))
            i_text = Tex(r"$i$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+30).shift(1.6 * RIGHT + 0.4 * UP)
            parent.scale(0.9).move_to(1.6 * RIGHT + 0.6 * UP)  
            self.play(Write(i_text))
            self.play(parent.animate.move_to(0.97 * LEFT + 0.6 * UP))

            parent_table = Table(
                [["0", "floor()))))"], ["0", ""],["1", ""],["1", ""], ["2", ""]],
                row_labels=[Text("1"), Text("2"), Text("3"), Text("4"), Text("5")],
                col_labels=[Text("Parent's i"), Text(" ")],
                line_config={"stroke_width": TABLE_STROKE_WIDTH, "color": GRAY},
                element_to_mobject_config={"font": FONT},
                include_outer_lines=False,
                top_left_entry=Text("i")
                ).scale(0.7).next_to(tree, RIGHT, buff=0.5)
            for entry in parent_table.get_entries_without_labels():
                entry.set_color(BACKGROUND)   # Ad-hoc way to create an empty table
            self.play(FadeOut(array_table, i_text), parent.animate.scale(1.1).move_to(4.3 * RIGHT + 2.5 * UP))
            self.play(Create(tree.move_to(3.8 * LEFT + 0.2 * DOWN)))
            self.play(parent_table.create())

            self.play(self.highlight_node(tree["c2"]))
            self.play(self.highlight_node(tree["c1"], True))

            self.play(parent_table.get_entries((2, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            c1 = Tex(r"$\lfloor \frac{0}{2} \rfloor = 0$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 0.4)
            self.play(Write(c1))
            self.play(FadeIn(tree))

            self.play(self.dehighlight_node(tree["c2"]), self.highlight_node(tree["c3"]))
            self.play(parent_table.get_entries((3, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            c2 = Tex(r"$\lfloor \frac{1}{2} \rfloor = 0$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 1.3).align_to(c1, LEFT)
            self.play(Write(c2))
            self.play(FadeIn(tree))

            self.play(self.dehighlight_node(tree["c3"]), self.dehighlight_node(tree["c1"]))
            self.play(self.highlight_node(tree["c4"]))
            self.play(self.highlight_node(tree["c2"], True))
            self.play(parent_table.get_entries((4, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            c3 = Tex(r"$\lfloor \frac{2}{2} \rfloor = 1$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 2.2).align_to(c1, LEFT)
            self.play(Write(c3))
            self.play(FadeIn(tree))
        
            self.play(self.dehighlight_node(tree["c4"]), self.highlight_node(tree["c5"]))
            self.play(parent_table.get_entries((5, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            c4 = Tex(r"$\lfloor \frac{3}{2} \rfloor = 1$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 3.1).align_to(c1, LEFT)
            self.play(Write(c4))
            self.play(FadeIn(tree))

            self.play(self.dehighlight_node(tree["c5"]), self.dehighlight_node(tree["c2"]))
            self.play(self.highlight_node(tree["c6"]))
            self.play(self.highlight_node(tree["c3"], True))
            self.play(parent_table.get_entries((6, 2)).animate.set_color(GRAY))
            self.play(FadeOut(tree))
            c5 = Tex(r"$\lfloor \frac{4}{2} \rfloor = 2$", tex_template=TexFontTemplates.gnu_freeserif_freesans, color=PINK1, font_size=TEXT_SIZE+15).next_to(parent, DOWN, buff = 4).align_to(c1, LEFT)
            self.play(Write(c5))
            self.play(FadeIn(tree))
            self.play(self.dehighlight_node(tree["c6"]), self.dehighlight_node(tree["c3"]))
            self.play(FadeOut(parent_table, c1, c2, c3, c4, c5, parent))

        # ## Left child ##
        #     self.play(Write(condition_text.move_to(2 * RIGHT + 1 * UP)))
        #     self.play(Write(condition_text2.next_to(condition_text, DOWN, buff=0.4)))
        #     rule2 = Text("left child?", color=PINK1, weight="BOLD", font=FONT, font_size=LG_TEXT_SIZE).next_to(condition_text2, DOWN, buff=0.4)
        #     self.play(Write(rule2))

        #     temp_group = VGroup(condition_text, condition_text2, rule2)
        #     self.play(temp_group.animate.move_to(2 * RIGHT + 0.5 * UP))
        #     left_child = Tex(r"$2i+1$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+15).next_to(temp_group, DOWN, buff=0.6)
        #     self.play(Write(left_child))
        #     left_child_table = Table(
        #         [["1", "floor()))))"], ["3", ""],["5", ""]],
        #         row_labels=[Text("0"), Text("1"), Text("2")],
        #         col_labels=[Text("L Child's i"), Text(" ")],
        #         line_config={"stroke_width": TABLE_STROKE_WIDTH, "color": GRAY},
        #         element_to_mobject_config={"font": FONT},
        #         include_outer_lines=False,
        #         top_left_entry=Text("i")
        #         ).scale(0.7).next_to(tree, RIGHT, buff=0.8)
        #     for entry in left_child_table.get_entries_without_labels():
        #         entry.set_color(BACKGROUND)
        #     self.play(FadeOut(temp_group))
        #     self.play(left_child.animate.move_to(4 * RIGHT + 1.2 * UP))
        #     self.play(left_child_table.create())

        #     self.play(self.highlight_node(tree["c1"]))
        #     self.play(self.highlight_node(tree["c2"], True))
        #     self.play(left_child_table.get_entries((2, 2)).animate.set_color(GRAY))
        #     self.play(FadeOut(tree))
        #     c1 = Tex(r"$2\times0+1=1$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(left_child, DOWN, buff = 0.7)
        #     self.play(Write(c1))
        #     self.play(FadeIn(tree))

        #     self.play(self.dehighlight_node(tree["c1"]), self.highlight_node(tree["c2"]))
        #     self.play(self.highlight_node(tree["c4"], True))
        #     self.play(left_child_table.get_entries((3, 2)).animate.set_color(GRAY))
        #     self.play(FadeOut(tree))
        #     c2 = Tex(r"$2\times1+1=3$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(left_child, DOWN, buff = 1.6).align_to(c1, LEFT)
        #     self.play(Write(c2))
        #     self.play(FadeIn(tree))

        #     self.play(self.dehighlight_node(tree["c2"]), self.dehighlight_node(tree["c4"]))
        #     self.play(self.highlight_node(tree["c3"]))
        #     self.play(self.highlight_node(tree["c6"], True))
        #     self.play(left_child_table.get_entries((4, 2)).animate.set_color(GRAY))
        #     self.play(FadeOut(tree))
        #     c3 = Tex(r"$2\times2+1=5$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(left_child, DOWN, buff = 2.5).align_to(c1, LEFT)
        #     self.play(Write(c3))
        #     self.play(FadeIn(tree))
        #     self.play(self.dehighlight_node(tree["c6"]), self.dehighlight_node(tree["c3"]))
        #     self.play(tree["c6"].animate.set_fill(BACKGROUND), tree["c3"].animate.set_fill(BACKGROUND))
        #     self.play(FadeOut(left_child_table, c1, c2, c3, left_child))


        # ## Right child ##
        #     self.play(Write(condition_text.move_to(2 * RIGHT + 1 * UP)))
        #     self.play(Write(condition_text2.next_to(condition_text, DOWN, buff=0.4)))
        #     rule3 = Text("right child?", color=PINK1, weight="BOLD", font=FONT, font_size=LG_TEXT_SIZE).next_to(condition_text2, DOWN, buff=0.4)
        #     self.play(Write(rule3))

        #     temp_group = VGroup(condition_text, condition_text2, rule3)
        #     self.play(temp_group.animate.move_to(2 * RIGHT + 0.5 * UP))
        #     right_child = Tex(r"$2i+2$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=LG_TEXT_SIZE+15).next_to(temp_group, DOWN, buff=0.6)
        #     self.play(Write(right_child))
        #     right_child_table = Table(
        #         [["2", "floor()))))"], ["4", ""]],
        #         row_labels=[Text("0"), Text("1")],
        #         col_labels=[Text("R Child's i"), Text(" ")],
        #         line_config={"stroke_width": TABLE_STROKE_WIDTH, "color": GRAY},
        #         element_to_mobject_config={"font": FONT},
        #         include_outer_lines=False,
        #         top_left_entry=Text("i")
        #         ).scale(0.7).next_to(tree, RIGHT, buff=0.8)
        #     for entry in right_child_table.get_entries_without_labels():
        #         entry.set_color(BACKGROUND)   # Ad-hoc way to create an empty table
        #     self.play(FadeOut(temp_group))
        #     self.play(right_child.animate.move_to(4 * RIGHT + 0.8 * UP))
        #     self.play(right_child_table.create())

        #     self.play(self.highlight_node(tree["c1"]))
        #     self.play(self.highlight_node(tree["c3"], True))
        #     self.play(right_child_table.get_entries((2, 2)).animate.set_color(GRAY))
        #     self.play(FadeOut(tree))
        #     c1 = Tex(r"$2\times0+2=2$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(right_child, DOWN, buff = 0.7)
        #     self.play(Write(c1))
        #     self.play(FadeIn(tree))   

        #     self.play(self.dehighlight_node(tree["c1"]), self.dehighlight_node(tree["c3"]))
        #     self.play(self.highlight_node(tree["c2"]), self.highlight_node(tree["c5"], True))
        #     self.play(right_child_table.get_entries((3, 2)).animate.set_color(GRAY))
        #     self.play(FadeOut(tree))
        #     c2 = Tex(r"$2\times1+2=4$", color=PINK1, tex_template=TexFontTemplates.gnu_freeserif_freesans, font_size=TEXT_SIZE+5).next_to(right_child, DOWN, buff = 1.7).align_to(c1, LEFT)
        #     self.play(Write(c2))
        #     self.play(FadeIn(tree))

        #     self.play(FadeOut(tree, right_child_table, c1, c2, right_child))

        #     array_table.move_to(ORIGIN)
        #     self.play(Create(array_table))
        #     i_text.move_to(0.97 * LEFT + 1.2 * UP)
        #     parent.scale(0.9).move_to(0.97 * LEFT + 1.2* UP)  
        #     left_child.scale(0.9).move_to(0.97 * LEFT + 1.2 * UP)  
        #     right_child.scale(0.9).move_to(0.97 * LEFT + 1.2 * UP)  
        #     self.play(Write(i_text))
        #     self.play(parent.animate.shift(1.26 * LEFT))
        #     parent_text = Text("P", color=PINK1, weight="BOLD", font=FONT, font_size=70).next_to(parent, DOWN, buff=1.7)
        #     self.play(FadeIn(parent_text))
        #     self.play(left_child.animate.shift(2.5 * RIGHT))
        #     left_text = Text("L", color=PINK1, weight="BOLD", font=FONT, font_size=70).next_to(left_child, DOWN, buff=1.7).align_to(parent_text, UP)
        #     self.play(FadeIn(left_text))
        #     self.play(right_child.animate.shift(3.8 * RIGHT))
        #     right_text = Text("R", color=PINK1, weight="BOLD", font=FONT, font_size=70).next_to(right_child, DOWN, buff=1.7).align_to(parent_text, UP)
        #     self.play(FadeIn(right_text))
        #     self.wait(2)