## Add items to collect

Add items in the rooms for the player to collect as they move through the house.

In `main.py`, add an `'item'` to the room's dictionary. The code below adds a **key** in the Hall.

```python filename="main.py" line_numbers="true" line_number_start="3" line_highlights="7-8"
# A dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    },
```

> [!DEBUG]
>
> Remember to put a comma after the line above the new item, or your program won't run!

## Now run your code

Click **Run**. The **Text output** now tells you there is a key in the Hall. Type `get key` in the **Text output** and press **Enter** to pick it up and add it to your inventory.
