import sys
import os

import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.rus_roul import Player, RussianRoulete

TEST_NAME = "Zlatan Ibragimovich"
TEST_NUM_OF_PLAYERS = 5

@pytest.fixture
def create_player():
    player = Player(TEST_NAME)
    return player

@pytest.fixture
def create_game():
    game = RussianRoulete()
    return game

def test_get_result():
    assert RussianRoulete.roll() is not None

def test_default_player(create_player):
    player = create_player
    assert player.get_name() == TEST_NAME 
    assert player.is_alive() == True

def test_kill_player(create_player):
    player = create_player
    player.kill()
    assert player.is_alive() == False

def test_can_add_player_in_game(create_game, create_player):
    game = create_game
    player = create_player
    game.add_player(player)
    assert game.num_of_players == 1
    
    