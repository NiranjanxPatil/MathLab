from manim import *

class TriangleArea(Scene):
    def construct(self):
        background = Rectangle(width=14, height=8, color=BLUE_E, fill_opacity=0.2)
        self.add(background)

        title = Tex("Finding the Area of a Triangle").scale(1.2).to_edge(UP)
        self.play(Write(title))

        triangle = Polygon([-4, -2, 0], [4, -2, 0], [0, 2, 0], color=YELLOW, fill_opacity=0.7)
        base = Line([-4, -2, 0], [4, -2, 0]).set_color(RED)
        height = Line([0, -2, 0], [0, 2, 0]).set_color(GREEN)
        self.play(Create(triangle))
        self.play(Create(base), Create(height))

        base_text = MathTex("b = 8").scale(0.7).next_to(base, DOWN)
        height_text = MathTex("h = 5").scale(0.7).next_to(height, RIGHT)
        self.play(Write(base_text), Write(height_text))

        formula_step1 = MathTex("Area = \\frac{1}{2} \\times base \\times height").scale(0.7)
        formula_step2 = MathTex("Area = \\frac{1}{2} \\times 8 \\times 5").scale(0.7)
        formula_step3 = MathTex("Area = 20").scale(0.7)

        formula_group = VGroup(formula_step1, formula_step2, formula_step3).arrange(DOWN, buff=0.5).move_to(ORIGIN).to_edge(DOWN)

        self.play(Write(formula_step1))
        self.wait(1)
        self.play(TransformMatchingTex(formula_step1, formula_step2))
        self.wait(1)
        self.play(TransformMatchingTex(formula_step2, formula_step3))
        self.wait(1)


        final_answer = MathTex("Area = 20 cm^2").scale(1).to_edge(DOWN)
        self.play(TransformMatchingTex(formula_step3, final_answer))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(triangle), FadeOut(base), FadeOut(height), FadeOut(base_text), FadeOut(height_text),FadeOut(final_answer))
        self.wait()