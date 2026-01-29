<h2 class="c-project-heading--task">Add enemies</h2>
--- task ---

Add enemies to some rooms that the player must avoid.

--- /task ---

--- task ---

Adding an enemy to a room is the same as adding an item. Add a **monster** to the Kitchen.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 14-15
---
# A dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    },
    'Kitchen' : {
        'north' : 'Hall',
        'item' : 'monster'
    },
--- /code ---
--- task ---

If the player enters a room with a monster in, the game ends. Test out your code by going into the Kitchen, which now contains a monster.

Click **run** and type `go south`.

--- /task ---
</div>

<div class="c-project-output">
<pre>

You are in the Hall
Inventory : []
You see a key
---------------------------
>go south

A monster has got you... GAME OVER!
</pre>
