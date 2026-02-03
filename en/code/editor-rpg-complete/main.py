from game import *

# A dictionary linking a room to other rooms
rooms = {
    "Hall": {
        "south": "Kitchen",
        'east' : 'Dining Room',
        'item' : 'key'
    }, 
    "Kitchen": {
        "north": "Hall",
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

# Run the game loop from the helper so learners keep state in this file
currentRoom, inventory = run_game(currentRoom, inventory, rooms)
