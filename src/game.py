import cmd
from src.die import Die
from src.player import Player
from src.intelligence import Intelligence

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
# TODO: Add some file that can be written and read, which contains the amount of games played by the player.
# It's not clear whether I should just store "player1's score" and keep updating it every game no matter what the name of the player is, or if different names should count as separate players and their scores are kept separate in the file..
# TODO: Fix Makefile with either SINGLE SHELL or that youtube video that has the venv activation function as a make-target?
# TODO: Error handling for name change (only allow if players already have names, and validate input)
# TODO: Don't ask players for their name again in round 2 and later

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
        (player_number, new_name) = arg.split()
        player = self.player1 if player_number == 1 else self.player2
        current_name = player.name
        player.set_name(new_name)
        print(f"Player {current_name} has changed name to {new_name}")

    def do_cheat(self, arg):
        self.setup_game()

        for _ in range(33):
            # Add 33 dice with value 3 each (=99 points) to player 1's hand to start the first round.
            self.player1.dice_hand.add_die(Die(3))
        self.game_loop()

    def do_reset(self, arg):
        """Clear the screen and return turtle to center:  RESET"""
        pass

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
        print(f"The winner is {self.player1.name if self.player1.score >= 100 else self.player2.name}")
        print("Thank you for playing!")
        print(self.intro)

    def handle_player_turn(self, player, opponent):
        print(f"\nIt's {player.name}'s turn")
        while True:
            print(f"\nYour total score is {player.score}.")
            print(f"You are currently holding {player.dice_hand} (value: {player.dice_hand.get_value()})")
            choice = player.get_roll_dice_choice(opponent)
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
        name_player1 = input("Player 1 name: ")
        name_player2 = input("Player 2 name. Leave blank to play against the computer: ")
        self.player1 = Player(name_player1)
        self.play_against_computer = not name_player2
        if self.play_against_computer:
            self.player2 = Intelligence("Computer", self.get_difficulty())
        else:
            self.player2 = Player(name_player2)


if __name__ == '__main__':
    Game().cmdloop()
