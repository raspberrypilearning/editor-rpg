<h2 class="c-project-heading--task">Add a new room</h2>
--- task ---

Add a Dining Room east of the hall.

--- /task ---

--- task ---

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them. A dining room has been added to the right of the hall.](images/rpg-dining.png)

Each room on the map can be coded as a **dictionary**, and rooms are linked together using directions.  

--- /task ---

--- task ---

Add the code below to make a new room, and link it to the Hall.

--- /task ---

<div class="c-project-output">
--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 9-10, 15-16
---
# A dictionary linking a room to other rooms
rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room'
    },
    'Kitchen' : {
        'north' : 'Hall'
    },
    'Dining Room' : {
        'west' : 'Hall'
    }
}
--- /code ---
</div>

--- task ---

Click **Run** to try out the game with your new Dining Room code. 

Type `go east` from the Hall to move into to the Dining Room, and `go west` to move back to the Hall.

--- /task ---


<div class="c-project-callout c-project-callout--debug">

### Debugging

+ Don't forget to add a comma after 'kitchen' when you add a new direction.
+ Make sure you have "closed" the dictionary using curly brackets.

</div>


