import random
import time
# re-use previous labs (guess the number, rock-paper-scissors)


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Cat(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🐱')
        self.name = ''


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👧')
        self.cats = []


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def __getitem__(self, j):
        return self.board[j]

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



board = Board(10, 10)

pi, pj = board.random_location()
player = Player(pi, pj)

entities = [player]
cats = []

for i in range(10):
    ei, ej = board.random_location()
    cat = Cat(ei, ej)
    entities.append(cat)
    cats.append(cat)

# x = random.randint(1, 10)
print('''
        ,----,                                                                                                                                            
      ,/   .`|                                                                                                                                            
    ,`   .'  :  ,---,                        ,----..                 ___              ,---,                                                               
  ;    ;     /,--.' |                       /   /   \              ,--.'|_          ,--.' |                                      ,---,                    
.'___,/    ,' |  |  :                      |   :     :             |  | :,'         |  |  :       ,---.               __  ,-.  ,---.'|            __  ,-. 
|    :     |  :  :  :                      .   |  ;. /             :  : ' :         :  :  :      '   ,'\            ,' ,'/ /|  |   | :          ,' ,'/ /| 
;    |.';  ;  :  |  |,--.   ,---.          .   ; /--`   ,--.--.  .;__,'  /          :  |  |,--. /   /   |  ,--.--.  '  | |' |  |   | |   ,---.  '  | |' | 
`----'  |  |  |  :  '   |  /     \         ;   | ;     /       \ |  |   |           |  :  '   |.   ; ,. : /       \ |  |   ,',--.__| |  /     \ |  |   ,' 
    '   :  ;  |  |   /' : /    /  |        |   : |    .--.  .-. |:__,'| :           |  |   /' :'   | |: :.--.  .-. |'  :  / /   ,'   | /    /  |'  :  /   
    |   |  '  '  :  | | |.    ' / |        .   | '___  \__\/: . .  '  : |__         '  :  | | |'   | .; : \__\/: . .|  | ' .   '  /  |.    ' / ||  | '    
    '   :  |  |  |  ' | :'   ;   /|        '   ; : .'| ," .--.; |  |  | '.'|        |  |  ' | :|   :    | ," .--.; |;  : | '   ; |:  |'   ;   /|;  : |    
    ;   |.'   |  :  :_:,''   |  / |        '   | '/  :/  /  ,.  |  ;  :    ;        |  :  :_:,' \   \  / /  /  ,.  ||  , ; |   | '/  ''   |  / ||  , ;    
    '---'     |  | ,'    |   :    |        |   :    /;  :   .'   \ |  ,   /         |  | ,'      `----' ;  :   .'   \---'  |   :    :||   :    | ---'     
              `--''       \   \  /          \   \ .' |  ,     .-./  ---`-'          `--''               |  ,     .-./       \   \  /   \   \  /           
                           `----'            `---`    `--`---'                                           `--`---'            `----'     `----'            


'''

      )
time.sleep(2)

while True:
    board.print(entities)

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down

    collector = 0
    names = []
    for cat in cats:
        if cat.location_i == player.location_i and cat.location_j == player.location_j:
            print('you\'ve encountered a kitty!')
            action = input('what will you do? ')
            if action == 'collect':
                collector += 1
                print('you\'ve captured a kitty')

                name = input('what will you name the kitty?')
                self.name[name]
                # names.append[input]
                # put the kitty name in a list
                entities.remove(cat)
                cats.remove(cat)
                break
            else:
                print('you hestitated and the kitty ran off')
                exit()


    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)
