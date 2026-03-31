## Add items to collect

Add items in the rooms for the player to collect as they move through the house.

Add an `'item'`{:.language-python} in the room's dictionary. The code below adds a **key** in the Hall.

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

### Now run your code
You can now see a key in the Hall. You can pick it up by typing `get key`, which adds it to your inventory.


> ### Debugging
> 
> Remember to put a comma after the line above the new item, or your program won’t run!
{: .c-project-callout .c-project-callout--debug}

