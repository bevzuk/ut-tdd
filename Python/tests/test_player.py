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

def test_player_cant_join_twice_to_one_game(setup_player_and_game):
    player, game = setup_player_and_game
    player.join(game)
    with pytest.raises(InvalidOperationException):
        player.join(game)

def test_player_can_join_after_leave(setup_player_and_game):
    player, game = setup_player_and_game
    player.join(game)
    player.leave_game()
    player.join(game)
    
def test_player_can_play_in_one_game_only(setup_player_and_game):
    player, game_one = setup_player_and_game
    game_two = RollDiceGame()
    player.join(game_one)
    with pytest.raises(InvalidOperationException):
        player.join(game_two)
        
def test_player_cant_leave_game_if_he_outside_the_game():
    player = Player()
    with pytest.raises(InvalidOperationException):
        player.leave_game()

def test_player_in_game(setup_player_and_game):
    player, game = setup_player_and_game
    player.join(game)
    assert True == player.is_in_game()


def test_game_with_multiplie_players():
    game = RollDiceGame()
    
    for _ in range(6):
        Player().join(game)

    with pytest.raises(TooManyPlayersException):
        Player().join(game)


def test_player_cannot_leave_twice(setup_player_and_game):
    player, game = setup_player_and_game
    
    player.join(game)
    player.leave_game()
    
    with pytest.raises(InvalidOperationException):
        player.leave_game()
        
# def test_player_buy_chips():
    