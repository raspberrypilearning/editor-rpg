<h2 class="c-project-heading--task">Winning the game</h2>

Make it so player wins by getting to the garden with the key and the magic potion.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

## Step 1

More game play is in the `game.py`{:.language-python} file. Open this by clicking on the file tab.

<div class="c-project-output">
![screenshot of the file system](images/edit-game.png)
</div>

## Step 2

Add the code below to `game.py`{:.language-python} so that the player wins when they get to the **garden** with the **key** and the **potion**.

<div class="c-project-code">
--- code ---
---
language: python
filename: game.py
line_numbers: true
line_number_start: 74
line_highlights: 75-77
---
    # add more game play here
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break


    return currentRoom, inventory
--- /code ---
</div>

### Debugging
<div class="c-project-callout c-project-callout--debug">

Make sure the code is indented, in line with the code above it.

</div>

## Now run your code

Test your game to make sure the player can win.

<div class="c-project-output">
<pre>
Monster Game
========
Commands:
go [direction]
get [item]

---------------------------
You are in the Hall
Inventory : []
You see a key
---------------------------
>
go west
You cannot go that way!
---------------------------
You are in the Hall
Inventory : []
You see a key
---------------------------
>
get key
You picked up the key
---------------------------
You are in the Hall
Inventory : ['key']
---------------------------
>
</pre>
</div>
