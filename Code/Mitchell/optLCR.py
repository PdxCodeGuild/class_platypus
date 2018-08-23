dice = 'LCR...'
center = 0
# User enters player's names into dictionary with 3 chips each
name = input('Welcome to LCR Simulator, please enter the name of a the first player: ')
players = {name: 3}
while name != 'done':
    name = input('Enter another player\'s name or type "done" if all players are entered: ')
    if name == 'done':
        break
    players[name] = 3
# Game is simulated until all players but one are out of chips
total_chips = len(players) * 3
playing = True
for i in range(len(players)):
#while playing:
    for key, value in players.items():
        # Checks if there is a winner if so end
        if (value) + center == total_chips:
            print(key + ' won this round of LCR!')
            break
    print(value)
        # for value in range(value):
        #     print(f'{key} has {value} chips.')
