#  🔥 EMOJI 👨‍🚒 FIRE 🚒 FIGHTER 🔥 - A Game By Mitchell Estes
# A simple python game that can be run in terminal
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
# Firetruck can be driven, acts as water when out of gas
class Firetruck(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🚒')
# Water sources that can refill Water Tank
class Fountain(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⛲️')
class Ocean(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🌊')
# Obstacles that can not be passed through
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
    # Returns a random location on the board not occupied by a entity
    def random_location_safe(self, entities):
        while True:
            location_i = random.randint(0, self.height - 1)
            location_j = random.randint(0, self.width - 1)
            for entity in entities:
                if entity.location_i == location_i and entity.location_j == location_j:
                    break
            else:
                break
        return location_i, location_j
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
board = Board(25, 10)
# Player information
default_player = '👨‍🚒'
pi = 9
pj = 21
player = Player(pi, pj)
max_water = 5
water_level = max_water
# Firetruck variables
in_firetruck = False
firetruck = Firetruck(9,22)
gas = 16
# Water posistions
fountain = Fountain(4,15)
ocean1 = Ocean(9,0)
ocean2 = Ocean(9,0)
ocean3 = Ocean(9,0)
# Obsticle posistions
mointain1 = Mountain(0,1) # left range
mointain2 = Mountain(1,1)
mointain3 = Mountain(0,1)
mointain4 = Mountain(0,1)
mointain5 = Mountain(0,1)
mointain6 = Mountain(0,19) #right range
mointain7 = Mountain(1,19)
mointain8 = Mountain(0,19)
tree1 = Tree(4,0)
tree2 = Tree(6,12)
tree3 = Tree(7,2)
tree4 = Tree(2,5)
tree5 = Tree(4,23)
tree6 = Tree(0,8)
tree7 = Tree(0,10)
tree8 = Tree(8,20)
tree9 = Tree(7,17)
building1 = Building(3,9)
building2 = Building(6,3)
building3 = Building(3,3)
building4 = Building(8,14)
building5 = Building(5,5)
building6 = Building(5,5)
building7 = Building(5,16)
building8 = Building(5,5)
store1 = Store(5,5)
store2 = Store(1,21)
store3 = Store(3,3)
house1 = House(7,24)
house2 = House(4,23)
house3 = House(2,20)
# Entities includes all printed emojis
entities = [player, firetruck, fountain, ocean1, ocean2, ocean3, mointain1,
mointain2, mointain3, mointain4, mointain5, mointain6, mointain7, mointain8,
tree1, tree2, tree3, tree4, tree5, tree6, tree7, tree8, tree9, building1,
building2, building3, building4, building5, building6, building7, building8,
store1, store2, store3, house1, house2, house3]
# Obsticles are objects that player can not move through
obstacles = [mointain1, mointain2, mointain3, mointain4, mointain5, mointain6,
mointain7, mointain8, tree1, tree2, tree3, tree4, tree5, tree6, tree7, tree8,
tree9, building1, building2, building3, building4, building5,
building6, building7,building8, store1, store2, store3, house1, house2, house3]
# Waters are water sources that can fill Water Tank
waters = [fountain, ocean1, ocean2, ocean3]
# List of all current fires
fires = []

# GAME'S ACTIONS & FUNCTIONALITY
# Sets fire at random posistions to start game
for i in range(3):
    ei, ej = board.random_location_safe(entities)
    fire = Fire(ei, ej)
    entities.append(fire)
    fires.append(fire)
# Title displayed at start of game
print('-----------------------------------')
print('🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥')
print('🔥🔥 EMOJI 👨‍🚒 FIRE 🚒 FIGHTER 🔥🔥')
print('🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥')
print('🔥  Your computer\'s Firewall has🔥')
print('🔥failed, now fires are starting🔥')
print('🔥all across your terminal! Use 🔥')
print('🔥the emoji firefighter to fight🔥')
print('🔥all the fires quickly! However🔥')
print('🔥be careful to watch your water🔥')
print('🔥level and be sure to refill it🔥')
print('🔥when needed at a water source.🔥')
print('🔥 Are you the digital defender 🔥')
print('🔥your computer needs to save it🔥')
print('🔥from overheating?!            🔥')
print('🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥')
print('-----------------------------------')
start = None
# Waits for the user to hit a key before starting game
while start == None:
    start = input('     :Press Enter To Start: ')
print('-----------------------------------')
# Loops while game is being plaid
while True:
    # Every action taken has a 1 in 20 chance of starting a fire
    fire_starter = random.randint(1,20)
    if fire_starter == 1:
        # Adds fire to board at random location
        ei, ej = board.random_location_safe(entities)
        fire = Fire(ei, ej)
        entities.append(fire)
        fires.append(fire)
    # Firetruck adds special stats
    if in_firetruck:
        gas -= 1
        # If gas reaches 0, player hops out and firetruck becomes water source
        if gas < 0:
            dead_firetruck = Firetruck(player.location_i,player.location_j+1)
            waters.append(dead_firetruck)
            entities.append(dead_firetruck)
            player.character = default_player
            in_firetruck = False
        # Player has max water at all times while in firetruck
        water_level = max_water
    # Prints out the board
    board.print(entities)
    print('-----------------------------------')
    # Displays gas gauge if in firetruck
    if in_firetruck:
        print('GAS: ', end='')
        for i in range(gas):
            print('⛽️', end='')
        print()
    # Displays water level bellow board
    print('WATER TANK: ', end='')
    for i in range(water_level):
        print('💧', end='')
    print()
    # Ask the player for directional input
    command = input('Use the arrow keys to move: ')
    # Lets user get into firetruck if move to it
    if (firetruck.location_i == player.location_i and firetruck.location_j == player.location_j):
        use_firetruck = input('🚒Hit space to get in firetruck?🚒 ')
        if use_firetruck == ' ':
            in_firetruck = True
            player.character = firetruck.character
            entities.remove(firetruck)
            firetruck.location_i = 27
            firetruck.location_j = 27
    print('-----------------------------------')
    # Checks if it is a legal move and makes it if it is
    if player.check_move(command, obstacles):
        player.make_move(player.location_i, player.location_j, command)
    # Code for if the player encounters fire
    for fire in fires:
        if fire.location_i == player.location_i and fire.location_j == player.location_j:
            print('🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥')
            # User will be asked to type a random letter to fight fire
            letter = letters[random.randint(0,len(letters)-1)]
            action = input('Press the "' + letter + '" key to spray the fire! ').upper()
            # If they type correct and have water, remove the fire
            if action == letter and water_level > 0:
                print('💦You successfuly faught the fire!💦')
                water_level -= 1
                entities.remove(fire)
                fires.remove(fire)
                print('-----------------------------------')
                break
            # If they fail at fighting it, GAME OVER
            else:
                print('🔥You\'re out of water or burned!🔥')
                print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
                print('💀💀💀💀💀 GAME 💀 OVER 💀💀💀💀💀💀')
                print('💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀')
                print('-----------------------------------')
                exit()
    # Code for if player encounters water source
    for water in waters:
        if (water.location_i == player.location_i and water.location_j == player.location_j):
            print('🚰 You found a water source! 🚰')
            fill = input('Type "F" to refill or "C" to cancel: ').lower()
            # If the user fills there tank add water drop to it, 3 drops max
            if fill == 'fill' or fill == 'f':
                while (fill == 'fill' or fill == 'f') and water_level < max_water:
                    water_level += 1
                    print('WATER TANK: ', end='')
                    for i in range(water_level):
                        print('💧', end='')
                    print()
                    fill = input('Hit "F" to fill again or "C" to cancel: ').lower()
    # Checks if player has won yet
    if len(fires) == 0:
        # If they won prints this then closes
        print('💦 You put out all the fires! 💦')
        print('🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖')
        print('🏅🎖🏅🎖🏅🎖🏅 YOU 👨‍🚒 WON! 🏅🎖🏅🎖🏅🎖')
        print('🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖🏅🎖')
        print('-----------------------------------')
        exit()
