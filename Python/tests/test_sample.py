from app import *


def test_pass():
    assert Chip(1) == Chip(1)

def test_dice_le6():
    assert Dice.roll() <= 6

def test_dice_ge1():
    assert Dice.roll() >= 1

def test_bet_init():
    bet = Bet(Chip(1), 1)
    assert bet.chips == Chip(1)
    assert bet.score == 1

def test_chip_ge():
    chip1 = Chip(1)
    chip2 = Chip(2)
    assert chip2 >= chip1

def test_chip_le():
    chip1 = Chip(1)
    chip2 = Chip(2)
    assert chip1 <= chip2

def test_chip_add():
    chip1 = Chip(1)
    chip2 = Chip(2)
    chip_sum = chip1 + chip2
    assert chip_sum._amount == 3

def test_chip_sub():
    chip1 = Chip(11)
    chip2 = Chip(29)
    chip_sub = chip2 - chip1
    assert chip_sub._amount == 18

def test_chip_mul():
    chip1 = Chip(9945)
    chip_mul = chip1 * 198
    assert chip_mul._amount == 1969110

def test_player_init():
    player = Player()
    assert player._available_chips._amount == 0

