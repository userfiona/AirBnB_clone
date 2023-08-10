#!/usr/bin/python3

"""
get the cmd module
"""

import cmd
import models

"""
class HBNBCommand console
"""


class HBNBCommand(cmd.Cmd):

    """ prompt to be shown when the console starts """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'FileStorage']

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
        Creates a new instance of <className> and saves it to file.JSON
        prints the instance id
        command is:-> create <className>

        if <className> not provided
        prints: ** class name missing **

        if <className> is wrong
        prints: ** class doesn't exist **
        """
        className = self.parseline(line)[0]
        if not className:
            print("** class name missing **")
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                my_model = models.base_model.BaseModel()
                my_model.save()
                print(my_model.id)

    def do_show(self, line):
        """
        show retrives an instance of <className>
        prints the instance
        command is:-> show <className> <instanceId>

        if <className> not provided
        prints: ** class name missing **

        if <className> is wrong
        prints: ** class doesn't exist **

        if <instanceId> is wrong
        prints: ** no instance found **
        """
        className = self.parseline(line)[0]
        classId = self.parseline(line)[1]
        if not className:
            print("** class name missing **")
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if not classId:
                print("** instance id missing **")
            else:
                inst_data = models.storage.all().get(className + '.' + classId)
                if inst_data is None:
                    print('** no instance found **')
                else:
                    print(inst_data)

    def do_destroy(self, line):
        """
        destroy destroys an instance of <className> and
        save changes to json file
        command is:-> destroy <className> <instanceId>

        if <className> not provided
        prints: ** class name missing **

        if <className> is wrong
        prints: ** class doesn't exist **

        if <instanceId> is wrong
        prints: ** no instance found **
        """
        className = self.parseline(line)[0]
        classId = self.parseline(line)[1]
        if not className:
            print("** class name missing **")
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if not classId:
                print("** instance id missing **")
            else:
                inst_data = models.storage.all().get(className + '.' + classId)
                if inst_data is None:
                    print('** no instance found **')
                else:
                    del (models.storage.all())[className + '.' + classId]
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
