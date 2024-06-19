import pytest

from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException
from unittest.mock import MagicMock

@pytest.fixture
def mocked_game_winning_score_always_1():
    dice = Dice()
    dice.roll = MagicMock(return_value=1)
    game = RollDiceGame(dice=dice)
    return game


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


def test_player_wins_x6_if_winning_score(setup_player_with_10_chips_in_game,
                                             mocked_game_winning_score_always_1):
    player, game = setup_player_with_10_chips_in_game
    game = mocked_game_winning_score_always_1
    bet = Bet(Chip(10), 1)

    game.bet(player, bet)
    game.play()

    assert (player.has(Chip(60)) is True)


def test_player_lost_if_losing_score(setup_player_with_10_chips_in_game,
                                     mocked_game_winning_score_always_1):
    player, game = setup_player_with_10_chips_in_game
    game = mocked_game_winning_score_always_1
    bet = Bet(Chip(10), 2)

    game.bet(player, bet)
    game.play()

    assert (player.has(Chip(0)) is True)