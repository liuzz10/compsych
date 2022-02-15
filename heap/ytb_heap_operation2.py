from manim import *
from style import *
from heap_array import HeapArray
from util import *


# create low quality video $ manim -ql -p heap.py BinaryHeap
# create medium quality video $ manim -qm -p heap.py BinaryHeap
# create high quality video $ manim -qh -p heap.py BinaryHeap

# Zindex: line 0, circle 1, description text 2


class Show(Scene):
    def _color(self, node, is_delete):
        """
        Color a node to highlight
        """
        if is_delete:
            node.mobject["circle"].set_color(MISTAKE_COLOR)
            node.mobject["text"].set_color(BACKGROUND)
            node.text_mobject.set_color(MISTAKE_COLOR)
        else:
            node.mobject["circle"].set_color(PINK2)  
            node.mobject["text"].set_color(BACKGROUND)
            node.text_mobject.set_color(PINK2)

    def _decolor(self, node):
        """
        Deolor a node to de-highlight
        """
        node.mobject["circle"].set_color(BACKGROUND).set_stroke(GRAY)
        node.mobject["text"].set_color(GRAY)
        node.text_mobject.set_color(GRAY)

    def _decolor_all(self, heap_array):
        """
        Deolor all nodes to de-highlight
        """
        for node in heap_array:
            node.mobject["circle"].set_color(BACKGROUND).set_stroke(GRAY)
            node.mobject["text"].set_color(GRAY)
            node.text_mobject.set_color(GRAY)

    def swap(self, heap, node, node_to_swap, is_delete=False):
        """
        Draw the swap animation and update the array structure
        """
        node.value, node_to_swap.value = node_to_swap.value, node.value
        node.mobject, node_to_swap.mobject = node_to_swap.mobject, node.mobject
        self.play(Swap(node.mobject, node_to_swap.mobject), heap.table.swap(node.text_mobject, node_to_swap.text_mobject), run_time=1.5)
        node.text_mobject, node_to_swap.text_mobject = node_to_swap.text_mobject, node.text_mobject
        # if not is_delete:
        #     self._decolor(node_to_swap)
    
    def _heapify(self, heap, node, is_min_heap):
        """
        Heapify the subtree started at curr_node
        """
        if is_min_heap:
            smallest = node
            if node.left < len(heap.array) and smallest.value > heap.array[node.left].value:
                smallest = heap.array[node.left]
            if node.right < len(heap.array) and smallest.value > heap.array[node.right].value:
                smallest = heap.array[node.right]
            if smallest.value != node.value: # Need swap
                self.swap(heap, node, smallest) # Draw the swap animation
                self._heapify(heap, smallest, is_min_heap)
        else:
            largest = node
            if node.left < len(heap.array) and largest.value < heap[node.left].value:
                largest = heap.array[node.left]
            if node.right < len(heap.array) and largest.value < heap[node.right].value:
                largest = heap.array[node.right]
            if largest != node: # Need swap
                self.swap(heap, node, largest) # Draw the swap animation
                self._heapify(heap, largest, is_min_heap)

    def _filterup(self, heap, node, is_min_heap):
        if node.parent < 0:
            return
        parent = heap.array[node.parent]
        if is_min_heap:
            if node.value < parent.value:
                self.swap(heap, node, parent)
                self._filterup(heap, parent, is_min_heap)
        else:
            if node.value > parent.value:
                self.swap(heap, node, parent)
                self._filterup(heap, parent, is_min_heap)
    
    def build_heap(self, heap, is_min_heap=True):
        """
        Build a heap by heapify each node from bottom to up
        """
        self.play(FadeIn(heap.code_for_build.code, heap.code_for_build.create_title('Building the heap')))
        self.wait()
        self.play(heap.code_for_build.highlight(1))
        self.wait(1)
        for i in range((len(heap.array)-1) // 2, -1, -1):
            node = heap.array[i]
            # Color
            self.play(heap.code_for_build.highlight(2))
            self.wait(0.5)
            self._color(node, False)
            self.wait(0.5)
            # Heapify
            self.play(heap.code_for_build.highlight(3))
            self._heapify(heap, node, is_min_heap)
            self.wait(0.5)
            self._decolor_all(heap.array)
        self.play(heap.code_for_build.highlight(4))
        self.play(FadeOut(heap.code_for_build.code, heap.code_for_build.highlight_rect, heap.code_for_build.title, heap.tree, heap.table.first_line))


    def extract(self, heap):
        if len(heap.array) == 0:
            print("Heap is empty")
            return
        self.play(FadeIn(heap.code_for_extract.code, heap.code_for_build.create_title('Deletion')))
        self.wait(0.5)
        # Swap
        self.play(heap.code_for_extract.highlight(3))
        first = heap.array[0]
        last = heap.array[-1]
        self._color(first, False)
        self._color(last, False)
        self.swap(heap, first, last, True)
        # Remove last
        self.play(heap.code_for_extract.highlight(4))
        self.wait(1)
        self.play(FadeOut(last.mobject), FadeOut(last.line_mobject), heap.table.remove())
        heap.remove()
        # Heapify
        self.play(heap.code_for_extract.highlight(5))
        self.wait(1)
        self._heapify(heap, first, True)
        self._decolor_all(heap.array)
        # Clean up
        self.play(FadeOut(heap.code_for_extract.code, heap.code_for_extract.highlight_rect, heap.code_for_build.title))


    def insert(self, heap, value):
        if len(heap.array) == 0:
            print("Heap is empty")
            return
        self.play(FadeIn(heap.code_for_insert.code, heap.code_for_build.create_title('Insertion')))
        self.wait(0.5)
        # Insert
        self.play(heap.code_for_insert.highlight(3))
        node = heap.add(value)
        self.play(FadeIn(node.line_mobject), FadeIn(node.mobject), heap.table.add(node.text_mobject))
        # Heapify
        self._color(node, False)
        self.play(heap.code_for_insert.highlight(4))
        self.wait(1)
        self._filterup(heap, node, True)
        self._decolor_all(heap.array)
        # Clean up
        self.play(FadeOut(heap.code_for_insert.code, heap.code_for_insert.highlight_rect, heap.code_for_build.title))


    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(watermark())

        build_heap_title = get_text("build_heap(A)", SECONDARY_TITLE_SIZE-20).scale(1)
        heapify_title = get_text("heapify(i)", SECONDARY_TITLE_SIZE-20).scale(1).next_to(build_heap_title, DOWN, buff=1.3)
        heapify_title.set_fill(GRAY)
        build_arrow_title = Line(heapify_title.get_top(), build_heap_title.get_bottom(), buff=0.2, stroke_width=5).add_tip(tip_length=0.3)
        title_group = VGroup(build_heap_title, heapify_title, build_arrow_title).scale(0.5).to_edge(UL, buff=0.8).shift(0.2 * UP)
        self.add(title_group)
        self.wait()

        double_box, animations = show_example(title_group, False)
        for a in animations:
            self.play(a)

        array = [90,7,6,40,70,60,80,3,0,2,1,4]
        heap = HeapArray(array)
        heap.tree.scale(0.9)
        # Draw an array and a tree 
        self.play(heap.show(), run_time=3)
        self.wait()

        text = get_text("Min heap", TEXT_SIZE).next_to(heap.tree, RIGHT, buff=1)
        arrow = Line(heap.tree.get_right(), text.get_left(), buff=0.2, stroke_width=5).add_tip(tip_length=0.2)
        question_mark = get_text("?", TEXT_SIZE).next_to(arrow, UP, buff=0.1).shift(0.3*RIGHT)
        text.shift(0.6*RIGHT)
        arrow.shift(0.4*RIGHT)
        self.play(Write(arrow))
        self.play(Write(text))
        self.play(Write(question_mark))
        self.wait()
        self.play(Uncreate(arrow), Uncreate(text), Uncreate(question_mark))
        self.play(heap.tree.animate.shift(SHIFT_RIGHT_UNIT * RIGHT), heap.table.first_line.animate.shift(SHIFT_RIGHT_UNIT * RIGHT))
        self.wait()
        # Building the heap
        self.build_heap(heap, is_min_heap=True)

        self.play(Uncreate(double_box))








