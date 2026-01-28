## Add a new room

--- task ---
Open the [starter project](https://editor.raspberrypi.org/en/projects/rpg-starter){:target="_blank"}.
--- /task ---


Here is a basic maze that represents a house with two rooms. The rooms are both empty for now. Here’s a map of the game:

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them.](images/rpg-map1.png)

--- task ---
Press **Run** to start the game. Type `go south` to move from the Hall to the Kitchen, and then `go north` to go back to the Hall again.
--- /task ---

--- task ---

What happens when you type in a direction that you cannot go? Type `go west` in the Hall.

--- collapse ---
---
title: Answer
---
You'll see a friendly error message, and a reminder of where you are plus any items in your inventory.

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

--- /collapse ---
--- /task ---

