"""Code related to a collection of dice held by a specific player."""


class DiceHand:
    """Class representing a single player's collection of dice during a single round in the game."""

    def __init__(self):
        """Constructor."""
        self.dice = []

    def add_die(self, die):
        """Adds a die to the dice hand.

        Args
        ----
        - `Die:` A newly rolled die which the player would like to keep during this round.
        """
        self.dice.append(die)

    def get_value(self):
        """Gets the sum of all the dice in the dice hand.

        Returns
        -------
        - `int:` The sum of all dice in the dice hand.
        """
        return sum(die.value for die in self.dice)

    def __str__(self):
        """Overrides the default __str__ method.

        This means that if we ever try to print a DiceHand object, it will print as a list of dice symbols.
        This is used in the game loop.

        Returns
        -------
        - `str:` A list of dice symbols representing the contents of the dice hand, separated by spaces.
        Example: ⚃ ⚄ ⚃ ⚅ ⚄ ⚃ ⚁ ⚃ ⚄ ⚂
        """
        return " ".join(map(str, self.dice))

    def clear(self):
        """Empties the dice hand."""
        self.dice.clear()
