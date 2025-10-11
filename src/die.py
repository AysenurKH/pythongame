import random

DICE = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]


class Die:

    value = None

    def __init__(self, value=None):
        if value:
            self.value = value

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

    def __str__(self):
        return DICE[self.value-1] if self.value else "N/A"
