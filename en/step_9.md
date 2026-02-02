<h2 class="c-project-heading--task">Add instructions</h2>
--- task ---

Add some instructions to your game, so that the player knows what they have to do.

--- /task ---

--- task ---

The player instructions are also in the `game.py` file. Find the  `showInstructions()` and edit it to include more information about how to play.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 
line_highlights: 12-15
---
def showInstructions():
    # Print a main menu and the commands
    print(
        """
          RPG Game
          ========

          Get to the Garden with a key and a potion
          Avoid the monsters!

          Commands:
          go [direction]
          get [item]
          """
    )
--- /code ---
</div>

--- task ---

**Test** your game and you should see your new instructions.

--- /task ---
