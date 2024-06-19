from app import *


def test_pass():
    assert Chip(1) == Chip(1)

def test_buy():
    chips = Chip(3)
    player = Player()
    player.buy(chips)
    assert player._available_chips == chips

def test_init_player():
    player = Player()
    assert player._available_chips == Chip(0)
    assert player._current_game is None

