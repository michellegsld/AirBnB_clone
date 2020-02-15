#!/usr/bin/python3
"""
console.py
HBNBCommand(cmd.Cmd) Class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point for command interpreter
    """
    prompt = '(hbnb) '

    def help_help(self):
        """ Explains the help command """
        print("List available commands with \"help\" or detailed help with \"help cmd\".\n")

    def help_quit(self):
        """ Explains the quit command """
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def help_EOF(self):
        """ Explains the EOF command """
        print("End of file command to exit the program\n")

    def do_EOF(self, arg):
        """ End of file command to exit the program """
        print()
        return True

    def emptyline(self):
        """ Do nothing if a blank line is entered """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
