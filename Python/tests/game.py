from app import *
from  unittest.mock import MagicMock
from .player_dsl import PlayerContext

class GameProcess:
    def __init__(self):
        self.game = None

    def create_game(self):
        self.game = RollDiceGame()
        return self
    
    def create_game_with_roll(self, roll_value):
        dice = Dice()
        dice.roll = MagicMock(return_value=roll_value)
        self.game = RollDiceGame(dice)
        return self
    
    def add_player(self, player : PlayerContext):
        player.join(self.game)
        return self
    
    def bet(self, player, bet, score):
        self.game.bet(player, Bet(Chip(bet), score))
        return self
    
    def start_game(self):
        self.game.play()
        return self
