import pytest
from app import *
from unittest.mock import MagicMock


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

@pytest.fixture
def get_mocked_dice():
    dice = Dice()
    dice.roll = MagicMock(return_value=1)
    return dice