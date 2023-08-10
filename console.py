#!/usr/bin/python3

"""
get the cmd module
"""

import cmd


"""
class HBNBCommand console
"""


class HBNBCommand(cmd.Cmd):

    """ prompt to be shown when the console starts """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ function to exit from the console """
        return True

    def do_quit(self, line):
        """ function to exit from the console """
        return True

    def emptyline(self):
        """ empty line should do nothing """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
