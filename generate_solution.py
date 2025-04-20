from manim import *

class SquareArea(Scene):
    def construct(self):
        square = Square(side_length=3, color=BLUE)
        square.shift(2*DOWN + 2*LEFT)
        fifteen = MathTex("15").scale(1.5).next_to(square, RIGHT, buff=0.5)
        cm = MathTex("cm").scale(1).next_to(fifteen, DOWN, buff=0.2)
        fifteen_cm = VGroup(fifteen, cm)


        self.play(Create(square), Write(fifteen_cm))
        self.wait(1)

        formula = MathTex("Area = side \\times side").to_edge(UP)
        self.play(Write(formula))
        self.wait(1)

        calculation = MathTex("Area = 15 \\times 15").next_to(formula, DOWN, buff=1)
        self.play(Write(calculation))
        self.wait(1)


        result = MathTex("Area = 225").next_to(calculation, DOWN, buff=1)
        self.play(Write(result))
        self.wait(1)

        cm2 = MathTex("cm^2").next_to(result, RIGHT, buff=0.5)
        self.play(Write(cm2))
        self.wait(1)


        bigger_square = Square(side_length=7.5, color=GREEN).move_to(ORIGIN)
        self.play(Transform(square, bigger_square))
        self.wait(1)

        self.play(FadeOut(fifteen_cm), FadeOut(formula), FadeOut(calculation), FadeOut(result), FadeOut(cm2))

        final_result = MathTex("Area = 225 cm^2").scale(2).to_edge(DOWN)
        self.play(Write(final_result))
        self.wait(2)