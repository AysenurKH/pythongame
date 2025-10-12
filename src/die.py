"""Code related to a die which can be rolled."""

import random

DICE = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]


class Die:
    """Class representing a single die which can be rolled."""

    value = None

    def __init__(self, value=None):
        """Constructor.

        Args
        ----
        - `value:` int, the value of the die, i.e. the result of rolling the die (1 - 6).
        """
        if value:
            self.value = value

    def roll(self):
        """Rolls the die and sets the value in the Die object. Also return this value.

        Returns
        -------
        - `int:` The result of the die roll.
        """
        self.value = random.randint(1, 6)
        return self.value

    def __str__(self):
        """Overrides the default __str__ method.

        This means that if we try to print a Die object, it will print as a die symbol.

        Returns
        -------
        - `str:` The die symbol equivalent to the value of the rolled die. Example: ⚃
        """
        return DICE[self.value-1] if self.value else "N/A"
