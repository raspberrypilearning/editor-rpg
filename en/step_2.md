<h2 class="c-project-heading--task">Go the wrong way</h2>
--- task ---

When you type in a direction that you cannot go, you'll see a friendly error message, and a reminder of where you are plus any items in your inventory.

--- /task ---


<h2 class="c-project-heading--explainer">Here’s a map of the game:</h2>

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them.](images/rpg-map1.png)

The house is a basic maze, and the error message helps you to find your way.

--- task ---

Press **run** to start the game. Type a direction you can't go, such as `go west` from the Hall.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: text
line_numbers: false
line_number_start: 
line_highlights: 
---
go west
You can't go that way!
---------------------------
You are in the Hall
Inventory : []
---------------------------
>
--- /code ---
</div>

--- task ---

Experiment with other directions to. Type `go south` to move from the Hall to the Kitchen, and then `go north` to go back to the Hall again

--- /task ---