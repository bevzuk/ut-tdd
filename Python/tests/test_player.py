import pytest

from Python.app import *


@pytest.fixture
def setup_game_with_one_player():
    game = RollDiceGame()
    lucky_player = Player()
    lucky_player.join(game)

    return game, lucky_player


def test_can_join_game(setup_game_with_one_player):
    _, lucky_player = setup_game_with_one_player

    assert lucky_player.is_in_game(), "Player cannot join the game"


def test_can_buy_chips():
    lucky_player = Player()
    chips = Chip(4)
    lucky_player.buy(chips)

    assert lucky_player.has(chips)


def test_can_bet(setup_game_with_one_player):
    game, lucky_player = setup_game_with_one_player
    lucky_player.buy(Chip(4))

    try:
        game.bet(lucky_player, Bet(Chip(2), 4))
    except BaseException:
        assert False, "Player cannot bet 2 chips"


def test_can_leave_game(setup_game_with_one_player):
    game, lucky_player = setup_game_with_one_player

    lucky_player.leave_game()

    assert lucky_player.is_in_game() is False, "Player cannot leave the game"


def test_cannot_join_2games(setup_game_with_one_player):
    game, lucky_player = setup_game_with_one_player
    second_game = RollDiceGame()

    with pytest.raises(BaseException):
        lucky_player.join(second_game)
