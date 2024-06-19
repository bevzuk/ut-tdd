from app import *

def test_buy():
    player = Player()
    player.buy(Chip(10))
    assert (player.has(Chip(10)) is True)

def test_win():
    player = Player()
    player.buy(Chip(10))
    player.win(Chip(10))
    assert (player.has(Chip(20)) is True)

def test_take():
    player = Player()
    player.buy(Chip(10))
    player.take(Chip(5))
    assert (player.has(Chip(5)) is True)

def test_has_initial():
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


    