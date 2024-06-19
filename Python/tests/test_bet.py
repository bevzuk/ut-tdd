from Python.app import *


def test_bet_creation():
    bet_ex = Bet(score=1, chips=Chip(1))
    assert bet_ex.score == 1 and bet_ex.chips == Chip(1)


