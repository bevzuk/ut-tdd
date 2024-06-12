import pytest
from unittest.mock import MagicMock
import random

from app.Exceptions.too_many_players_exception import TooManyPlayersException
from app.roll_dice_game import RollDiceGame


# Assuming RollDiceGame and TooManyPlayersException are defined somewhere above or in imported modules.

@pytest.fixture
def game():
    return RollDiceGame()


def test_add_player_success(game):
    game.add_player()
    assert game._players_count == 1


def test_add_player_exception(game):
    game._players_count = 6
    with pytest.raises(TooManyPlayersException):
        game.add_player()


def test_remove_player(game):
    game._players_count = 1
    game.remove_player()
    assert game._players_count == 0


def test_remove_player_no_players(game):
    game._players_count = 0
    game.remove_player()
    assert game._players_count == 0  # or adjust test based on the expected behavior


def test_bet(game):
    mock_player = MagicMock()
    mock_bet = MagicMock(chips=100, score=3)
    game.bet(mock_player, mock_bet)
    assert {'player': mock_player, 'chips': 100, 'score': 3} in game._bets
    mock_player.take.assert_called_once_with(100)


def test_play(game):
    mock_player = MagicMock()
    game._bets = [{'player': mock_player, 'chips': 100, 'score': 3}]
    with pytest.mock.patch('random.randrange', return_value=3):
        game.play()
        mock_player.win.assert_called_once_with(600)
