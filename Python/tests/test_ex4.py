import pytest
from app import *
from unittest.mock import MagicMock


@pytest.fixture
def setup_game_and_player_with_bet_5_chips_on_6_score():
    player = Player()
    player.buy(Chip(5))
    game = RollDiceGame()
    game.bet(player, Bet(chips=Chip(5), score=6))

    return game, player


def test_player_can_win(setup_game_and_player_with_bet_5_chips_on_6_score):
    game, player = setup_game_and_player_with_bet_5_chips_on_6_score
    dice = Dice()
    dice.roll = MagicMock(return_value=6)

    game.play(dice)

    assert player.has(Chip(30))


def test_player_can_lose(setup_game_and_player_with_bet_5_chips_on_6_score):
    game, player = setup_game_and_player_with_bet_5_chips_on_6_score
    dice = Dice()
    dice.roll = MagicMock(return_value=5)

    game.play(dice)

    assert not player.has(Chip(1))
