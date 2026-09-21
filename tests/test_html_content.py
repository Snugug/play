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
