from unittest.mock import MagicMock

import pytest

from app import *
import unittest

from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.Exceptions.too_many_players_exception import TooManyPlayersException


@pytest.fixture
def setup_player_with_10_chips_in_game():
    game = RollDiceGame()
    player = Player()
    player.buy(Chip(10))
    player.join(game)
    return player, game


def test_pass():
    assert Chip(1) == Chip(1)


def test_player_buy_chips():
    chips = Chip(3)

    player = Player()
    player.buy(chips)

    assert player.has(Chip(4)) is False
    assert player.has(Chip(3)) is True


#def test_init_player():
#    player = Player()
#    assert player._available_chips == Chip(0)
#    assert player._current_game is None

def test_player_can_join_game():
    new_player = Player()
    game = RollDiceGame()

    new_player.join(game)
    assert new_player.is_in_game()


class TestGame(unittest.TestCase):
    def test_player_whithout_chips_can_not_bet(self):
        new_player = Player()
        game = RollDiceGame()

        new_player.join(game)

        with self.assertRaises(BaseException):
            game.bet(new_player, Bet(Chip(2), 6))

    def test_player_can_bet(self):
        new_player = Player()

        game = RollDiceGame()

        new_player.join(game)
        new_player.buy(Chip(10))

        game.bet(new_player, Bet(Chip(2), 6))


@pytest.fixture
def setup_game_with_6_players():
    game = RollDiceGame()
    players = [Player() for _ in range(6)]
    for player in players:
        player.join(game)

    return game


@pytest.fixture
def setup_player_and_game():
    game = RollDiceGame()
    player = Player()

    return player, game


def test_unable_to_join_to_game_with_6_players(setup_game_with_6_players):
    player = Player()
    game = setup_game_with_6_players

    with pytest.raises(TooManyPlayersException):
        player.join(game)


def test_able_to_join_to_game_with_less_than_6_players(setup_game_with_6_players):
    player = Player()
    game = setup_game_with_6_players

    with pytest.raises(TooManyPlayersException):
        player.join(game)


def test_mock_can_work():
    player = Player()
    player.buy = MagicMock(return_value=1)

    magic_mock_value = player.buy()

    assert magic_mock_value == 1


def test_player_can_win(setup_player_with_10_chips_in_game):
    player, game = setup_player_with_10_chips_in_game
    game.dice.roll = MagicMock(return_value=1)

    game.bet(player, Bet(Chip(5), 1))
    game.play()

    assert player.has(Chip(15)) is True


def test_player_can_lose(setup_player_with_10_chips_in_game):
    player, game = setup_player_with_10_chips_in_game
    game.dice.roll = MagicMock(return_value=1)

    game.bet(player, Bet(Chip(5), 2))
    game.play()

    assert player.has(Chip(10)) is False
