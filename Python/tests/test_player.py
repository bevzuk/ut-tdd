from unittest.mock import MagicMock

import pytest
from app import *


# Exercise 1
def test_player_can_buy_chips():
    player = Player()
    player.buy(Chip(1))
    assert player.has(Chip(1))


def test_player_can_make_bet():
    player = Player()
    player.buy(Chip(1))
    game = RollDiceGame(Dice())
    player.join(game)

    game.bet(player, Bet(Chip(1), 6))

    assert player.has(Chip(1)) is False
    assert player.has(Chip(0))


# Exercise 2
def test_player_by_default_has_no_chips():
    player = Player()
    assert player.has(Chip(0))


def test_player_cant_make_bet_without_chips():
    player = Player()
    game = RollDiceGame(Dice())
    player.join(game)

    with pytest.raises(InvalidOperationException) as e:
        game.bet(player, Bet(Chip(1), 1))


def test_player_can_make_two_bets_on_different_face_values():
    player = Player()
    player.buy(Chip(2))
    game = RollDiceGame(Dice())
    player.join(game)

    game.bet(player, Bet(Chip(1), 6))
    game.bet(player, Bet(Chip(1), 5))

    assert player.has(Chip(1)) is False
    assert player.has(Chip(0))


def test_player_can_make_two_bets_on_the_same_face_value():
    player = Player()
    player.buy(Chip(2))
    game = RollDiceGame(Dice())
    player.join(game)

    game.bet(player, Bet(Chip(1), 6))
    game.bet(player, Bet(Chip(1), 6))

    assert player.has(Chip(1)) is False
    assert player.has(Chip(0))

# Exercise 3 – make fixture

# Exercise 4 - test doubles

def test_player_can_win_two_bets():
    player = Player()
    player.buy(Chip(3))
    dice = Dice()
    dice.roll = MagicMock(return_value=6)
    game = RollDiceGame(dice)
    player.join(game)
    game.bet(player, Bet(Chip(1), 6))
    game.bet(player, Bet(Chip(2), 6))

    game.play()

    assert player.has(Chip(19)) is False
    assert player.has(Chip(18))


def test_player_by_default_not_in_game():
    player = Player()
    assert player.is_in_game() is False


def test_player_can_join_game():
    player = Player()

    player.join(RollDiceGame(Dice()))

    assert player.is_in_game() is True


def test_player_can_leave_game():
    player = Player()
    player.join(RollDiceGame(Dice()))

    player.leave_game()

    assert not player.is_in_game()


@pytest.mark.skip
def test_player_can_loose():
    player = Player()
    game = RollDiceGame(Dice())
    player.join(game)
    player.buy(Chip(10))
    game.bet(player, Bet(Chip(10), 1))

    game.play()

    assert not player.has(Chip(1))
