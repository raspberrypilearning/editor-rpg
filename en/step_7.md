## Add instructions

Add some instructions to your game, so that the player knows what they have to do.

The player instructions are also in the `game.py`{:.language-python} file. Find the  `showInstructions()`{:.language-python} and edit it to include more information about how to play.

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

### Now run your code
Test your game and you should see your new instructions.