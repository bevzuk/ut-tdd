import pytest

from Python.app import *


def test_can_join_game():
    game = RollDiceGame()
    lucky_player = Player()

    try:
        lucky_player.join(game)
    except BaseException:
        assert False, "Player cannot join the game"


def test_can_buy_chips():
    lucky_player = Player()

    try:
        lucky_player.buy(Chip(4))
    except BaseException:
        assert False, "Player cannot buy chips"


def test_can_bet():
    game = RollDiceGame()
    lucky_player = Player()
    lucky_player.join(game)
    lucky_player.buy(Chip(4))

    try:
        game.bet(lucky_player, Bet(Chip(2), 4))
    except BaseException:
        assert False, "Player cannot bet 2 chips"


def test_can_leave_game():
    game = RollDiceGame()
    lucky_player = Player()
    lucky_player.join(game)

    assert lucky_player.is_in_game(), "Player cannot leave the game"


def test_cannot_join_2games():
    game = RollDiceGame()
    second_game = RollDiceGame()
    lucky_player = Player()
    lucky_player.join(game)

    with pytest.raises(BaseException):
        lucky_player.join(second_game)
