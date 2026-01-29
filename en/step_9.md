<h2 class="c-project-heading--task">Add instructions</h2>
--- task ---

Add some instructions to your game, so that the player knows what they have to do.

--- /task ---

--- task ---

Edit the `showInstructions()` function to include more information.

--- /task ---

<div class="c-project-output">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8-9
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
