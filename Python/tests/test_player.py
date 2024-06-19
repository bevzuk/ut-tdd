from app import Chip, RollDiceGame, Player
from app.Exceptions.invalid_operation_exception import InvalidOperationException

import pytest


class TestPlayer:
    @pytest.fixture
    def one_default_player_in_default_game(self):
        game = RollDiceGame()
        player = Player()

        player.join(game)

        return game, player

    def test_can_join_game(self, one_default_player_in_default_game):
        _, player = one_default_player_in_default_game

        assert player.is_in_game() is True

    def test_cannot_join_different_game_twice(self, one_default_player_in_default_game):
        _, player = one_default_player_in_default_game
        game_2 = RollDiceGame()

        with pytest.raises(InvalidOperationException):
            player.join(game_2)

    def test_cannot_join_same_game_twice(self, one_default_player_in_default_game):
        game, player = one_default_player_in_default_game

        with pytest.raises(InvalidOperationException):
            player.join(game)

    def test_cant_join_few_games(self):
        pass

    def test_can_buy_chips(self):
        pass

    def test_can_take(self):
        pass

    def test_can_leave_game(self):
        pass
