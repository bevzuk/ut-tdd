from app import *
import unittest


class TestPlayer(unittest.TestCase):

    def test_can_join_game(self):
        test_player = Player()
        test_player.join(RollDiceGame())
        assert test_player.is_in_game() is True

    def test_can_buy_chips(self):
        test_player = Player()
        test_player.buy(Chip(10))
        assert test_player.has(Chip(10)) is True

    def test_can_bet(self):
        test_player = Player()
        test_game = RollDiceGame()
        test_player.join(test_game)
        test_player.buy(Chip(10))
        test_game.bet(test_player, Bet(Chip(10), 6))
        test_game.play()
        assert test_player.has(
            Chip(60)) is True or test_player.has(Chip(0)) is True

    def test_can_leave_game(self):
        test_player = Player()
        test_player.join(RollDiceGame())
        test_player.leave_game()
        assert test_player.is_in_game() is False
