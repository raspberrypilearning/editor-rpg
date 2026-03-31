## Add enemies
Add a monster that the player must avoid.

Adding a character into a room is the same as adding an item. 

Add a **monster** to the Kitchen.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 11-12
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

If the player enters a room with a monster in, the game ends. 

### Now run your code
Type `go south`{:.language-python} to test out your code by going into the Kitchen, which now contains a monster.


<div class="c-project-output">
```
You are in the Hall
Inventory : []
You see a key

---------------------------
> go south

A monster has got you... GAME OVER!
```
</div>