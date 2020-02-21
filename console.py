#!/usr/bin/python3
"""
console.py
HBNBCommand(cmd.Cmd) Class
"""
import cmd
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Entry point for command interpreter
    - prompt: What to display as the prompt
    - class_names: A dictionary containing multiple classes
        |-> Makes the methods dynamic to work with any class
        |-> Just compare arg to dict and retrieve the value for class
    """
    prompt = '(hbnb) '
    class_names = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def default(self, line):
        """
        Accepts the other way of calling commands, ex: <class name>.<command>()
        """
        command_names = {'quit': self.do_quit, 'EOF': self.do_EOF,
                         'create': self.do_create, 'show': self.do_show,
                         'destroy': self.do_destroy, 'all': self.do_all,
                         'update': self.do_update, 'count': self.do_count}
        table_change = {44: 32, 40: 32, 41: 32, 46: 32}
        new_line = line.translate(table_change)
        new_line = new_line.replace("  ", " ")
        new_line = new_line.strip(" ")
        split_line = new_line.split(" ")
        for i in range(len(split_line)):
            if "\"" in split_line[i]:
                split_line[i] = split_line[i].strip('\"')
        if len(split_line) > 1 and split_line[1] in command_names:
            arg = ""
            for i in range(len(split_line)):
                if i != 1:
                    arg = arg + (split_line[i])
                    if i != (len(split_line) - 1):
                        arg = arg + " "
            command_names[split_line[1]](arg)
        else:
            return cmd.Cmd.default(self, line)

    def emptyline(self):
        """
        Do nothing if a blank line is entered
        """
        pass

    def help_help(self):
        """
        Explains the help command
        """
        print("List available commands with \"help\" or \
detailed help with \"help cmd\".\n")

    def help_quit(self):
        """
        Explains the quit command
        """
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_EOF(self):
        """
        Explains the EOF command
        """
        print("End of file command to exit the program\n")

    def do_EOF(self, arg):
        """
        End of file command to exit the program
        """
        print()
        return True

    def help_create(self):
        """
        Explains the create command
        """
        print("Creates a new instance of a class and prints its id \
(after having been saved in a JSON file)\n")

    def do_create(self, arg):
        """
        Creates a new instance of a specified class
            -->| create <class name>
        If <class name> was not inputted then:
            |-> print error: ** class name missing **
        If <class name> is not within the class_names dictionary:
            |-> print error: ** class doesn't exist **
        Else the instance will be created:
            |-> HBNBCommand.class_names[arg] would retrieve the class
                |-> Placing it before the () creates a new instance
                |-> .save() Saves the instance to the file
                |-> The id of the instance is then printed
        """
        if arg is '':
            print("** class name missing **")
        elif arg not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        else:
            new_inst = HBNBCommand.class_names[arg]()
            new_inst.save()
            print(new_inst.id)

    def help_show(self):
        """ Explains the show command """
        print("Prints the string representation of an instance \
based upon class name and id\n")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
            -->| show <class name> <id>
        If <class name> was not entered then:
            |-> print error: ** class name missing **
        If <class name> is not within the class_names dictionary:
            |-> print error: ** class doesn't exist **
        If <id> was not entered then:
            |-> print error: ** instance id missing **
        Else see if the instance exists:
            |-> find instance by stringing together <classname> + "." + <id>
                |-> use to find a matching key in storage.all()
                    |-> if found then print the object
                    |-> if not found then print error: ** no instance found **
        """
        list_arg = arg.split(" ")
        if arg is '':
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        elif len(list_arg) is 1:
            print("** instance id missing **")
        else:
            key = list_arg[0] + "." + list_arg[1]
            obj_dict = storage.all()
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def help_destroy(self):
        """ Explains the destroy command """
        print("Deletes an instance based upon class name and id \
(the change is saved in the JSON file)\n")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
            -->| destroy <class name> <id>
        If <class name> was not entered then:
            |-> print error: ** class name missing **
        If <class name> is not within the class_names dictionary:
            |-> print error: ** class doesn't exist **
        If <id> was not entered then:
            |-> print error: ** instance id missing **
        Else see if the instance exists:
            |-> find instance by stringing together <classname> + "." + <id>
                |-> use to find a matching key in storage.all()
                    |-> if found then delete the object/instance
                    |-> if not found then print error: ** no instance found **
        """
        list_arg = arg.split(" ")
        if arg is '':
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        elif len(list_arg) is 1:
            print("** instance id missing **")
        else:
            key = list_arg[0] + "." + list_arg[1]
            obj_dict = storage.all()
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def help_all(self):
        """ Explains the all command """
        print("Prints each string representation of every instance \
based upon whether the class name was provided or not\n")

    def do_all(self, arg):
        """
        Prints every __str__ of instances based or not upon class name
            -->| all
            -->| all <class name>
        If <class name> was not entered then:
            |-> Save the string representation of every instance in a list
                |-> then print the list
        If <class name> was provided:
            |-> check if <classname> was within the class_names dictionary
                |-> if not then print error: ** class doesn't exist **
                |-> otherwise save each instance of that class in a list
                    |-> print the list
        """
        list_arg = arg.split(" ")
        obj_dict = storage.all()
        obj_list = []
        if arg is '':
            for key, value in obj_dict.items():
                obj_list.append(str(obj_dict[key]))
            print(obj_list)
        elif list_arg[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        else:
            for key, value in obj_dict.items():
                dict_key = key.split(".")
                if dict_key[0] == list_arg[0]:
                    obj_list.append(str(obj_dict[key]))
            print(obj_list)

    def help_update(self):
        """ Explains the update command """
        print("Updates an instance based upon class name and id \
by adding or updating attribute\n")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
            -->| update <class name> <id> <attribute name> "<attribute value>"
        If <class name> was not entered then:
            |-> print error: ** class name missing **
        If <class name> is not within the class_names dictionary:
            |-> print error: ** class doesn't exist **
        If <id> was not entered then:
            |-> print error: ** instance id missing **
        If <classname> + "." + <id> is not found
            |-> print error: ** no instance found **
        If <attribute> was not entered then:
            |-> print error: ** attribute name missing **
        If <attribute value> was not entered then:
            |-> print error: ** value missing **
        Else update the attribute but first:
            |-> Slice first and last char of <attribute value> for the quotes
            |-> If the <class name> was Place:
                |-> Depending on <attribute>, <attribute value> may be casted
            |-> Update __dict__ of object by <attribute> and <attribute value>
            |-> Save the change by calling the instance's .save() method
        """
        list_arg = arg.split(" ")
        obj_dict = storage.all()
        obj_list = []
        float_list = ["latitude", "longitude"]
        int_list = ["price_by_night", "max_guest",
                    "number_bathrooms", "number_rooms"]
        if len(list_arg) > 1:
            key = list_arg[0] + "." + list_arg[1]

        if arg is '':
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        elif len(list_arg) is 1:
            print("** instance id missing **")
        elif key not in obj_dict.keys():
            print("** no instance found **")
        elif len(list_arg) is 2:
            print("** attribute name missing **")
        elif len(list_arg) is 3:
            print("** value missing **")
        else:
            value = list_arg[3].strip("\"")
            if list_arg[0] is "Place":
                if list_arg[2] in float_list:
                    value = float(value)
                elif list_arg[2] in int_list:
                    value = int(value)
            ((obj_dict[key]).__dict__).update({list_arg[2]: value})
            obj_dict[key].save()

    def help_count(self):
        """
        Explains the count command
        """
        print("Prints the number of instances of a class\n")

    def do_count(self, arg):
        """
        Counts how many instances there are of a certain class
        """
        arg = arg.strip()
        obj_dict = storage.all()
        count = 0
        if arg in HBNBCommand.class_names:
            for key in obj_dict.keys():
                dict_keys = key.split(".")
                if arg == dict_keys[0]:
                    count = count + 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
