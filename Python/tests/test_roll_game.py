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
         

    