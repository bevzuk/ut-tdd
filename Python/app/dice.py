import random


class IDice:
    @staticmethod
    def roll():
        pass


class Dice(IDice):
    @staticmethod
    def roll():
        return random.randrange(1, 6)
