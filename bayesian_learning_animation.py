# %%
from manim import *
from manim_presentation import Slide

# %%
FS = 20
class BayesianLearningIntro(Slide):
    def construct(self):

        model_def = MathTex("lambda \\quad \\theta: random.choices([\"cara\", \"cruz\"]],[\\theta, 1-\\theta])",
                            substrings_to_isolate=["\\theta", "lambda"])
        model_def.set_color_by_tex("\\theta", YELLOW)
        model_def.set_color_by_tex("lambda", BLUE)
        self.play(GrowFromCenter(model_def))
        self.pause()
        self.play(FadeOut(model_def))
        self.pause()


        prior = SampleSpace(stroke_width=2, height=4, width=1, fill_color=GREEN,
                            fill_opacity=1.0, stroke_color=WHITE)
        prior.move_to(LEFT * 3)
        prior.divide_horizontally([0.8, 0.2], colors=[GREEN, RED])
        self.play(GrowFromCenter(prior))
        self.pause()

        b, l = prior.get_side_braces_and_labels([Tex('$P(\\theta=0.5)=0.8$', font_size=FS),
                                                 Tex('$P(\\theta=0.9)=0.2$', font_size=FS)])
        self.play(FadeIn(b), FadeIn(l))
        self.pause()

        complete = SampleSpace(stroke_width=2, height=4, width=4,
                               fill_color=GREEN, fill_opacity=1.0, stroke_color=WHITE)
        complete.move_to(LEFT * 3)
        complete.divide_horizontally([0.8, 0.2], colors=[GREEN, RED])
        parts = complete.horizontal_parts
        parts[0].divide_vertically([0.5**3, 1-0.5 ** 3], colors=[GREEN, YELLOW])
        parts[1].divide_vertically([0.9 ** 3, 1 - 0.9 ** 3], colors=[RED, ORANGE])

        b_c, l_c = complete.get_side_braces_and_labels([Tex('$P(\\theta=0.5)$', font_size=FS),
                                                        Tex('$P(\\theta=0.9)$', font_size=FS)])
        b_o, l_o = parts[1].get_bottom_braces_and_labels([Tex('$P(c = 3)$', font_size=FS),
                                                          Tex('$P(c \\neq 3)$', font_size=FS)])

        self.play(Transform(prior, complete),
                  Transform(b, b_c),
                  Transform(l, l_c),
                  FadeIn(b_o),
                  FadeIn(l_o))

        self.pause()


        c_new = complete.copy()
        posterior = VGroup(
            Tex('$P(\\theta=0.5 | c = 3) = $', font_size=FS*4),
            VGroup(
                c_new.horizontal_parts[0].vertical_parts[0].copy(),
                Tex("/(", font_size=FS*4),
                c_new.horizontal_parts[0].vertical_parts[0].copy(),
                Tex("+", font_size=FS*4),
                c_new.horizontal_parts[1].vertical_parts[0].copy(),
                Tex(") = ", font_size=FS*4)
            ).arrange(RIGHT)
        ).arrange(DOWN)

        prior = VGroup(Tex("* $P(\\theta=0.5)$", font_size=FS*4),
                       VGroup(
                       Tex("*", font_size=FS * 4),
                       c_new.horizontal_parts[0].copy())\
            .arrange(RIGHT))\
            .arrange(DOWN)\

        likelihood = VGroup(
            Tex('$P(c = 3 | \\theta=0.5 )$', font_size=FS*4),
            VGroup(
                Tex("(", font_size=FS * 4),
                c_new.horizontal_parts[0].vertical_parts[0].copy(),
                Tex("/", font_size=FS*4),
                c_new.horizontal_parts[0],
                Tex(")", font_size=FS * 4)
            ).arrange(RIGHT)
        ).arrange(DOWN)

        evidence_marginal = VGroup(
            Tex('/ $P(c = 3)$', font_size=FS*4),
            VGroup(
                Tex("/(", font_size=FS * 4),
                c_new.horizontal_parts[0].vertical_parts[0].copy(),
                Tex("+", font_size=FS * 4),
                c_new.horizontal_parts[1].vertical_parts[0].copy(),
                Tex("); ", font_size=FS * 4)
            ).arrange(RIGHT)
        ).arrange(DOWN)

        self.play(
            posterior.animate().scale(0.25).move_to(1 * RIGHT),
        )
        self.pause()
        self.play(likelihood.animate().scale(0.25).move_to(2.8 * RIGHT))
        self.pause()
        self.play(prior.animate().scale(0.25).move_to(4.2 * RIGHT))
        self.pause()
        self.play(evidence_marginal.animate().scale(0.25).move_to(5.8 * RIGHT))
        self.pause()

        final_count = VGroup(
            Tex("likelihood: $P(c=3|\\theta=0.5) = 0.5^{3}$", font_size=FS),
            Tex("prior: $P(\\theta=0.5) = 0.8$", font_size=FS),
            Tex("marginal likelihood: $P(c=3) = 0.5^{3} * 0.8 + 0.9^{3} * 0.2$", font_size=FS),
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        final_count.move_to(DOWN * 1.5 + RIGHT * 3)

        for c in final_count:
            self.play(FadeIn(c), time=0.5)
            self.pause()


