from typing import Text
from manim import *
from style import *
from manim_fonts import * 

def show_title(text, up_mobject=None, title_scale=0.25):
    t, animation1, animation2 = None, None, None
    if not up_mobject:
        # The Title
        t = Paragraph(text, color=GRAY, font=FONT, weight="BOLD", font_size=TITLE_SIZE)
        animation1 = Write(t)
        animation2 = t.animate.scale(title_scale).set_color(GRAY_OUT).to_edge(UL, buff=0.8).shift(0.2 * UP)
    else:
        # The secondary title
        t = Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=SECONDARY_TITLE_SIZE)
        animation1 = Write(t)
        animation2 = t.animate.scale(0.5).next_to(up_mobject, DOWN, buff=0.2).align_to(up_mobject, LEFT)
    return t, animation1, animation2

def show_title_end(title_group, scale_value=1.5):
    new_title_group = title_group.copy().move_to(ORIGIN).scale(scale_value).set_color(GRAY)
    box = SurroundingRectangle(new_title_group, color=PINK2, buff=0.5, stroke_width=SM_STROKE_WIDTH)
    return new_title_group, box

def highlight_node(mobject, secondary=False):
    # Highlight node to dark pink
    if not secondary:
        return AnimationGroup(mobject["c"].animate.set_fill(PINK1).set_stroke(PINK1), mobject["t"].animate.set_color(BACKGROUND))
    # Highlight node to light pink
    else:
        return AnimationGroup(mobject["c"].animate.set_fill(PINK3).set_stroke(PINK3), mobject["t"].animate.set_color(BACKGROUND))

def dehighlight_node(mobject):
    return AnimationGroup(mobject["c"].animate.set_fill(BACKGROUND).set_stroke(GRAY), mobject["t"].animate.set_color(GRAY))


def exercise_title(size=TITLE_SHRINK_SIZE):
    t = Text("EXERCISE", color=GRAY_OUT, font=FONT, weight="BOLD", font_size=size).to_edge(UL, buff=0.8).shift(0.2 * UP)
    return FadeIn(t)

def exercise_question(text):
    t = Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=TEXT_SIZE)
    b = SurroundingRectangle(t, color=BLUE1, buff=0.2, stroke_width=SM_STROKE_WIDTH)
    return VGroup(t, b)

def exercise_text(text):
    return Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=TEXT_SIZE)

def get_text(text, font_size):
    return Text(text, color=GRAY, font=FONT, weight="BOLD", font_size=font_size)

def get_text_2line(line1, line2, font_size1, font_size2):
    t1 = Text(line1, color=GRAY, font=FONT, weight="BOLD", font_size=font_size1)
    t2 = Text(line2, color=GRAY, font=FONT, weight="BOLD", font_size=font_size2).next_to(t1, DOWN, buff=0.2)
    return VDict({"l1": t1, "l2": t2})

def create_tree(array):
    c1 = Circle(radius=RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.2 * UP).set_z_index(1)
    t1 = Text(array[0], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c1.get_center()).set_z_index(2)
    ct1 = VDict([("c", c1), ("t", t1)])
    c2 = Circle(radius=RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.1 * LEFT + 0.2 * DOWN).set_z_index(1)
    t2 = Text(array[1], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c2.get_center()).set_z_index(2)
    ct2 = VDict([("c", c2), ("t", t2)])
    c3 = Circle(radius=RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.1 * RIGHT + 0.2 * DOWN).set_z_index(1)
    t3 = Text(array[2], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c3.get_center()).set_z_index(2)
    ct3 = VDict([("c", c3), ("t", t3)])
    c4 = Circle(radius=RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(1.7 * LEFT + 1.6 * DOWN).set_z_index(1)
    t4 = Text(array[3], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c4.get_center()).set_z_index(2)
    ct4 = VDict([("c", c4), ("t", t4)])
    c5 = Circle(radius=RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(0.5 * LEFT + 1.6 * DOWN).set_z_index(1)
    t5 = Text(array[4], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c5.get_center()).set_z_index(2)
    ct5 = VDict([("c", c5), ("t", t5)])
    c6 = Circle(radius=RADIUS, stroke_width=STROKE_WIDTH).set_stroke(color=GRAY).set_fill(BACKGROUND, opacity=1.0).shift(0.5 * RIGHT + 1.6 * DOWN).set_z_index(1)
    t6 = Text(array[5], font=FONT, weight="BOLD", font_size=VALUE_SIZE).move_to(c6.get_center()).set_z_index(2)
    ct6 = VDict([("c", c6), ("t", t6)])
    l12 = Line(c1.get_center(), c2.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
    l13 = Line(c1.get_center(), c3.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
    l24= Line(c2.get_center(), c4.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
    l25 = Line(c2.get_center(), c5.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
    l36= Line(c3.get_center(), c6.get_center()).set_stroke(color=GRAY, width=STROKE_WIDTH).set_z_index(0)
    tree = VDict([("c1", ct1), ("l12", l12), ("c2", ct2), ("l13", l13), ("c3", ct3), ("l24", l24), ("c4", ct4), ("l25", l25), ("c5", ct5), ("l36", l36), ("c6", ct6)])
    return tree

def create_array(array):
    return Table([array], 
    row_labels=[Text("A[i]", font=FONT, weight="BOLD")], 
    include_outer_lines=True,
    element_to_mobject_config={"font": FONT},
    line_config={"stroke_width": TABLE_STROKE_WIDTH}
    )