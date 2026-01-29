<h2 class="c-project-heading--task">Add a new room</h2>
--- task ---

Add a Dining Room to your game

--- /task ---

--- task ---

The new room will be east of the hall.

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them. A dining room has been added to the right of the hall.](images/rpg-dining.png)

--- /task ---

--- task ---

Each room is coded as a **dictionary**, and rooms are linked together using directions.  

--- code ---
---
language: python
line_numbers: true
line_number_start: 29
line_highlights: 32-33, 37-40
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

--- /task ---

--- task ---

Click **Stop**, then click **Run** to try out the game with your new Dining Room code. 

Type `go east` from the Hall to move into to the Dining Room, and `go west` to move back to the Hall.

--- /task ---


**Don't forget to add a comma to the end of the previous line when you add a new direction.**