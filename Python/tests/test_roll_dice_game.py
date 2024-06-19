import pytest
from app.roll_dice_game import RollDiceGame
from app.Exceptions.too_many_players_exception import TooManyPlayersException
from app.player import Player


def test_single_player_can_join_game():
    game = RollDiceGame()
    game.add_player()
    # NEVER DO IT!!
    assert True

def test_when_overflow_game_players_should_assert():
    game = RollDiceGame()
    for _ in range(6):
        game.add_player()
    with pytest.raises(TooManyPlayersException):
        game.add_player()






