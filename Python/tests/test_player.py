from app import Chip, RollDiceGame, Player, Bet
from unittest.mock import MagicMock
from app.Exceptions.invalid_operation_exception import InvalidOperationException

import pytest


class TestPlayer:
    @pytest.fixture
    def one_default_player_in_game(self):
        game = RollDiceGame()
        player = Player()

        player.join(game)

        return game, player

    @pytest.fixture
    def player_with_10_chips_and_game(self, one_default_player_in_game):
        game, player = one_default_player_in_game
        player.buy(Chip(10))
        return game, player

    def test_can_join_game(self, one_default_player_in_game):
        _, player = one_default_player_in_game

        assert player.is_in_game() is True

    def test_cannot_join_different_game_twice(self, one_default_player_in_game):
        _, player = one_default_player_in_game
        game_2 = RollDiceGame()

        with pytest.raises(InvalidOperationException):
            player.join(game_2)

    def test_cannot_join_same_game_twice(self, one_default_player_in_game):
        game, player = one_default_player_in_game

        with pytest.raises(InvalidOperationException):
            player.join(game)

    def test_can_win_6_bets_when_guessed_score(self, player_with_10_chips_and_game):
        game, player = player_with_10_chips_and_game

        player = Create.player(lucky=True).bet(Chip(5))
        player = Create.player(lucky=True).bet(Chip(5))
        player = Create.player(lucky=True).bet(Chip(5))
        Create.game(player).add_player(player).add_player(player).

        game.winning_score = MagicMock(return_value=6)
        game.bet(player, Bet(Chip(10), score=6))
        game.play()
        assert player.has(Chip(60))

    def test_can_lose_bet_when_not_guessed_score(self, player_with_10_chips_and_game):
        game, player = player_with_10_chips_and_game

        game.winning_score = MagicMock(return_value=6)
        game.bet(player, Bet(Chip(10), score=5))
        game.play()
        assert player.has(Chip(0))
