import unittest
import pytest
from app.player import Player
from app.roll_dice_game import RollDiceGame
from app.chip import Chip
from app.bet import Bet
from app.Exceptions.invalid_operation_exception import InvalidOperationException


@pytest.fixture
def setup_game_and_player_with_5_chips():
    player = Player()
    player.buy(Chip(5))
    game = RollDiceGame()
    return game, player


def test_player_can_make_bet(setup_game_and_player_with_5_chips):
    game, player = setup_game_and_player_with_5_chips

    bet = Bet(Chip(5), 1)
    game.bet(player, bet)

    assert not player.has(Chip(5))


def test_raise_when_player_trys_make_bet_but_dont_have_enought_chips(setup_game_and_player_with_5_chips):
    game, player = setup_game_and_player_with_5_chips

    bet = Bet(Chip(6), 1)

    with pytest.raises(InvalidOperationException):
        game.bet(player, bet)
