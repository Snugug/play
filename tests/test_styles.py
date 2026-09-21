import os
import re

def test_styles():
    css_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
    assert os.path.exists(css_path), "style.css must exist"

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Check fonts
    assert "MedievalSharp" in css or "Almendra" in css, "Display font missing in CSS"
    assert "Patrick Hand" in css or "Kalam" in css or "Caveat" in css, "Handwriting font missing in CSS"

    # 2. Check parchment colors
    assert "--parchment" in css, "Parchment CSS variable missing"
    assert "--ink" in css, "Ink CSS variable missing"

    # 3. Check hand-drawn border styling
    assert "255px 15px 225px 15px" in css, "Organic hand-drawn border-radius missing"

    # 4. Check hand-drawn tables styling
    assert ".hand-drawn-table" in css, "hand-drawn-table styling missing"

    # 5. Check screen styling
    assert ".parchment-sheet" in css, "parchment-sheet styling missing"

    # 6. Check callouts and rule cards
    assert ".rule-card" in css, "rule-card styling missing"
    assert ".nom-callout" in css, "nom-callout styling missing"

    print("ALL BASIC STYLE TESTS PASSED!")

if __name__ == "__main__":
    test_styles()
