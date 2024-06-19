from unittest.mock import MagicMock

from pytest import fixture

from app import Player, RollDiceGame, Chip, Bet, Dice


@fixture
def setup_game_with_defined_dice_value():
    def _setup_game_with_defined_dice_value(is_win=True):
        dice = Dice()
        if is_win:
            dice.roll = MagicMock(return_value=6)
        else:
            dice.roll = MagicMock(return_value=1)

        test_game = RollDiceGame(dice)
        test_player = Player()
        test_player.join(test_game)
        test_player.buy(Chip(10))
        test_game.bet(test_player, Bet(Chip(10), 6))
        test_game.play()
        return test_player
    return _setup_game_with_defined_dice_value


class TestPlayer():
    def test_should_win(self, setup_game_with_defined_dice_value):
        player = setup_game_with_defined_dice_value(is_win=True)
        assert player.has(Chip(60)) is True

    def test_should_lose(self, setup_game_with_defined_dice_value):
        player = setup_game_with_defined_dice_value(is_win=False)
        assert player.has(Chip(0)) is True
