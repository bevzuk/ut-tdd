from unittest.mock import MagicMock

import pytest

from app import *


@pytest.fixture
def setup_player_in_game():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    player_chips = Chip(10)
    player.buy(player_chips)
    return player, game, player_chips


def test_can_make_bet(setup_player_in_game):
    player, game, chips = setup_player_in_game

    game.bet(player, Bet(chips, 10))

    assert not player.has(chips)


def test_win_6_chips(setup_player_in_game):
    player, game, chips = setup_player_in_game
    game.bet(player, Bet(chips, 1))

    game.roll = MagicMock(return_value=1)

    game.play()

    assert player.has(Chip(60))


def test_lose_bet(setup_player_in_game):
    player, game, chips = setup_player_in_game
    game.bet(player, Bet(chips, 6))

    game.roll = MagicMock(return_value=1)

    game.play()

    assert player.has(Chip(0))
