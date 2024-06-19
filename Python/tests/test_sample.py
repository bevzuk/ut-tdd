import unittest
from app import Bet, Chip, Dice, RollDiceGame, Player


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


class TestDice(unittest.TestCase):
    def test_is_rolling(self):
        dice = Dice()
        assert isinstance(dice.roll(), int)


class TestPlayer(unittest.TestCase):
    def test_cannot_join_twice_on_same_game(self):
        player = Player()
        game = RollDiceGame()
        player.join(game)

        with self.assertRaises(BaseException):
            player.join(game)

    def test_cannot_join_different_games_at_same_time(self):
        player = Player()
        game1 = RollDiceGame()
        game2 = RollDiceGame()
        player.join(game1)

        with self.assertRaises(BaseException):
            player.join(game2)

    def test_cannot_leave_game_twice(self):
        player = Player()
        game = RollDiceGame()
        player.join(game)
        player.leave_game()

        with self.assertRaises(BaseException):
            player.leave_game()

    def test_can_join_game(self):
        player = Player()
        game = RollDiceGame()
        assert player.join(game) is None

    def test_can_buy_chips(self):
        player = Player()
        chips = Chip(10)
        assert player.buy(chips) is None

    def test_can_place_bet(self):
        player = Player()
        player.buy(Chip(10))
        game = RollDiceGame()
        bet = Bet(Chip(10), 10)
        assert game.bet(player, bet) is None

    def test_cannot_place_bet_if_not_enough_chips(self):
        player = Player()
        player.buy(Chip(10))
        game = RollDiceGame()
        bet = Bet(Chip(15), 1)
        with self.assertRaises(BaseException):
            game.bet(player, bet)

    def test_can_leave_game(self):
        player = Player()
        game = RollDiceGame()
        player.join(game)
        assert player.leave_game() is None
