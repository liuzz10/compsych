from typing import Text
from manim import *
from style import *
from manim_fonts import *
from util import *

class Show(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(watermark())
    ## P1
        title_text, title_animation1, title_animation2 = show_title(["堆：几种操作"], title_scale=0.3)
        self.play(title_animation1)
        self.wait()
        self.play(title_animation2)
        self.wait()

    ## P2
        title_text2, title_animation1, _ = show_title(["堆的功能？"])
        self.play(title_animation1)
        self.wait()
        self.play(title_text2.animate.shift(UP*2.9).scale(0.5))
        
        max = ["9","8","6","7","4","5"]
        max_heap = Text("最大堆", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(2.6 * LEFT + 1.9 * UP)
        self.play(Write(max_heap))
        min = ["1","2","4","3","6","5"]
        min_heap = Text("最小堆", color=GRAY , font=FONT, weight="BOLD", font_size=TEXT_SIZE).shift(2.6 * RIGHT + 1.9 * UP)
        self.play(Write(min_heap))
        self.wait()

        tree = create_tree(max).shift(2.6 * LEFT + (0.1) * UP)
        tree.scale(0.8)
        self.play(Create(tree), run_time=2)
        self.wait()

        array_table = create_array(max)
        array_table.scale(0.3).next_to(tree, DOWN, buff=0.5)
        self.play(array_table.create())

        tree2 = create_tree(min).shift(2.6 * RIGHT + (0.1) * UP)
        tree2.scale(0.8)
        self.play(Create(tree2, run_time=2))
        self.wait()

        array_table2 = create_array(min)
        array_table2.scale(0.3).next_to(tree2, DOWN, buff=0.5)
        self.play(array_table2.create())
        self.wait()

        self.play(highlight_node(tree["c1"]))
        array_table.add_highlighted_cell((1,2), color=PINK1)
        array_table.set_column_colors(GRAY, BACKGROUND)
        self.add(array_table)
        self.wait()

        self.play(highlight_node(tree2["c1"]))
        array_table2.add_highlighted_cell((1,2), color=PINK1)
        array_table2.set_column_colors(GRAY, BACKGROUND)
        self.add(array_table2)
        self.wait()

        answer = get_text("找到最值", LG_TEXT_SIZE-5).set_fill(PINK1).move_to(2.9*UP+1.3*RIGHT)
        self.play(title_text2.animate.shift(1*LEFT))
        self.play(Write(answer))
        self.wait(2)

        self.play(FadeOut(answer, title_text2, tree, tree2, min_heap, max_heap, array_table, array_table2))
        self.wait()

    # P3
        create_text = get_text("增", TITLE_SIZE+110).set_fill(opacity=0.9).shift(-2*RIGHT+1.5*UP)
        delete_text = get_text("删", TITLE_SIZE+110).set_fill(opacity=0.9).shift(2*RIGHT+1.5*UP)
        update_text = get_text("改", TITLE_SIZE+110).set_fill(opacity=0.9).shift(-2*RIGHT+(-1.5)*UP)
        read_text = get_text("查", TITLE_SIZE+110).set_fill(opacity=0.9).shift(2*RIGHT+(-1.5)*UP)
        self.play(Write(create_text))
        self.play(Write(delete_text))
        self.play(Write(update_text))
        self.play(Write(read_text))
        self.wait()

        create = get_text_2line("插入", "insert(k)", SECONDARY_TITLE_SIZE-10, SECONDARY_TITLE_SIZE-30).move_to(create_text.get_center())
        self.play(create_text.animate.set_fill(opacity=0.1))
        self.wait()
        self.play(Write(create))
        self.wait()

        delete = get_text_2line("删除", "delete(i)", SECONDARY_TITLE_SIZE-10, SECONDARY_TITLE_SIZE-30).move_to(delete_text.get_center())
        self.play(delete_text.animate.set_fill(opacity=0.1))
        self.wait()
        self.play(Write(delete))
        self.wait()

        self.play(FadeOut(update_text))
        self.wait()

        read = get_text_2line("查看最值", "get_m()", SECONDARY_TITLE_SIZE-10, SECONDARY_TITLE_SIZE-30).move_to(read_text.get_center())
        self.play(read_text.animate.set_fill(opacity=0.1))
        self.wait()
        self.play(Write(read))
        self.wait()

        self.play(FadeOut(create_text, delete_text, read_text))
        self.wait()
        self.play(create.animate.scale(0.7).move_to(2*LEFT+2*UP), delete.animate.scale(0.7).move_to(2*LEFT+0*UP), read.animate.scale(0.7).move_to(2*LEFT+(-2)*UP))
        
        self.wait()
        extract = get_text_2line("取走最值", "extract_m()", SECONDARY_TITLE_SIZE-10, SECONDARY_TITLE_SIZE-30).scale(0.7).move_to(2*RIGHT+2*UP)
        build_heap = get_text_2line("建堆", "build_heap(A)", SECONDARY_TITLE_SIZE-10, SECONDARY_TITLE_SIZE-30).scale(0.7).move_to(2*RIGHT+0*UP)
        heapify = get_text_2line("堆化", "heapify(i)", SECONDARY_TITLE_SIZE-10, SECONDARY_TITLE_SIZE-30).scale(0.7).move_to(2*RIGHT+(-2)*UP)
        self.play(Write(extract))
        self.wait()
        self.play(Write(build_heap))
        self.wait()
        self.play(Write(heapify))
        self.wait()

    ## P4
        box = SurroundingRectangle(heapify, buff=0.2, color=PINK2)
        self.play(Create(box), heapify["l1"].animate.set_color(PINK2), heapify["l2"].animate.set_color(PINK2))
        heapify_box = VGroup(heapify, box)
        self.wait()
        self.play(FadeOut(read))
        self.wait()
        self.play(heapify_box.animate.scale(0.9).move_to(1.3*DOWN), create.animate.scale(0.9).move_to(4*LEFT+1.3*UP), delete.scale(0.9).animate.move_to(1.7*LEFT+1.3*UP), extract.animate.scale(0.9).move_to(1.2*RIGHT+1.3*UP), build_heap.animate.scale(0.9).move_to(4*RIGHT+1.3*UP))
        create_arrow = Line(heapify_box.get_top(), create.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        delete_arrow = Line(heapify_box.get_top(), delete.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        extract_arrow = Line(heapify_box.get_top(), extract.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        build_heap2 = build_heap.copy()
        build_arrow = always_redraw(lambda : Line(heapify_box.get_top(), build_heap2.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3))
        self.wait()
        self.play(Create(create_arrow), Create(delete_arrow), Create(extract_arrow), Create(build_arrow))
        self.wait()

        temp_group = VGroup(create, delete, extract, build_heap)
        box1 = SurroundingRectangle(temp_group, buff=0.4, color=BACKGROUND, corner_radius=0.1).set_fill(GRAY_OUT, opacity=0.1).set_z_index(-10)
        text1 = get_text("堆层面", SM_TEXT_SIZE).next_to(box1, UP, buff=0.2).align_to(box1, LEFT)
        self.play(Create(box1), Write(text1))
        self.wait()

        self.play(box1.animate.shift(2.6*DOWN), FadeOut(text1))
        text2 = get_text("点层面", SM_TEXT_SIZE).next_to(box1, UP, buff=0.2).align_to(box1, LEFT)
        self.play(Write(text2))
        self.wait()

        temp_group = VGroup(create, delete, extract, build_heap, create_arrow, delete_arrow, extract_arrow, build_arrow, heapify_box)
        heap_box = SurroundingRectangle(temp_group, buff=0.4, color=BACKGROUND, corner_radius=0.1).set_fill(GRAY_OUT, opacity=0.1).set_z_index(-10)
        temp_group += heap_box
        self.play(FadeOut(text2))
        self.play(ReplacementTransform(box1, heap_box))
        self.wait()

        user = get_text("用户", TEXT_SIZE).shift(3*UP)
        build_heap2.shift(0.7*DOWN)
        self.play(temp_group.animate.shift(0.7*DOWN))
        create_arrow2 = Line(create.get_top(), user.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        delete_arrow2 = Line(delete.get_top(), user.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        extract_arrow2 = Line(extract.get_top(), user.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        build_arrow2 = Line(build_heap.get_top(), user.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        self.play(Create(user))
        self.play(Create(create_arrow2), Create(delete_arrow2), Create(extract_arrow2), Create(build_arrow2))
        self.wait()
        you = get_text("你", TEXT_SIZE).shift(user.get_center())
        borrow = get_text("借钱", SECONDARY_TITLE_SIZE-30).shift(create.get_center())
        treat = get_text("请客", SECONDARY_TITLE_SIZE-30).shift(delete.get_center())
        phone = get_text("充话费", SECONDARY_TITLE_SIZE-30).shift(extract.get_center())
        red_pocket = get_text("发红包", SECONDARY_TITLE_SIZE-30).shift(build_heap.get_center())
        money = get_text("取钱", SECONDARY_TITLE_SIZE-30).set_fill(PINK2).shift(heapify_box.get_center())
        friend = Paragraph("""
        你
        朋
        友
        """, color=GRAY, font=FONT, weight="BOLD", font_size=TEXT_SIZE).next_to(heap_box, LEFT)
        user2 = user.copy()
        create2 = create.copy()
        delete2 = delete.copy()
        extract2 = extract.copy()
        heapify2 = heapify.copy()
        heapify_box = VGroup(heapify2, box)
        self.play(ReplacementTransform(user, you), ReplacementTransform(create, borrow), ReplacementTransform(delete, treat), ReplacementTransform(extract, phone), ReplacementTransform(build_heap, red_pocket), ReplacementTransform(heapify, money), Write(friend))
        self.wait()
        self.play(ReplacementTransform(you, user2), ReplacementTransform(borrow, create2), ReplacementTransform(treat, delete2), ReplacementTransform(phone, extract2), ReplacementTransform(red_pocket, build_heap2), ReplacementTransform(money, heapify2), Unwrite(friend))
        self.wait()
        self.play(FadeOut(user2, create2, delete2, extract2, heap_box, create_arrow, create_arrow2, delete_arrow, delete_arrow2, extract_arrow, extract_arrow2, build_arrow2, title_text, box))
    ## P5
        self.add(build_arrow)
        self.play(build_heap2.animate.shift(4*LEFT))
        self.wait()
        build_group = VGroup(build_heap2, build_arrow, heapify2)

        # build a title group to be used on another file
        build_heap_title = get_text_2line("建堆", "build_heap(A)", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).scale(0.7)
        heapify_title = get_text_2line("堆化", "heapify(i)", SECONDARY_TITLE_SIZE, SECONDARY_TITLE_SIZE-20).scale(0.7).next_to(build_heap_title, DOWN, buff=1.3)
        heapify_title.set_fill(GRAY)
        build_arrow_title = Line(heapify_title.get_top(), build_heap_title.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        title_group = VGroup(build_heap_title, heapify_title, build_arrow_title).scale(0.5).to_edge(UL, buff=0.8).shift(0.2 * UP)

        build_group_new = build_group.copy()
        self.play(ReplacementTransform(build_group, title_group))
        self.wait(2)

        build_group_new[0].shift(4*RIGHT)
        build_group_new[1] = always_redraw(lambda : Line(box.get_top(), build_group_new[0].get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3))
        self.play(ReplacementTransform(title_group, build_group_new), FadeIn(user2, create2, delete2, extract2, heap_box, create_arrow, create_arrow2, delete_arrow, delete_arrow2, extract_arrow, extract_arrow2, build_arrow2, title_text, box))
        self.wait(2)

        self.play(heap_box.animate)
        self.play(FadeOut(build_group_new, user2, create2, delete2, extract2, heap_box, create_arrow, create_arrow2, delete_arrow, delete_arrow2, extract_arrow, extract_arrow2, build_arrow2, box))

        new_title_group, title_box = show_title_end(title_text, scale_value=3)
        self.play(ReplacementTransform(title_text, new_title_group))
        self.play(Create(title_box))
        self.wait(2)
        self.play(Uncreate(new_title_group), Uncreate(title_box))
        self.wait()