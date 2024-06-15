from app.chips import Chips


class Player:
    def __init__(self):
        self._available_chips: Chips = Chips(0)

    def get_chips(self):
        return self._available_chips

    def deposit(self, chips):
        self._available_chips += chips
