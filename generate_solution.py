from manim import *

class CylinderVolume(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-6,6,1], y_range=[-6,6,1], axis_config={"include_numbers":True})
        self.add(plane)
        cylinder = Cylinder(radius=5, height=15, fill_opacity=0.5, fill_color=BLUE)
        cylinder.shift(2*DOWN)
        self.play(Create(cylinder))
        diameter_text = Tex("Diameter = 10 m").next_to(cylinder, UP)
        height_text = Tex("Height = 15 m").next_to(cylinder, RIGHT)
        self.play(Write(diameter_text), Write(height_text))
        radius = DecimalNumber(5, num_decimal_places=2, include_sign=False).next_to(cylinder, LEFT+UP)
        radius.add_updater(lambda x: x.set_value(cylinder.radius))
        height = DecimalNumber(15, num_decimal_places=2, include_sign=False).next_to(cylinder, RIGHT+UP)
        height.add_updater(lambda x: x.set_value(cylinder.height))

        self.play(Write(radius), Write(height))
        pi = MathTex(r"\pi").scale(1.5).next_to(radius, LEFT)
        self.play(Write(pi))
        formula = MathTex(r"V = \pi r^2 h").scale(1.5).to_edge(UP)
        self.play(Write(formula))
        r_squared = MathTex(r"r^2 = 5^2 = 25").next_to(formula, DOWN)
        self.play(Write(r_squared))
        volume_calc = MathTex(r"V = \pi \times 25 \times 15").next_to(r_squared, DOWN)
        self.play(Write(volume_calc))
        approx_volume = MathTex(r"V \approx 1178.1").next_to(volume_calc, DOWN)
        self.play(Write(approx_volume))
        final_answer = Tex("Volume $\\approx$ 1178.1 m$^3$").to_edge(DOWN)
        self.play(Write(final_answer))
        self.wait(1)

        self.play(FadeOut(cylinder), FadeOut(diameter_text), FadeOut(height_text), FadeOut(radius), FadeOut(height), FadeOut(pi), FadeOut(formula), FadeOut(r_squared), FadeOut(volume_calc), FadeOut(approx_volume), FadeOut(final_answer))
        self.wait(1)