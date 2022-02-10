class GoodIfrit:
    def __init__(self, height, name, goodness):
        self.name = name
        self.height = height
        self.goodness = goodness

    def change_goodness(self, amount):
        self.goodness = max(self.goodness + amount, 0)

    def __tuple__(self):
        return self.goodness, self.height, self.name

    def __add__(self, other):
        return GoodIfrit(self.height + other, self.name, self.goodness)

    def __eq__(self, other):
        return self.__tuple__() == other.__tuple__()

    def __gt__(self, other):
        return self.__tuple__() > other.__tuple__()

    def __lt__(self, other):
        return self.__tuple__() < other.__tuple__()

    def __le__(self, other):
        return self.__tuple__() <= other.__tuple__()

    def __ge__(self, other):
        return self.__tuple__() >= other.__tuple__()

    def __ne__(self, other):
        return self.__tuple__() != other.__tuple__()

    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"

    def __call__(self, num):
        return num * self.goodness // self.height