from app import *
import unittest


class TestBet(unittest.TestCase):
    @unittest.skip('Invalid code, should be fixed')
    def test_cannot_be_negative(self):
        with self.assertRaises(BaseException):
            Bet(Chip(-2), 1)


class TestChip(unittest.TestCase):
    @unittest.skip('Invalid code, should be fixed')
    def test_cannot_be_negative(self):
        with self.assertRaises(BaseException):
            Chip(-2)

    @unittest.skip('Invalid code, should be fixed')
    def test_cannot_be_not_integer(self):
        value = "example"
        with self.assertRaises(BaseException):
            Chip(value)


class TestGame(unittest.TestCase):
    pass


class TestPlayer(unittest.TestCase):
    def test_cannot_join_twice_on_same_game(self):
        player = Player()
        game = RollDiceGame()
        player.join(game)

        with self.assertRaises(BaseException):
            player.join(game)

    def test_cannot_join_different_games(self):
        player = Player()
        game1 = RollDiceGame()
        game2 = RollDiceGame()
        player.join(game1)

        with self.assertRaises(BaseException):
            player.join(game2)


def test_pass():
    assert Chip(1) == Chip(1)
