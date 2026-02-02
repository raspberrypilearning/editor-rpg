<h2 class="c-project-heading--task">Add items to collect</h2>
--- task ---

Add items in the rooms for the player to collect as they move through the house.

--- /task ---

--- task ---

Add an `'item'` in the room's dictionary. The code below adds a **key** in the Hall.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 10-11
---
# A dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    },
--- /code ---
--- task ---

Click **Stop** and then **Run**, and you can now see a key in the Hall. You can pick it up by typing `get key`, which adds it to your inventory.

--- /task ---
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Remember to put a comma after the line above the new item, or your program won’t run!

</div>
