from helper import *

# An inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {
    "Hall": {
        "south": "Kitchen"
    }, 
    "Kitchen": {
        "north": "Hall"
    }
}

# Start the player in the Hall
currentRoom = "Hall"

# Show instructions (moved to helper)
# Run the game loop from the helper so learners keep state in this file
currentRoom, inventory = run_game(currentRoom, inventory, rooms)
