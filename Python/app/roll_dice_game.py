from typing import List
import random

from .Exceptions.invalid_operation_exception import InvalidOperationException
from .Exceptions.too_many_players_exception import TooManyPlayersException
from .player import Player
from .bet import Bet
from .dice import Dice


class RollDiceGame:
    _players_count: int
    _bets: List

    def __init__(self):
        self._players_count = 0
        self._bets = []
        self._dice = Dice()

    def set_dice(self, dice: Dice):
        self._dice = dice

    def add_player(self):
        if self._players_count == 6:
            raise TooManyPlayersException()
        self._players_count += 1

    def remove_player(self):
        self._players_count -= 1

    def bet(self, player: Player, bet: Bet):
        if not player.has(bet.chips):
            raise InvalidOperationException

        self._bets.append({'player': player, 'chips': bet.chips, 'score': bet.score})
        player.take(bet.chips)

    def play(self):
        # winning_score = random.randrange(1, 6)
        winning_score = self._dice.roll()
        for bet in self._bets:
            if bet['score'] == winning_score:
                bet['player'].win(bet['chips'] * 6)
