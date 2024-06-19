import pytest

from Python.app import *
from Python.app.Exceptions.invalid_operation_exception import InvalidOperationException


def test_player_cant_join_2games():
    first_game = RollDiceGame()
    second_game = RollDiceGame()
    ex_player = Player()
    ex_player.join(first_game)

    with pytest.raises(InvalidOperationException):
        ex_player.join(second_game)
