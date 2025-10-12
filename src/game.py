"""Code related to a game of Pig."""

from src.die import Die
from src import high_score


class Game:
    """Class representing a single game of Pig."""

    def __init__(self, player1, player2, cheat=False):
        """Constructor.

        Args
        ----
        - `player1:` Player, player 1.
        - `player2:` Player, player 2.
        - `cheat:` bool, decides whether player 1 should start the game with 99 points in their hand.
        """
        self.player1 = player1
        self.player2 = player2
        if cheat:
            for _ in range(33):
                # Add 33 dice with value 3 each (=99 points) to player 1's hand to start the first round.
                self.player1.dice_hand.add_die(Die(3))

    def start_game_loop(self):
        """Starts the game loop.

        This function will handle switching turns back and forth until one of the players reaches 100 points.
        When the game is over, the result of the game is persisted to the high score file, and the players' dice hands
        are emptied.
        """
        player1s_turn = True
        while self.player1.get_score() < 100 and self.player2.get_score() < 100:
            if player1s_turn:
                self.handle_player_turn(self.player1, self.player2)
            else:
                self.handle_player_turn(self.player2, self.player1)
            player1s_turn = not player1s_turn

        if self.player1.score >= 100:
            (winning_player, losing_player) = (self.player1, self.player2)
        else:
            (winning_player, losing_player) = (self.player2, self.player1)
        print(f"The winner is {winning_player.name}")
        print("Thank you for playing!")
        high_score.persist_win(winning_player, losing_player)
        self.player1.reset()
        self.player2.reset()

    def handle_player_turn(self, player, opponent):
        """Handles a single turn for a single player.

        Allows the player to roll dice over and over again, collecting points.
        The player can choose to stop rolling new dice, and add the points to their score.
        If the player rolls 1, they forfeit their points and their turn ends.
        The player can always choose to surrender.

        Args
        ----
        - `player:` Player, the player who gets to play this round.
        - `opponent:` Player, the opponent.
        """
        print(f"\nIt's {player.name}'s turn")

        while True:
            print(f"\nYour total score is {player.score}.")
            if player.dice_hand.get_value == 0:
                print("Your dice hand is currently empty")
            else:
                print(f"You are currently holding {player.dice_hand} (value: {player.dice_hand.get_value()})")
            choice = player.get_roll_dice_choice(opponent)
            if choice.lower() == "q":
                print("You decided to surrender the game. This counts as a loss.")
                opponent.increment_score(100)
                break
            if choice.lower() == "n":
                print(f"You decided to stop rolling. Adding {player.dice_hand.get_value()} to your score.")
                player.increment_score(player.dice_hand.get_value())
                player.empty_dice_hand()
                print(f"Your new score is {player.score}")
                break
            if choice.lower() == "y":
                die = Die()
                value = die.roll()
                print(f"You rolled {die} ({die.value})")
                if value == 1:
                    print("Too bad! You rolled 1 and forfeited your points. Your round has ended.")
                    player.empty_dice_hand()
                    break
                print(f"Added {die.value} to your current hand.")
                player.dice_hand.add_die(die)
        print("-----------------------------------------------------")
