from typing import List

from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.chips import Chips
from app.game import Game
from app.player import Player


class Casino:
    def __init__(self):
        self._games: List[Game] = []

    def sell(self, player: Player, chips: Chips):
        player.deposit(chips)

    def get_open_game(self):
        game = Game()
        self._games.append(game)
        return game

    def get_players_of(self, game: Game):
        return game.get_players()

    def add(self, player: Player, game: Game):
        if self.player_already_in_game(player):
            raise InvalidOperationException("Player should leave the game before joining another game")
        game.add(player)

    def player_already_in_game(self, player: Player):
        for game in self._games:
            if player in game.get_players():
                return True
        return False
