from typing import List

from .Exceptions.invalid_operation_exception import InvalidOperationException
from .player import Player


class Game:
    def __init__(self):
        self._players: List[Player] = []

    def add(self, player: Player):
        if player in self._players:
            raise InvalidOperationException("Player can't be added second time")
        self._players.append(player)

    def get_players(self):
        return self._players
