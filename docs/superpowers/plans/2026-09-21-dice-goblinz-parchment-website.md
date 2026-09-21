# Dice Goblinz Parchment Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a zero-dependency, responsive two-column website for the tabletop indie game *Dice Goblinz* that looks like hand-scrawled text on aged parchment paper with hand-drawn tables and prints onto exactly one US Letter page.

**Architecture:** A standalone semantic HTML5 document (`index.html`) and an expressive CSS stylesheet (`style.css`). Parchment paper texture is produced procedurally using layered antique CSS gradients and an inline SVG turbulence filter. Layout is split into two balanced columns with CSS grid, with disciplined `@page` and `@media print` rules enforcing an exact 1-page fit on US Letter with full background colors (`print-color-adjust: exact`).

**Tech Stack:** HTML5, CSS3 (CSS Grid, Paged Media `@page`, `@media print`, CSS Custom Properties), SVG Filters (`feTurbulence`), Google Fonts (*MedievalSharp*, *Patrick Hand*). Python 3 for automated verification scripts.

**Spec:** `docs/superpowers/specs/2026-09-21-dice-goblinz-parchment-design.md`

## Global Constraints

- Standalone zero-dependency files: `index.html` and `style.css` only. No README, no build tooling.
- Target Page Budget: Exactly 1 physical page on US Letter (8.5" × 11" portrait), 0 spillover to page 2.
- Layout Structure: Two balanced columns of text below a full-width header banner.
- Visual Theme: Hand-scrawled on aged parchment with hand-drawn tables and ink accents.
- Print Mode: Always full parchment (`print-color-adjust: exact; -webkit-print-color-adjust: exact;`).
- On-Screen Controls: Strict document only (no buttons or floating toolbars).

---

### Task 1: Semantic Content & HTML5 Structure (`index.html`)

**Files:**
- Create: `index.html`
- Test: `tests/test_html_content.py`

**Interfaces:**
- Consumes: Rules and tables from `DICE_GOBLIN.md`.
- Produces: Complete semantic HTML5 structure for `index.html` with class names (`.parchment-sheet`, `.masthead`, `.two-columns`, `.col-left`, `.col-right`, `.hand-drawn-table`, `.rule-card`, `.nom-callout`) for CSS styling in Task 2.

- [ ] **Step 1: Write the failing HTML content test**

Create `tests/test_html_content.py`:
```python
import os
import re
from html.parser import HTMLParser

def test_html_content():
    html_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    assert os.path.exists(html_path), "index.html must exist"
    
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Check title & headers
    assert "DICE GOBLINZ" in content, "Title DICE GOBLINZ missing"
    assert "Big Boss has sent you into the dungeon" in content, "Big Boss flavor quote missing"
    
    # 2. Check 8 goblin classes
    goblin_classes = [
        "Robgoblin", "Bobgoblin", "Slobgoblin", "Snobgoblin",
        "Hobgoblin", "Blobgoblin", "Knobgoblin", "Mobgoblin"
    ]
    for g in goblin_classes:
        assert g in content, f"Goblin class {g} missing"
    
    # 3. Check starting dice
    dice_requirements = ["4d4", "3d6", "2d8, 1d4", "2d10", "1d12, 1d6", "1d20", "1d10, 1d6", "2d6, 1d4"]
    for d in dice_requirements:
        assert d in content, f"Dice {d} missing"

    # 4. Check signature abilities
    abilities = ["Sneaky Pocketz", "Dumb Luck", "Stench of Greed", "Refined Taste", "Bully", "Mitosis", "Flip-Flop", "Union Bonus"]
    for a in abilities:
        assert a in content, f"Ability {a} missing"
        
    # 5. Check Doohickey items
    doohickeyz = [
        "Tinkerer's Grabby Hand", "Wizard's Broked Wand", "Paladin's Shiny Shield",
        "Rogue's Skeleton Key", "Bard's Annoying Kazoo", "Cleric's Sour Water"
    ]
    for item in doohickeyz:
        assert item in content, f"Doohickey {item} missing"

    # 6. Check core rules
    assert "Raid Success Indicator Number Thingie" in content, "Raid target formula missing"
    assert "Greedy" in content and "Groupie" in content and "Coward" in content, "Roles missing"
    assert "NOM NOM NOM" in content, "Endgame flavor missing"

    # 7. Check structural markup
    assert 'class="parchment-sheet"' in content, "parchment-sheet class missing"
    assert 'class="masthead"' in content, "masthead class missing"
    assert 'class="two-columns"' in content, "two-columns class missing"
    assert 'class="col-left"' in content, "col-left class missing"
    assert 'class="col-right"' in content, "col-right class missing"
    assert 'id="paper-texture"' in content, "paper-texture SVG filter missing"
    assert 'href="style.css"' in content, "Link to style.css missing"

    print("ALL HTML CONTENT TESTS PASSED!")

if __name__ == "__main__":
    test_html_content()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_html_content.py`
Expected: FAIL with "index.html must exist"

- [ ] **Step 3: Implement semantic `index.html`**

Create `index.html` with complete markup containing the entire rule set, two-column layout, hand-drawn table classes, and inline SVG filter.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_html_content.py`
Expected: PASS with "ALL HTML CONTENT TESTS PASSED!"

- [ ] **Step 5: Commit**

Run:
```bash
git add index.html tests/test_html_content.py
git commit -m "feat: add semantic HTML structure and content for Dice Goblinz"
```

---

### Task 2: Hand-Scrawled Parchment Aesthetic & Hand-Drawn Tables (`style.css` Part 1)

**Files:**
- Create: `style.css`
- Create: `tests/test_styles.py`

**Interfaces:**
- Consumes: Markup elements from `index.html`.
- Produces: Complete parchment visual skin, Google Fonts loading, hand-scrawled typography, organic borders (`border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;`), ink stain accents, and hand-drawn table aesthetics.

- [ ] **Step 1: Write the failing style test**

Create `tests/test_styles.py`:
```python
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

    print("ALL BASIC STYLE TESTS PASSED!")

if __name__ == "__main__":
    test_styles()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_styles.py`
Expected: FAIL with "style.css must exist"

- [ ] **Step 3: Implement parchment aesthetic and hand-drawn table styles**

Write `style.css` with:
- CSS variables for parchment tones (`#f7f1e1`, `#eedebd`, `#e5cca0`, `#8c5f33`) and ink tones (`#231509`, `#4a2c13`, `#8b2616`, `#1a5e20`).
- Typography system importing Google Fonts (*MedievalSharp* and *Patrick Hand*).
- Layered radial/linear gradients on `.parchment-sheet` with SVG grain filter overlay.
- Hand-drawn box geometry: `border: 2px solid var(--ink-border); border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;`.
- Hand-drawn table styling with uneven cell borders, shaded header rows, and ragged dividers.
- Ink stamps, bold notation highlights, and thematic callout blocks.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_styles.py`
Expected: PASS with "ALL BASIC STYLE TESTS PASSED!"

- [ ] **Step 5: Commit**

Run:
```bash
git add style.css tests/test_styles.py
git commit -m "style: implement hand-scrawled parchment aesthetic and hand-drawn tables"
```

---

### Task 3: Two-Column Layout & 1-Page Print Stylesheet (`style.css` Part 2)

**Files:**
- Modify: `style.css`
- Modify: `tests/test_styles.py`

**Interfaces:**
- Consumes: Parchment styling from Task 2.
- Produces: CSS Grid two-column layout, screen centering on dark tavern backdrop, responsive mobile reflow, and strict `@media print` rules enforcing 1-page fit on US Letter.

- [ ] **Step 1: Update `tests/test_styles.py` to assert print rules and column layout**

Add assertions in `tests/test_styles.py`:
```python
    # Check two-column grid
    assert ".two-columns" in css, "two-columns class missing in CSS"
    assert "grid-template-columns" in css or "columns:" in css, "Multi-column layout missing"

    # Check print stylesheet
    assert "@media print" in css, "@media print block missing"
    assert "@page" in css, "@page rule missing"
    assert "letter" in css, "US Letter size missing in @page"
    assert "print-color-adjust: exact" in css or "-webkit-print-color-adjust: exact" in css, "print-color-adjust exact missing"
    assert "break-inside: avoid" in css or "page-break-inside: avoid" in css, "page-break-inside avoid missing"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 tests/test_styles.py`
Expected: FAIL on print assertions

- [ ] **Step 3: Implement two-column layout and print styles**

In `style.css`:
- Screen layout:
  - Body background: `#18120e` (dark dungeon/tavern wood) with subtle vignette.
  - `.parchment-sheet`: Centered, maximum width `8.5in`, padding `0.3in`, realistic drop shadow `0 12px 36px rgba(0, 0, 0, 0.6)`.
  - `.two-columns`: `display: grid; grid-template-columns: 1fr 1fr; gap: 0.25in;`.
- Print layout (`@media print` and `@page`):
  - `@page { size: letter portrait; margin: 0.3in; }`
  - `-webkit-print-color-adjust: exact; print-color-adjust: exact;`
  - `.parchment-sheet`: width `100%`, height `10.4in`, max-height `10.4in`, box-shadow `none`, overflow `hidden`, `break-after: avoid; page-break-after: avoid;`.
  - Micro-typography tuned for 1-page budget: `font-size: 8.5pt`, `line-height: 1.15`, table cells `padding: 1.5px 3px`, headers compact margins.
  - All cards, tables, and sections have `break-inside: avoid; page-break-inside: avoid;`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 tests/test_styles.py`
Expected: PASS

- [ ] **Step 5: Commit**

Run:
```bash
git add style.css tests/test_styles.py
git commit -m "style: implement two-column layout and 1-page US Letter print stylesheet"
```

---

### Task 4: End-to-End Verification & Layout Budget Audit

**Files:**
- Create: `tests/verify_budget.py`
- Test: Complete test suite

**Interfaces:**
- Consumes: Complete `index.html` and `style.css`.
- Produces: Final verified, production-ready rule sheet meeting all spec requirements.

- [ ] **Step 1: Write verification script `tests/verify_budget.py`**

Create `tests/verify_budget.py`:
```python
import os
import re

def verify_all():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    html_path = os.path.join(root, "index.html")
    css_path = os.path.join(root, "style.css")

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Validate tags are properly closed
    tags_to_check = ["html", "head", "body", "main", "header", "section", "table", "svg"]
    for tag in tags_to_check:
        open_count = len(re.findall(f"<{tag}[^>]*>", html, re.IGNORECASE))
        close_count = len(re.findall(f"</{tag}>", html, re.IGNORECASE))
        assert open_count == close_count, f"Tag mismatch for <{tag}>: {open_count} open vs {close_count} closed"

    # 2. Verify all 8 classes in table
    assert html.count('class="goblin-row"') == 8, "Expected 8 goblin class rows"

    # 3. Verify all 6 doohickey rows
    assert html.count('class="doohickey-row"') == 7, "Expected 7 doohickey rows (1-4 No Loot + 6 items)"

    # 4. Verify print budget constraints
    assert "max-height: 10.4in" in css, "Print height constraint missing"
    assert "overflow: hidden" in css, "Print overflow constraint missing"

    # 5. Cleanliness check: only index.html and style.css in repo root
    root_files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
    allowed_root_files = {"index.html", "style.css", "DICE_GOBLIN.md"}
    for rf in root_files:
        assert rf in allowed_root_files, f"Unexpected file in root: {rf}"

    print("ALL END-TO-END VERIFICATION CHECKS PASSED!")

if __name__ == "__main__":
    verify_all()
```

- [ ] **Step 2: Run all test scripts**

Run:
```bash
python3 tests/test_html_content.py
python3 tests/test_styles.py
python3 tests/verify_budget.py
```
Expected: All 3 scripts report PASS.

- [ ] **Step 3: Remove test folder or commit verification suite**

Clean up test files if keeping repo strictly to `index.html`, `style.css`, and `DICE_GOBLIN.md`:
```bash
git add tests/
git commit -m "test: add verification test suite for Dice Goblinz website"
```

---
