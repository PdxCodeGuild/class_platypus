import random
# CLASSES FOR ALL ENTITIES
# Most genreal class, includes all emojis
class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character
# The enemy class player is trying to fight
class Fire(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🔥')
# Water sources that can refill Water Tank
class Firetruck(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🚒')
class Fountain(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⛲️')
class Ocean(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🌊')
# obstacles that can not be passed through
class Building(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🏢')
class Store(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🏬')
class House(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🏡')
class Mountain(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⛰')
class Tree(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🌲')
# Player's moves and position
class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👨‍🚒')
    # Checks if inputted comand is a valid move
    def check_move(self, command, obsticles):
        next_i = self.location_i
        next_j = self.location_j
        # Stops program if user requests
        if command == 'done' or command == 'exit' or command == 'quit':
            print('-----------------------------------')
            exit()  # exit the game
        # Find cordinates player wants to move to
        elif command in left:
            next_j -= 1
        elif command in right:
            next_j += 1
        elif command in up:
            next_i -= 1
        elif command in down:
            next_i += 1
        else: # Invalid comand entered
            return False
        # Loop over obstacles & see if any are at cordinates
        for obsticle in obstacles:
            if obsticle.location_i == next_i and obsticle.location_j == next_j:
                # Not a legal move if there is one
                return False
        return True
    # Performs the move after proven legal
    def make_move(self, location_i, location_j, move):
        if command in left:
            player.location_j -= 1  # move left
        elif command in right:
            player.location_j += 1  # move right
        elif command in up:
            player.location_i -= 1  # move up
        elif command in down:
            player.location_i += 1  # move down
# Board keeps track of the position and displays all emojis
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # Returns a random location on the board
    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)
    # Gets an item at a certain spot on the board
    def __getitem__(self, j):
        return self.board[j]
    # Prints/displays the board and emojis
    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print(' ', end='')
            print()

# VARIABLES, CORDINATES & GROUPED OBJECTS
# Possible movement commands
left = ['left', 'west', '\x1b[D', 'a']
right = ['right', 'east', '\x1b[C', 'd']
up = ['up', 'north', '\x1b[A', 'w']
down = ['down', 'south', '\x1b[B', 's']
# Used for fighting fire
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Board dimmensions: board(col, row)
board = Board(30, 10)
# Player information
pi = 9
pj = 24
player = Player(pi, pj)
water_level = 3
# Water posistions
firetruck = Firetruck(9,26)
fountain = Fountain(3,13)
ocean1 = Ocean(9,0)
ocean2 = Ocean(9,1)
ocean3 = Ocean(9,2)
# Obsticle posistions
mointain1 = Mountain(0,1) # left range
mointain2 = Mountain(1,2)
mointain3 = Mountain(0,4)
mointain4 = Mountain(0,5)
mointain5 = Mountain(1,6)
mointain6 = Mountain(0,3)
mointain7 = Mountain(0,27) #right range
mointain8 = Mountain(1,27)
mointain9 = Mountain(0,26)
tree1 = Tree(3,0)
tree2 = Tree(6,12)
tree3 = Tree(7,2)
tree4 = Tree(2,5)
tree5 = Tree(0,14)
tree6 = Tree(0,10)
tree7 = Tree(1,12)
tree8 = Tree(5,10)
tree9 = Tree(0,17)
tree10 = Tree(7,27)
tree11 = Tree(4,24)
tree12 = Tree(8,20)
building1 = Building(3,9)
building2 = Building(6,3)
building3 = Building(3,4)
building4 = Building(8,14)
building5 = Building(5,5)
building6 = Building(5,6)
building7 = Building(5,17)
building8 = Building(5,8)
store1 = Store(5,7)
store2 = Store(5,25)
store3 = Store(3,3)
store4 = Store(0,22)
house1 = House(1,17)
house2 = House(3,18)
house3 = House(9,9)
house4 = House(2,26)
# Entities includes all printed emojis
entities = [player, firetruck, fountain, ocean1, ocean2, ocean3, mointain1, mointain2, mointain3,
 mointain4, mointain5, mointain6, mointain7, mointain8, mointain9, tree1, tree2, tree3, tree4, tree5, tree6,
 tree7, tree8, tree9, tree10, tree11, tree12, building1, building2, building3, building4,
 building5, building6, building7, building8, store1, store2, store3, store4, house1, house2, house3, house4]
# Obsticles are objects that player can not move through
obstacles = [mointain1, mointain2, mointain3, mointain4, mointain5, mointain6, mointain7, mointain8, mointain9, tree1, tree2, tree3, tree4, tree5, tree6,
tree7, tree8, tree9, tree10, tree11, tree12, building1, building2, building3, building4, building5, building6, building7, building8, store1, store2, store3, store4,
house1, house2, house3, house4]
# Waters are water sources that can fill Water Tank
waters = [firetruck, fountain, ocean1, ocean2, ocean3]
# List of all current fires
fires = []

# GAME'S ACTIONS & FUNCTIONALITY
# Sets fire at random posistions to start game
for i in range(15):
    ei, ej = board.random_location()
    fire = Fire(ei, ej)
    entities.append(fire)
    fires.append(fire)
# Title displayed at start of game
print('-----------------------------------')
print('🔥🔥 EMOJI 👨‍🚒 FIRE 🚒 FIGHTER 🔥🔥')
print('-----------------------------------')
# Loops while game is being plaid
while True:
    # Prints out the board
    board.print(entities)
    print('-----------------------------------')
    # Displays water level bellow board
    print('WATER TANK: ', end='')
    for i in range(water_level):
        print('💧', end='')
    print()
    # Ask the player for directional input
    command = input('Use the arrow keys to move: ')
    print('-----------------------------------')
    # Checks if it is a legal move and makes it if it is
    if player.check_move(command, obstacles):
        player.make_move(player.location_i, player.location_j, command)
    # Code for if the player encounters fire
    for fire in fires:
        if fire.location_i == player.location_i and fire.location_j == player.location_j:
            print('🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥')
            # User will be asked to type a random letter to fight fire
            letter = letters[random.randint(1,len(letters))]
            action = input('Press the "' + letter + '" key to spray the fire! ').upper()
            # If they type correct and have water, remove the fire
            if action == letter and water_level >= 0:
                print('💦You successfuly faught the fire!💦')
                water_level -= 1
                entities.remove(fire)
                fires.remove(fire)
                print('-----------------------------------')
                break
            # If they fail at fighting it, GAME OVER
            else:
                print('🔥You\'re out of water or burned!🔥')
                print('💀💀💀💀💀💀 GAME OVER 💀💀💀💀💀💀')
                print('-----------------------------------')
                exit()
    # code for if player encounters water source 
    for water in waters:
        if (fountain.location_i == player.location_i and fountain.location_j == player.location_j) \
         or (ocean1.location_i == player.location_i and ocean1.location_j == player.location_j) \
         or (ocean2.location_i == player.location_i and ocean2.location_j == player.location_j) \
         or (ocean3.location_i == player.location_i and ocean3.location_j == player.location_j) \
          or (firetruck.location_i == player.location_i and firetruck.location_j == player.location_j):
            print('🚰You found a water source!🚰')
            fill = input('Type "F" to refill or "C" to cancel: ').lower()
            # If the user fills there tank add water drop to it, 3 drops max
            if fill == 'fill' or fill == 'f':
                while (fill == 'fill' or fill == 'f') and water_level < 3:
                    water_level += 1
                    print('WATER TANK: ', end='')
                    for i in range(water_level):
                        print('💧', end='')
                    print()
                    fill = input('Hit "F" to fill again or "C" to cancel: ').lower()
        break
