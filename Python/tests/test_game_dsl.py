from Python.app import *
from Python.tests.dsl import *


def test_player_wins():
    state = Helper.create_game(fixed_dice_value=5).with_one_player().buy_chips_for_player(number=0, count=4)
    state = state.player_place_a_bet(number=0, chip_count=4, score=5)

    state.game.play()

    assert state.check_player_chips(number=0, chip_count=4*6), "Game plays wrong"


def test_player_lose():
    state = Helper.create_game(fixed_dice_value=5).with_one_player().buy_chips_for_player(number=0, count=4)
    state = state.player_place_a_bet(number=0, chip_count=4, score=4)

    state.game.play()

    assert state.check_player_chips(number=0, chip_count=0), "Game plays wrong"
