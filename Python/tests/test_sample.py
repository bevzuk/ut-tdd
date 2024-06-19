import unittest

import pytest

from app import *


def test_pass():
    assert Chip(1) == Chip(1)

def test_bet_creation():
    chips = Chip(1)

    assert Bet(chips, 1)

def test_bet_should_not_create_with_float_score():
    chips = Chip(1)

    with pytest.raises(BaseException):
        Bet(chips, 1.0)

def test_bet_should_not_create_with_string_score():
    chips = Chip(1)

    with pytest.raises(BaseException):
        Bet(chips, "one")

@pytest.fixture
def set_game_and_joined_player():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    return player, game

def test_player_creation():
    assert Player()

def test_not_joined_player_should_not_be_in_game():
    player = Player()

    assert not player.is_in_game()

def test_joined_player_should_be_in_game(set_game_and_joined_player):
    player, game = set_game_and_joined_player
    assert player.is_in_game()

def test_left_player_should_not_be_in_game(set_game_and_joined_player):
    player, game = set_game_and_joined_player

    player.leave_game()

    assert not player.is_in_game()
