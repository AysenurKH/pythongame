from src.dice_hand import DiceHand


class Player:

    def __init__(self, name):
        self.dice_hand = DiceHand()
        self.name = name
        self.score = 0

    def set_name(self, new_name):
        self.name = new_name

    def get_score(self):
        return self.score

    def increment_score(self, increment_amount):
        self.score += increment_amount

    def empty_dice_hand(self):
        self.dice_hand.empty()

    def get_roll_dice_choice(self, opponent):
        choice = None
        while not choice or choice.lower() not in ("y", "n", "q"):
            choice = input("Want to roll another die? (y/n). Or type q if you would like to surrender.")
        return choice

    def reset(self):
        self.empty_dice_hand()
        self.score = 0
