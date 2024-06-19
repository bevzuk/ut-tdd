from app import *


def test_can_join_game(game, player):
    player.join(game)

    assert player.is_in_game()


def test_can_leave_game(game, player):
    player.join(game)

    player.leave_game()

    assert player.is_in_game() is False


def test_can_buy_chips(player):
    player.buy(Chip(10))

    assert (player.has(Chip(10)) is True)
    assert (player.has(Chip(11)) is False)


def test_can_win(player_with_10_chips):
    player.win(Chip(10))

    assert (player.has(Chip(20)) is True)


def test_can_take(player_with_10_chips):
    player.take(Chip(5))

    assert (player.has(Chip(5)) is True)


def test_has_initial_zero_chips(player):
    assert (player.has(Chip(0)) is True)


def test_has_equals_chips(player):
    player.buy(Chip(10))

    assert (player.has(Chip(10)) is True)


def test_has_less_chips(player):
    player.buy(Chip(10))

    assert (player.has(Chip(5)) is True)


def test_has_not_enough_chips(player):
    player.buy(Chip(5))

    assert (player.has(Chip(10)) is False)
