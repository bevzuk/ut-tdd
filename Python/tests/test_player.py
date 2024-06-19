import pytest

from app import *


@pytest.fixture(scope='function')
def player():
    return Player()


def test_not_in_game(player):
    assert player.is_in_game() is False


def test_can_join_game(player):
    player.join(RollDiceGame())
    assert player.is_in_game() is True


def test_can_buy_chips(player):
    player.buy(Chip(3))
    assert player.has(Chip(3))


def test_can_bet(player):
    game = RollDiceGame()
    player.join(game)
    player.buy(Chip(3))
    game.bet(player, Bet(Chip(3), score=6))
    assert player.has(Chip(0))

def test_can_leave_game(player):
    game = RollDiceGame()
    player.join(game)
    player.leave_game()
    assert player.is_in_game() is False
