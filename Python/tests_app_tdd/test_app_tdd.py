from app_tdd.game import Game
from app_tdd.player import Player

def test_number_players_not_enough_to_start():
    game = Game()

    assert not game.players_enough_to_start_game()

def test_number_players_enough_to_start():
    game = Game()
    player1 = Player()
    player2 = Player()

    game.add_player(player1)
    game.add_player(player2)

    assert game.players_enough_to_start_game()

def test_player_state_is_none_before_game_start():
    player = Player()

    assert player.get_current_state() is None

def test_player_can_make_move():
    player = Player()
    player.move()

    assert player.get_current_state is not None