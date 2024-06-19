from app import Chip, RollDiceGame, Player
from app.Exceptions.invalid_operation_exception import InvalidOperationException

import pytest


class TestPlayer:

    def test_can_join_game(self):
        game = RollDiceGame()
        player_1 = Player()

        player_1.join(game)

        assert player_1.is_in_game() is True

    def test_cannot_join_different_game_twice(self):
        game_1 = RollDiceGame()
        game_2 = RollDiceGame()
        player_1 = Player()

        player_1.join(game_1)

        with pytest.raises(InvalidOperationException):
            player_1.join(game_2)

    def test_cannot_join_same_game_twice(self):
        game_1 = RollDiceGame()
        player_1 = Player()

        player_1.join(game_1)

        with pytest.raises(InvalidOperationException):
            player_1.join(game_1)

    def test_cant_join_few_games(self):
        pass

    def test_can_buy_chips(self):
        pass

    def test_can_take(self):
        pass

    def test_can_leave_game(self):
        pass
