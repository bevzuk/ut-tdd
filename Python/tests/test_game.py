import pytest

from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException


def test_player_can_bet_enough_chips():
    game = RollDiceGame()
    player = Player()
    player.buy(Chip(10))
    player.join(game)
    bet = Bet(Chip(5), 3)

    game.bet(player, bet)

    assert (player.has(Chip(5)) is True)
    assert (player.has(Chip(6)) is False)


def test_player_can_not_bet_not_enough_chips():
    game = RollDiceGame()
    player = Player()
    player.buy(Chip(10))
    player.join(game)
    bet = Bet(Chip(100), 3)

    with pytest.raises(InvalidOperationException):
        game.bet(player, bet)
