from typing import Protocol

from .chip import Chip


class ICasino(Protocol):
    def sell(self, chips: Chip):
        pass
