from Python.app import *


def test_game_add_player():
    game = RollDiceGame()
    game.add_player()

    assert game._players_count == 1
