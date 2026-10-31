## Add instructions

Add some instructions to your game, so that the player knows what they have to do.

The player instructions are also in the `game.py`{:.language-python} file. Click the **game.py** tab above your code, find the `showInstructions()`{:.language-python} function, and change it to include more information about how to play.

```python filename="game.py" line_numbers="true" line_number_start="7" line_highlights="12-15"
def showInstructions():
    # Print a main menu and the commands
    print('''
Monster Game
========

Get to the garden with a key 🔑 and a potion 🧪
Avoid the monsters!

Commands:
go [direction]
get [item]
''')
```

> [!TIP]
>
> Emojis are optional. Plain words work just as well. To add one, open the emoji keyboard:
> + **Windows:** press the Windows key and **.** (full stop)
> + **Mac:** press **Control**, **Command** and **Space**
> + **Chromebook:** press **Search**, **Shift** and **Space**
>
> Then search for the emoji, for example "key" or "test tube".

## Now run your code

Click **Run**. Your new instructions appear at the top of the **Text output**.
