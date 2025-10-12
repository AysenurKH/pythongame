"""Code related to players in the Pig dice game."""

from src.dice_hand import DiceHand


class Player:
    """Represents a player in the Pig dice game."""

    def __init__(self, name):
        """Constructor.

        Args
        ----
        - `name:` The name of the player
        """
        self.dice_hand = DiceHand()
        self.name = name
        self.score = 0

    def set_name(self, new_name):
        """Sets/updates the name of the player.

        Args
        ----
        - `new_name:` The name of the player
        """
        self.name = new_name

    def get_score(self):
        """Gets the score of the player in this game.

        The score is the number of points that the player has decided to hold during this game after rolling dice.
        The score is reset back to 0 after every game.

        Returns
        -------
        - `int:` The player's score
        """
        return self.score

    def increment_score(self, increment_amount):
        """Increase the score of the player.

        Args
        ----
        - `increment_amount:` How much to increase the score of the player
        """
        self.score += increment_amount

    def empty_dice_hand(self):
        """Empties the dice hand of the player, so they are no longer holding any dice."""
        self.dice_hand.clear()

    # The opponent parameter must be expected because the Intelligence subclass needs it
    # But we do not use it here, and pylint will complain it is not used. Add underscore to the beginning of the name.
    # This makes pylint not complain anymore.
    def get_roll_dice_choice(self, _opponent=None):
        """Asks the player in the terminal whether to roll another die.

        Args
        ----
        - `opponent:` Not used

        Returns
        -------
        - `str:` Can return either y, n or q. Y rolls another die, n keeps the points rolled so far, and q surrenders.
        """
        choice = None
        while not choice or choice.lower() not in ("y", "n", "q"):
            choice = input("Want to roll another die? (y/n). Or type q if you would like to surrender: ")
        return choice

    def reset(self):
        """Empties the player's dice hand, and sets the player's score to 0."""
        self.empty_dice_hand()
        self.score = 0
