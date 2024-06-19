from enum import Enum
import random

class PossibleMoves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Player:
    def __init__(self) -> None:
        self.state = None
        
    def get_current_state(self):
        return self.state
    
    def move(self):
        self.state = random.randrange(1, len(PossibleMoves) + 1)
