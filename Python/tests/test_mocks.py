from unittest.mock import MagicMock

from app import Player, RollDiceGame, Chip, Bet, Dice


class GameDSL:
    def __init__(self):
        self.dice = Dice()
        self.player = Player()
        self.game = RollDiceGame(self.dice)
        self.player.join(self.game)
        self.player.buy(Chip(10))

    def set_win(self):
        self.dice.roll = MagicMock(return_value=6)
        return self

    def set_loss(self):
        self.dice.roll = MagicMock(return_value=1)
        return self

    def play_game(self):
        self.game.bet(self.player, Bet(Chip(10), 6))
        self.game.play()
        return self.player


class TestPlayer:
    def test_should_win(self):
        player = GameDSL().set_win().play_game()
        assert player.has(Chip(60)) is True

    def test_should_lose(self):
        player = GameDSL().set_loss().play_game()
        assert player.has(Chip(0)) is True
