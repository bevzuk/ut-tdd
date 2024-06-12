import random


class Dice:
    @staticmethod
    def roll():
        return random.randrange(1, 6)
