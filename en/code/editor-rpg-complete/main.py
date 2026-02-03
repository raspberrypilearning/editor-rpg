from game import *

# A dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    }, 
    "Kitchen": {
        'north': 'Hall',
        'item' : 'monster'
    },
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Garden',
        'item' : 'potion'
    },
    'Garden' : {
        'north' : 'Dining Room'
    }
}

# Keep this to run the game loop from game.py
currentRoom, inventory = run_game(currentRoom, inventory, rooms)
