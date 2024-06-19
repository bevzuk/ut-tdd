from app import *


def test_can_join_game():
    game = RollDiceGame()
    player = Player()

    player.join(game)

    assert player.is_in_game()


def test_can_leave_game():
    game = RollDiceGame()
    player = Player()
    player.join(game)

    player.leave_game()

    assert player.is_in_game() is False


def test_can_buy_chips():
    player = Player()

    player.buy(Chip(10))

    assert (player.has(Chip(10)) is True)
    assert (player.has(Chip(11)) is False)


def test_can_win():
    player = Player()
    player.buy(Chip(10))

    player.win(Chip(10))

    assert (player.has(Chip(20)) is True)


def test_can_take():
    player = Player()
    player.buy(Chip(10))

    player.take(Chip(5))

    assert (player.has(Chip(5)) is True)


def test_has_initial_zero_chips():
    player = Player()
    assert (player.has(Chip(0)) is True)


def test_has_equals_chips():
    player = Player()

    player.buy(Chip(10))

    assert (player.has(Chip(10)) is True)


def test_has_less_chips():
    player = Player()

    player.buy(Chip(10))

    assert (player.has(Chip(5)) is True)


def test_has_not_enough_chips():
    player = Player()

    player.buy(Chip(5))

    assert (player.has(Chip(10)) is False)
