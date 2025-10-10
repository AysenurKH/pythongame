import cmd, sys


class Game(cmd.Cmd):
    intro = "Welcome to the Pig dice game.   Type help or ? to list commands.\n"
    prompt = "(test) "
    file = None

    def __init__(self):
        super(Game, self).__init__()

    def do_printsomething(self, arg):
        """Docstring for do_printsomething."""
        print("hello " + arg)

    def do_reset(self, arg):
        """Clear the screen and return turtle to center:  RESET"""
        pass

    def do_bye(self, arg):
        """Stop recording, close the turtle window, and exit:  BYE"""
        print('Thank you for using Turtle')
        return True


if __name__ == '__main__':
    Game().cmdloop()
