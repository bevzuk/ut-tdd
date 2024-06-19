import pytest
from app import *


@pytest.fixture
def player():
    player = Player()
    return player


@pytest.fixture
def game():
    game = RollDiceGame()
    return game

@pytest.fixture
def player_with_10_chips(player):
    player.buy(Chip(10))
    return player
