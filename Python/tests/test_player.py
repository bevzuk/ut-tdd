from app import *


def test_can_join_to_game():
    player = Player()
    game = RollDiceGame()

    player.join(game)

    assert player.is_in_game() is True


def test_has_zero_chips_on_init():
    player = Player()

    assert player.has(0) is True

def test_can_buy_chips():
    player = Player()

    player.buy(2)

    assert player.has(2) is True


def test_can_make_bet():
    player = Player()

    # TODO: to do

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




