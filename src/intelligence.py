from src.player import Player
import random


class Intelligence(Player):
    def __init__(self, name, computer_difficulty):
        super(Intelligence, self).__init__(name)
        self.computer_difficulty = computer_difficulty

    def get_roll_dice_choice(self, opponent):
        if self.computer_difficulty == 1:
            return self.roll_dice_easy()
        elif self.computer_difficulty == 2:
            return self.roll_dice_medium()
        else:
            return self.roll_dice_hard(opponent)

    def roll_dice_easy(self):
        """If we have any points at all in this round, just decide randomly if we should stop."""
        return "n" if self.dice_hand.get_value() > 0 and random.choice([True, False]) else "y"

    def roll_dice_medium(self):
        """Keep rolling until we have at least 20 points in the current round."""
        return "y" if self.dice_hand.get_value() < 20 else "n"

    def roll_dice_hard(self, opponent):
        """https://en.wikipedia.org/wiki/Pig_(dice_game)#Optimal_play
        Almost optimal strategy."""
        opponent_score = opponent.score
        if opponent_score >= 71 or self.score >= 71:
            # If eiher player has a score of at least 71, then roll to win
            return "n" if self.dice_hand.get_value() >= 29 else "y"
        # Both players have less than 71 points.
        # Roll the die until we hold 21 + the difference between our scores divided by 8
        score_diff_divided = (opponent_score - self.score) // 8
        return "n" if self.dice_hand.get_value() > (21 + score_diff_divided) else "y"

