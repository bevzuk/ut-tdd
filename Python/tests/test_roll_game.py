from unittest.mock import MagicMock
from app import *
import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/Python")
from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.Exceptions.too_many_players_exception import TooManyPlayersException


@pytest.fixture
def setup_player_and_game():
    player = Player()
    game = RollDiceGame()
    return  player, game


def test_roll_game_default_values(setup_player_and_game):
    player, game = setup_player_and_game
    player.join(game)
    with pytest.raises(InvalidOperationException):
        game.bet(player, Bet(Chip(1), 2))
         

def test_player_win_game():
    player = Player()
    dice = Dice()
    dice.roll = MagicMock(return_value = 1)
    bet = Bet(Chip(2), 1)
    game = RollDiceGame(dice)
    player.buy(Chip(2))
    player.join(game)

    game.bet(player, bet)
    game.play()
    
    assert player.has(Chip(12))
    