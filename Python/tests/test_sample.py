from app import *
import pytest



def test_game_cannot_be_played_when_no_players():
    game = Game()
    assert not game.is_ready_to_start()
    with pytest.raises(NoPlayersException):
        game.play()

def test_game_can_accept_single_player():
    game = Game()
    player = Player()
    game.accept(player)
    assert game.get_players_count() == 1

def test_game_can_be_played_when_more_than_one_players():
    game = Game()
    player1 = Player()
    player2 = Player()
    game.accept(player1)
    game.accept(player2)

    assert game.is_ready_to_start()

# def test_game_cannot_be_started_when_more_than_6_players():
#     game = Game()
#     for _ in range(6):
#         player = Player()
#         game.accept(player)

#     assert not game.is_ready_to_start()
