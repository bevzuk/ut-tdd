from Python.app import *


class FakeDice(IDice):
    def __init__(self, value):
        self._value = value

    def roll(self):
        return self._value


class Helper:
    def __init__(self, game):
        self.game = game
        self.players = []

    @staticmethod
    def create_game(fixed_value=5):
        return Helper(RollDiceGame(FakeDice(fixed_value)))

    def with_one_player(self):
        self.players = [Player()]
        self.players[0].join(self.game)
        return self

    def buy_chips_for_player(self, number, count):
        self.players[number].buy(Chip(number))
        return self

    def with_players(self, count=6):
        self.players = []
        for _ in range(count):
            player = Player()
            self.players.append(player)
            player.join(self.game)
        return self

    def player_place_a_bet(self, number, chip_count, score):
        self.game.bet(self.players[number], Bet(Chip(chip_count), score))
