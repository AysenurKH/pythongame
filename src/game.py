import cmd
import os
from src.die import Die
from src.player import Player
from src.intelligence import Intelligence
from src.high_score import HighScore, from_persisted_line

RULES = """
Welcome to the Dice game "Pig".
This game is played with 2 players. You can play against a friend, or against the computer.
Player 1 starts.
Keep rolling one die at a time and sum the value of each throw. 
At any point, you can decide to stop rolling dice, and the points you've collected so far in this round are 
added to your score.
If you roll a 1 though, your turn ends and you do not get to keep these points. 
Once your turn ends, it's player 2's turn. Once their turn ends, it's your turn again, and so on.
First player to reach 100 points wins.
"""


# TODO: Maybe find a better place to put all this game logic, and keep the input/cmd separate?
# TODO: Docstrings
# TODO: Tests
# TODO: Add better error handlng (like handling bad/unexpected inputs)
# It's not clear whether I should just store "player1's score" and keep updating it every game no matter what the name of the player is, or if different names should count as separate players and their scores are kept separate in the file..
# TODO: Fix Makefile with either SINGLE SHELL or that youtube video that has the venv activation function as a make-target?
# TODO: Consider just creating a new Game object whenever we play a game. Then we don't need to reset everything in between games
# TODO: Update README with things like Computer Intelligence
# TOdO: Add black dependency and create new make target
class Game(cmd.Cmd):
    """Here is a test or two.
    """

    intro = "Welcome to the Pig dice game.   Type help or ? to list commands.\n"
    prompt = "Input: "

    file = None
    player1 = None
    player2 = None
    play_against_computer = False
    player1s_turn = True

    def __init__(self):
        """Constructor."""
        super(Game, self).__init__()

    def do_play(self, arg):
        """Docstring for do_printsomething."""
        self.setup_game()
        self.game_loop()

    def do_rules(self, arg):
        """View the rules of the game."""
        print(RULES)

    def do_changename(self, arg):
        """Set name of player."""
        try:
            player_number = int(arg)
        except ValueError:
            print("player number must be an integer")
            return

        if player_number not in (1, 2):
            print("The player number must be either 1 or 2")
            return

        player = self.player1 if player_number == 1 else self.player2

        if not player:
            print(f"Player {player_number} does not exist. Play a game first")
            return

        print(f"Renaming {player.name}..")
        new_name = self.get_name_from_player(player_number)
        current_name = player.name
        player.set_name(new_name)
        print(f"Player {current_name} has changed name to {new_name}")

    def do_cheat(self, arg):
        self.setup_game()

        for _ in range(33):
            # Add 33 dice with value 3 each (=99 points) to player 1's hand to start the first round.
            self.player1.dice_hand.add_die(Die(3))
        self.game_loop()

    def do_quit(self, arg):
        """Quits the game."""
        print('Thank you for using Turtle')
        return True

    def game_loop(self):
        while self.player1.get_score() < 100 and self.player2.get_score() < 100:
            if self.player1s_turn:
                self.handle_player_turn(self.player1, self.player2)
            else:
                self.handle_player_turn(self.player2, self.player1)
        (winning_player, losing_player) = (self.player1, self.player2) if self.player1.score >= 100 else (self.player2, self.player1)
        print(f"The winner is {winning_player.name}")
        print("Thank you for playing!")
        self.persist_win(winning_player, losing_player)
        self.reset_game()
        print(self.intro)

    def handle_player_turn(self, player, opponent):
        print(f"\nIt's {player.name}'s turn")
        while True:
            print(f"\nYour total score is {player.score}.")
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
                self.player1s_turn = not self.player1s_turn
                print(f"Your new score is {player.score}")
                break
            elif choice.lower() == "y":
                die = Die()
                value = die.roll()
                print(f"You rolled {die} ({die.value})")
                if value == 1:
                    print(f"Too bad!")
                    player.empty_dice_hand()
                    self.player1s_turn = not self.player1s_turn
                    break
                else:
                    print(f"Added {die.value} to your current hand.")
                    player.dice_hand.add_die(die)
        print("-----------------------------------------------------")

    def get_difficulty(self):
        print("You are playing against the computer")
        while True:
            try:
                value = int(input("Pick a difficulty: 1 (EASY), 2 (MEDIUM), 3 (HARD)"))
            except ValueError:
                print("Bad input")
                continue
            if 0 <= value <= 3:
                return value
            else:
                print("Pick a number between 1 and 3")

    def setup_game(self):
        if self.player1 or self.player2:
            # No need to ask players for their names if they have just played a game previously
            return
        name_player1 = self.get_name_from_player(1)
        self.player1 = Player(name_player1)

        self.play_against_computer = self.yes_no_prompt("Play against computer? [y/n]")
        if self.play_against_computer:
            self.player2 = Intelligence("Computer", self.get_difficulty())
        else:
            name_player2 = self.get_name_from_player(2)
            self.player2 = Player(name_player2)

    def persist_win(self, winning_player, losing_player):
        file_name = "highscore.txt"

        # First load the existing high scores
        high_scores = {}
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                for line in file:
                    high_score = from_persisted_line(line)
                    high_scores[high_score.name] = high_score

        # Ensure both players exist in the dict
        for player in (winning_player, losing_player):
            high_scores.setdefault(player.name, HighScore(player.name))

        # Next, update the stats for the winning player and losing player
        high_scores[winning_player.name].increment_games_won()
        for player in (winning_player, losing_player):
            high_scores[player.name].increment_games_played()

        # Finally, store it all back in the file
        with open(file_name, "w") as file:
            for high_score in high_scores.values():
                # You can print to files, while specifying line separator. This avoids a linebreak at the end of the file, causing an empty line at the bottom
                # the HighScore class overrides the __str__ method, which formats the high score correctly in the file.
                print(high_score, sep=os.linesep, file=file)

    def get_name_from_player(self, player_number):
        name = None
        while not name:
            name = input(f"Player {player_number} name: ")
            if not name:
                print("Name must be a non-blank string")
        return name

    def yes_no_prompt(self, text):
        choice = None
        while not choice or choice.lower() not in ("y", "n"):
            choice = input(text)
        return choice.lower() == "y"

    def reset_game(self):
        self.player1.reset()
        self.player2.reset()
        self.player1s_turn = True


if __name__ == '__main__':
    Game().cmdloop()
