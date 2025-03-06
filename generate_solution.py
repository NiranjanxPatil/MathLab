from manim import *

class TwoPlusTwo(Scene):
    def construct(self):
        background = Rectangle(width=14, height=8, fill_color=DARK_GRAY, fill_opacity=1).to_edge(LEFT)
        self.add(background)

        two_1 = MathTex("2").set_color(BLUE).scale(3).shift(2*LEFT+2*UP)
        plus = MathTex("+").set_color(YELLOW).scale(3).next_to(two_1, RIGHT)
        two_2 = MathTex("2").set_color(GREEN).scale(3).next_to(plus, RIGHT)
        equals = MathTex("=").set_color(RED).scale(3).next_to(two_2, RIGHT)
        question_mark = MathTex("?").set_color(WHITE).scale(3).next_to(equals, RIGHT)

        self.play(Write(two_1), run_time=1)
        self.play(Write(plus), run_time=1)
        self.play(Write(two_2), run_time=1)
        self.play(Write(equals), run_time=1)
        self.play(Write(question_mark), run_time=1)

        circle_1 = Circle(radius=0.5, color=BLUE).move_to(two_1)
        circle_2 = Circle(radius=0.5, color=BLUE).move_to(two_1).shift(RIGHT)

        circle_3 = Circle(radius=0.5, color=GREEN).move_to(two_2)
        circle_4 = Circle(radius=0.5, color=GREEN).move_to(two_2).shift(RIGHT)


        self.play(Create(circle_1),Create(circle_2),Create(circle_3),Create(circle_4))
        self.play(circle_1.animate.shift(4*RIGHT),circle_2.animate.shift(4*RIGHT),circle_3.animate.shift(3.8*RIGHT),circle_4.animate.shift(3.8*RIGHT))

        self.play(Transform(question_mark, MathTex("4").set_color(GOLD).scale(3)))

        self.wait(1)

        four_dots = VGroup(Dot(color=GOLD),Dot(color=GOLD),Dot(color=GOLD),Dot(color=GOLD)).arrange_submobjects(RIGHT, buff=0.5).next_to(equals,RIGHT)
        self.play(ReplacementTransform(four_dots,MathTex("4").set_color(GOLD).scale(3).next_to(equals,RIGHT)))

        self.wait(2)