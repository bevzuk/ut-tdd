import pytest
from app.roll_dice_game import RollDiceGame
from app.Exceptions.too_many_players_exception import TooManyPlayersException
from app.player import Player


def test_single_player_can_join_game():
    game = RollDiceGame()
    game.add_player()
    assert True

def test_when_overflow_game_players_should_assert():
    game = RollDiceGame()
    for _ in range(6):
        game.add_player()
    with pytest.raises(TooManyPlayersException):
        game.add_player()

# def test_game_init():
#     game = RollDiceGame()
#     assert game._players_count == 0
#     assert game._bets == []
        
# def test_game_can_add_single_player():
#     game = RollDiceGame()
#     game.add_player()
#     assert game._players_count == 1

# def test_game_can_add_multiple_players():
#     game = RollDiceGame()
#     for _ in range(4):
#         game.add_player()
#     assert game._players_count == 4





