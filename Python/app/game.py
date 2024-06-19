from .player import Player

class NoPlayersException(BaseException):
    pass

class Game:
    def __init__(self):
        self._players_count = 0
    
    def get_players_count(self):
        return self._players_count

    def play(self):
        if self._players_count == 0:
            raise NoPlayersException

    def accept(self, player: Player):
        self._players_count += 1
    
    def is_ready_to_start(self):
        return True if self._players_count > 1 else False