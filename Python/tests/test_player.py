from app import *
import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/Python")
from app.Exceptions.invalid_operation_exception import InvalidOperationException

def test_player_cant_join_twice_to_one_game():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    with pytest.raises(InvalidOperationException):
        player.join(game)

def test_player_can_join_after_leave():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    player.leave_game()
    player.join(game)
    
def test_player_can_play_in_one_game_only():
    player = Player()
    game_one = RollDiceGame()
    game_two = RollDiceGame()
    player.join(game_one)
    with pytest.raises(InvalidOperationException):
        player.join(game_two)
        
def test_player_cant_leave_game_if_he_outside_the_game():
    player = Player()
    with pytest.raises(InvalidOperationException):
        player.leave_game()

def test_player_in_game():
    player = Player()
    game_one = RollDiceGame()
    player.join(game_one)
    assert True == player.is_in_game()

def test_player_in_game():
    player = Player()
    game_one = RollDiceGame()
    player.join(game_one)
    assert True == player.is_in_game()

def test_game_with_multiplie_players():
    player_1 = Player()
    player_2 = Player()
    player_3 = Player()
    player_4 = Player()
    
    game = RollDiceGame()
    player_1.join(game)
    player_2.join(game)
    player_3.join(game)
    player_4.join(game)


