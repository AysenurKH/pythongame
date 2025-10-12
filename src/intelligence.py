"""Code related to the Computer Opponent."""

import random
from time import sleep
from src.player import Player


class Intelligence(Player):
    """Inherits from Player, which lets the gameplay code handle player2 polymorphically/generically."""

    def __init__(self, computer_difficulty):
        """Constructor.

        Calls the Player's constructor with the hardcoded name "Computer"

        Args
        ----
        - `computer_difficulty:` Int, either 1, 2 or 3. This is used when generating the roll decision below.
        """
        super().__init__("Computer")
        self.computer_difficulty = computer_difficulty

    def get_roll_dice_choice(self, _opponent=None):
        """Generates a decision on whether to roll another die.

        In the superclass Player's implementation, the player is asked in the terminal.
        This is player is the computer though, so instead of asking in the terminal, we generate the choice
        based on the difficulty level chosen, and the opponents score.

        Args
        ----
        - `opponent:` Player. The opponents score is used to generate a decision on whether to roll another die.
        """
        # Sleep 1 second between each die roll to make the terminal output more natural
        sleep(1)
        if self.computer_difficulty == 1:
            return self.roll_dice_easy()
        if self.computer_difficulty == 2:
            return self.roll_dice_medium()
        return self.roll_dice_hard(_opponent)

    def roll_dice_easy(self):
        """If we have any points at all in this round, just decide randomly if we should stop."""
        return (
            "n"
            if self.dice_hand.get_value() > 0 and random.choice([True, False])
            else "y"
        )

    def roll_dice_medium(self):
        """Keep rolling until we have at least 20 points in the current round."""
        return "y" if self.dice_hand.get_value() < 20 else "n"

    def roll_dice_hard(self, opponent):
        """Almost optimal strategy.

        https://en.wikipedia.org/wiki/Pig_(dice_game)#Optimal_play

        Args
        ----
        - `opponent:` Player. The opponents score is used to generate a decision on whether to roll another die.
        """
        opponent_score = opponent.score
        if opponent_score >= 71 or self.score >= 71:
            # If eiher player has a score of at least 71, then roll to win
            return "n" if self.dice_hand.get_value() >= 29 else "y"
        # Both players have less than 71 points.
        # Roll the die until we hold 21 + the difference between our scores divided by 8
        score_diff_divided = (opponent_score - self.score) // 8
        return "n" if self.dice_hand.get_value() > (21 + score_diff_divided) else "y"
