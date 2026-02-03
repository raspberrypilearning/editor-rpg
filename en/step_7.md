<h2 class="c-project-heading--task">Winning the game</h2>
--- task ---

Make it so player wins by getting to the garden with the key and the magic potion.

--- /task ---

More game play is in `game.py`, which you can see by clicking on the file tab.

![screenshot of the file system](images/edit-game.png)

--- task ---

Add the code below to `game.py` so that the player wins when they get to the **garden** with the **key** and the **potion**. 

--- /task ---

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

--- task ---

Click **Stop** and then **Run** to test your game to make sure the player can win!

--- /task ---
</div>

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

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure the code is indented, in line with the code above it. 

</div>
