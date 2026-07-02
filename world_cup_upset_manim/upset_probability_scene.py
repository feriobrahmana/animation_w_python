from manimlib import *
from manimlib.utils.color import color_to_rgba


class FivePercentUpset(Scene):
    def construct(self):
        self.camera.frame.set_height(8)
        self.camera.frame.set_width(4.5)
        self.camera.background_color = "#050914"
        self.camera.background_rgba = color_to_rgba("#050914")

        self.bg_color = "#050914"
        self.panel_color = "#091A31"
        self.field_color = "#0B2138"
        self.line_color = "#78B7FF"
        self.team_a_color = "#5EA8FF"
        self.team_b_color = "#39F2E0"
        self.muted_color = "#7E95B7"
        self.text_color = "#EDF6FF"
        self.font = "Segoe UI Semibold"

        background = FullScreenRectangle()
        background.set_fill(self.bg_color, opacity=1)
        background.set_stroke(self.bg_color, width=0)
        self.add(background)

        self.show_matchup_intro()
        self.show_probability_question()
        self.show_universe_setup()
        self.show_match_sequence()
        self.show_b_wins()

    def show_matchup_intro(self):
        headline = self.make_text("Estimated win probability", font_size=31, color=self.text_color)
        headline.to_edge(UP, buff=0.42)

        context = self.make_text("Team A has stronger recent form", font_size=20, color=self.muted_color)
        context.next_to(headline, DOWN, buff=0.12)

        team_a = self.make_team_square("TEAM A", self.team_a_color)
        team_b = self.make_team_square("TEAM B", self.team_b_color)
        vs = self.make_text("VS", font_size=26, color=self.muted_color)

        teams = VGroup(team_a, vs, team_b)
        teams.arrange(RIGHT, buff=0.18)
        teams.move_to(UP * 0.65)

        label_a = self.make_text("win probability", font_size=18, color=self.muted_color)
        label_b = self.make_text("win probability", font_size=18, color=self.muted_color)

        odds_a = self.make_text("95%", font_size=58, color=self.team_a_color)
        odds_b = self.make_text("5%", font_size=58, color=self.team_b_color)

        prob_a = VGroup(label_a, odds_a)
        prob_b = VGroup(label_b, odds_b)
        prob_a.arrange(DOWN, buff=0.08)
        prob_b.arrange(DOWN, buff=0.08)
        prob_a.next_to(team_a, DOWN, buff=0.28)
        prob_b.next_to(team_b, DOWN, buff=0.28)

        self.play(FadeIn(headline, shift=DOWN))
        self.play(FadeIn(context, shift=DOWN))
        self.play(FadeIn(team_a, scale=0.9), FadeIn(team_b, scale=0.9), FadeIn(vs))
        self.play(
            FadeIn(prob_a, shift=UP),
            FadeIn(prob_b, shift=UP),
        )
        self.wait(1.1)
        self.play(
            FadeOut(headline),
            FadeOut(context),
            FadeOut(teams),
            FadeOut(prob_a),
            FadeOut(prob_b),
            run_time=0.55,
        )

    def show_probability_question(self):
        number = self.make_text("5%", font_size=92, color=self.team_b_color)
        label = self.make_text("how should we read this?", font_size=24, color=self.text_color)
        label.next_to(number, DOWN, buff=0.15)

        self.play(FadeIn(number, scale=1.2))
        self.play(FadeIn(label, shift=UP))
        self.wait(0.65)
        self.play(FadeOut(number), FadeOut(label), run_time=0.45)

    def show_universe_setup(self):
        title = self.make_text("Repeated-trial view", font_size=33, color=self.text_color)
        title.to_edge(UP, buff=0.48)

        field = self.make_field("A vs B")
        field.set_width(3.25)
        field.move_to(UP * 0.7)

        shadow_fields = VGroup()
        for offset, opacity in [(0.16, 0.26), (0.32, 0.14)]:
            shadow = self.make_field("")
            shadow.set_width(3.25)
            shadow.move_to(field.get_center() + DOWN * offset + RIGHT * offset * 0.28)
            shadow.set_opacity(opacity)
            shadow_fields.add(shadow)

        caption = VGroup(
            self.make_text("same fixture, same assumptions", font_size=21, color=self.line_color),
            self.make_text("many possible outcomes", font_size=24, color=self.text_color),
            self.make_text("low probability is not zero", font_size=22, color=self.team_b_color),
        )
        caption.arrange(DOWN, buff=0.12)
        caption.next_to(field, DOWN, buff=0.42)

        self.play(FadeIn(title, shift=DOWN))
        self.play(FadeIn(shadow_fields), FadeIn(field, scale=0.92))
        self.play(FadeIn(caption, shift=UP))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(field), FadeOut(shadow_fields), FadeOut(caption), run_time=0.55)

    def show_match_sequence(self):
        self.header = self.make_text("100 identical trials", font_size=31, color=self.text_color)
        self.header.to_edge(UP, buff=0.36)

        self.subheader = self.make_text("one possible outcome each", font_size=19, color=self.muted_color)
        self.subheader.next_to(self.header, DOWN, buff=0.08)

        match_numbers = [1, 2, 3, None, 37, 38, None, 64, 65, None, 99, 100]
        self.fields = VGroup()
        self.match_to_field = {}

        for number in match_numbers:
            field = self.make_ellipsis_cell() if number is None else self.make_field(number)
            self.fields.add(field)
            if number is not None:
                self.match_to_field[number] = field

        self.fields.arrange_in_grid(n_rows=6, n_cols=2, buff=0.13)
        self.fields.set_width(3.58)
        self.fields.next_to(self.subheader, DOWN, buff=0.22)

        self.play(FadeIn(self.header, shift=DOWN))
        self.play(FadeIn(self.subheader, shift=DOWN))
        self.play(LaggedStartMap(FadeIn, self.fields, lag_ratio=0.045, run_time=2.7))
        self.wait(0.45)

    def show_b_wins(self):
        b_win_numbers = [2, 37, 64, 99, 100]
        b_fields = VGroup(*[self.match_to_field[number] for number in b_win_numbers])

        new_header = self.make_text("5 out of 100", font_size=37, color=self.team_b_color)
        new_header.to_edge(UP, buff=0.36)
        new_subheader = self.make_text("rare, but possible", font_size=22, color=self.text_color)
        new_subheader.next_to(new_header, DOWN, buff=0.08)

        self.play(Transform(self.header, new_header))
        self.play(Transform(self.subheader, new_subheader))

        markers = VGroup()
        rings = VGroup()
        for field in b_fields:
            marker_bg = Circle(radius=0.18)
            marker_bg.set_fill(self.team_b_color, opacity=1)
            marker_bg.set_stroke(WHITE, width=1.3)

            marker = self.make_text("B", font_size=25, color=self.bg_color)
            marker_group = VGroup(marker_bg, marker)
            marker_group.move_to(field)
            markers.add(marker_group)

            ring = SurroundingRectangle(field, color=self.team_b_color, buff=0.025)
            ring.set_stroke(self.team_b_color, width=2.5)
            rings.add(ring)

        for field, marker, ring in zip(b_fields, markers, rings):
            self.play(
                field.animate.set_fill(self.team_b_color, opacity=0.22),
                ShowCreation(ring),
                FadeIn(marker, scale=1.35),
                run_time=0.36,
            )

        self.play(b_fields.animate.scale(1.04), run_time=0.28)
        self.play(b_fields.animate.scale(1 / 1.04), run_time=0.28)
        self.wait(1.6)

    def make_text(self, text, font_size, color):
        return Text(text, font=self.font, font_size=font_size, color=color)

    def make_team_square(self, label, accent_color):
        square = RoundedRectangle(width=1.55, height=1.55, corner_radius=0.13)
        square.set_fill(self.panel_color, opacity=0.98)
        square.set_stroke(accent_color, width=2.5)

        glow = RoundedRectangle(width=1.68, height=1.68, corner_radius=0.15)
        glow.set_fill(accent_color, opacity=0.08)
        glow.set_stroke(accent_color, width=1.0, opacity=0.35)

        text = self.make_text(label, font_size=22, color=self.text_color)
        text.move_to(square)

        return VGroup(glow, square, text)

    def make_field(self, match_number):
        pitch = RoundedRectangle(width=1.42, height=0.76, corner_radius=0.06)
        pitch.set_fill(self.field_color, opacity=0.9)
        pitch.set_stroke(self.line_color, width=1.15)

        midline = Line(UP * 0.34, DOWN * 0.34)
        midline.set_stroke(self.line_color, width=0.75, opacity=0.75)
        midline.move_to(pitch)

        center = Circle(radius=0.095)
        center.set_stroke(self.line_color, width=0.75, opacity=0.75)
        center.move_to(pitch)

        label_text = f"M{match_number}" if isinstance(match_number, int) else str(match_number)
        label = self.make_text(label_text, font_size=12, color=self.text_color)
        label.move_to(pitch.get_center() + DOWN * 0.25)

        return VGroup(pitch, midline, center, label)

    def make_ellipsis_cell(self):
        dots = self.make_text("...", font_size=46, color=self.muted_color)
        box = RoundedRectangle(width=1.42, height=0.76, corner_radius=0.06)
        box.set_fill(self.panel_color, opacity=0.35)
        box.set_stroke(self.muted_color, width=1, opacity=0.35)
        dots.move_to(box)
        return VGroup(box, dots)
