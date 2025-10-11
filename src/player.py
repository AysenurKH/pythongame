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
        return input("Want to roll another die? (y/n)")
