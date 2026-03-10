<h2 class="c-project-heading--task">Go the wrong way</h2>

The game is set in a house, type commands to move around the rooms.

<h2 class="c-project-heading--explainer">Here’s what the house looks like to start with:</h2>

![A map with two rooms - hall is in the North and kitchen is below it. There is a door between them.](images/rpg-map1.png)

### Now run your code

### Step 1

Type a direction you can't go, such as `go west` from the Hall.

When you type the wrong direction, the error message reminds you where you are plus any items in your inventory.


<div class="c-project-output">
```
go west
You can't go that way!
---------------------------
You are in the Hall
Inventory : []
---------------------------
> 
```
</div>


Experiment with other directions. Type `go south` to move from the Hall to the Kitchen, and then `go north` to go back to the Hall again
