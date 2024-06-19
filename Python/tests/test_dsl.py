from unittest.mock import MagicMock

from app import *


class Helper():
    def __init__(self):
        self.player = None
        self.game = None
        self.dice = None

    def set_player(self):
        self.player = Player()
        return self

    def set_dice(self):
        self.dice = Dice()
        return self

    def set_game(self):
        self.set_dice()
        self.game = RollDiceGame(self.dice)
        return self

    def player_buy_chips(self, count):
        self.player.buy(Chip(count))
        return self

    def add_player_to_game(self):
        self.game.add_player()
        return self

    def add_bet(self, amount, score):
        self.game.bet(self.player, Bet(Chip(amount), score))
        return self


def test_player_can_win():
    helper = Helper()
    helper.set_player().set_game().player_buy_chips(1).add_player_to_game().add_bet(1, 1)
    helper.dice.roll = MagicMock(return_value=1)

    helper.game.play()

    assert helper.player.get_chips_amount() == 6


def test_player_can_loose():
    helper = Helper()
    helper.set_player().set_game().player_buy_chips(1).add_player_to_game().add_bet(1, 1)
    helper.dice.roll = MagicMock(return_value=2)

    helper.game.play()

    assert helper.player.get_chips_amount() == 0
