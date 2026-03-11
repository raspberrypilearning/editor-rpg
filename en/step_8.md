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
filename: game.py
line_numbers: true
line_number_start: 7
line_highlights: 12-15
---
def showInstructions():
    # Print a main menu and the commands
    print('''
Monster Game
========

Get to the garden with a key 🗝️ and a potion 🧪  
Avoid the monsters❗

Commands 
go [direction]
get [item] 
''')
--- /code ---
</div>

--- task ---

Click **Stop** and then **Run** to test your game and you should see your new instructions.

--- /task ---
