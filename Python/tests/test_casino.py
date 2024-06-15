import pytest

from app import *


class TestCasino:
    def test_casino_has_multiple_tables(self):
        casino = Casino()

        has_free_table = casino.has_free_table()

        assert has_free_table is True

    def test_player_can_join_to_game(self):
        casino = Casino()
        player = Player()

        casino.join_to_game(player)

        assert player.is_in_game() is True

    def test_player_cant_join_to_game_when_there_are_no_free_tables(self):
        casino = Casino(tables=5)

        for i in range(5 * RollDiceGame.MAX_PLAYER_COUNT):
            player = Player()
            casino.join_to_game(player)

        player = Player()
        with pytest.raises(InvalidOperationException):
            casino.join_to_game(player)

    def test_player_can_bet(self):
        casino = Casino()
        player = Player()
        player.buy(Chip(1))
        game = casino.join_to_game(player)

        game.bet(player, Bet(Chip(1), face_value=0))

        assert player.is_in_game() is True
        assert player.has(Chip(0))
        assert not player.has(Chip(1))

    def test_casino_informs_if_there_no_free_seats(self):
        casino = Casino(tables=1)

        for i in range(1 * RollDiceGame.MAX_PLAYER_COUNT):
            player = Player()
            casino.join_to_game(player)

        assert casino.has_free_table() is False

    def test_casino_has_bank_of_chips(self):
        casino = Casino(chips_in_bank = 10)
        player = Player()

        player.buy2(casino, 9)

        assert casino.has_chips(1) is True
        assert casino.has_chips(2) is False
