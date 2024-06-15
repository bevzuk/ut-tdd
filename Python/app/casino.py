from app.chips import Chips
from app.game import Game
from app.player import Player


class Casino:
    def sell(self, player: Player, chips: Chips):
        player.deposit(chips)

    def get_open_game(self):
        return Game()

    def get_players_of(self, game: Game):
        return game.get_players()
