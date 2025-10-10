class DiceHand:

    dice = []

    def __init__(self):
        pass

    def add_die(self, die):
        self.dice.append(die)

    def get_value(self):
        return sum(die.value for die in self.dice)

    def __str__(self):
        return " ".join(map(str, self.dice))

    def empty(self):
        self.dice.clear()
