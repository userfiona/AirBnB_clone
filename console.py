#!/usr/bin/python3

"""
get the cmd module
"""

import cmd
from models.base_model import BaseModel

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

    def do_create(self, line):
        """
        Creates a new instance of BaseModel and saves it to file.JSON
        prints the instance id
        command is:-> create <className>

        if <className> not provided
        prints: ** class name missing **

        if <className> is wrong 
        prints: ** class doesn't exist **
        """
        classes = ['BaseModel', 'FileStorage']
        if not line:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                my_model = BaseModel()
                my_model.save()
                print(my_model.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
