import random


class IDice:
    @staticmethod
    def roll():
        pass


class Dice(IDice):
    @staticmethod
    def roll():
        return random.randint(1, 6)
