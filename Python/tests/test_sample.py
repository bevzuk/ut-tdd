from app import *
import unittest


class TestBet(unittest.TestCase):
    def test_bet_non_negative(self):
        with self.assertRaises(Exception):
            Bet(Chip(-2), 1)


class TestGame(unittest.TestCase):
    pass

class TestPlayer(unittest.TestCase):
    pass

def test_pass():
    assert Chip(1) == Chip(1)
