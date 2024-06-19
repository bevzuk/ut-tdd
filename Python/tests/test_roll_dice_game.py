import pytest
from app.roll_dice_game import RollDiceGame
from app.Exceptions.too_many_players_exception import TooManyPlayersException



def test_init():
    game = RollDiceGame()
    assert game._players_count == 0
    assert game._bets == []
    
def test_add_single_player():
    game = RollDiceGame()
    game.add_player()
    assert game._players_count == 1

def test_add_multiple_players():
    game = RollDiceGame()
    for _ in range(4):
        game.add_player()
    assert game._players_count == 4

def test_overflow_players():
    game = RollDiceGame()
    for _ in range(6):
        game.add_player()
    with pytest.raises(TooManyPlayersException):
        game.add_player()


