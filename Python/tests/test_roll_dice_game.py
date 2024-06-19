import pytest

from Python.app import *


class FakeDice(IDice):
    @staticmethod
    def roll():
        return 5


def test_plays_correctly():
    game = RollDiceGame(FakeDice())
    lucky_player = Player()
    lucky_player.join(game)
    lucky_player.buy(Chip(4))

    game.bet(lucky_player, Bet(Chip(2), 5))
    game.play()

    assert lucky_player.has(Chip(14)), "Game plays wrong"
