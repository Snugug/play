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
        open_count = len(re.findall(rf"<{tag}\b[^>]*>", html, re.IGNORECASE))
        close_count = len(re.findall(rf"</{tag}\b[^>]*>", html, re.IGNORECASE))
        assert open_count == close_count, f"Tag mismatch for <{tag}>: {open_count} open vs {close_count} closed"

    # 2. Verify all 8 classes in table
    assert html.count('class="goblin-row"') == 8, "Expected 8 goblin class rows"

    # 3. Verify all 6 doohickey rows (1-4 No Loot + 6 items = 7 rows)
    assert html.count('class="doohickey-row"') == 7, "Expected 7 doohickey rows (1-4 No Loot + 6 items)"

    # 4. Verify print budget constraints
    assert "max-height: 10.4in" in css, "Print height constraint missing"
    assert "overflow: hidden" in css, "Print overflow constraint missing"

    # 5. Cleanliness check: only index.html, style.css, and DICE_GOBLIN.md in repo root
    root_files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
    allowed_root_files = {"index.html", "style.css", "DICE_GOBLIN.md"}
    for rf in root_files:
        assert rf in allowed_root_files, f"Unexpected file in root: {rf}"

    print("ALL END-TO-END VERIFICATION CHECKS PASSED!")

if __name__ == "__main__":
    verify_all()
