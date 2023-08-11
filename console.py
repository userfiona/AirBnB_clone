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

    def do_all(self, line):
        """
        all command prints all string rep of all instances bases on
        <className> provided or only all command still prints
        if class does not exists ptints(** class doesn't exist **)
        """
        className = self.parseline(line)[0]
        if not className:
            my_obj_list = []
            my_obj = models.storage.all()
            for key, value in my_obj.items():
                my_obj_list.append(str(value))
            print(my_obj_list)
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            my_obj_list = []
            my_obj = models.storage.all()
            for key, value in my_obj.items():
                my_obj_list.append(str(value))
            print(my_obj_list)

    def do_update(self, line):
        """
        update command updates an instance based on the className and id
        by adding or updating atribute then save changes into a json file.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        linelist = line.split(" ")
        className = None
        classId = None
        classAtt = None
        classAttValue = None
        linelength = len(linelist)
        if linelength > 0:
            className = linelist[0]
        if linelength > 1:
            classId = linelist[1]
        if linelength > 2:
            classAtt = linelist[2]
        if linelength > 3:
            classAttValue = linelist[3]
        if not className:
            print("** class name missing **")
        elif className not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif not classId:
            print("** instance id missing **")
        else:
            inst_data = models.storage.all().get(className + '.' + classId)
            if not inst_data:
                print("** no instance found **")
            else:
                if not classAtt:
                    print("** attribute name missing **")
                else:
                    my_dict = inst_data.to_dict()
                    try:
                        attValue = my_dict[classAtt]
                    except KeyError:
                        if not classAttValue:
                            print("** value missing **")
                            # add key,value if missing
                        else:
                            setattr(inst_data, classAtt, classAttValue)
                            # save changes
                            models.storage.save()
                    else:
                        # update if exist except ones in notAllowedUpdate list
                        notAllowedUpdate = ["id", "created_at", "updated_at"]
                        if str(classAtt) in notAllowedUpdate:
                            print(f"{classAtt} Not allowed to be updated")
                        else:
                            setattr(inst_data, classAtt, classAttValue)
                            # save changes
                            models.storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
