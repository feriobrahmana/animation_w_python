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
        self.gold_color = "#FFD166"
        self.warning_color = "#FF6B6B"
        self.muted_color = "#7E95B7"
        self.text_color = "#CFEAFF"
        self.font = "Segoe UI Semibold"

        background = FullScreenRectangle()
        background.set_fill(self.bg_color, opacity=1)
        background.set_stroke(self.bg_color, width=0)
        self.add(background)

        self.show_imagine_intro()
        self.show_probability_meaning()
        self.show_parallel_universes()
        self.show_match_sequence()
        self.show_outcomes()

    def show_imagine_intro(self):
        title = self.make_phrase([
            ("Imagine", self.gold_color, 36),
            ("two teams", self.line_color, 36),
        ], direction=DOWN, buff=0.05)
        title.to_edge(UP, buff=0.42)

        subtitle = self.make_text("same match, very different odds", 21, self.muted_color)
        subtitle.next_to(title, DOWN, buff=0.18)

        team_a = self.make_team_square("TEAM A", self.team_a_color)
        team_b = self.make_team_square("TEAM B", self.team_b_color)
        vs = self.make_text("VS", 25, self.gold_color)

        teams = VGroup(team_a, vs, team_b)
        teams.arrange(RIGHT, buff=0.18)
        teams.move_to(UP * 0.62)

        prob_a = self.make_probability_block("win probability", "95%", self.team_a_color)
        prob_b = self.make_probability_block("win probability", "5%", self.team_b_color)
        prob_a.next_to(team_a, DOWN, buff=0.26)
        prob_b.next_to(team_b, DOWN, buff=0.26)

        self.play(FadeIn(title, shift=DOWN))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.play(FadeIn(team_a, scale=0.9), FadeIn(team_b, scale=0.9), FadeIn(vs))
        self.play(FadeIn(prob_a, shift=UP), FadeIn(prob_b, shift=UP))
        self.wait(1.0)
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(teams),
            FadeOut(prob_a),
            FadeOut(prob_b),
            run_time=0.55,
        )

    def show_probability_meaning(self):
        top = self.make_phrase([
            ("Team B:", self.team_b_color, 34),
            ("5%", self.gold_color, 64),
        ], direction=DOWN, buff=0.08)
        top.to_edge(UP, buff=0.62)

        not_loss = self.make_phrase([
            ("not", self.warning_color, 34),
            ("guaranteed loss", self.line_color, 34),
        ], direction=DOWN, buff=0.06)
        not_loss.move_to(ORIGIN + DOWN * 0.15)

        meaning = self.make_text("it is a low-probability outcome", 23, self.muted_color)
        meaning.next_to(not_loss, DOWN, buff=0.42)

        self.play(FadeIn(top, shift=DOWN))
        self.play(FadeIn(not_loss, scale=0.95))
        self.play(FadeIn(meaning, shift=UP))
        self.wait(1.0)
        self.play(FadeOut(top), FadeOut(not_loss), FadeOut(meaning), run_time=0.5)

    def show_parallel_universes(self):
        title = self.make_phrase([
            ("Think in", self.muted_color, 30),
            ("parallel universes", self.team_b_color, 33),
        ], direction=DOWN, buff=0.04)
        title.to_edge(UP, buff=0.42)

        universes = VGroup()
        offsets = [
            LEFT * 0.42 + UP * 0.68,
            LEFT * 0.24 + UP * 0.38,
            LEFT * 0.06 + UP * 0.08,
            RIGHT * 0.12 + DOWN * 0.22,
            RIGHT * 0.30 + DOWN * 0.52,
        ]
        for index, offset in enumerate(offsets):
            label = "A vs B" if index == len(offsets) - 1 else ""
            field = self.make_field(label, match_label=None, width=2.55)
            field.move_to(offset)
            field.set_opacity(0.34 + 0.13 * index)
            universes.add(field)

        caption = self.make_phrase([
            ("same teams", self.line_color, 23),
            ("different possible outcomes", self.gold_color, 23),
        ], direction=DOWN, buff=0.08)
        caption.move_to(DOWN * 2.66)

        self.play(FadeIn(title, shift=DOWN))
        self.play(LaggedStartMap(FadeIn, universes, lag_ratio=0.10, run_time=1.7))
        self.play(FadeIn(caption, shift=UP))
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(universes), FadeOut(caption), run_time=0.55)

    def show_match_sequence(self):
        self.header = self.make_phrase([
            ("100", self.gold_color, 36),
            ("possible matches", self.line_color, 30),
        ], direction=DOWN, buff=0.0)
        self.header.to_edge(UP, buff=0.34)

        self.subheader = self.make_text("each field is Team A vs Team B", 18, self.muted_color)
        self.subheader.next_to(self.header, DOWN, buff=0.10)

        match_numbers = [1, 2, 3, None, 37, 38, None, 64, 65, None, 99, 100]
        self.fields = VGroup()
        self.match_to_field = {}

        for number in match_numbers:
            field = self.make_ellipsis_cell() if number is None else self.make_field("A vs B", match_label=f"M{number}")
            self.fields.add(field)
            if number is not None:
                self.match_to_field[number] = field

        self.fields.arrange_in_grid(n_rows=6, n_cols=2, buff=0.12)
        self.fields.set_width(3.58)
        self.fields.next_to(self.subheader, DOWN, buff=0.18)

        self.play(FadeIn(self.header, shift=DOWN))
        self.play(FadeIn(self.subheader, shift=DOWN))
        self.play(LaggedStartMap(FadeIn, self.fields, lag_ratio=0.045, run_time=2.5))
        self.wait(0.45)

    def show_outcomes(self):
        b_win_numbers = [2, 37, 64, 99, 100]
        visible_numbers = [1, 2, 3, 37, 38, 64, 65, 99, 100]
        a_win_numbers = [number for number in visible_numbers if number not in b_win_numbers]

        b_fields = VGroup(*[self.match_to_field[number] for number in b_win_numbers])
        a_fields = VGroup(*[self.match_to_field[number] for number in a_win_numbers])

        new_header = self.make_phrase([
            ("5", self.team_b_color, 42),
            ("out of 100", self.gold_color, 34),
        ], direction=RIGHT, buff=0.14)
        new_header.to_edge(UP, buff=0.36)
        new_subheader = self.make_text("B wins in five possible outcomes", 19, self.line_color)
        new_subheader.next_to(new_header, DOWN, buff=0.08)

        self.play(Transform(self.header, new_header))
        self.play(Transform(self.subheader, new_subheader))

        a_markers = VGroup()
        for field in a_fields:
            marker = self.make_winner_marker("A", self.team_a_color)
            marker.move_to(field)
            a_markers.add(marker)

        self.play(
            a_fields.animate.set_fill(self.team_a_color, opacity=0.12),
            LaggedStartMap(FadeIn, a_markers, lag_ratio=0.08, run_time=0.7),
        )

        b_markers = VGroup()
        rings = VGroup()
        for field in b_fields:
            marker = self.make_winner_marker("B", self.team_b_color)
            marker.move_to(field)
            b_markers.add(marker)

            ring = SurroundingRectangle(field, color=self.team_b_color, buff=0.025)
            ring.set_stroke(self.team_b_color, width=2.6)
            rings.add(ring)

        for field, marker, ring in zip(b_fields, b_markers, rings):
            self.play(
                field.animate.set_fill(self.team_b_color, opacity=0.24),
                ShowCreation(ring),
                FadeIn(marker, scale=1.25),
                run_time=0.32,
            )

        final_subheader = self.make_text("5% is rare, not impossible", 21, self.gold_color)
        final_subheader.next_to(self.header, DOWN, buff=0.10)
        self.play(Transform(self.subheader, final_subheader))
        self.wait(1.4)

    def make_text(self, text, font_size, color):
        mob = Text(text, font=self.font, font_size=font_size)
        mob.set_color(color)
        return mob

    def make_phrase(self, parts, direction=RIGHT, buff=0.1):
        phrase = VGroup(*[self.make_text(text, size, color) for text, color, size in parts])
        phrase.arrange(direction, buff=buff)
        return phrase

    def make_probability_block(self, label, value, color):
        label_mob = self.make_text(label, 17, self.muted_color)
        value_mob = self.make_text(value, 57, color)
        block = VGroup(label_mob, value_mob)
        block.arrange(DOWN, buff=0.05)
        return block

    def make_team_square(self, label, accent_color):
        square = RoundedRectangle(width=1.5, height=1.5, corner_radius=0.12)
        square.set_fill(self.panel_color, opacity=0.98)
        square.set_stroke(accent_color, width=2.6)

        glow = RoundedRectangle(width=1.64, height=1.64, corner_radius=0.14)
        glow.set_fill(accent_color, opacity=0.09)
        glow.set_stroke(accent_color, width=1.0, opacity=0.38)

        text = self.make_text(label, 21, accent_color)
        text.move_to(square)

        return VGroup(glow, square, text)

    def make_field(self, center_label, match_label=None, width=1.42):
        pitch = RoundedRectangle(width=1.42, height=0.76, corner_radius=0.06)
        pitch.set_fill(self.field_color, opacity=0.9)
        pitch.set_stroke(self.line_color, width=1.15)

        midline = Line(UP * 0.34, DOWN * 0.34)
        midline.set_stroke(self.line_color, width=0.75, opacity=0.75)
        midline.move_to(pitch)

        center = Circle(radius=0.095)
        center.set_stroke(self.line_color, width=0.75, opacity=0.75)
        center.move_to(pitch)

        center_text = self.make_text(center_label, 10, self.text_color)
        center_text.move_to(pitch.get_center() + UP * 0.20)

        field = VGroup(pitch, midline, center, center_text)

        if match_label is not None:
            label = self.make_text(match_label, 11, self.gold_color)
            label.move_to(pitch.get_center() + DOWN * 0.25)
            field.add(label)

        field.set_width(width)
        return field

    def make_winner_marker(self, label, color):
        marker_bg = Circle(radius=0.17)
        marker_bg.set_fill(color, opacity=1)
        marker_bg.set_stroke(self.gold_color, width=1.0)
        marker = self.make_text(label, 23, self.bg_color)
        return VGroup(marker_bg, marker)

    def make_ellipsis_cell(self):
        dots = self.make_text("...", 42, self.muted_color)
        box = RoundedRectangle(width=1.42, height=0.76, corner_radius=0.06)
        box.set_fill(self.panel_color, opacity=0.35)
        box.set_stroke(self.muted_color, width=1, opacity=0.35)
        dots.move_to(box)
        return VGroup(box, dots)
