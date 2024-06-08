from typing import Protocol

class IRollDiceGame(Protocol):
    def add_player(self):
        pass

    def remove_player(self):
        pass
