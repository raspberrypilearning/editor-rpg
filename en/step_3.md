<h2 class="c-project-heading--task">Add items to collect</h2>

Add items in the rooms for the player to collect as they move through the house.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Add an `'item'`{:.language-python} in the room's dictionary. The code below adds a **key** in the Hall.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 7-8
---
# A dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    },
--- /code ---
</div>

### Debugging
<div class="c-project-callout c-project-callout--debug">

Remember to put a comma after the line above the new item, or your program won't run!

</div>

## Now run your code

You can now see a key in the Hall. You can pick it up by typing `get key`, which adds it to your inventory.
