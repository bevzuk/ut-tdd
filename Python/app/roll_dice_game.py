from typing import List

from .Exceptions.invalid_operation_exception import InvalidOperationException
from .Exceptions.too_many_players_exception import TooManyPlayersException
from .dice import Dice
from .player import Player
from .bet import Bet


class RollDiceGame:
    MAX_PLAYER_COUNT = 6
    _players_count: int
    _bets: List

    def __init__(self, dice: Dice):
        self._dice = dice
        self._players_count = 0
        self._bets = []

    def add_player(self):
        if self._players_count == RollDiceGame.MAX_PLAYER_COUNT:
            raise TooManyPlayersException()
        self._players_count += 1

    def remove_player(self):
        self._players_count -= 1

    def bet(self, player: Player, bet: Bet):
        if not player.has(bet.chips):
            raise InvalidOperationException

        self._bets.append({'player': player, 'chips': bet.chips, 'face_value': bet.face_value})
        player.take(bet.chips)

    def play(self):
        winning_face_value = self._dice.roll()
        for bet in self._bets:
            if bet['face_value'] == winning_face_value:
                bet['player'].win(bet['chips'] * 6)
