from unittest.mock import MagicMock

import pytest
from app import *


@pytest.fixture
def setup_player_and_game():
    player = Player()
    game = RollDiceGame(Dice())
    player.join(game)
    return player, game

# Exercise 1
def test_player_can_make_bet(setup_player_and_game):
    player, game = setup_player_and_game
    player.buy(Chip(1))

    game.bet(player, Bet(Chip(1), 6))

    assert player.has(Chip(1)) is False
    assert player.has(Chip(0))


# Exercise 2
def test_player_cant_make_bet_without_chips(setup_player_and_game):
    player, game = setup_player_and_game

    with pytest.raises(InvalidOperationException) as e:
        game.bet(player, Bet(Chip(1), 1))


def test_player_can_make_two_bets_on_different_face_values(setup_player_and_game):
    player, game = setup_player_and_game
    player.buy(Chip(2))

    game.bet(player, Bet(Chip(1), 6))
    game.bet(player, Bet(Chip(1), 5))

    assert player.has(Chip(1)) is False
    assert player.has(Chip(0))
