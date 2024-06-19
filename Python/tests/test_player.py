import pytest

from app import *


@pytest.fixture
def setup_player_in_game():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    return player, game


def test_can_join_to_game(setup_player_in_game):
    player, _ = setup_player_in_game

    assert player.is_in_game() is True


def test_has_zero_chips_on_init():
    player = Player()

    assert player.has(Chip(0)) is True


def test_can_buy_chips():
    player = Player()

    player.buy(2)

    assert player.has(2) is True





def test_can_leave_game():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    player.leave_game()
    assert player.is_in_game() is False


def test_player_not_in_game():
    player = Player()
    assert player.is_in_game() is False
