from app import *
from  unittest.mock import MagicMock

class PlayerContext:
    
    def create_player(self):
        self.player = Player()
        return self
    
    def buy_chips(self, chip_count):
        self.player.buy(Chip(chip_count))
        return self
    
    def join(self, game):
        self.player.join(game)
        return self
    
    def get_player(self) -> Player:
        return self.player
    
    def checkChips(self, number_chips):
        return (self.player.has(Chip(number_chips)) and
                not self.player.has(Chip(number_chips + 1)))
