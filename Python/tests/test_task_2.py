from pytest import fixture, mark
from app import Player, RollDiceGame, Chip, Bet


@fixture(autouse=True)
def setup_game_and_player_with_10_chips():
    test_player = Player()
    test_game = RollDiceGame()
    test_player.join(test_game)
    test_player.buy(Chip(10))
    return test_player, test_game


@mark.usefixtures("setup_game_and_player_with_10_chips")
class TestPlayer():
    def test_can_join_game(self, setup_game_and_player_with_10_chips):
        player, _ = setup_game_and_player_with_10_chips
        assert player.is_in_game() is True

    def test_can_buy_chips(self, setup_game_and_player_with_10_chips):
        player, _ = setup_game_and_player_with_10_chips
        assert player.has(Chip(10)) is True

    def test_can_bet(self, setup_game_and_player_with_10_chips):
        player, game = setup_game_and_player_with_10_chips
        game.bet(player, Bet(Chip(10), 6))
        game.play()
        assert player.has(
            Chip(60)) is True or player.has(Chip(0)) is True

    def test_can_leave_game(self, setup_game_and_player_with_10_chips):
        player, _ = setup_game_and_player_with_10_chips
        player.leave_game()
        assert player.is_in_game() is False
