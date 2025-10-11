import cmd
from src.die import Die
from src.player import Player

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
# TODO: Implement Cheat
# TODO: Implement some intelligence and use it instead of asking for input, if playing against computer
# TODO: Docstrings
# TODO: Tests
# TODO: Make it possible for both players to change name
# TODO: Add better error handlng (like handling bad/unexpected inputs)
# TODO: Add some file that can be written and read, which contains the amount of games played by the player.
# It's not clear whether I should just store "player1's score" and keep updating it every game no matter what the name of the player is, or if different names should count as separate players and their scores are kept separate in the file..
# TODO: Implement a loop that re-runs the game once it has been won/lost
# TODO: Show total score AND your current hand (maybe with number and dice)
# BUG: Seems that the dice_hand is not really cleared and is re-used by both players?
# TODO: Fix Makefile with either SINGLE SHELL or that youtube video that has the venv activation function as a make-target?

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
        name_player1 = input("Player 1 name: ")
        name_player2 = input("Player 2 name. Leave blank to play against the computer: ")
        self.play_against_computer = not name_player2
        if not name_player2:
            name_player2 = "Computer"
        self.player1 = Player(name_player1)
        self.player2 = Player(name_player2)
        self.game_loop()

    def do_rules(self, arg):
        print(RULES)

    def do_changename(self, arg):
        self.player.set_name(arg)

    def do_cheat(self):
        pass

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
                self.handle_player_turn(self.player1)
            else:
                self.handle_player_turn(self.player2)

    def handle_player_turn(self, player):
        print(f"\nIt's {player.name}'s turn")
        print(f"Your score for this round is {player.dice_hand.get_value()}.")
        choice = input("Want to roll another die? (y/n)")
        if choice.lower() == "n":
            player.increment_score(player.dice_hand.get_value())
            player.empty_dice_hand()
            self.player1s_turn = not self.player1s_turn
        if choice.lower() == "y":
            die = Die()
            value = die.roll();
            print(f"You rolled {die} ({die.value})")
            if value == 1:
                print(f"Too bad!")
                player.empty_dice_hand()
                self.player1s_turn = not self.player1s_turn
            else:
                print(f"Added {die.value} to your current hand.")
                player.dice_hand.add_die(die)


if __name__ == '__main__':
    Game().cmdloop()
