from random import randint
class RussianRoulete:
    _num_of_players: int
    _players: List[Players]
    def __init__(self):
        self._num_of_players = 0
    
    def add_player(self, player):
        self._num_of_players += 1

    def num_of_players(self):
        return self._num_of_players
    @staticmethod
    def roll() -> str:
        val = randint(0,5)
        if val == 0:
            return "BOOOM!!!!"
        return "You are lucky boy!"

class Player:
    _is_alive: bool
    _name: str
    def __init__(self, name: str):
        self._is_alive = True
        self._name = name
    def get_name(self):
        return self._name
    def is_alive(self):
        return self._is_alive
    def kill(self):
        self._is_alive = False