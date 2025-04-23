from manim import *

class TriangleArea(Scene):
    def construct(self):
        title = Tex("Finding the Area of a Triangle").scale(1.2).to_edge(UP)
        self.play(Write(title))

        rect = Rectangle(width=14, height=8, color=WHITE, fill_opacity=0.1)
        self.add(rect)

        triangle = Polygon([-4, -2, 0], [4, -2, 0], [0, 2, 0], color=BLUE, fill_opacity=0.7)
        self.play(Create(triangle))

        base = Line([-4, -2, 0], [4, -2, 0]).set_color(YELLOW)
        height = Line([0, 2, 0], [0, -2, 0]).set_color(YELLOW)
        base_label = MathTex("8 \\text{ cm}").next_to(base, DOWN)
        height_label = MathTex("5 \\text{ cm}").next_to(height, RIGHT, buff=0.2)


        self.play(Create(base), Create(height), Write(base_label), Write(height_label))

        formula1 = MathTex("Area = \\frac{1}{2} \\times base \\times height").scale(0.7)
        formula2 = MathTex("Area = \\frac{1}{2} \\times 8 \\text{ cm} \\times 5 \\text{ cm}").scale(0.7)
        formula3 = MathTex("Area = 20 \\text{ cm}^2").scale(0.7)

        formula_group = VGroup(formula1, formula2, formula3).arrange(DOWN, buff=0.5).move_to(2*RIGHT+UP)

        self.play(Write(formula1))
        self.wait(1)
        self.play(TransformMatchingTex(formula1, formula2))
        self.wait(1)
        self.play(TransformMatchingTex(formula2, formula3))
        self.wait(2)

        self.play(FadeOut(formula_group), FadeOut(title), FadeOut(triangle), FadeOut(base), FadeOut(height), FadeOut(base_label), FadeOut(height_label))