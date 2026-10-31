## Go the wrong way

The game is set in a house. To play, you type commands into the **Text output** to move around the house. You don't type them into your code.

> [!INFO]
>
> Here's what the house looks like to start with:
>
> ![A map with two rooms. The hall is in the north and kitchen is below it. There is a door between them.](images/rpg-map1.png)

## Step 1

Click **Run**. The game starts in the **Text output**. Depending on the size of your screen, this is next to your code or below it.

![The Text output tab showing the start of the game. It lists the commands, says You are in the Hall, and ends with a > prompt.](images/text-output.png)

## Step 2

When you see the `>` prompt in the **Text output**, type `go west` and press **Enter**. What you type appears in blue under the `>`.

> [!TIP]
>
> If nothing appears when you type, click in the **Text output** and try again.

You can't go west from the hall, so the game reminds you where you are and what's in your inventory:

```
>
go west
You cannot go that way!
---------------------------
You are in the Hall
Inventory : []
---------------------------
>
```

## Step 3

In the **Text output**, type `go south` to move to the kitchen, then `go north` to go back to the hall.

## Now run your code

Your game is still running, so the button under your code now says **Stop**. Click **Stop**, then click **Run** to start a new game.

In the **Text output**, try a direction that does not work, then move south to the kitchen and north back to the hall.
