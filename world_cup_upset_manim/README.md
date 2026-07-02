# World Cup 5% Upset ManimGL Scene

This is a 3Blue1Brown ManimGL scene for explaining that a 5% upset chance is not "basically impossible".

The animation uses a blue/black vertical short-form layout. It introduces Team A vs Team B with minimal wording, then shows large repeated match fields with ellipses for the skipped middle. Five scattered fields are filled as Team B wins to make the 5% concrete.

## Render

Install 3b1b ManimGL:

```powershell
pip install manimgl
```

Render the scene:

```powershell
manimgl upset_probability_scene.py FivePercentUpset -w
```

Render vertical 9:16 for TikTok/Reels/Shorts:

```powershell
manimgl upset_probability_scene.py FivePercentUpset -w -r 1080x1920 --file_name FivePercentUpset_TikTok
```

Preview interactively:

```powershell
manimgl upset_probability_scene.py FivePercentUpset
```

## Notes

- This uses `from manimlib import *`, which matches the 3b1b ManimGL package.
- The scene uses regular text objects and no LaTeX formulas, so it should be easier to render on Windows.
