## Add enemies

Add a monster that the player must avoid.

Adding a character into a room is the same as adding an item.

In `main.py`, add a **monster** to the kitchen.

```python filename="main.py" line_numbers="true" line_number_start="3" line_highlights="11-12"
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
```

If the player enters a room with a monster in, the game ends.

## Now run your code

Click **Run**. In the **Text output**, type `go south` and press **Enter** to go into the kitchen, which now has a monster in it.

```
---------------------------
You are in the Hall
Inventory : []
You see a key
---------------------------
>
go south
A monster has got you... GAME OVER!
```
