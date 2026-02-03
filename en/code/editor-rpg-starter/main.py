from game import *

# A dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen'
    }, 
    'Kitchen': {
        'north': 'Hall'
    }
}

# Keep this to run the game loop from game.py 
currentRoom, inventory = run_game(currentRoom, inventory, rooms)
