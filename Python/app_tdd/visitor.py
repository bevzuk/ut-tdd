class Visitor:
    age: int
    promille: float
    banruptcy: bool

    def __init__(self, age, promille, bankruptcy):
        self.age = age
        self.promille = promille
        self.banruptcy = bankruptcy

    def get_age(self):
        return self.age

    def get_promille(self):
        return self.promille

    def get_bankruptcy(self):
        return self.banruptcy
