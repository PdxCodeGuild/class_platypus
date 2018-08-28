import random
class Player:
    def __init__(self, name, chips=3):
        self.name = name
        self.chips = chips

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Game:
    def __init__(self):
        self.center = 0
        self.player_index = 0
        # self.players = []
        # while True:
        #     user = input('Enter player names, enter done, when done... ').title()
        #     if user == 'Done':
        #         break
        #     player = Player(user)
        #     self.players.append(player)
        self.players = [Player(name) for name in ['Al', 'Mitchell', 'Kagome', 'Indu', 'Angle', 'Colton', 'Matthew']]


    def roll_die(self):
        dice = 'LCR...'
        die = random.choice(dice)
        if die == 'L':
            self.players[self.player_index].chips -=1
            left_index = (self.player_index -1)%len(self.players)
            self.players[left_index].chips +=1
        elif die == 'C':
            self.players[self.player_index].chips -=1
            self.center += 1
        elif die == 'R':
            self.players[self.player_index].chips -= 1
            right_index = (self.player_index + 1) % len(self.players)
            self.players[right_index].chips += 1

    def check_win(self):
        counter = 0
        winner = None
        for i in range(len(self.players)):
            if self.players[i].chips > 0:
                counter += 1
                winner = i
        if counter == 1:
            return winner
        return None

    def run(self):
        while True:
            rolls = self.players[self.player_index].chips
            if rolls >= 3:
                rolls = 3
            for i in range(rolls):
                self.roll_die()
            if self.check_win():
                break
            self.player_index += 1
            self.player_index %= len(self.players)

        print(self)

    def __str__(self):
        return ', '.join([f'{player.name}: {player.chips}' for player in self.players])

game = Game()
game.run()











