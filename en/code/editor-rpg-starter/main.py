from game import *

# An inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen'
    }, 
    'Kitchen': {
        'north': 'Hall'
    }
}

# Run the game loop from the helper so learners keep state in this file
currentRoom, inventory = run_game(currentRoom, inventory, rooms)
