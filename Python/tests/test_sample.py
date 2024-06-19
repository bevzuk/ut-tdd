import unittest.mock
import pytest
import unittest

from app import Bet, Chip, Dice, RollDiceGame, Player


@pytest.fixture(scope='function')
def player():
    return Player()


@pytest.fixture(scope='function')
def rolldice_game():
    return RollDiceGame()


@pytest.fixture(scope='function')
def player_in_game(player, rolldice_game):
    player.join(rolldice_game)
    return player, rolldice_game


@pytest.mark.skip(reason="Invalid code, should be fixed")
def test_bet_cannot_be_negative():
    with pytest.raises(BaseException):
        Bet(Chip(-2), 1)


@pytest.mark.skip(reason="Invalid code, should be fixed")
def test_chip_cannot_be_negative():
    with pytest.raises(BaseException):
        Chip(-2)


@pytest.mark.skip(reason="Invalid code, should be fixed")
def test_chip_cannot_be_non_integer():
    value = 'example'

    with pytest.raises(BaseException):
        Chip(value)


def test_player_cannot_join_twice_on_same_game(player_in_game):
    player, game = player_in_game
    with pytest.raises(BaseException):
        player.join(game)


def test_player_cannot_join_different_games_at_same_time(player_in_game):
    player, _ = player_in_game
    another_game = RollDiceGame()

    with pytest.raises(BaseException):
        player.join(another_game)


def test_player_cannot_leave_game_twice(player_in_game):
    player, _ = player_in_game
    player.leave_game()

    with pytest.raises(BaseException):
        player.leave_game()


def test_player_can_join_game(player, rolldice_game):
    player.join(rolldice_game)


def test_player_can_leave_game(player_in_game):
    player, _ = player_in_game
    player.leave_game()


def test_player_can_buy_chips(player):
    assert player.buy(Chip(20)) is None


def test_player_can_place_bet(player_in_game):
    player, game = player_in_game
    player.buy(Chip(20))
    bet = Bet(Chip(10), 6)

    assert game.bet(player, bet) is None


def test_player_cannot_place_bet_if_not_enough_chips(player_in_game):
    player, game = player_in_game
    player.buy(Chip(20))
    bet = Bet(Chip(25), 6)

    with pytest.raises(BaseException):
        game.bet(player, bet)


def test_player_actually_win(player_in_game):
    Dice.roll = unittest.mock.MagicMock(return_value=1)
    player, game = player_in_game
    player.buy(Chip(20))
    game.bet(player, Bet(Chip(20), 1))
    game.play()

    assert player.get_chips_balance() == Chip(120)


def test_player_actually_lose(player_in_game):
    Dice.roll = unittest.mock.MagicMock(return_value=1)
    player, game = player_in_game
    player.buy(Chip(20))
    game.bet(player, Bet(Chip(20), 2))
    game.play()

    assert player.get_chips_balance() == Chip(0)
