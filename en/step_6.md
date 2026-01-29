<h2 class="c-project-heading--task">Add a garden/h2>
--- task ---

Add a garden to the south of the dining room. Remember to link the garden to the dining room.

--- /task ---


--- task ---

Here’s a map of the game.

![A map showing the hall containing a key, witih the dining room to the East containing a potion. The kitchen is South of the hall and contains a monster. The garden is East of the kitchen and South of the dining room.](images/rpg-final-map.png)

--- /task ---


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 29
line_highlights: 41-42, 43-46
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
    },
    'Garden' : {
        'north' : 'Dining Room'
    }
}
--- /code ---

--- /task ---

Click **run** and navigate to the `'Garden'`.

--- task ---
</div>
