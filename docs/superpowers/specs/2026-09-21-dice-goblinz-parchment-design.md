# Design Specification: Dice Goblinz 1-Page Parchment Website

## 1. Overview & Goals
Create a responsive, hand-scrawled parchment website for the tabletop indie game **Dice Goblinz** based on `DICE_GOBLIN.md`.
The design's primary focus is **print fidelity**: when printed or exported to PDF via browser native print (Ctrl+P / Cmd+P), the entire rule set, including both tables and flavor text, must fit onto **exactly one US Letter page** (8.5" × 11") in **two columns of text** with rich, aged parchment textures, sepia tones, and hand-drawn tables.

## 2. Constraints & Requirements
1. **Target Page Budget:** Exactly 1 physical page on US Letter (8.5" × 11" portrait), 0 spillover to page 2.
2. **Layout Structure:** Two balanced columns of text below a full-width header banner.
3. **Aesthetic:** Hand-scrawled on aged parchment paper with ink tones, procedural paper grain, organic hand-drawn table borders, and goblin scribbles/doodles.
4. **Color & Print Strategy:** Always full parchment—both on screen and in print. Styles must declare `-webkit-print-color-adjust: exact; print-color-adjust: exact;` so background paper textures, tints, and borders render on paper.
5. **On-Screen Controls:** Strict document only. No buttons, floating toolbars, or UI widgets; user uses native browser print.
6. **Codebase & Tech Stack:** Standalone, zero-dependency `index.html` and `style.css`. No README, no build pipeline.

## 3. Visual & Aesthetic System

### 3.1 Color Palette
* **Parchment Surface:** Layered warm antique gradients:
  * Primary paper body: `#f5eedc` to `#eedebd`
  * Weathered / stained spots: `#e5cca0`, `#ddbf8e`
  * Scorched / aged edges: `#b88d57` to `#8c5f33`
* **Ink Tones:**
  * Primary ink: `#231509` (deep iron-gall dark brown)
  * Secondary ink / annotations: `#4a2c13`
  * Accents / blood/loot tints: `#8b2616` (subtle dark crimson) and `#a8782a` (burnished gold)
* **Screen Backdrop:** `#15100c` (dark rustic tavern wood / dungeon stone).

### 3.2 Typography
* **Web Fonts (Google Fonts):**
  * Display Header Font: *MedievalSharp* or *Almendra* / *Henny Penny* for goblin flavor.
  * Body & Table Font: *Patrick Hand* (or *Kalam* / *Caveat*) for clear, fast hand-scrawled ink script.
  * Fallbacks: `cursive, "Comic Sans MS", fantasy, sans-serif`.
* **Type Hierarchy (Print Sizing):**
  * Title ($H_1$): ~22pt–24pt (prominent, ragged, centered)
  * Section Headers ($H_2$): ~12pt–13pt (hand-underlined / boxed)
  * Subsection Headers ($H_3$): ~10pt–10.5pt (bold ink scrawl)
  * Body text: ~8.5pt–9pt with ~1.15–1.2 line height
  * Table cells: ~8pt–8.5pt, compact padding (2px 4px)

### 3.3 Parchment Texture & Paper Effects
* Embedded inline SVG filter `<filter id="paper-texture">` with `feTurbulence` (type="fractalNoise", baseFrequency="0.04", numOctaves="4") and `feColorMatrix` overlaying the CSS gradients via `mix-blend-mode`.
* Organic borders: `border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;` applied to cards, tables, and callouts to give an authentic hand-drawn feel.
* Hand-drawn dividers: uneven rough borders simulating rapid ink strokes.

## 4. Content Architecture & Two-Column Layout

```
+--------------------------------------------------------------------------+
|  HEADER BANNER (Full-width)                                              |
|  - DICE GOBLINZ Title (hand-lettered display)                            |
|  - Big Boss Quote & Game Overview (up to 8 goblinz, Pile-O-Die, d8 roll) |
+--------------------------------------------------------------------------+
|  COLUMN 1 (~50% width)                 |  COLUMN 2 (~50% width)          |
|  ------------------------------------- |  ------------------------------ |
|  [H2: Goblinz Classes]                 |  [H2: Da Raid]                  |
|  - Hand-drawn Table: 8 rows            |  - Choosing Roles (Greedy,      |
|    (Robgoblin ... Mobgoblin, dice,     |    Groupie, Coward d6)          |
|    signature abilities)                |  - Wager Raid Die into Area     |
|                                        |                                 |
|  [H2: Hunt for Adventurerzez]          |  [H2: Raid Resolution]          |
|  - Dungeon Raid count (1d4 + goblinz)  |  - Roll countdown & reveal      |
|  - Raid Leader setup rolls:            |  - Cowards removed, Groupies    |
|    1d6 diff, 1d4 exp, 1d10 doohickey   |    minus Greedies vs Target     |
|  - Raid Target calculation formula     |                                 |
|  - Loot pool count                     |  [H2: Loot & Greed Showdown]    |
|                                        |  - Groupie Snake Draft          |
|  [H3: Adventurer Doohickeyz]           |  - Greed vs Group showdown      |
|  - Hand-drawn Table: 6 rows (1d10,     |                                 |
|    Item, Effect)                       |  [H2: Failure & Death]          |
|                                        |  - Half difficulty die lost     |
|                                        |  - Resurrection rule            |
|                                        |                                 |
|                                        |  [Callout: WINNER & NOM NOM!]   |
+--------------------------------------------------------------------------+
```

### 4.1 Column Content Specifications
* **Masthead:**
  * Title: `DICE GOBLINZ`
  * Flavor: Big Boss has sent you into the dungeon to clear out Those Pesky Adventurerzez...
  * Setup requirements: up to 8 goblinz, dice hider, Pile-O-Die.
* **Column 1:**
  * Section: Goblinz (Roll 1d8 to pick class).
  * Table: Columns `[1d8, Class, Starting Dice, Signature Ability]` for:
    1. Robgoblin (4d4) - Sneaky Pocketz
    2. Bobgoblin (3d6) - Dumb Luck
    3. Slobgoblin (2d8, 1d4) - Stench of Greed
    4. Snobgoblin (2d10) - Refined Taste
    5. Hobgoblin (1d12, 1d6) - Bully
    6. Blobgoblin (1d20) - Mitosis
    7. Knobgoblin (1d10, 1d6) - Flip-Flop
    8. Mobgoblin (2d6, 1d4) - Union Bonus
  * Section: Hunt for Adventurerzez.
    * Raids to clear = 1d4 + number of goblinz.
    * Raid Leader rolls 1d6 (difficulty), 1d4 (experience), 1d10 (doohickey).
    * Raid Success Indicator Number Thingie = (Difficulty + Experience) + (Goblinz × 4).
    * Loot pool = Rolled experience + half goblinz (rounded up).
  * Doohickey Table:
    * 1–4: No Loot
    * 5: Tinkerer's Grabby Hand (First pick of Loot regardless of role)
    * 6: Wizard's Broked Wand (+4 to Raid roll)
    * 7: Paladin's Shiny Shield (Keep all die if goblinz win but you lose)
    * 8: Rogue's Skeleton Key (Roll raid die twice and keep either set)
    * 9: Bard's Annoying Kazoo (Force any goblin to reroll a die)
    * 10: Cleric's Sour Water (Revive immediately)
* **Column 2:**
  * Section: Da Raid.
    * Pick Role secretly (d6: 1=Greedy, 2=Groupie, 3=Coward).
    * Commit Raid Die from Pocket into Raid Area.
  * Section: Raid Resolution.
    * Countdown roll and reveal. Remove Coward die.
    * Formula: $\text{Groupie Total} - \text{Greedy Total} \ge \text{Target Number} \implies \text{Success}$.
  * Section: Loot & Greed.
    * No Greedies: Groupie snake draft started by Raid Leader.
    * Greed Showdown: Compare highest Groupie roll vs highest Greedy roll. If Group wins, each Greedy loses 1 Raid Die to Loot. If Greed wins, each Groupie loses 1 Raid Die to Loot, and Greediest takes ALL Loot!
  * Section: Failure & Resurrection.
    * Failure: Lose $\lceil \text{Difficulty} / 2 \rceil$ die (from raid die first).
    * Out of die: Skip next raid, resurrect with starting dice minus 1 (min 1) and kept doohickeyz.
  * Section: Winning.
    * Goblin with most die at end wins. The rest get eaten NOM NOM NOM!

## 5. Print Layout & Media Query Rules

```css
@page {
  size: letter portrait;
  margin: 0.3in;
}

@media print {
  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background: none;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .parchment-page {
    width: 100%;
    max-width: none;
    height: 100%;
    max-height: 10.4in;
    margin: 0;
    padding: 0.25in;
    box-shadow: none;
    border: 2px solid #5c3a1e;
    overflow: hidden;
    page-break-after: avoid;
    break-after: avoid;
  }

  .column-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.25in;
  }

  table, .rule-box {
    break-inside: avoid;
    page-break-inside: avoid;
  }
}
```

## 6. Screen Presentation
* Screen view wraps `.parchment-page` in a viewport centered on a rich dark rustic background (`#18120e`).
* On desktop, the page is rendered as an 8.5" × 11" document sheet (aspect ratio ~1:1.294) with a subtle drop shadow and deckled edge styling.
* On smaller screens / mobile, media queries allow responsive scrolling while maintaining 2-column or stacked layout gracefully.

## 7. Verification & Acceptance Criteria
1. **1-Page Print Verification:**
   * Render `index.html` to PDF using headless Chrome:
     `google-chrome --headless --disable-gpu --print-to-pdf=dice-goblinz-test.pdf index.html`
   * Inspect page count using `pdfinfo` or `pdfimages`/`pdftoppm`: must equal **1 page**.
2. **Content Completeness:**
   * All 8 goblin classes present with exact starting dice and signature abilities.
   * All 6 doohickey entries present.
   * Full setup, raid math, participation, resolution, loot division, failure, resurrection, and win condition accurately represented.
3. **Visual Quality:**
   * Hand-drawn aesthetic for tables and callouts.
   * Legible scrawled typography.
   * Textured parchment appearance with warm sepia tones.
