<h2 class="c-project-heading--task">Winning the game</h2>
--- task ---

The player wins by getting to the garden with the key and the magic potion.

--- /task ---

--- task ---

Add this code so that the player wins the game when they get to the garden with the key and the potion. 

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 96
line_highlights: 96-99
---
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break

        NEEDS SORTING!!!!
--- /code ---

--- task ---

Click **run** to test your game to make sure the player can win!

--- /task ---
</div>

<div class="c-project-output">
<pre>
---
language: text
line_numbers: false
line_number_start: 
---
---------------------------
You are in the Hall
Inventory : []
You see a key
---------------------------
>get key
You picked up the key
---------------------------
You are in the Hall
Inventory : ['key']
---------------------------
>go east
---------------------------
You are in the Dining Room
Inventory : ['key']
You see a potion
---------------------------
>get potion
You picked up the potion
---------------------------
You are in the Dining Room
Inventory : ['key', 'potion']
---------------------------
>go south
You escaped the house... YOU WIN!
</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure the code is indented, in line with the code above it. 

</div>
