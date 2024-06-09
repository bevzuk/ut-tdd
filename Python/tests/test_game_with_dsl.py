from unittest.mock import MagicMock

from app.bet import Bet
from app.chip import Chip
from app.player import Player
from app.roll_dice_game import RollDiceGame, Dice


class TestRollDiceGame:

    def test_lucky_player_wins_6_bets(self):
        player = Player()
        dice = Dice()
        dice.roll = MagicMock(return_value=1)
        game = RollDiceGame(dice)
        player.join(game)
        player.buy(Chip(10))
        game.bet(player, Bet(Chip(10), 1))

        game.play()

        assert player.has(Chip(60))

    def test_lucky_player_wins_6_bets_dsl(self):
        player = Player()
        dice = Dice()
        dice.roll = MagicMock(return_value=1)
        game = RollDiceGame(dice)
        player.join(game)
        player.buy(Chip(10))
        game.bet(player, Bet(Chip(10), 1))

        game.play()

        assert player.has(Chip(60))
