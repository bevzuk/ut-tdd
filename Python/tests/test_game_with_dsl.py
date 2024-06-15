from unittest.mock import MagicMock

from app import *
from .dsl.create import Create


class TestRollDiceGame:
    # Exercise 3 – make fixture
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
        game = Create.game()
        player = Create.player().lucky_in(game).with_bet(10)

        game.play()

        assert player.has(Chip(60))

    def test_unlucky_player_loses_his_bet_dsl(self):
        game = Create.game()
        player = (Create.player()
                  .unlucky_in(game)
                  .with_chips(100)
                  .with_bet(10))

        game.play()

        assert player.has(Chip(90))
        assert not player.has(Chip(91))
