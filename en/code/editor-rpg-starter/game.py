# Helper module for the starter `main.py`.

# Start the player in the Hall
currentRoom = 'Hall'

# An inventory, which is initially empty
inventory = []


def showInstructions():
    # Print a main menu and the commands
    print('''
Monster Game
========
Commands:
go [direction]
get [item]
''')

def showStatus(currentRoom, inventory, rooms):
  '''Print the player's current status using passed-in state.

  Accepting state as arguments keeps the module simple and lets learners
  keep `rooms` / `inventory` / `currentRoom` in `main.py` where they can
  easily edit them.
  '''
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Inventory : ' + str(inventory))
  if 'item' in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print('---------------------------')


def run_game(currentRoom, inventory, rooms):
  '''Run the main game loop using state kept in `main.py`.

  This keeps `rooms`, `inventory` and `currentRoom` visible and editable
  in `main.py` for learners, while placing the loop logic here.
  Returns the final `(currentRoom, inventory)` when the game ends.
  '''
  showInstructions()


  while True:

    showStatus(currentRoom, inventory, rooms)

    move = ''
    while move == '':
      move = input(>')

    move = move.lower().split()

    if move[0] == 'go':
      if move[1] in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][move[1]]
      else:
        print('You can't go that way!'')

    elif move[0] == 'get':
      if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        inventory += [move[1]]
        print('You picked up the ' + move[1])
        del rooms[currentRoom]['item']
      else:
        print('There is no ' + move[1] + ' here!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
      print('A monster has got you... GAME OVER!')
      break
    
    # add more game play here

  return currentRoom, inventory

