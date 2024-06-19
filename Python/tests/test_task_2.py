from pytest import fixture, mark
from unittest.mock import MagicMock
from app import Player, RollDiceGame, Chip, Bet, Dice


@fixture()
def setup_game_and_player_with_10_chips():
    test_player = Player()
    test_player.buy(Chip(10))
    return test_player


@fixture
def setup_game_with_defined_dice_value(setup_game_and_player_with_10_chips):
    def _setup_game_with_defined_dice_value(is_win=True):
        dice = Dice()
        if is_win:
            dice.roll = MagicMock(return_value=6)
        else:
            dice.roll = MagicMock(return_value=1)

        test_game = RollDiceGame(dice)
        test_player = setup_game_and_player_with_10_chips
        test_player.join(test_game)
        test_game.bet(test_player, Bet(Chip(10), 6))
        test_game.play()
        return test_player
    return _setup_game_with_defined_dice_value


@mark.usefixtures("setup_game_and_player_with_10_chips")
class TestPlayer():
    def test_can_join_game(self, setup_game_and_player_with_10_chips):
        player = setup_game_and_player_with_10_chips
        game = RollDiceGame(Dice())
        player.join(game)
        assert player.is_in_game() is True

    def test_can_buy_chips(self, setup_game_and_player_with_10_chips):
        player = setup_game_and_player_with_10_chips
        assert player.has(Chip(10)) is True

    def test_can_bet(self, setup_game_and_player_with_10_chips):
        player = setup_game_and_player_with_10_chips
        game = RollDiceGame(Dice())
        player.join(game)
        game.bet(player, Bet(Chip(10), 6))
        game.play()
        assert player.has(
            Chip(60)) is True or player.has(Chip(0)) is True

    def test_can_leave_game(self, setup_game_and_player_with_10_chips):
        player = setup_game_and_player_with_10_chips
        game = RollDiceGame(Dice())
        player.join(game)
        player.leave_game()
        assert player.is_in_game() is False

    def test_should_win(self, setup_game_with_defined_dice_value):
        player = setup_game_with_defined_dice_value(is_win=True)
        assert player.has(Chip(60)) is True

    def test_should_lose(self, setup_game_with_defined_dice_value):
        player = setup_game_with_defined_dice_value(is_win=False)
        assert player.has(Chip(0)) is True
