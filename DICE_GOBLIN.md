# DICE GOBLIN
*A One-Page TTRPG About Greed, Glory, and Not Getting Eaten*
*Designed for 3 to 6 players | Play time: 25–35 minutes*

---

> ### THE PITCH
> **"Big Boss has sent you into the dungeon to clear out Those Pesky Adventurerzez. Scope the room, ambush the dopes, get big and strong. Big Boss says whoever strongest and cleverererest don’t get eaten!"**

---

## 1. WHAT YOU NEED TO PLAY
* **3 to 6 Players** (You are all Goblins).
* **Two-Sided Tokens** (1 coin or token per player: **Heads = Group**, **Tails = Greed**).
* **A Communal Dice Bag** stuffed with assorted polyhedral dice ($\text{d4, d6, d8, d10, d12, d20}$).
* **Personal Dice**: Each goblin starts with a distinct starter set of polyhedrals based on their class.

> **DICE = GOBLIN EXPERIENCE / MOJO**  
> Dice represent your swagger, stamina, and renown. Gaining dice means leveling up and getting tough. Losing dice means getting bruised and humiliated. **If your dice pool ever reaches 0, you crash out!**

---

## 2. GOBLIN CLASSES (Roll 1d6 or Pick)

| 1d6 | Class | Starting Dice | Archetype | Signature Ability |
| :---: | :--- | :---: | :--- | :--- |
| **1** | **Robgoblin** | **4d4** | *Caltrop Hoarder* | **Sneaky Pocket**: After all dice are rolled, but *before* tokens are revealed, you may roll 1 extra d4 from your hand into your total. |
| **2** | **Bobgoblin** | **3d6** | *Everyday Average* | **Dumb Luck**: Treat any die you rolled that shows a 1 or 2 as a **3**. |
| **3** | **Slobgoblin** | **2d8, 1d4** | *Grime Scavenger* | **Stench of Greed**: If you chose Greed on a successful raid, subtract 1 from all rival Greed totals; you win all Greed ties. |
| **4** | **Snobgoblin** | **2d10** | *Posh Arrogance* | **Refined Taste**: When surrendering a die on a loss, you may surrender a die of your choice from your hand instead of a rolled die. |
| **5** | **Hobgoblin** | **1d12, 1d6** | *Heavy Enforcer* | **Bully**: When you win as top Greed, you steal **2 rolled dice** from the highest Group contributor instead of 1. |
| **6** | **Blobgoblin** | **1d20** | *Unstable Slime* | **Mitosis**: When surrendering a die, you may permanently downgrade your die tier by 1 step ($\text{d20} \rightarrow \text{d12} \rightarrow \text{d10} \rightarrow \text{d6} \rightarrow \text{d4}$) instead of surrendering a die from your hand. |

### Optional: Garbage Fashion & Quirk (Roll 1d6)
* **1:** Wears a dented tea kettle as a helmet; screams every time someone rolls an odd number.
* **2:** Armed with a rusty fork; insists on licking every shiny die before rolling it.
* **3:** Draped in a moth-eaten velvet curtain; speaks in a high-pitched, fake noble accent.
* **4:** Glued broken glass to their kneecaps; communicates entirely in suspicious whispers.
* **5:** Covered head-to-toe in dungeon grease; leaves slimy handprints on other players' dice.
* **6:** Carries a dead rat named "Sir Reginald"; consults it before choosing Group or Greed.

---

## 3. DUNGEON SETUP & TURN ORDER
1. **Dungeon Length**: Roll **$\text{Number of Goblins } (G) + 1d4$**. This is the total number of Dungeon Areas to clear (e.g., 4 goblins $+ 1d4 = 5 \text{ to } 8$ areas).
2. **Raid Leader**: Turns rotate **clockwise**. The active player is the **Raid Leader**.
   * The Leader names the room and describes the terrible ambush plan on the adventurers.
   * The Leader rolls the area dice and breaks ties in Group drafting.

---

## 4. PROCEDURAL AREA GENERATOR
When entering a new area, the Raid Leader rolls **1d6 ($dA$), 1d4 ($dB$), and 1d10 ($dC$)**:

1. **Threshold ($T$)**: 

$$T = (G \times 4) + dA + dB$$

2. **Loot Pot**: Blindly draw **$dB + \lceil G / 2 \rceil$ dice** from the communal dice bag.
3. **Failure Penalty**: If the raid fails, every participant loses **$\lceil dA / 2 \rceil$ dice** (1 to 3 dice).
4. **Adventurer Doohickey**: Check **$dC$** on the table below:

### The Adventurer Doohickey Table (1d10)
| 1d10 | Item | Origin | Single-Use Discard Effect |
| :---: | :--- | :---: | :--- |
| **1 – 4** | **No Loot** | — | Just muddy boots, dry hardtack, and smelly socks. |
| **5** | **Tinkerer's Grabby Hand** | Artificer | Discard on any Room Clear ($M \ge T$): You get first pick of the loot (dice or item) before anyone else drafts or claims the pot, regardless of which side won! |
| **6** | **Wizard's Wand (Cracked)** | Wizard | Discard after rolling: Add **+4** to your personal rolled total. |
| **7** | **Paladin's Shiny Shield** | Paladin | Discard when your side loses: Ignore a 1-die penalty. |
| **8** | **Rogue's Smoke Bomb** | Rogue | Discard after tokens are revealed: Flip your token (Group $\leftrightarrow$ Greed). |
| **9** | **Bard's Annoying Kazoo** | Bard | Discard before rolling: Force any one opponent to re-roll their highest die. |
| **10** | **Cleric's Holy Water (Sour)** | Cleric | Discard: Revive a dead cousin immediately without skipping a round! |

---

## 5. THE RAID SEQUENCE (GROUP VS. GREED)

Every area raid is resolved in six steps:

1. **Commit Secret Token**: Every player secretly sets their token face-down (**Heads = Group**, **Tails = Greed**).
2. **Wager Dice from Hand**: Each player chooses which dice from their hand to roll. *(Unrolled dice remain 100% safe in your hand).*
3. **The Roll**: Everyone rolls their wagered dice **openly on the table**.
4. **Pre-Reveal Triggers**: Robgoblin may trigger *Sneaky Pocket* to roll 1 extra d4 from their hand.
5. **The Reveal**: All tokens are flipped simultaneously! Group and Greed are unmasked.
6. **Calculate Net**:

$$\text{Net } (M) = \sum \text{Group Rolls} - \sum \text{Greed Rolls}$$

---

## 6. RAID RESOLUTION & PAYOUT

### CASE A: $\text{Net} < T$ (MUTUAL DISASTER!)
The goblins were too greedy or botched the ambush. The adventurers beat you back!
* **Penalty**: *Every participating player* (Group and Greed alike) loses **$\lceil dA / 2 \rceil$ dice** (1 to 3 dice).
* **The Hand-Loss Rule**: You must surrender dice starting with the dice you rolled. Any remaining shortfall comes **directly out of unrolled dice in your hand**!
* **Loot Lost**: The Loot Pot and any Doohickey are dumped back into the communal dice bag.

### CASE B: $\text{Net} \ge T$ (THE AMBUSH SUCCEEDS!)
The adventurers are squashed! Compare the **highest individual Greed total** ($P_{\text{greed\_max}}$) vs. the **highest individual Group total** ($P_{\text{group\_max}}$):

#### 1. Greed Wins ($P_{\text{greed\_max}} > P_{\text{group\_max}}$)
* **The Top Greed Player Takes Everything**:
  * Claims the **entire Loot Pot** from the room.
  * Takes **any Doohickey** present.
  * Steals **1 rolled die** from each Group player.
  * Steals **1 rolled die** from every losing Greed player.

#### 2. Group Wins ($P_{\text{group\_max}} \ge P_{\text{greed\_max}}$)
* **Group Drafts the Spoils**:
  * Add the Loot Pot + 1 rolled die surrendered by *every* Greed player into the reward pool.
  * Group players **draft dice in order of their personal rolled total** (highest total picks first, second-highest picks next, etc.).
  * *Ties in Group*: Broken by the Raid Leader.
  * If a Doohickey was present, the Raid Leader awards it to any Group member (or takes it).
* **Greed Penalty**: All Greed players lose 1 rolled die to the pot.

---

## 7. CRASHING OUT & COUSINS
* **0 Dice = Dead Goblin**: When your last die is lost, you crash out.
* **The Cousin Catch-Up**: You skip **exactly 1 area raid** while your cousin sprints through the dungeon corridors to catch up.
* **Inheritance**: Your cousin inherits all Doohickies held by the dead goblin.
* **Respawn Pool**: Your cousin rejoins with **Starting Dice $- 1\text{ die}$ (minimum 1 die)**.

---

## 8. WINNING THE GAME (DON’T GET EATEN!)

The adventure ends once all **$N$ Dungeon Areas** ($G + 1d4$) have been raided!

* **The Winner**: The goblin with the **most total dice** in their personal hoard at the end of the adventure wins the game!
* **Breaking Ties**: If tied for most dice, the goblin holding the single highest-tier polyhedral die in their hoard wins ($\text{d20} > \text{d12} > \text{d10} > \text{d8} > \text{d6} > \text{d4}$). If still tied, whoever holds the most Adventurer Doohickies wins.
* **The Big Boss Verdict**: Big Boss crowns the winner as the new **Under-Boss**. **Big Boss eats everyone else!**
