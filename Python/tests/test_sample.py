from app import *


def test_pass():
    assert Chip(1) == Chip(1)


def test_dice_range():
    assert Dice.roll() in range(1, 6)

