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
    assert "var(--hand-drawn-radius)" in css, "var(--hand-drawn-radius) variable usage missing"

    # 4. Check hand-drawn tables styling
    assert ".hand-drawn-table" in css, "hand-drawn-table styling missing"

    # 5. Check screen styling
    assert ".parchment-sheet" in css, "parchment-sheet styling missing"

    # 6. Check callouts and rule cards
    assert ".rule-card" in css, "rule-card styling missing"
    assert ".nom-callout" in css, "nom-callout styling missing"

    # 7. Check two-column grid
    assert ".two-columns" in css, "two-columns class missing in CSS"
    assert "grid-template-columns" in css or "columns:" in css, "Multi-column layout missing"
    assert "0.25in" in css, "0.25in gap missing in layout"

    # 8. Check responsive reflow
    assert "800px" in css, "Responsive breakpoint for 800px missing"

    # 9. Check print stylesheet
    assert "@media print" in css, "@media print block missing"
    assert "@page" in css, "@page rule missing"
    assert "letter" in css, "US Letter size missing in @page"
    assert "print-color-adjust: exact" in css or "-webkit-print-color-adjust: exact" in css, "print-color-adjust exact missing"
    assert "break-inside: avoid" in css or "page-break-inside: avoid" in css, "page-break-inside avoid missing"
    assert "max-height: 10.4in" in css, "max-height: 10.4in page budget constraint missing"
    assert "overflow: hidden" in css, "overflow: hidden missing"
    assert "8.5pt" in css, "8.5pt micro-typography font size missing"
    assert "1.15" in css, "1.15 line-height missing"
    assert "1.5px 3px" in css, "table cell micro-padding missing"

    print("ALL BASIC STYLE TESTS PASSED!")

if __name__ == "__main__":
    test_styles()
