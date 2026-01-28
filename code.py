from manim import *


class Demo(Scene):

    def construct(self):
        ax = Axes(x_range=(-3,3), y_range=(-3,3))

        pow_value = 1
        curve = ax.plot(lambda x: x**pow_value, color=RED)
        text = MathTex(f"f(x) = x^{{{pow_value}}}").to_edge(UL)
        self.add(ax, curve, text)
        self.wait(1)
        
        for i in range(1,10):
            new_pow = pow_value + i
            new_curve = ax.plot(lambda x: x**new_pow, color=BLUE)

            new_text = MathTex(f"f(x) = x^{{{new_pow}}}").to_edge(UL)

            self.play(Transform(curve, new_curve))
            self.play(Transform(text, new_text), run_time=0.1)
            self.wait(0.5)
        
        self.wait()