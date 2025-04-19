from manim import *

class ConsecutiveOddSquares(Scene):
    def construct(self):
        background = Rectangle(width=14, height=8, fill_color=DARK_GRAY, fill_opacity=1).to_edge(LEFT, buff=0)
        self.add(background)

        title = Tex("Solving a Quadratic Equation").scale(1.2).to_edge(UP, buff=0.5).set_color(YELLOW)
        self.play(Write(title))
        self.wait(1)


        problem = MathTex("x^2 + (x+2)^2 = 394").scale(1.1).set_color(BLUE).next_to(title, DOWN, buff=1)
        self.play(Write(problem))
        self.wait(1)


        expand = MathTex("x^2 + x^2 + 4x + 4 = 394").scale(1).set_color(GREEN).next_to(problem, DOWN, buff=1)
        self.play(TransformMatchingTex(problem.copy(), expand))
        self.wait(1)


        simplify = MathTex("2x^2 + 4x - 390 = 0").scale(1).set_color(GOLD).next_to(expand, DOWN, buff=1)
        self.play(TransformMatchingTex(expand.copy(), simplify))
        self.wait(1)


        divide = MathTex("x^2 + 2x - 195 = 0").scale(1).set_color(PURPLE).next_to(simplify, DOWN, buff=1)
        self.play(TransformMatchingTex(simplify.copy(), divide))
        self.wait(1)


        factoring = MathTex("(x-13)(x+15) = 0").scale(1).set_color(TEAL).next_to(divide, DOWN, buff=1)
        self.play(TransformMatchingTex(divide.copy(), factoring))
        self.wait(1)


        solutions = MathTex("x = 13, x = -15").scale(1).set_color(RED).next_to(factoring, DOWN, buff=1)
        self.play(Write(solutions))
        self.wait(1)


        odd_numbers = MathTex("13, 15 \\text{ or } -15, -13").scale(1).set_color(PINK).next_to(solutions, DOWN, buff=1)
        self.play(Write(odd_numbers))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(problem), FadeOut(expand), FadeOut(simplify), FadeOut(divide), FadeOut(factoring), FadeOut(solutions), FadeOut(odd_numbers), FadeOut(background))