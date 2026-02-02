<h2 class="c-project-heading--task">Add a garden</h2>
--- task ---

Add a garden to the south of the dining room. 

--- /task ---


--- task ---

Here’s the final map of the game.

![A map showing the hall containing a key, with the dining room to the East containing a potion. The kitchen is South of the hall and contains a monster. The garden is East of the kitchen and South of the dining room.](images/rpg-final-map.png)

--- /task ---

--- task ---

Add a garden and potion with the code below. Remember to link the garden to the dining room.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 24-29
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
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Garden'
        'item' : 'potion'
    },
    'Garden' : {
        'north' : 'Dining Room'
    }
}
--- /code ---

--- task ---

Click **Stop** and then **Run** and navigate to the `'Garden'`.

--- /task ---
</div>
