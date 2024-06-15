from typing import List

from .player import Player


class Game:
    def __init__(self):
        self._players: List[Player] = []

    def add(self, player: Player):
        self._players.append(player)

    def get_players(self):
        return self._players
