class NotEnoughPlayers(Exception):
    pass


class Player:
    def __init__(self, name, starting_funds):
        self.name = name
        self.money = starting_funds
        self.curr_bet = 0
        self.folded = False

    def bet(self, amount):
        pass

    def fold(self):
        pass

    def lose(self):
        pass

    def win(self, amount):
        pass

    def reset(self):
        pass

    def __repr__(self):
        return self.name


class Game:
    STARTING_WEALTH = 100  # measured in 10c
    BIG_BLIND_BID = 2
    SMALL_BLIND_BID = 1

    def __init__(self, names_list):
        if len(names_list) < 3:
            raise NotEnoughPlayers("Poker is not fun with less than 3 players.")
        self.players = [Player(name, self.STARTING_WEALTH) for name in names_list]
        self.num_players = len(names_list)
        self.history = []

    def _make_bets(self):
        pass

    def play_round(self):
        pass

    def play(self):
        pass


print("Welcome to poker!")

while True:
    names = input("Enter player names, in order, ending with big blind, separated by spaces: ")
    try:
        game = Game(names.split())
    except NotEnoughPlayers as e:
        print(e)
        continue
    game.play()
    play_again = input("Play again? (y/n): ")
    if play_again == "n":
        break
