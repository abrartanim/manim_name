

from manim import *


SLATE_500 = "#64748b"
PURPLE_600 = "#7c3aed"


class AbrarTanimAnimation(Scene):
    """
    An animation that displays the text 'abrar_tanim' with several effects.
    1. The text is written from left to right.
    2. The text color changes from slate to purple while growing larger.
    3. The text is erased from left to right.
    """
    def construct(self):
        # --- Configuration ---
        text_to_display = "abrar_tanim"
        text_font = "Poppins"
        animation_run_time = 2.5  # Duration in seconds for each major animation
        pause_duration = 0.5      # Duration in seconds for pauses between animations
        final_scale_factor = 1.5 # How much larger the text will get

        # --- Animation Steps ---

        # 1. Create the Text object

        main_text = Text(
            text_to_display,
            font=text_font,
            color=SLATE_500,
            weight=BOLD  # This makes the font thicker
        ).scale(2)

        # 2. Write the text on screen

        self.play(Write(main_text), run_time=animation_run_time)
        self.wait(pause_duration)

        # 3. Change color and scale up for a cinematic effect

        self.play(
            main_text.animate.set_color(PURPLE_600).scale(final_scale_factor),
            run_time=animation_run_time
        )
        self.wait(pause_duration)

        # 4. Erase the text from the screen

        self.play(Unwrite(main_text, reverse=False), run_time=animation_run_time)
        self.wait(pause_duration)
