import unittest

from app import *


def test_pass():
    assert Chip(1) == Chip(1)

class TestBet(unittest.TestCase):
    def test_bet_creation(self):
        chips = Chip(1)
        assert Bet(chips, 1)

    def test_bet_should_not_create_with_float_score(self):
        chips = Chip(1)
        with self.assertRaises(BaseException):
            Bet(chips, 1.0)

    def test_bet_should_not_create_with_string_score(self):
        chips = Chip(1)
        with self.assertRaises(BaseException):
            Bet(chips, "one")

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        assert Player()

    def test_not_joined_player_should_not_be_in_game(self):
        player = Player()
        assert not player.is_in_game()

    def test_joined_player_should_be_in_game(self):
        player = Player()
        game = RollDiceGame()
        player.join(game)
        assert player.is_in_game()

    def test_left_player_should_not_be_in_game(self):
        player = Player()
        game = RollDiceGame()
        player.join(game)
        player.leave_game()
        assert not player.is_in_game()

    def test_player_can_buy_positive_chips(self):
        player = Player()
        assert player.buy(Chip(5))

    def test_player_can_not_buy_negative_chips(self):
        player = Player()
        with self.assertRaises(BaseException):
            player.buy(Chip(-5))
