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
        casino = Casino(tables=5, seats_per_table=2)

        for i in range(5 * 2):
            player = Player()
            casino.join_to_game(player)

        player = Player()
        with pytest.raises(InvalidOperationException):
            casino.join_to_game(player)
