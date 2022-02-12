from typing import Text

from matplotlib.transforms import Transform
from manim import *
from style import *
from manim_fonts import *
from util import *

class Show(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
    ## P1
        # title_text, title_animation1, title_animation2 = show_title("堆的几种操作")
        # self.play(title_animation1)
        # self.wait()
        # self.play(title_animation2)
        # self.wait()

    # ## P2
    #     title_text, title_animation1, title_animation2 = show_title("堆的功能？")
    #     self.play(title_animation1)
    #     self.wait()
    #     self.play(title_text.animate.shift(UP*2.9).scale(0.6))
        
    #     max = ["9","8","6","7","4","5"]
    #     max_heap = Text("最大堆", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(2.5 * LEFT + 1.7 * UP)
    #     self.play(Write(max_heap))
    #     tree = create_tree(max).shift(2.5 * LEFT + (-0.2) * UP)
    #     tree.scale(0.8)
    #     self.play(Create(tree), run_time=2)
    #     self.wait(1)

    #     min = ["1","2","4","3","6","5"]
    #     min_heap = Text("最小堆", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(2.5 * RIGHT + 1.7 * UP)
    #     self.play(Write(min_heap))
    #     tree2 = create_tree(min).shift(2.5 * RIGHT + (-0.2) * UP)
    #     tree2.scale(0.8)
    #     self.play(Create(tree2, run_time=2))
    #     self.wait(1)

    #     array_table = create_array(max)
    #     array_table.scale(0.3).next_to(tree, DOWN, buff=0.5)
    #     self.play(array_table.create())

    #     array_table2 = create_array(min)
    #     array_table2.scale(0.3).next_to(tree2, DOWN, buff=0.5)
    #     self.play(array_table2.create())
    #     self.wait()

    #     array_table.add_highlighted_cell((1,2), color=PINK1)
    #     self.play(highlight_node(tree["c1"]))
    #     # self.play(array_table.animate.get_highlighted_cell(1,2))
    #     # ???

    #     array_table2.add_highlighted_cell((1,2), color=PINK1)
    #     self.play(highlight_node(tree2["c1"]))
    #     # self.play(array_table2.animate.get_highlighted_cell(1,2))
    #     self.wait()

    #     self.play(FadeOut(title_text, tree, tree2, min_heap, max_heap, array_table, array_table2))
    #     self.wait()

    # P3
        create_text = get_text("增", TITLE_SIZE+110).set_fill(opacity=0.8).shift(-2*RIGHT+1.5*UP)
        delete_text = get_text("删", TITLE_SIZE+110).set_fill(opacity=0.8).shift(2*RIGHT+1.5*UP)
        update_text = get_text("改", TITLE_SIZE+110).set_fill(opacity=0.8).shift(-2*RIGHT+(-1.5)*UP)
        read_text = get_text("查", TITLE_SIZE+110).set_fill(opacity=0.8).shift(2*RIGHT+(-1.5)*UP)
        # self.play(Write(create_text))
        # self.play(Write(delete_text))
        # self.play(Write(update_text))
        # self.play(Write(read_text))
        # self.wait()

        create = get_text_2line("插入", "insert(k)", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).move_to(create_text.get_center())
        # self.play(create_text.animate.set_fill(opacity=0.1))
        # self.wait()
        # self.play(Write(create))
        # self.wait()

        delete = get_text_2line("删除", "delete(i)", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).move_to(delete_text.get_center())
        # self.play(delete_text.animate.set_fill(opacity=0.1))
        # self.wait()
        # self.play(Write(delete))
        # self.wait()

        # self.play(FadeOut(update_text))
        # self.wait()

        read = get_text_2line("查看最值", "get_m()", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).move_to(read_text.get_center())
        # self.play(read_text.animate.set_fill(opacity=0.1))
        # self.wait()
        # self.play(Write(read))
        # self.wait()

        # self.play(FadeOut(create_text, delete_text, read_text))
        # self.wait()
        self.play(create.animate.scale(0.7).move_to(2*LEFT+2*UP), delete.animate.scale(0.7).move_to(2*LEFT+0*UP), read.animate.scale(0.7).move_to(2*LEFT+(-2)*UP))
        
        self.wait()
        extract = get_text_2line("取走最值", "extract_m()", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).scale(0.7).move_to(2*RIGHT+2*UP)
        build_heap = get_text_2line("建堆", "build_heap(A)", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).scale(0.7).move_to(2*RIGHT+0*UP)
        heapify = get_text_2line("堆化", "heapify(i)", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).scale(0.7).move_to(2*RIGHT+(-2)*UP)
        self.play(Write(extract))
        self.wait()
        self.play(Write(build_heap))
        self.wait()
        self.play(Write(heapify))

    ## P4
        box = SurroundingRectangle(heapify, buff=0.3, color=PINK2)
        self.play(Create(box), heapify["l1"].animate.set_color(PINK2), heapify["l2"].animate.set_color(PINK2))
        heapify_box = VGroup(heapify, box)
        self.play(FadeOut(extract))
        self.play(heapify_box.animate.move_to(1.3*DOWN), create.animate.move_to(4*LEFT+1.3*UP), delete.animate.move_to(1.7*LEFT+1.3*UP), read.animate.move_to(1.2*RIGHT+1.3*UP), build_heap.animate.move_to(4*RIGHT+1.3*UP))
        create_arrow = Arrow(heapify_box.get_top(), create.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        delete_arrow = Arrow(heapify_box.get_top(), delete.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        read_arrow = Arrow(heapify_box.get_top(), read.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        build_arrow = Arrow(heapify_box.get_top(), build_heap.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        self.play(Create(create_arrow), Create(delete_arrow), Create(read_arrow), Create(build_arrow))
        self.wait()

        temp_group = VGroup(create, delete, read, build_heap, create_arrow, delete_arrow, read_arrow, build_arrow, heapify_box)
        heap_box = SurroundingRectangle(temp_group, buff=0.4, color=BACKGROUND, corner_radius=0.2).set_fill(GRAY_OUT, opacity=0.1).set_z_index(-10)
        temp_group += heap_box
        self.play(Create(heap_box))
        heap_text = get_text("堆", TEXT_SIZE).next_to(heap_box, LEFT)
        temp_group += heap_text
        self.play(Write(heap_text))
        self.wait()

        user = get_text("用户", TEXT_SIZE).shift(3*UP)
        self.play(temp_group.animate.shift(0.7*DOWN))
        create_arrow2 = Arrow(create.get_top(), user.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        delete_arrow2 = Arrow(delete.get_top(), user.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        read_arrow2 = Arrow(read.get_top(), user.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        build_arrow2 = Arrow(build_heap.get_top(), user.get_bottom(), buff=0.3, stroke_width=5, max_tip_length_to_length_ratio=0.2)
        self.play(Create(user))
        self.play(Create(create_arrow2), Create(delete_arrow2), Create(read_arrow2), Create(build_arrow2))
        self.wait()
        you = get_text("你", TEXT_SIZE).shift(user.get_center())
        borrow = get_text("借钱", SECONDARY_TITLE_SIZE-20).shift(create.get_center())
        treat = get_text("请客", SECONDARY_TITLE_SIZE-20).shift(delete.get_center())
        phone = get_text("充话费", SECONDARY_TITLE_SIZE-20).shift(read.get_center())
        red_pocket = get_text("发红包", SECONDARY_TITLE_SIZE-20).shift(build_heap.get_center())
        money = get_text("取钱", SECONDARY_TITLE_SIZE-20).set_fill(PINK2).shift(heapify_box.get_center())
        friend = Paragraph("""
        你
        朋
        友
        """, color=GRAY, font=FONT, weight="BOLD", font_size=TEXT_SIZE).next_to(heap_box, LEFT)
        self.play(Transform(user, you), Transform(create, borrow), Transform(delete, treat), Transform(read, phone), Transform(build_heap, red_pocket), Transform(heapify, money), Transform(heap_text, friend))
        self.wait()