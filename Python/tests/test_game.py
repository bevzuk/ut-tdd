import pytest

from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException


@pytest.fixture
def setup_player_with_10_chips_in_game(game, player_with_10_chips):
    player_with_10_chips.join(game)
    return player_with_10_chips, game

def test_player_can_bet_enough_chips(setup_player_with_10_chips_in_game):
    player, game = setup_player_with_10_chips_in_game

    bet = Bet(Chip(5), 3)
    game.bet(player, bet)

    assert (player.has(Chip(5)) is True)
    assert (player.has(Chip(6)) is False)


def test_player_can_not_bet_not_enough_chips(setup_player_with_10_chips_in_game):
    player, game = setup_player_with_10_chips_in_game

    bet = Bet(Chip(100), 3)

    with pytest.raises(InvalidOperationException):
        game.bet(player, bet)
